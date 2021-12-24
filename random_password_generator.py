from random import randint

#random password with lowercase, uppercase, and special characters
password = ""
for i in range(10):
    i = chr(randint(65, 90)).upper()
    j = chr(randint(65, 90)).lower()
    for n in range(0, 6):
        n = str(randint(0, 9))
        for s in range(0,3):
            s = chr(randint(33, 47))
    password = str(password) + n + i + j + s
print(password)
