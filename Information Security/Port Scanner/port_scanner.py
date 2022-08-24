# https://replit.com/@Mmesek/fcc-port-scanner
import socket
from common_ports import ports_and_services


def get_open_ports(target: str, port_range: list[int], verbose: bool = False) -> str | tuple[int]:
    open_ports = []
    socket.setdefaulttimeout(0.5)

    if not target.split(".")[-1].isalpha():
        try:
            socket.inet_aton(target)
            try:
                _ = socket.gethostbyaddr(target)
                target = _[0]
                ip_address = _[-1][0]
            except socket.herror:
                ip_address = target
        except socket.error:
            return "Error: Invalid IP address"
    else:
        try:
            ip_address = socket.gethostbyname(target)
        except socket.error:
            return "Error: Invalid hostname"

    def scan(port: int):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((ip_address, port))
            open_ports.append(port)
        except (ConnectionRefusedError, socket.timeout):
            pass
        finally:
            s.close()

    port_range[1] += 1

    for x in range(*port_range):
        scan(x)

    if verbose:
        port_template = "{port}      {service_name}"
        ports = "\n".join(
            [port_template.format(port=f"{p:<3}", service_name=ports_and_services.get(p)) for p in open_ports]
        )
        host = f"{target} ({ip_address})" if target != ip_address else ip_address
        return f"""Open ports for {host}\nPORT     SERVICE\n{ports}"""

    return open_ports


if __name__ == "__main__":
    print(
        get_open_ports(
            input("IP Address or URL to scan: "),
            [int(input("Starting Port (ex: 21): ") or 21), int(input("Final Port (ex: 22): ") or 22)],
            True,
        )
    )
