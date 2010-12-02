from .. import TVDriver

class LG_LH3000(TVDriver):
        '''
        The LG LH3000 series of TVs.
        
        - command list: http://code.google.com/p/pyhomectl/wiki/LH3000
        - product page: http://goo.gl/J0b21

        '''
        _code_power_off       = 'ka {0} 0\r' # {0} is a placeholder for the set id, which is resolved in BaseDriver.write
        _code_power_on        = 'ka {0} 1\r'
        _code_screen_mute_off = 'kd {0} 1\r'
        _code_screen_mute_on  = 'kd {0} 0\r'
        _code_vol_mute_off    = 'ke {0} 1\r'
        _code_vol_mute_on     = 'ke {0} 0\r'
        _code_volume          = 'kf {0} {1}\r'
        _code_contrast        = 'kg {0} {1}\r'
        _code_brightness      = 'kh {0} {1}\r'
        _code_colour          = 'ki {0} {1}\r'
        _code_tint            = 'kj {0} {1}\r'
        _code_sharpness       = 'kk {0} {1}\r'
        _code_energy_savings  = 'jq {0} {1}\r'

        def __init__(self, setid=1, debug=False, devaddr='/dev/ttyUSB0'):
                TVDriver.__init__(self, debug=debug, setid=setid, baudrate=9600, devaddr=devaddr)
                self.commands = {
                    'power': self.power,
                    'screen': self.screen,
                    'mute': self.mute,
                    'energysaving': self.energysaving,
                    'brightness': self.brightness,
                    'volume': self.volume,
                    'contrast': self.contrast,
                    'colour': self.colour,
                    'tint': self.tint,
                    'sharpness': self.sharpness,
                    }

        def sharpness(self, level=50):
            '''
            set sharpness levels (0-100) (default 50).
            '''
            self._write(self._code_sharpness.format(self.setid, int(level/100.0*64)))

        def tint(self, level=50):
            '''
            set tint levels (0-100) (default 50).
            '''
            self._write(self._code_tint.format(self.setid, int(level/100.0*64)))

        def colour(self, level=50):
            '''
            set colour levels (0-100) (default 50).
            '''
            self._write(self._code_colour.format(self.setid, int(level/100.0*64)))

        def volume(self, level=10):
            '''
            set volume (0-100) (default 10).
            '''
            self._write(self._code_volume.format(self.setid, int(level/100.0*64)))

        def contrast(self, level=50):
            '''
            set contrast (0-100) (default 50).
            '''
            self._write(self._code_contrast.format(self.setid, int(level/100.0*64)))

        def power(self, on=True):
            self._write(self._code_power_on if on else self._code_power_off)

        def screen(self, on=True):
            self._write(self._code_screen_mute_on if on else self._code_screen_mute_off)

        def mute(self, on=True):
                self._write(self._code_vol_mute_on if on else self._code_vol_mute_off)

        def energysaving(self, level=0):
            '''
            Set the energy saving level 0-4 (default 0)
            @type  level: int
            @param level: (default 0) the level of energy saving to use (0-4)
            '''
            self._write(self._code_energy_savings.format(self.setid, level))

        def brightness(self, level=50):
            '''
            Set the energy saving level 0-100 (default 50)
            @type  level: int
            @param level: (default 32) the level of energy saving to use (0-100)
            '''
            self._write(self._code_brightness.format(self.setid, int(level/100.0*64)))
