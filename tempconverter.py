#temperature conveter
units = input("enter your units- c or f? ").strip().lower()
temp = input("enter your temperature: ")
if units == "c" :
    newtemp = float(temp)*1.8 + 32
    newunits = "f"
    print(f"{temp} {units} is equal to {newtemp} {newunits}")
elif units == "f" :
    newtemp = (float(temp)-32)*0.56
    newunits = "c"
    print(f"{temp} {units} is equal to {newtemp} {newunits}")
else:
    print("get lost man")
    
