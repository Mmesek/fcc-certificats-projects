# https://replit.com/@Mmesek/fcc-SHA-1-password-cracker
import hashlib

hashes: dict[str, bytes] = {}
salted_hashes: dict[str, bytes] = {}


def hash_passwords(passwords: list[str]) -> None:
    for password in passwords:
        hashes[hashlib.sha1(password).hexdigest()] = password


def salt_passwords(passwords: list[str], salt: str) -> None:
    for password in passwords:
        salted_hashes[hashlib.sha1(salt + password).hexdigest()] = password
        salted_hashes[hashlib.sha1(password + salt).hexdigest()] = password


def load_file(file: str) -> list[str]:
    with open(file, "rb") as _file:
        return [i.strip() for i in _file.readlines()]


def prepare(password_list: str) -> None:
    passwords = load_file(password_list)
    salts = load_file("known-salts.txt")
    hash_passwords(passwords)
    for salt in salts:
        salt_passwords(passwords, salt)


def crack_sha1_hash(hash: str, use_salts: bool = False, password_list: str = "top-10000-passwords.txt") -> str:
    if not hashes:
        prepare(password_list)

    if use_salts:
        return salted_hashes.get(hash, b"PASSWORD NOT IN DATABASE").decode()
    return hashes.get(hash, b"PASSWORD NOT IN DATABASE").decode()


if __name__ == "__main__":
    print(
        crack_sha1_hash(
            hash=input("SHA1 Hash to compare against known password list: "),
            use_salts=bool(input("Use salts? (0/1. Default: 0) ") or 0),
            password_list=input("Password list to use (Default: top-10000-passwords.txt): ")
            or "top-10000-passwords.txt",
        )
    )
