## SendFrames ##

a simple python utility to send image frames from one computer to another

FAQ:
Q. why not just use ffmpeg?
A. This method does not encode the video, leading to much higher bandwidth usage, but at dramatically lower cpu usage. On a LAN network this is fine. a 720p source will take around 100mbits/s of data, but on my core i5 macbook took around 30% of one thread of cpu. also making this was more fun.
