# 📡 Task 2: Basic Network Sniffer

## 📌 Project Overview
This project is a Python-based **Network Packet Sniffer** developed for the **CodeAlpha Cybersecurity Internship**. The tool captures, decodes, and analyzes live network traffic packets in real-time to inspect protocol structures and payload data[cite: 1].

---

### ⚙️ Features & Functionality
* **Packet Capture:** Intercepts incoming and outgoing network traffic using the `scapy` library[cite: 1].
* **Protocol Analysis:** Decodes IP headers, TCP/UDP layers, and ICMP packets[cite: 1].
* **Data Extraction:** Displays source IP, destination IP, port numbers, and raw payload contents[cite: 1].
* **Multi-Platform Support:** Executable on both Linux environments (Kali Linux) and Windows systems[cite: 1].

---

### 🛠️ Prerequisites & Execution

1. **Install Scapy:**
   ```bash
   pip install scapy

   python network_sniffer.py


   Files Included
network_sniffer.py: Primary Python implementation for packet sniffing[cite: 1].

README_Kali.md: Specific setup and privilege escalation guidelines for Kali Linux execution.

Output Screenshots: Practical demonstration of captured network packets.

👤 Author
Name: Nada Mamdouh

Domain: Cyber Security (SOC Analyst)

Internship: CodeAlpha Cybersecurity Internship
