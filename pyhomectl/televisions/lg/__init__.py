from .. import TVDriver

class LG_LH3000(BaseDriver):
        '''
        The LG LH3000 series of TVs.
        
        - command list: http://code.google.com/p/pyhomectl/wiki/LH3000
        - product page: http://goo.gl/J0b21

        '''
        _code_power_off       = 'ka {0} 00\r' # {0} is a placeholder for the set id, which is resolved in BaseDriver.write
        _code_power_on        = 'ka {0} 01\r'
        _code_screen_mute_off = 'kd {0} 00\r'
        _code_screen_mute_on  = 'kd {0} 01\r'
        _code_vol_mute_off    = 'ke {0} 00\r'
        _code_vol_mute_on     = 'ke {0} 01\r'
        def __init__(self, setid=1, devaddr):
                self.BaseDriver(self, setid=setid, baudrate=9600, devaddr=devaddr)

        def power(self, on=True):
                self.write(self._code_power_on if on else self._code.power_off)

        def screen_mute(self, on=True):
                self.write(self._code_screen_mute_on if on else self._code_screen_mute_off)

        def mute(self, on=True):
                self.write(self._code_vol_mute_on if on else self._code_vol_mute_off)
