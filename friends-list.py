friends=[]
flag=True
while flag:
    name=input("write your friends name, end if finished    :   ")
    
    if name=="end":
        flag=False
    elif not name.isalpha():
        print("error")
    else:
        friends.append(name)
   
Friend=""

for index in range(0,len(friends)):

    Friend="+".join(friends)

print(Friend)
print('Greaaaaat')
