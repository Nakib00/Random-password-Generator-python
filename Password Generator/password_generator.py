import random
uperlatter ="ABCDEFGHIGKLMNOPQSTUVWXYZ"
lowerlatter = uperlatter.lower()
digits ="1234567890"
symbols ="/*,.()[]!@$%^&+-?<>|"

uper, lowar, number, symbol = True ,True, True,True

add = ""

if uper:
    add+=uperlatter
if lowar:
    add+=lowerlatter
if number:
    add+=digits
if symbol:
    add+=symbols

length = 15
amount_of_pass = 10

for x in range(amount_of_pass):
    password = "".join(random.sample(add,length))
    print(password)