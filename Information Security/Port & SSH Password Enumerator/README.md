# Network Attacker
Due to scapy reasons, it'll only work on Linux (Windows requires additional dependencies) when run as root (for example using sudo).
Additionally, make sure there is `PasswordList.txt` file in directory (Though, it's only needed when scan is finished)

Tasks 3-40 are inside `Network Attacker.py`, Task 41 is in file `Task_41.png`

As an extra, script can attempt SSH bruteforce on another port if 22 is closed (for example when server is on another port, it happens)

# Installation
*(also known as Task 2)*
```sh
python3 -m pip install scapy
```

# Usage
```sh
sudo python3 Network\ Attacker.py
```
