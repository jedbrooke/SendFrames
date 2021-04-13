""" 
    run this on the computer where you want to have the feed
    reads the frames from the newtwork and displays them in a window
"""
import cv2
import socket
import sys
import pickle
import struct


def recv_n_bytes(socket,n):
    data = bytearray()
    while len(data) < n:
        packet = socket.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)

    print("read",len(data),"bytes")
    return data

def recv_frame(socket):
    raw_size = recv_n_bytes(socket, 4)
    if not raw_size:
        return None
    frame_size = struct.unpack('>I',raw_size)[0]
    return recv_n_bytes(socket,frame_size)


def main(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    while True:

        frame = pickle.loads(recv_frame(s))
        cv2.imshow("frame",frame)
        cv2.waitKey(1000//30)
    s.close()

if __name__ == '__main__':
    main(sys.argv[1],int(sys.argv[2]))