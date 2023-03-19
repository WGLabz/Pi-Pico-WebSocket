# The used lib from http://bit.ly/3n2t9il
import uwebsockets.ws_client
from machine import Timer


class wsclient:
    def initialize(self, uri):
        self.websocket = uwebsockets.ws_client.connect(uri)
        self.reconnect = True
        self.uri = uri
        tim = Timer()
        tim.init(period=1000, callback=self.msg_check)

    def msg_check(self, timer):
        print(self.websocket.open)
        if not self.websocket.open:
            self.websocket = uwebsockets.client.connect(self.uri)

        resp = self.websocket.recv()    
        print(resp)

    def send(self,msg):
        self.websocket.send(msg)
    
