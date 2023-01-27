email = input("Enter an email")

for e in email:
    if (e == "@"):
        print("An at sign has been entered")
        break;
else: # if break has not been executed
    print("An at sign has not been entered")
