#PYTHON NUMBER TYPES

print("Welcome to Python Number Methods")
R = "input R for Rounding Calculator"
P = "input P for Power Calculator"
A = "input A for Absolute Value"
Q = "input Q for Quotient & Remainder \n"
print(R)
print(P)
print(A)
print(Q)
user_option = input("Choose any of the operation needed \n")
if user_option == "R":
    print("ROUNDING CALCULATOR")
    user_valueR = float(input("Input your number below \n"))
    roundnum = int(input("input round up to \n"))
    round_cal = str(round(user_valueR, roundnum))
    print(round_cal + " is the answer")
elif user_option == "P":
    print("Power calculator")
    user_valueP = eval(input("input your base number below \n"))
    power = eval(input("Input your power \n"))
    power_cal = pow(user_valueP, power)
    print(power_cal + " is the answer")
elif user_option == "A":
    print("Absolute Value")
    print("Absolute Value is the non negative value of a number")
    user_valueA = eval(input("Input your number \n"))
    absolute = str(abs(user_valueA))
    print(absolute + " is the answer")
elif user_option == "Q":
    print("Quotient & Remainder")
    print("Quotient & Remainder is used to take two numbers and return a pair of numbers consisting of their quotient and remainder"
          "For example, 5 (Divisor) is divided by 2 (Divider) therefore the quotient is 2 and the remainder is 1")
    user_valueQ = eval(input("Input the divisor \n"))
    user_valueQQ = eval(input("input the divisor \n"))
    quotient = str(divmod(user_valueQ, user_valueQQ))
    print(quotient + " is the answer")
else:
    print("error")