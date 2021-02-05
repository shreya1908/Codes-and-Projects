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
    
