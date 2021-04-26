secret = "swordfish"
pw = ""
count = 0
auth = False
max_attempt = 3

while pw != secret:
    count += 1
    if count > max_attempt:
        print("Calling the FBI")
        break
    pw = input(f'{count}: '"What is your password?")
else:
    auth = True
    print("Authorized")
