current_users = ['Kwadwo','Christabel','Ella','Ama','Prince']
new_users = ['Christabel','John','Ama','John','Malex']

current_users = [user.lower()for user in current_users]

for user in new_users:
    if user.lower() in current_users:
        print(f"The username {user} is not available. Please enter a new username.")
    else:
        print(f"The username  is available.")


#QUESTION 2

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)
