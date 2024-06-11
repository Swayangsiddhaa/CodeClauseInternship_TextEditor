import os 

#This function creates file.
def File_create():
    a=input("Enter the name of the file(remember please add .txt or .docx at the end of the file name):-")
    with open(a,"x") as f:
        print("File is created.")

#This function opens exist file.
def Exist_file_open():
    a=input("Enter the name of the exist file you want to open (remember please add .txt or .docx at the end of the file name):-")
    if os.path.exists(a):
        with open(a,"r") as f:
            data=f.read()
            print("File exists!.")
            print("The content in the file is:",data)
    else:
        print("File does not exists!.")

#This function edits and saves a file.
def File_edit_and_save():
    a=input("Enter the name of the file you want to open for edit and save (remember please add .txt or .docx at the end of the file name):-")
    if os.path.exists(a):
        append=input("Do you want to add something at the next line?(yes/no):-").lower()
        if(append=="yes"):
            with open(a,"a") as f:
                b=input("Write something:-")
                f.write("\n"+b)
                print("File is edited and saved!.")
        else:
            with open(a,"w") as f:
                b=input("Write something:")
                f.write(b)
                print("File is edited and saved!.")
    else:
        print("File does not exists!.")

#This function counts the word the file contains.
def Word_count():
    a=input("Enter the name of the  file you want to count words for (remember please add .txt or .docx at the end of the file name):-")
    if os.path.exists(a):
        with open(a,"r") as f:
            data=f.read()
            words = data.split()
            print(f"The file contains {len(words)} words.")
    else:
        print("File does not exists!.")

#This function deletes file.
def Delete_file():
    a=input("Enter the name of the  file you want to delete (remember please add .txt or .docx at the end of the file name):-")
    if os.path.exists(a):
        os.remove(a)
        print("File is deleted.")
    else:
        print("File does not exists!.")

#This function does work according to the user choise.
def Conduct(choose):
    if(choose=="a"):
        File_create()
    elif(choose=="b"):
        Exist_file_open()
    elif(choose=="c"):
        File_edit_and_save()
    elif(choose=="d"):
        Word_count()
    elif(choose=="e"):
        Delete_file()

#Opening statement.
print("Hello friend !. it is a TEXT EDITOR!.")
print("It supports creating file, opening exist file, edit and save file, word count in a file, delete file.")
print("So the options are:-")
print("a)Create New File.")
print("b)Open Exist File.")
print("c)Edit and save File.")
print("d)Word count in a File.")
print("e)Delete File")

#This loop checks validity of given user input.
while(True):
    choose=input("Please write the option you want to choose form the above options:-").lower()
    if(choose not in ["a","b","c","d","e"] ):
        print("Invalid choise! please select a valid option it supports.")
        continue
    else:
        Conduct(choose)
    break
