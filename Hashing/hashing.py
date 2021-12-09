def hash(string: str) -> int:
    total = 0
    multiplication = 1
    M = 1000

    for ind in range(len(string)):
        if ind % 4 == 0:
            multiplication = 1
        else:
            multiplication *= 256
        total += multiplication * ord(string[ind])

    return abs(total) % M


s1 = "AhmedmeshrefPassword"
s2 = "AhmedMeshrefPassword"
s3 = "pa$$$wordMeshrefasss"
print(f"Hash for {s1} = '{hash(s1)}'")
print(f"Hash for {s2} = '{hash(s2)}'")
print(f"Hash for {s3} = '{hash(s3)}'")
