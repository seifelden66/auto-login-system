import csv 
def register():
    with open("C:\\Users\\seife\\OneDrive\\Desktop\\login system\\logs.csv", mode="a+") as f:
        writer = csv.writer(f,delimiter=",")
        email  = input("enter email : ")
        password = input("enter password : ")
        password2 =input("confirm password : ") 
        if password == password2:
                with open("C:\\Users\\seife\\OneDrive\\Desktop\\login system\\logs.csv", mode = "r") as f:
                    reader = csv.reader(f,delimiter= ",")
                    for emails in reader:
                        if email in emails:
                            print("email already exists ")
                            break
                    else:
                        writer.writerow([email, password])
                        print("registered ")
        else:
            print("try again ")


def login():
    email = input("enter email : ")
    password = input("enter password : " )
    with open("C:\\Users\\seife\\OneDrive\\Desktop\\login system\\logs.csv", mode = "r") as f:
        reader = csv.reader(f,delimiter= ",")
        for row in reader:
            if row == [email,password]:
                print("u r logged in ")
                return True
    print("try again")
    return False
request = input("register or login : ")
if request == "register":
    register()
elif request == "login":
    login()
