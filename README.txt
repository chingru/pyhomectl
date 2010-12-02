Python LG TV
============

 * Author: **Thomas Medhurst &lt;tom [AT] tommed.co.uk&gt;**
 * Project: **Python LG TV (pylgtv)**
 * License: http://www.gnu.org/licenses/gpl.html **GPL v3**


Project Summary
---------------

This project enables you to control your LG Television from a computer over a crossed serial cable.

It is tested in a http://goo.gl/a8TJp **LG 47LH3000**, so if you have issues, please send a patch over with the make and model of your TV and I will integrate!


Pre-requisites
--------------

 * Python (2.6+) http://python.org 
 * pyserial http://pyserial.sourceforge.net/ 
 * A null modem cable (aka. reversed/crossed serial RS-232) - about £1 from Amazon
 * GNU/Linux (developed with Ubuntu 10.10)

Test
----

 1. Open up pyhomectl/test/example_config.ini and edit it appropriately
 2. Now run cd into the pyhomectl module and run cmd.py with arguments:
        $python cmd.py -vi ./test/example_config.ini tv power on
        $python cmd.py -vi ./test/example_config.ini tv mute on
        $python cmd.py -vi ./test/example_config.ini tv mute off
        $python cmd.py -vi ./test/example_config.ini tv power off

**More details to follow soon!**
