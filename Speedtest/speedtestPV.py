# Vidmar P.
# Pyton version 3.10.6 64-bit
# Pytonshell:
#   pip install speedtest-cli
#   speedtest-cli --version

import sys
from xml.etree.ElementTree import tostring

import speedtest
# st = speedtest.Speedtest()
# st.download()
# st.upload()
# st.results.ping

import time as iTime
#  time.sleep( sekond )
import matplotlib.pyplot as plt

import datetime
# now = datetime.datetime.now()
# print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# MAIN-Program -----------------------------------------------------------------------------------

dwonloadDataList = []
uploadDataList = []
XAchsTime = []

now = datetime.datetime.now()
st = speedtest.Speedtest()
servernames = []

delayTime = 1  # Sekonds
numberOfMeasurements = 3

XTime = 0

print("Start at ", now.hour, ":", now.minute,
      "|", now.day, ".", now.month, ".", now.year)
print("delayTime:", delayTime, "sek",
      "numberOfMeasurements:", numberOfMeasurements)


# SPEEDTEST --
for x in range(numberOfMeasurements):

    downloadMBs = st.download() / 1000000
    dwonloadDataList.append(downloadMBs)

    uploadMBs = st.upload() / 1000000
    uploadDataList.append(uploadMBs)

    print("Download: ", downloadMBs)
    print("Upload  : ", uploadMBs)

    XTime = XTime + delayTime
    XAchsTime.append(XTime)

    iTime.sleep(delayTime)

# PLOT --
# (x-Value,y-Value)
plt.plot(XAchsTime, dwonloadDataList, 'r--')
plt.plot(XAchsTime, uploadDataList)
plt.grid()
plt.title("SpeedTest")
plt.ylabel('Download(red) Upload(blue) [MBs] ')
plt.xlabel('Time [sec]')
plt.show()
