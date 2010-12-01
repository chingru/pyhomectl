from .. import TVDriver

class LG_LH3000(TVDriver):
        '''
        The LG LH3000 series of TVs.
        
        - command list: http://code.google.com/p/pyhomectl/wiki/LH3000
        - product page: http://goo.gl/J0b21

        '''
        _code_power_off       = 'ka {0} 0\r' # {0} is a placeholder for the set id, which is resolved in BaseDriver.write
        _code_power_on        = 'ka {0} 1\r'
        _code_screen_mute_off = 'kd {0} 0\r'
        _code_screen_mute_on  = 'kd {0} 1\r'
        _code_vol_mute_off    = 'ke {0} 1\r'
        _code_vol_mute_on     = 'ke {0} 0\r'
        _code_energy_savings  = 'jq {0} {1}\r'
        _code_brightness      = 'kh {0} {1}\r'

        def __init__(self, setid=1, devaddr='/dev/ttyUSB0'):
                TVDriver.__init__(self, setid=setid, baudrate=9600, devaddr=devaddr)

        def power(self, on=True):
                self._write(self._code_power_on if on else self._code.power_off)

        def screen_mute(self, on=True):
                self._write(self._code_screen_mute_on if on else self._code_screen_mute_off)

        def mute(self, on=True):
                self._write(self._code_vol_mute_on if on else self._code_vol_mute_off)

        def energy_saving(self, level=0):
            '''
            Set the energy saving level 0-4 (default 0)
            @type  level: int
            @param level: (default 0) the level of energy saving to use (0-4)
            '''
            self._write(self._code_energy_savings.format(self.setid, level))

        def brightness(self, level=32):
            '''
            Set the energy saving level 0-64 (default 32)
            @type  level: int
            @param level: (default 32) the level of energy saving to use (0-64)
            '''
            self._write(self._code_energy_savings.format(self.setid, level))
