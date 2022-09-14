# 1. Write a python script to print MySirG N times on the screen
num=int(input("Enter number of times you want to print MySirG NAME"))
i=1
while(i<=num):
    print(" MySirG ")
    i+=1
print()    

# 2. Write a python script to print first N natural numbers
num=int(input("Enter natural number till you want to print"))
i=1
while(i<=num):
    print(i)
    i+=1
print()    

# 3. Write a python script to print first N natural numbers in reverse order
num=int(input(" Enter number till you want to print first natural numbers in reverse order  "))
i=num
while(i>0):
    print(i)
    i-=1
print() 

# 4. Write a python script to print first N odd natural numbers
num=int(input(" Enter how many number you want to print odd number"))
i=1
while(i<=2*num):
    if i%2!=0:
        print(i)
    else:
        pass
    i+=1
print()        

# 5. Write a python script to print first N odd natural numbers in reverse order
num=int(input(" Enter  how many first N odd natural numbers print in reverse order "))
i=2*num
while(i>=0):
    if i%2!=0:
        print(i,sep=" ")
    else:
        pass
    i-=1
print() 

# 6. Write a python script to print first N even natural numbers
num=int(input("Enter how many first N even natural numbers"))
i=1
while(i<=2*num):
    if i%2==0:
        print(i,sep=" ")
    else:
        pass
    i+=1
print()  

# 7. Write a python script to print first N even natural numbers in reverse order
num=int(input("Enter how many first N even natural numbers in reverse order  you want to print "))
i=2*num
while(i>0):
    if i%2==0:
        print(i)
    i-=1
print()   

# 8. Write a python script to print squares of first N natural numbers
num=int(input("Enter how many number you want to print  squares of first N natural numbers "))
i=1
while(i<=num):
    print(i*i)
    i+=1
print()    

# 9. Write a python script to print cubes of first N natural numbers
num=int(input("Enter how many number you want to print  cubes of first N natural numbers  "))
i=1
while(i<=num):
    print(i*i*i)
    i+=1
print()   
 
# 10. Write a python script to print first 10 multiples of N
num=int(input("Enter print first 10 multiples of N "))
i=1
while(i<=num):
    print(num,"*",i,"=",i*num)
    i+=1
    if i>10:
        break
print()    