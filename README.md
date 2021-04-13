## SendFrames ##

a simple python utility to send image frames from one computer to another

usage: 
on the computer with a webcam:

`$ python3 server.py [Port]`

on the computer to recieve the video

`$ python3 client.py [Host IP] [Port]`

if a port is not provided it will default to 42699

Features:

 * Low CPU usage
 * Zero to Low Latency (after initial startup)

Dependencies:
python opencv

`pip3 install opencv-python`


FAQ:

Q. why not just use ffmpeg?

A. This method does not encode the video, leading to much higher bandwidth usage, but at dramatically lower cpu usage. On a LAN network this is fine. a 720p source will take around 100mbits/s of data, but on my core i5 macbook took around 30% of one thread of cpu. also making this was more fun.



