num = int(input("Enter a number: "))
factCount = 0
i = 2
while i <= num/2:
    if( num % i == 0):
        factCount = factCount + 1 # 1
    i = i + 1
if factCount == 0: # 1 < 2
    print(f"prime:{factCount}")
else:
    print("not prime")

# i start from 2 
# loop num/2 i.e num 8 = 3
# prime 7 => 2, 3 num = 7 
# 1 and itself , loop num/ 2 
#  num = 4
#  loop=> num / 2 => 4 /2 => 2