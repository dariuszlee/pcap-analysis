from json import load, dump
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=1)

def get_all_http_ports():
    tcp = None
    with open("./tcp.json", mode="r", encoding="UTF-8") as f:
        tcp = load(f)
        
    ports = set([ p['_source']['layers']['tcp.port'][0] for p in tcp if 'http2' in p['_source']['layers']])
    return ports

def get_tcp_session(port):
    tcp = None
    with open("./capture.json", mode="r", encoding="UTF-8") as f:
        tcp = load(f)

    session = [ p for p in tcp if port in p['_source']['layers']['tcp']['tcp.port']]
    with open("./session.json", mode="w") as f:
        pp.pprint(session, stream=f)

if __name__ == "__main__":
    port = get_all_http_ports().pop()
    get_tcp_session(port)
