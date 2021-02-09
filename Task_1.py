Program 1(the program accepts the radius of a circle from the user and computes area): 
radius=float(input("Input the radius of the circle: "))
print("The area of the circle with radius", radius, "is:", 3.14*radius**2)




Program 2(the program accepts a filename from the user and print the extension of that):
filename=str(input("Enter filename:"))
x=filename.split(".")
if x[1]=="py":
    print ("The extension of the file is: 'python'")
elif x[1]=="txt":
    print ("The extension of the file is: 'text'")
elif x[1]=="java":
    print ("The extension of the file is: 'java'")
elif x[1]=="c":
    print ("The extension of the file is: 'C'")
elif x[1]=="docx":
    print ("The extension of the file is: 'document'")
else:
    print ("The extension of the file is: 'other'")
