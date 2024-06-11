from src.capture import start_capture
from src.analyzer import load_signatures, analyze_packet
from src.logger import log_intrusion

def packet_callback(packet):
    name, pattern = analyze_packet(packet, signatures)
    if name:
        log_intrusion(name, packet.summary())

if __name__ == "__main__":
    signatures = load_signatures('data/signatures.txt')
    start_capture(packet_callback, count=0)
