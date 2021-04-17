import random
import string

def passGen(a):
    letters = string.ascii_lowercase
    numbers = string.digits

    combine = letters + numbers
    rand = random.sample(combine, a)
    password = "".join(rand)
    print(password)