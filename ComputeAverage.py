#prompt the user to enter 3 numbers
'''Number1 = eval(input("Enter the first number: "))
Number2 = eval(input("Enter the second number: "))
Number3 = eval(input("Enter the third number: "))'''

#prompt the user to enter three  numbers simultaneously
Number1, Number2, Number3 = eval(input("Enter three numbers separated by a comma: "))

#compute the average
Average = (Number1 + Number2 + Number3) / 3

#Display the result
print("The average of", Number1, Number2, Number3, "is", Average)
