from pathlib import Path
import os

def readfileandfolder():
    path = Path(".")
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please Tell Your File Name:- ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file:- ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY!")
        else:
            print("This File Already Exists!")
    except Exception as err:
        print(f"An error occurred: {err}")


def readfile():
    try:
        readfileandfolder()
        name=input("Which File you want to Read")
        p = Path(name)
        if p.exists() and p.is_file:
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCESSFULLY!")
        else:
            print("THE FILE DOES NOT EXIST!")
    except Exception as err:
        print(f"An error Ocurred as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Tell Which File You Want to Update! :-")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 For Changing the name of the file")
            print("Press 2 for overwritting the Data of your File")
            print("Press 3 for appending some content in your file")
            
            response = int(input("Please tell your Response"))
            if response == 1:
                name2 = input("Tell your new file name :-")
                p2 = Path(name2)
                p.rename(p2)
                exit
            
            if response == 2:
                with open(p,'w') as fs:
                    data = input("Tell what you want to write it will overwrite the data")
                    fs.write(data)
                    exit

            if response ==3:
                with open(p,'a') as fs:
                    data = input("Tell what you want to append!")
                    fs.write(" "+data)
                    print("Data Updated sucessfully!")
                    exit
    except Exception as err:
        print(f"An Error Occured as {err}!")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which File you want to Delete :-")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE REMOVED SUCESSFULLY!")
        else:
            print("NO SUCH FILE EXISTS!")
    except Exception as err:
        print(f"An error occured as {err}")

print("Press 0 for Exiting the Program")
print("Press 1 for Creating a File")
print("Press 2 for Reading a File")
print("Press 3 for Updating a File")
print("Press 4 for Deleting a File")

check = int(input("Please Tell Your Response:- "))

while(check > 0):
    if check == 1:
        createfile()

    elif check == 2:
        readfile()

    elif check == 3:
        updatefile()

    elif check == 4:
        deletefile()

