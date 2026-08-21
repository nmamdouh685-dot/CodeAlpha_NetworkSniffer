"""
==================================================
 Basic Network Sniffer  —  CodeAlpha Task 1
==================================================
This program captures live network traffic on your computer and
shows useful information about each packet: source IP, destination
IP, protocol (TCP / UDP / ICMP), and a short preview of the data
being sent.

WHY WE USE 'scapy':
scapy is a Python library made specifically for building, capturing,
and analyzing network packets. It does the hard, low-level work for
us so we can focus on reading and understanding the traffic.

HOW TO RUN THIS FILE (Windows):
1. Install Npcap first (see the README file next to this script).
2. Open Command Prompt or PowerShell AS ADMINISTRATOR.
   (Right-click it -> "Run as administrator". Packet capture needs
   this permission, or you will get a "permission denied" error.)
3. Run:  python network_sniffer.py
4. Open a browser or any app that uses the internet — you will see
   packets appear live in the terminal.
5. Press CTRL + C to stop capturing.
"""

# scapy.all gives us everything we need: sniffing, and packet layers
# like IP, TCP, UDP, ICMP (these represent different "types" of network data)
from scapy.all import sniff, IP, TCP, UDP, ICMP

# We'll count packets just to show a running total — purely cosmetic.
packet_count = 0


def process_packet(packet):
    """
    This function runs automatically every time scapy captures ONE
    new packet. 'packet' is that single captured packet object.
    We pull out the useful fields and print them in a readable way.
    """
    global packet_count
    packet_count += 1

    # Every packet that has an IP layer contains source & destination
    # addresses. If a packet doesn't have an IP layer (rare), we skip it.
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        source_ip = ip_layer.src
        destination_ip = ip_layer.dst

        # Figure out which protocol is riding on top of IP, since each
        # one carries different useful details.
        if packet.haslayer(TCP):
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            port_info = f"  |  Port {src_port} -> {dst_port}"
        elif packet.haslayer(UDP):
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            port_info = f"  |  Port {src_port} -> {dst_port}"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"  # used by tools like "ping"
            port_info = ""
        else:
            protocol = "OTHER"
            port_info = ""

        # A short preview of the raw payload (the actual data being sent).
        # We only show the first 40 characters so the output stays readable,
        # and we ignore characters that can't be printed as text.
        payload_preview = ""
        if packet.haslayer(TCP) or packet.haslayer(UDP):
            raw_bytes = bytes(packet.payload.payload) if hasattr(packet.payload, "payload") else b""
            try:
                payload_preview = raw_bytes[:40].decode("utf-8", errors="ignore").strip()
            except Exception:
                payload_preview = ""

        print(f"[{packet_count:04d}] {protocol:5s}  {source_ip:15s} -> {destination_ip:15s}{port_info}")
        if payload_preview:
            print(f"        Data preview: {payload_preview}")


def main():
    print("=" * 60)
    print(" Basic Network Sniffer — capturing live traffic...")
    print(" Press CTRL + C to stop.")
    print("=" * 60)

    # sniff() is the core scapy function that captures packets.
    #   prn=process_packet   -> call our function for every packet captured
    #   store=False          -> don't keep packets in memory (saves RAM)
    #   count=0              -> 0 means "capture forever" until we stop it
    sniff(prn=process_packet, store=False, count=0)


if __name__ == "__main__":
    main()
