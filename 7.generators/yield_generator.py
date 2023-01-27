# yield will pause the execution of your function and save the state of your function until you decide to use it again

def generatePares(limite):
    num = 1
    print("Start iteration")
    while num < limite:
        yield num * 2
        num += 1
    print("Has reached the limit")

pairs = generatePares(10)

print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print(next(pairs))
print("I do other things...")
print(next(pairs))
print(next(pairs))
print(next(pairs))

print(next(pairs))
