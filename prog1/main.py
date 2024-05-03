f = open("password.txt", "r")
file_password = f.read().strip()

password = input("Enter password: ").strip()
if file_password == password:
    print("Access Granted")
else:
    print("Password doesn't match")
