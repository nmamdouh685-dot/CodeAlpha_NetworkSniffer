# Basic Network Sniffer — Setup Guide (Kali Linux)

This guide gets `network_sniffer.py` running on Kali Linux, step by step.

## 1. Check Python is installed (it already is on Kali)

Open a terminal and run:
```
python3 --version
```
You should see something like `Python 3.11.x`. Kali comes with Python
pre-installed, so you can skip straight to the next step.

## 2. Install scapy

Kali already includes scapy in most cases, but confirm it's there:
```
sudo apt update
sudo apt install python3-scapy -y
```

## 3. Run the sniffer (needs root — this is required)

Packet capture needs raw socket access, which only the root user has
on Linux. Run the script with `sudo`:

```
cd ~/Desktop        # or wherever you saved the script
sudo python3 network_sniffer.py
```

If you skip `sudo`, you'll get a "Permission denied" / "Operation not
permitted" error — that's expected, just re-run with `sudo`.

## 4. Generate some traffic to capture

While the script is running, open Firefox (built into Kali) in another
window and browse to any website, or run:
```
ping google.com
```
in a second terminal. You'll see packets appear live in the sniffer's
terminal window.

Press `CTRL + C` to stop capturing.

## What you should see

Each line printed looks like this:

```
[0001] TCP    192.168.1.5     -> 142.250.185.78  | Port 51322 -> 443
[0002] UDP    192.168.1.5     -> 8.8.8.8          | Port 54891 -> 53
[0003] ICMP   192.168.1.5     -> 142.250.185.46
```

- **Source IP / Destination IP** — where the packet came from and where it's going
- **Protocol** — TCP (most web traffic), UDP (DNS, streaming), ICMP (ping)
- **Ports** — e.g., port 443 = HTTPS, port 53 = DNS

## Optional: capture only specific traffic

If the output scrolls by too fast, you can filter it. Open the script
and change the `sniff()` line at the bottom to add a `filter`, e.g.:

```python
sniff(prn=process_packet, store=False, count=0, filter="tcp")   # TCP only
sniff(prn=process_packet, store=False, count=0, filter="icmp")  # ping only
sniff(prn=process_packet, store=False, count=20)                # stop after 20 packets
```

## For your GitHub submission

- Include this script and README in your repo `CodeAlpha_NetworkSniffer`.
- Take a screenshot of the terminal output while it's capturing packets
  (this is your proof it works).
- In your LinkedIn video, briefly explain: what a packet is, what
  source/destination IP and protocol mean, and walk through one line
  of your captured output.
