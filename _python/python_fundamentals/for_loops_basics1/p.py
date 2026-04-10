for i in range(51):
    print(i,end=" ")


print("\n\n\n#################################\n\n\n")
for i in range(5,1001,5):
    print(i,end=" ")

print("\n\n\n#################################\n\n\n")
for i in range(100):
    if(i%5==0):
        print("Coding",end=" ")
    elif(i%10==0):
        print("Coding Dojo",end=" ")
    else:
        print(i,end=" ")
print("\n\n\n#################################\n\n\n")

sum=0
for i in range(500000):
    if(i%2!=0):
        sum+=i
print(sum)
print("\n\n\n#################################\n\n\n")

for i in range(2018,0,-4):
    print(i,end=" ")

print("\n\n\n#################################\n\n\n")

lownum=2
highnum=9
mult=3
for i in range(lownum,highnum+1):
    if(i%mult==0):
        print(i,end=" ")

print("\n\n\n#################################\n\n\n")
