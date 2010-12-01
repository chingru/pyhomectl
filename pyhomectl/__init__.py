import pyserial

class FeatureNotAvailableError(Exception):
        '''
        Raised when a feature is not available for a given device
        '''
        def __init__(self, feature):
                '''
                ctor

                @type  feature: str
                @param feature: the feature which is not available
                '''
                self.feature = feature
                self.msg = "Feature '%s' is not available"
                Exception.__init__(self, self.msg)

        def __str__(self):
                return self.msg

        def __repr__(self):
                return str(self)


class BaseDriver(object):
        '''
        This base class should be used for all drivers.

        @type  setid: int
        @param setid: (default 1) the set id for the equipment (most equipment 
                has a set id to prevent commands going to multiple devices.

        @type  baudrate: int        
        @param baudrate: (default 9200) the baudrate of the device.

        @type  devaddr: str
        @param devaddr: (default /dev/ttyUSB0) the device address.

        @type  timeout: int
        @param timeout: (default 3) The number of seconds to wait for a response.
        '''
        def __init__(self, setid=1, baudrate=9200, devaddr='/dev/ttyUSB0', timeout=3):
                self.setid = setid
                self.serial = serial.Serial(devaddr, baudrate=baudrate, timeout=timeout)

        def _write(self, msg, expectresponse=False):
                '''
                Write data to TX. If L{expectresponse} is C{True}, 
                then expect a response too.

                @type  expectresponse: bool
                @param expectresponse: C{True} if a 
                        response should be checked for afterwards.  
                '''
                self.serial.write(msg.format(self.setid))
                if expectresponse:
                        return self._read()

        def _read(self, datalen=10):
                '''
                Read data from RX.

                @type  datalen: int
                @param datalen: The amount of bytes to expect (or timeout)
                '''
                return self.serial.read(datalen)
                
