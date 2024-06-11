from scapy.all import sniff

def start_capture(packet_callback, count=0):
    sniff(prn=packet_callback, count=count)
