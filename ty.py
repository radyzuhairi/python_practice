count = int(input("Enter numbers count: "))
mysum = 0
            
for x in range(count):
    num = int(input("Enter the number :" + str(x+1) + ": "))
    mysum+= num
    if num==0: continue
    print("sum is ok")          
print(mysum)                      
                      
