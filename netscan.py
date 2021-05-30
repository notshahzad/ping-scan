import subprocess
import socket


def ping_scan(IP):
    lastdigit = 1
    ishost = "Approximate round trip times in milli-seconds:"
    run = True
    while run:
        ping_ip = str(IP)+str(lastdigit)
        ping = subprocess.Popen(
            ["ping", ping_ip, "-n", "1"], stdout=subprocess.PIPE)
        stdout = ping.communicate()[0]
        stdout = stdout.decode()
        if(ishost in stdout):
            print(str(ping_ip) + " is connected to your wifi")
        else:
            print(str(ping_ip)+" is down")
        lastdigit += 1


ip = socket.gethostbyname(socket.gethostname())
ip = ip.split(".")
ip.remove(ip[3])
IP = "."
IP = IP.join(ip)
IP += "."
ping_scan(IP)
