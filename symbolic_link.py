#!/usr/bin/env python3

import os

os.system('clear')

print(" ")
print(" ")
print("Script written by: Mina Ramez Farag")
print("")
print("       **********************")
print("       ****Symbolic Links****")
print("       **********************")
print("")


while True:
    print("Select an option:")
    print("1. Create symbolic link")
    print("2. Delete symbolic link")
    print("3. Generate summary report")
    print("Type 'quit' to exit")

    choice = input("Enter option (1-3), or 'quit' to exit: ")

    if choice== "quit":
        break
    
    #create the symbolic link 
    elif choice =="1":
        filename =input("Enter filename or path: ")

        if os.path.exists(filename ):
            print( "File found in directory '/home/student/student/scripts/script03/'")
            proceed= input("Do you wish to proceed? (Y/N): ")

            if proceed.lower( ) =="y":
                target_path= os.path.abspath(filename )
                link_name = os.path.basename(filename)
                link_path = os.path.join(os.path.expanduser("~"), link_name)
                os.symlink (target_path, link_path)
                print("Symbolic link created" )
            
            else:
                print( "Symbolic link terminated")

        else:
            print("File not found" )

    #symbolic link deletion from /home directoy
    elif choice =="2" :

        filename=input("Enter filename: ")

        symlink_path =os.path.join(os.path.expanduser("~"), filename)
        if os.path.islink(symlink_path ):
            print("File found in directory '/home'")
            proceed = input("Do you wish to proceed? (Y/N): ")

            if proceed.lower( ) =="y":
                os.remove(symlink_path )
                print("Symbolic link deleted")
            
            else:
                print( "Deletion terminated")
        
        else:
            print( "Symbolic link not found")

    elif choice== "3":
        links =[ os.path.basename(link) for link in os.listdir(os.path.expanduser("~")) if os.path.islink(os.path.join(os.path.expanduser("~"), link))]

        print("Summary report:")
        print("{:<10} {:<50}  {:<50}".format("Number" , "Symbolic link", "Target path") )
        for i, link in enumerate(links):
            target_path = os.readlink(os.path.join(os.path.expanduser("~") , link))
            print("{:<10} {:<50} {:<50}".format( i+1, link, target_path) )

    else:
        print("Invalid option")
