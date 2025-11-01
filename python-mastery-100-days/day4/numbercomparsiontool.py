num1 =float(input("enter 1st num:")) 
num2 =float(input("enter 2nd number:"))

if num1> num2:
    print(f"1st {num1} is greater than 2nd {num2}")
elif num1 == num2:
    print(f"both number are equal {num1} = {num2}")
else:
    print(f"2nd {num2} is greater than 1st {num1}")
    
if num1 == 0 and num2 == 0:
    print("both numbers are zero")
else:
    print(f"any one num is zero {num1} or {num2}")