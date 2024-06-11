def load_signatures(file_path):
    signatures = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                name, pattern = line.strip().split(':')
                signatures.append((name.strip(), pattern.strip()))
    return signatures

def analyze_packet(packet, signatures):
    for name, pattern in signatures:
        if pattern in packet.sprintf('%TCP.flags%'):
            return name, packet.sprintf('%TCP.flags%')
    return None, None
