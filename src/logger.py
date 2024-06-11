import logging

logging.basicConfig(filename='logs/intrusion.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_intrusion(name, packet_summary):
    message = f"Intrusion Detected: {name}, Packet: {packet_summary}"
    logging.info(message)
    print(message)
