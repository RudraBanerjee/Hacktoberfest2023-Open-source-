a = input("Enter the list: ")#Input of list from user
b=[]#Initialisation of final list
for i in range(len(a)):
    c=0 #Used flag value
    for j in range (len(a)):
        if(a[i]==',' or a[i]=='[' or a[i]== ']'):#Used to remove comma and square brackets
            c=1
            break
        if(i==j):#Used to remove comparison between same elements of same place/index
            c=0
            break
        if(a[j]==a[i]):#Used to remove duplicates
            c=1
            break
    if(c==0):#Created a new list and appended the desired elements
        b.append(a[i])
print("The final list is: ",b)#Print of final element
