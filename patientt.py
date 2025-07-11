
Name=['Abu']
Phone_Number=["03090321073"]
Disease=['Animakar']
Age=['12']
Consultant=['Ahmed']
Date=['12-01-2022']
Time=['12:00']
Appointment_number=['21']
Fees=['5000']
while True:
    print("1-View the Data: ")
    print("2-Add the Data: ")
    print("3-Update the data: ")
    print("4-Search the Data: ")
    print("5-Delete the Data: ")
    print("6-Exit")
    choice=int(input("Enter the number: "))

    if choice==1:
     print("="*130)
     print("{:<15}{:<15}{:<15}{:<6}{:<15}{:<15}{:<15}{:<26}{:<16}".format("Name","Phone_Number","Disease","Age","Consultant","Date","Time","Appointment_number","Fees"))   
     print("="*130)
     for i in range(len(Name)):
        print("{:<15}{:15}{:<15}{:<6}{:<15}{:<15}{:<15}{:<26}{:<16}".format(Name[i],Phone_Number[i],Disease[i],Age[i],Consultant[i],Date[i],Time[i],Appointment_number[i],Fees[i]))
    elif choice==2:
       while True:
          print("1-Enter the Data: ")
          print("2-Exit")
          ch=int(input("Enter the number: "))
          if ch==1:
            Name.append(input("Enter a Name: "))
            Phone_Number.append(input("Enter the number: "))
            Disease.append(input("Enter the Disease: "))
            Age.append(input("Enter a Age: "))
            Consultant.append(input("Enter the Doctor Name: "))
            Date.append(input("Enter the Date: "))
            Time.append(input("Enter the Time: "))
            Appointment_number.append(input("Enter the Appointment: "))
            Fees.append(input("Enter the Fees: "))
          elif ch ==2:
             break
    elif choice==3:
       while True:
            print("1-Update the data: ")
            print("2-Exit")
            choice=int(input("Enter the Number: "))
            if choice==1:
               name = input("Enter the name: ")
               phone_Number = input("Enter the Phone_Number : ")
               index=-1
               for i in range(len(Name)):
                if Name[i]==name and Phone_Number[i]==phone_Number:
                  index=i
                  break
               if index==-1:
                  print("Not Found: ")
               else:
                  while True:
                     print("\nWhat do you want to update?")
                     print("1- Name")
                     print("2-Phone_Number: ")
                     print("3- Disease")
                     print("4- Age")
                     print("5- Doctor")
                     print("6- Date")
                     print("7-Time")
                     print("8-Appointment_Number")
                     print("9-Fees")
                     print("10-All")
                     print("11-Exit")
                     choice = int(input("Enter your choice: "))
                     if choice==1:
                        Name[index]=input("Enter the name: ")
                     elif choice==2:
                        phone_Number[index]=input("Enter the Phone Number: ")   
                     elif choice==3:
                        Disease[index]=input("Enter the Disease: ")
                     elif choice==4:
                        Age[index]=input("Enter the Age: ")
                     elif choice==5:
                        Consultant[index]=input("Enter the Doctor Name: ")
                     elif choice==6:
                        Date[index]=input("Enter the Date: ")
                     elif choice==7:
                        Time[index]=input("Enter the time: ")
                     elif choice==8:
                        Appointment_number[index]=input("Enter the Appointment_number: ")
                     elif choice==9:
                        Fees[index]= input("Enter the Fees")  
                     elif choice==10:
                        Name[index]=input("Enter the name: ")
                        Disease[index]=input("Enter the Disease: ")
                        Age[index]=input("Enter the Age: ")
                        Consultant[index]=input("Enter the Doctor Name: ")
                        Date[index]=input("Enter the Date: ")
                        Time[index]=input("Enter the time: ")
                        Fees[index]= input("Enter the Fees")
                        Appointment_number[index]=input("Enter the Appointment_number: ")
                     elif choice==11:
                       break
            elif choice==2:
               break
    elif choice==4:
        while True:
             print("1-Search a Student more")
             print("2-Exit")
             choice =int(input("Enter the number: "))
             if choice==1:
               search_name=input("Enter the name to search: ")
               Phone_Number = input("Enter the Phone Number : ")
               found = False
               print("\nSearch Result: ")
               for i in range(len(Name)):
                  if Name[i]==search_name and Phone_Number[i]==phone_Number:
                   print(Name[i],"\t",Phone_Number[i], "\t", Disease[i], "\t",Age[i], "\t", Consultant[i],"\t",Date[i],"\t",Time[i],"\t",Appointment_number[i],Fees[i])
                  found=True
               if not found:
                print("No student found that name")
             elif choice==2:
                 break
    elif choice==5:
         while True:
            print("1-Delete the student more")
            print("2-Exit")
            choice =int(input("Enter the number: "))
            if choice==1:
              delete = input("Enter the name of student to delete: ")
              Phone_Number = input("Enter the Phone Number : ")
              del_index=-1
              for i in range(len(Name)):
               if Name[i]==delete and Phone_Number[i]==phone_Number:
                   del_index=i
                   break
              if del_index==-1:
                   print(delete,"not found")
              else:
                del Name[del_index]
                del Phone_Number[del_index]
                del Disease[del_index]
                del Age[del_index]
                del Consultant[del_index]
                del Date[del_index]
                del Time[del_index]
                del Appointment_number[del_index]
                del Fees[del_index]
                print("Student deleted successfully.")
            elif choice==2:
             break
    elif choice == 6:
       break
