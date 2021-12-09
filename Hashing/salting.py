import os


def generateSalt(saltLength: int) -> str:
    # calculate a random salt value with a giving length
    return str(os.urandom(saltLength)[2:])


def hashWithSalt(string: str) -> int:
    saltedString = string + generateSalt(5)
    total = 0
    multiplication = 1
    M = 1000
    for ind in range(len(saltedString)):
        if ind % 4 == 0:
            multiplication = 1
        else:
            multiplication *= 256
        total += multiplication * ord(saltedString[ind])
    return abs(total) % M


s1 = "AhmedmeshrefPassword"
s2 = "AhmedMeshrefPassword"
s3 = "pa$$$wordMeshrefasss"
print(f"Hash & Salt for {s1} = '{hashWithSalt(s1)}'")
print(f"Hash & Salt for {s2} = '{hashWithSalt(s2)}'")
print(f"Hash & Salt for {s3} = '{hashWithSalt(s3)}'")
