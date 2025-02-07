import pyshark

capture = pyshark.LiveCapture(interface='lo')  # Use 'Wi-Fi' for Windows, 'eth0' for Linux
print("Capturing network packets...")

for packet in capture.sniff_continuously(packet_count=5):
    print(packet)