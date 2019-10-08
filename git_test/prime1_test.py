number = int(input("enter a number:"))

for num in range(2,number):
    factCount = 0
    i = 2
    while i <= num/2:
        if num % i == 0:
            factCount = factCount + 1 
        i = i + 1
    if factCount == 0:
       print(f"prime:{num}")
    # i = i + 1   
