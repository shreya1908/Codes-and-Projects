n = int(input("Enter how many terms? "))  
n1 = 0  
n2 = 1  
count = 2    
if n <= 0:  
   print("Plese enter a positive integer")  
elif n == 1:  
   print("Fibonacci sequence:")  
   print(n1)  
else:  
   print("Fibonacci sequence:")  
   print(n1,n2,end=' ')  
   while count < n:  
       nth = n1 + n2  
       print(nth,end=' ')   
       n1 = n2  
       n2 = nth  
       count += 1 
