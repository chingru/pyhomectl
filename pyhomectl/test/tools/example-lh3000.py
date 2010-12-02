from time import sleep
import sys

sys.path.append('../../../')
from pyhomectl.tvs.lg import LG_LH3000 as lgtv

def main():
        ctl = lgtv()

        print "TV turn on"
        ctl.power(on=True)
        sleep(3)

        print "mute on"
        ctl.mute(on=True)
        sleep(2)

        print "mute off"
        ctl.mute(on=False)
        sleep(2)

        print "TV turn off"
        ctl.power(on=False)

if __name__ == "__main__":
        main()
