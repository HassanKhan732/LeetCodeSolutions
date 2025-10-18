roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
UserInput = input("Enter any Roman Value: ").capitalize()
if UserInput in roman:
    val = roman.values
    print(val)
else:
    print("not a roman value")
