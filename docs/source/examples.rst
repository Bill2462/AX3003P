========
Examples
========

Simple example
^^^^^^^^^^^^^^
Hello world type example for the AX3003P programmable power supply
library. This example sets the output voltage to 1V, output current
to 0.01A, enables the output and then samples the output voltage and current
for 30 seconds.

Usage
::
    simple.py [device]

Example usage
::
    simple.py /dev/ttyUSB0

simple.py: https://github.com/Bill2462/AX3003P/blob/master/examples/simple.py


Overcurrent and Overvoltage protection example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Example that demonstrates the overcurrent protection (OVP)
and overvoltage protection (OVC).
This script sets the OVP level to 5V and OCP to 0.3A.
Then slowely increases the voltage until the OVP trips.
Next the OVP is reseted and the same procedure is repeated with the OCP.

Usage
::
    testProtection.py [device]

Example usage
::
    testProtection.py /dev/ttyUSB0

testProtection.py: https://github.com/Bill2462/AX3003P/blob/master/examples/testProtection.py