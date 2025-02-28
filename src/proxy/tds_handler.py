import pytds
from pytds import tds

class TDSHandler:
    def __init__(self):
        self.sessions = {}

    async def handle_login(self, packet):
        login = tds.Login7.from_packet(packet)
        return login.username, login.password

    def parse_sql_batch(self, data):
        packet = tds.Packet.unpack(data)
        if isinstance(packet.payload, tds.SqlBatch):
            return packet.payload.sql_text
        return None

    def format_response(self, results):
        header = tds.PacketHeader(type=tds.TDS_ROW)
        colmeta = tds.ColumnMetadata(columns=[
            tds.Column(name=k, type=tds.SQL_VARCHAR) 
            for k in results[0].keys()
        ])
        rowdata = [tds.Row(values=row.values()) for row in results]
        return header.pack() + colmeta.pack() + b''.join(r.pack() for r in rowdata)
