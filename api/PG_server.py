import encodings.utf_8
import socket


class ServerPG(object):
    def __init__(self, serv='10.10.10.10', port=5555):
        self._user = 'root'
        self._pw = 'mega.tech'
        self._tmp = '/tmp/'
        self._host = serv
        self._port = port
        self._sock = None

    def open(self):
        with socket.socket() as self._sock:
            self._sock.connect((self._host, self._port))
            pass

    def close(self):
        if self._sock:
            self._sock.close()
        pass

    def send(self, cmd):
        cmd = cmd + '\n'
        stream = encodings.utf_8.encode(cmd)
        self._sock.sendall(stream[0])

    def sendArbBytes(self, cmd, arbStream, tail=None):
        arbLen = len(arbStream)
        cmd = cmd + ",#4%04d" % (arbLen)
        headStream = encodings.utf_8.encode(cmd)
        headLen = len(headStream[0])
        tailStream = str
        # tail
        if tail is None:
            tailLen = 0
        else:
            tailStream, _ = encodings.utf_8.encode("," + tail)
            tailLen = len(tailStream)

        rawStream = bytearray(headLen + arbLen + tailLen + 1)

        # head
        for i in range(headLen):
            rawStream[i] = headStream[0][i]

        # payload
        for i in range(arbLen):
            rawStream[headLen + i] = arbStream[i]

        # tail
        for i in range(tailLen):
            rawStream[headLen + arbLen + i] = tailStream[i]

        rawStream[-1] = 0x0A
        print(rawStream)
        self._sock.sendall(rawStream)

    def sendArb(self, cmd, arb):

        arbStream, _ = encodings.utf_8.encode(arb)
        self.sendArbBytes(cmd, arbStream)

    def query(self, cmd):
        self.send(cmd)
        data = self._sock.recv(2048)
        buf = data.decode()
        return buf

    def readBytes(self):
        data = self._sock.recv(2048)
        return data

    def readArbBytes(self):
        data = self._sock.recv(2048)
        if (len(data) < 2):
            return None

        # print( data )
        # check the first
        if data[0] != ord('#'):
            return None
        headLen = (data[1]) - 0x30

        # the header
        if (len(data) < (2 + headLen)):
            return None

        lenStr = ""
        for i in range(headLen):
            lenStr = lenStr + chr(data[2 + i])

        payloadLen = int(lenStr)
        if (len(data) < (2 + headLen + payloadLen)):
            return None

        payloads = bytearray(payloadLen)
        for i in range(payloadLen):
            payloads[i] = data[2 + headLen + i]

        return payloads
