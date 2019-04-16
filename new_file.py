import subprocess
failed = []
failed1 = []

cmd = "cat /sys/class/net/eth0/statistics/rx_bytes"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()
failed.append(output)
print failed[0]

cmd1 = "cat /sys/class/net/eth0/statistics/rx_bytes"
process = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE)
output, error = process.communicate()
failed1.append(output)
print failed1[0]

calculate = ((int(failed1[0]) - int(failed[0])) * 8) / 1024
print calculate


import subprocess
import time


def myFunc():
    cmd = "cat /sys/class/net/eth0/statistics/rx_bytes"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output


value = myFunc()
print value
time.sleep(1)
value2 = myFunc()
print value2

calculate = ((int(value2) - int(value) * 8) / 1024
    print (calculate)