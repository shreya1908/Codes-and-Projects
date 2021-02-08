mylist1 = []
n = int(input("Enter the number of elements : "))  
for i in range(0, n):
   element = int(input())
   mylist1.append(element)
for p in mylist1:
   if p >= 0:
      print (p)
