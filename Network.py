from scapy.all import sniff, IP

# Define a callback function to process each packet
def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        print(f"Packet: {ip_src} --> {ip_dst}")

# Capture packets (the interface can be specified if needed, e.g., iface="eth0" for Linux)
print("Starting packet capture...")
sniff(prn=packet_callback, count=10)  # Capture 10 packets; remove count to capture indefinitely
