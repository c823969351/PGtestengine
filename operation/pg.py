from api.PG_server import ServerPG
from core.result_base import ResultBase

def connect_pg():
    result = ResultBase()
    res = ServerPG.open()