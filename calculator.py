print("Welcome to the Calculator!")

# Get the user's answer
user_operator = input("Your operator (+, -, /, *): ")
user_firstnumber = input("Your first (whole) number:")
user_secondnumber = input("Your second (whole) number:")

#print(user_firstnumber)

if user_operator =="+":
    result = int(user_firstnumber) + int(user_secondnumber) 
elif user_operator =="-":
    result = int(user_firstnumber) - int(user_secondnumber)
elif user_operator =="/":
    result = int(user_firstnumber) / int(user_secondnumber)
else: 
    user_operator =="*"
    result = int(user_firstnumber) * int(user_secondnumber)

print("The result is:", result)
