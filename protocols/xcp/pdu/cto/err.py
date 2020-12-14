from xcp.pdu.packet_base import PacketBase

class Err(Base):
    __slots__ = ("_code")
    
    def __init__(self):
        super(Err, self).__init__(None, pid = 0xFE)
        self._code                          = 0x0
        self.data                           = b''