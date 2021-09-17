# ARP-Spoofer
ARP Sppofing tool. It takes to ip one is target ip and another is spoof ip (the ip which it pretend to be).
Only we provide the target ip , target mac it finds itself.
Firstly it will spoof the ip then all the traffic will pass through our network ,now we can manipulate the victim data.
If user terminates the program by using keyboard intrrupt then the spoofed is resetted back to default ip configuration.

<br/>..........................................<br/>
Installation guide:<br/><br/>
sudo apt update<br/>
sudo apt install python3<br/>
sudo apt install python3-pip<br/>
git clone https://github.com/ravi518/ARP-Spoofer.git <br/>
<br/><br/>
python3 arp_spoof.py <br/>
usage: arp_spoof.py [-h] [-t TARGET] [-s SPOOF]
<br/><br/>
optional arguments:<br/>
  -h, --help            show this help message and exit<br/>
  -t TARGET, --target TARGET
                        Specify the target ip<br/>
  -s SPOOF, --spoof/gateway SPOOF
                        Specify the spoofing/local gateway ip<br/>
