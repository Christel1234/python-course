def rot13(plaintext: str) -> str:
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryption = ""
    for char in plaintext:
        if char.islower():
            encryption += abc[(abc.find(char) + 13) % 26]
        elif char.isupper():
            encryption += ABC[(ABC.find(char) + 13) % 26]
        else:
            encryption += char
    return encryption


if __name__ == '__main__':
    print(rot13("ohvyqvat n jro NCV sebz fpengpu"))
