import random

lower = 'zxcvbnmasdfghjklqwertyuiop'
upper = 'ZXCVBNMASDFGHJKLQWERTYUIOP'
numbers = '0123456789'
symbols = '[ ] { } ( ) * ; :'

all = lower + upper + numbers + symbols

lenght = 16

for x in range(10):
    password = " ".join(random.sample(all,lenght))
    print(password)
