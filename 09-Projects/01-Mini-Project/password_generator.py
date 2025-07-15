import random
import string

pw_len = 15

charValues = string.ascii_letters + string.digits + string.punctuation

# list comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pw_len)])

# password = ""
# for i in range(pw_len):
#     password += random.choice(charValues)


print("Your random password is:", password)


