import csv

def write_into_csv(info_list):
    with open("student_info.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        if (csv_file.tell()==0): # for creating a header in the csv file
            writer.writerow(["Name", "Age", "Contact Number", "Email ID"])
            
        writer.writerow(info_list)

if __name__ == '__main__':
    cond = True
    stud_num=1 # for keeping the count of no.of students
    
while (cond):
    student_info = input("Enter each student's information in given format (Name Age Contact_no Email):")
    print("Entered student's information is: "+ student_info)

    student_info_list = student_info.split(" ")

    print("\nThe entered information is ~~ \nName: {}\nAge: {}\nContact_no: {}\nEmail: {}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

    choice = input("Is the entered information correct? (Yes/No):")
    if (choice=="Yes" or choice=="yes"):
        write_into_csv(student_info_list)

        cond_check = input("Enter your choice if you want to enter information for another student (Yes/No):")
        if (cond_check=="Yes" or cond_check=="yes"):
            cond = True
            stud_num+=1
        elif (cond_check=="No" or cond_check=="no"):
            cond = False
    elif (choice=="No" or choice=="no"):
        print("\nPlease enter correct information!") 
