a = 0
b = 1
i = 0
print(a,b)
while i < 10:
    sum = a+b
    a = b
    b = sum
    print (sum)
    i = i+1
print(">>>>>done<<<<<<<")
x = int(input("Please enter an integer: "))
print("Enter value",x)
if x < 10:
    print("Less than 10")
elif x < 15:
    print("less than 15")
else:
    print("greater then  15")

print("<<<<<<Range>>>>>>>")
print("<<Range with single>>>")
ranVal = range(5)
for i in ranVal:
    print(i)
print("<<Range with multi>>>")
for i in range(5, 29, 6):
    print(i)