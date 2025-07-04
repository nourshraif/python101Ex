
message=""
numberIn=int(input("Enter a Number\n"))
if(numberIn % 2==0):
    message="The number is even"
    if(numberIn % 4==0):
        message+=" and it's divisible by 4"
else:
    message="The number is odd"
print(message)            

dividend=int(input("Enter the Dividend\n"))
divisor=int(input("Enter the divisor\n"))
if(dividend%divisor==0):
    print("The numbers are divided evenly")
else:
    print("The numbers are not divided evenly")    