#this is a hello world programself.
from random import randint as r

inp = input("Press any key OR q to Quit ")
while inp!="q":
    num = r(0, 10)
    print(num*" "+"Hello World")
