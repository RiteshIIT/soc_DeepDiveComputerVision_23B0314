#Password Generator
import random
import string

all_chars=string.ascii_letters+string.digits+string.punctuation
print(all_chars)

def generator(length):
    password=''
    for i in range(length):
        password+=str(random.choice(all_chars))
    return password

length=int(input("Enter password length : "))
password=generator(length)
print(password)
    