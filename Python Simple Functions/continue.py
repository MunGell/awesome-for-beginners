numbersTaken = [2, 6, 7, 13, 18, 20]

print("Here are the available numbers")

for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)