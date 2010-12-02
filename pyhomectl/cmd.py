from ConfigParser import ConfigParser
import sys, os
from optparse import OptionParser
sys.path.append('..')
import pyhomectl.tvs.lg as tvlg

def todict(namekeys):
    '''
    converts (name, value) key pairs into a dict
    '''
    d = dict()
    for key, value in namekeys:
        d[key] = value
    return d

class ApplicationError(Exception):
    pass

class CmdInterface:
    def __init__(self, options, args):
        self._options = options
        self._args = args
        # parse config file
        self.config = ConfigParser()
        self.config.read([options.config_path])
        if not self.config:
            raise ApplicationError("config file could not be parsed "+repr(options))

    def run(self):
        equipment = self._args[0].strip().lower()
        target    = self._args[1].strip().lower()
        data      = self._args[2].strip().lower() if len(self._args) > 2 else None
        equipcfg  = todict(self.config.items(equipment))
        if not equipcfg:
            raise ApplicationError("equipment %s does not exist in config file %s." % (equipment, self._options.config_path))
        # parse data
        if data in ['on','off']:
            data = True if data == 'on' else False
        elif data and data != 'help':
            data = int(data)
        self._run_command(equipment, equipcfg, target, data)

    def _run_command(self, equipment, equipcfg, target, data):
        '''
        Run a command which has been parsed by L{run}.
        @type  equipment: str
        @type  equipcfg:  dict
        @type  target:    str
        @type  data:      int or bool
        '''
        if equipcfg['driver'] == 'tv.lg.lh3000':
            self._run_tv_lg_lh3000(equipment, equipcfg, target, data)

    def _run_tv_lg_lh3000(self, equipment, equipcfg, target, data):
        '''
        Run a command for a LG LH3000 TV
        '''
        print "LG LH3000 %s = %s" % (target, repr(data))
        tv = tvlg.LG_LH3000(debug=self._options.verbose, setid=int(equipcfg['setid']), devaddr=equipcfg['devaddr'])
        if target == 'help':
            print "commands",repr(tv.commands.keys())
            sys.exit(1)
        elif target not in tv.commands:
            raise ApplicationError('unrecognised command %s, accepted commands: %s' % (target, repr(tv.commands.keys())))
        elif data == 'help':
            print "Help:",tv.commands[target].__doc__
            exit(1)
        tv.commands[target](data)
        tv.close()
        

if __name__ == "__main__":
    # parse command line options
    parser = OptionParser(usage="""
    python cmd.py [-i /path/to/config.ini] EQUIPMENT TARGET DATA

    EQUIPMENT: the equipment to control (eg. tv, cd, radio..)
    TARGET:    the target attribute to change (eg. power, mute, screen...)
    DATA:      the value to set the attribute (eg. on, off, 0, 32, 64...)

    Examples:
    $ python cmd.py -i config1.ini tv power on
    $ python cmd.py tv power off
    $ python cmd.py tv volume 64

    where [tv]
        """)
    parser.add_option('-i', '--config', dest="config_path", type="string", default="config.ini")
    parser.add_option('-v', '--verbose', dest="verbose", action="store_true")
    options, args = parser.parse_args()
    if not args or len(args) < 2:
        raise parser.error("please give equipment, target, and data (see usage --help/-h)")
    # run command
    CmdInterface(options, args).run()
