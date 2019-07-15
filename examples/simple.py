"""
Hello world type example for the AX3003P programmable power supply
library. This example will set the output voltage to 1V, output current
to 0.01A, enables the output and then samples the output voltage and current
for 30 seconds.

Usage: python3 helloWorld.py [device]
Example: Example: python3 helloWorld.py /dev/ttyUSB0
"""
# This file is part of AX3003P library.
# Copyright (c) 2019 Krzysztof Adamkiewicz <kadamkiewicz835@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in the
# Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions: THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import time
import AX3003P

# Get the port selection from the command line argument.
if len(sys.argv) < 2:
    print("usage: python3 helloWorld.py [device]")
    print("Example: python3 helloWorld.py /dev/ttyUSB0")
    sys.exit(1)
port = sys.argv[1]

# connect to the power supply
psu = AX3003P.connect(port)

# set the voltage and current values
psu.setVoltage(1.0)
psu.setCurrent(0.01)

# enable the output  
psu.enableOutput()
time.sleep(0.5) # wait 0.5s to allow the voltage to stabilize

# take measurements of voltage and current for 30 seconds
timeEnd = time.time()+30
while time.time() < timeEnd:
    voltage = psu.measureVoltage()
    current = psu.measureCurrent()
    print(str(voltage) + "V " + str(current) + "A")

# disable the output
psu.disableOutput()

# disconnect from the power supply
psu.disconnect()
