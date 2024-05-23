import random
import string

pass_len =12
CharVal = string.ascii_letters + string.punctuation + string.digits

password = ""
for i in range(pass_len):
    password = password + random.choice(CharVal)

print("Your Random Password is : " ,password)