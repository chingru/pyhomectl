import sys, unittest, serial
sys.path.append('../../')
from pyhomectl.tvs.lg import LG_LH3000
from pyhomectl import FeatureNotAvailableError, BaseDriver

class TestPyLGTV(unittest.TestCase):
        def setUp(self):
                pass
        def tearDown(self):
                pass

        def test_featurenotavailerr(self):
                err = FeatureNotAvailableError('test')
                self.assertEqual(err.feature, 'test')
                self.assertEqual(err.msg, "Feature 'test' is not available")
                self.assertEqual(err.msg, str(err))
                self.assertEqual(err.msg, repr(err))

        def test_defaultslh3000(self):
            tv = LG_LH3000()
            self.assertEqual(1, tv.setid)
            tv = LG_LH3000(2)
            self.assertEqual(2, tv.setid)
            self.assertEqual(9600, tv.serial.baudrate)
            self.assertEqual(serial.PARITY_NONE, tv.serial.parity)
            self.assertEqual(serial.STOPBITS_ONE, tv.serial.stopbits)
            self.assertEqual(False, tv.serial.xonxoff)
            self.assertEqual(False, tv.serial.rtscts)
            self.assertEqual(False, tv.serial.dsrdtr)
            self.assertEqual(serial.EIGHTBITS, tv.serial.bytesize)



if __name__ == "__main__":
        unittest.main()
