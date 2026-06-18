def login_user(username, password):
    if username == "admin" and password == "1234":
        return "Login successful!"
    else:
        return "Login failed!"


attempt = 1

while attempt <= 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    result = login_user(username, password)

    if result == "Login successful!":
        print(result)
        break
    else:
        remaining_attempts = 3 - attempt
        print(f"{result} You have {remaining_attempts} attempts left.")
        attempt = attempt + 1

if attempt > 3:
    print("Too many failed attempts. Please try again later.")