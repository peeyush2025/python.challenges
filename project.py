import random
import string
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
password_length = 12
password = ''.join(random.sample(chars, password_length))
password_list = list(password)
random.shuffle(password_list)
final_password = ''.join(password_list)
print("Your Random Password:", final_password)