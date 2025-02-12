'''
## Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.///
- Then return again to the first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''

while True:
    user_name = input("Hey what is your name ? ")
    user_input = input(f"\nWelcome {user_name} this is the to-do program \nDo you want to add a new To-Do item?\nAnswer by y for yes, n for no, exit to end the program: ")
    
    if user_input.lower() == "y":
        item_name = input("Enter your new To-Do item: ")
        with open("to_do.txt", "a+", encoding="UTF-8") as new_item:
            new_item.write(item_name + "\n")
    elif user_input.lower() == "n":
        ask_user = input("Do you want to list your To-Do items? answer y for yes and n for no: ")
        if ask_user.lower() == "y":
            with open("to_do.txt", "r", encoding="UTF-8") as new_item:
                items = new_item.readlines()
                for item in items:
                    print(item.strip())
    elif user_input.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break
            
