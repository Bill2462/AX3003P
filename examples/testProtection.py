""" Example that demonstrates the overcurrent protection (OVP)
and overvoltage protection (OVC).
This script sets the OVP level to 5V and OCP to 0.3A.
Then slowely increases the voltage until the OVP trips.
Next the OVP is reseted and the same procedure is repeated with the OCP.
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
from time import sleep
import AX3003P

# Get the port selection from the command line argument.
if len(sys.argv) < 2:
    print("usage: python3 helloWorld.py [device]")
    print("Example: python3 helloWorld.py /dev/ttyUSB0")
    sys.exit(1)
port = sys.argv[1]

# connect to the power supply and enable output
psu = AX3003P.connect(port)

# Set the OVP and OCP level.
print("Setting OVP threshold to 5V...")
psu.setOvpTreshold(5)
print("Setting OCP threshold to 0.5A")
psu.setOcpTreshold(0.3)

print("\n#########  Testing the OVP  #########")
# set the current to 50mA
psu.setCurrent(0.05)

psu.enableOutput()
# slowly increase the voltage until the OVP trips
voltages = [1, 2, 4, 9] # voltages that we are going to test
for voltage in voltages:

    # a little hack to trigger the OVP.
    # Normally PSU won't allow us to set voltage higher then OVP threshold.
    # However we can first turn the OVP off, set the voltage and turn it back on.
    psu.disableOvp()
    sleep(2)
    psu.setVoltage(voltage)
    sleep(4)
    psu.enableOvp()
    sleep(1) # delay to allow the voltage to stabilize

    # check if ovp is tripped
    if psu.ovpTripped():
        status = "TRIP"
    else:
        status = "RDY"

    # print the status
    print("Voltage: " + str(voltage) + "V   OVP: " + status)

    if status == "TRIP":
        break # exit if ovp tripped

# reset OVP and set voltage to 5V
print("Resetting the OVP...")
psu.resetOvp()
psu.setVoltage(5)

#now we have to short the PSU output
print("Short PSU output and press enter to continue")
input()

print("\n#########  Testing the OCP  #########")
psu.enableOutput()

# slowely increase the current until OCP trips
currents = [0.1, 0.2, 0.3, 1.0]
for current in currents:
    psu.disableOcp()
    sleep(2)
    psu.setCurrent(current)
    sleep(4)
    psu.enableOcp()
    sleep(1) # delay to allow the voltage to stabilize

    # check if ovp is tripped
    if psu.ocpTripped():
        status = "TRIP"
    else:
        status = "RDY"

    # print the status
    print("Curent: " + str(current) + "A    OCP: " + status)

    if status == "TRIP":
        break # exit if ocp tripped

#disable output and disconnect
psu.disableOutput()
psu.resetOcp()
psu.disconnect()
