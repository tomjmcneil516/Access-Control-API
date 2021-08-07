import sys
import os

Users_file = open("Users.txt", 'a+')
Domains_file = open("Domains.txt", 'a+')
Types_file = open("Types.txt", 'a+')
Access_file = open("Accesses.txt", 'a+')


def Search(target, file):
    for line in file:
        if target == (line.split(' ')[0]):
            return True
    return False

def SearchLine(target, file):
    for line in file:
        if target == (line.split(' ')[0]):
            return line.split(' ', 1)[1]
    return ""

def Authenticate(MyUser, MyPassword):
    f = open('Users.txt', 'r')
    for line in f:
        if line.strip('\n') == (MyUser + " " + MyPassword):
            return True
    return False

if len(sys.argv) < 2:
    print("Error: No Command")
    CMD = ""
else:
    CMD = sys.argv[1]


if CMD == "AddUser":

    if len(sys.argv) < 3:
        print("Error: Empty username")
    else:
        Username = sys.argv[2]
        Users_file = open("Users.txt", 'r')
   
        if Search(Username, Users_file) == True:
            print("Error: Duplicate username")
        else:
            if len(sys.argv) < 4:
                Password = ""
            else:
                Password = sys.argv[3]
            Users_file = open("Users.txt", 'a')
            Users_file.write(Username + " " + Password + "\n")
            print("Success")


elif CMD == "Authenticate":
    Username = sys.argv[2]
    Password = sys.argv[3]
    Users_file = open("Users.txt", 'r')

    if Search(Username, Users_file) == False:
        print("Error: No such user")
    else:
        if Authenticate(Username, Password) == False:
            print("Error: Wrong Password")
        else:
            print("Success")


elif CMD == "SetDomain":

     if len(sys.argv) < 4:
        print("Error: Missing Domain")

     else:
        Username = sys.argv[2]
        Domain = sys.argv[3]
        Users_file = open("Users.txt", 'r')
        Domains_file = open("Domains.txt", 'r')

        if Search(Username, Users_file) == False:
            print("Error: User not found")

        elif Search(Domain, Domains_file) == False:
            Domains_file = open('Domains.txt', 'a')
            Domains_file.write(Domain + " " + Username + "\n")
            print("Success")

        else:
            with open("Domains.txt","r") as f:
                newline=[]
                for word in f.readlines():        
                    newline.append(word.replace(Domain,Domain + " " + Username))
            with open("Domains.txt","w") as f:
                for line in newline:
                    f.writelines(line)
            print("Success")


elif CMD == "DomainInfo":
     if len(sys.argv) < 3:
        print("Error: Domain is empty")
     else:
        Domain = sys.argv[2]
        Domains_file = open('Domains.txt', 'r')
        for line in Domains_file:
            if Domain == (line.split(' ')[0]):
                for word in line.split():
                    if(word != Domain):
                        print(word)



elif CMD == "SetType":

    if len(sys.argv) < 4: 
         print("Error: Type is empty")
    else:
        Object = sys.argv[2]
        Type = sys.argv[3]
        Types_file = open("Types.txt", 'r')

        if Search(Type, Types_file) == False:
            Types_file = open('Types.txt', 'a')
            Types_file.write(Type + " " + Object + "\n")
            print("Success")

        else:
            with open("Types.txt","r") as f:
                newline=[]
                for word in f.readlines():        
                    newline.append(word.replace(Type,Type + " " + Object))
            with open("Types.txt","w") as f:
                for line in newline:
                    f.writelines(line)
            print("Success")



elif CMD == "TypeInfo":
     if len(sys.argv) < 3:
        print("Error: Type is empty")
     else:
        Type = sys.argv[2]
        Types_file = open('Types.txt', 'r')
        for line in Types_file:
            if Type == (line.split(' ')[0]):
                for word in line.split():
                    if(word != Type):
                        print(word)


elif CMD == "AddAccess":
     
     if len(sys.argv) < 3:
        print("Error: Operation is empty\n")
     elif len(sys.argv) < 4:
        print("Error: Domain is empty\n")
     elif len(sys.argv) < 5:
        print("Error: Type is empty")
     else:
         Operation = sys.argv[2]
         Domain = sys.argv[3]
         Type = sys.argv[4]

         Types_file = open('Types.txt', 'r')
         Domains_file = open('Domains.txt', 'r')

         if Search(Type, Types_file) == False:
             Types_file = open('Types.txt', 'a')
             Types_file.write(Type + "\n")

         if Search(Domain, Domains_file) == False:
             Domains_file = open('Domains.txt', 'a')
             Domains_file.write(Domain + "\n")

         Access_file = open('Accesses.txt', 'a')
         Access_file.write(Operation + " " + Domain + " " + Type + "\n")
         print("Success")



elif CMD == "CanAccess":
     Access_Granted = False
     Operation = sys.argv[2]
     User = sys.argv[3]
     Object = sys.argv[4]

     Access_file = open('Accesses.txt', 'r')

     for line in Access_file:
         if Operation == (line.split(' ')[0]):

            Domain = line.split(' ')[1]
            Type = line.split(' ')[2].strip("\n")

            Types_file = open('Types.txt', 'r')
            Domains_file = open('Domains.txt', 'r')

            Domain_vals = SearchLine(Domain, Domains_file)
            Type_vals = SearchLine(Type, Types_file)

            if (User in Domain_vals) and (Object in Types_vals):
                print("Success")
                Access_Granted = True
                break

     if Access_Granted == False:
         print("access denied")


            
else:
    if CMD != "":
        print("Error: Command not recognized")




Users_file.close()
Domains_file.close()
Types_file.close()
Access_file.close()


     
