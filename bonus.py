import json

while True:
    user_input = input("\nWelcome this is the to-do program, Do you want to add a new To-Do item?\nAnswer by y for yes, n for no, exit to end the program: ")
    
    if user_input.lower() == "y":
        item_name = input("Enter your new To-Do item in this format:( title, date & time, done or not yet ) ")
        title, date_n_time, done = item_name.split(", ")
        done = done.lower() == "done"
        
        new_item = {
            "title": title,
            "date_n_time": date_n_time,
            "done": done
        }
        
        try:
            with open("to_do.json", "r", encoding="UTF-8") as file:
                items = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            items = []
        
        items.append(new_item)
        
        with open("to_do.json", "w", encoding="UTF-8") as file:
            json.dump(items, file, indent=4)
    
    elif user_input.lower() == "n":
        ask_user = input("Do you want to list your To-Do items? answer y for yes and n for no: ")
        if ask_user.lower() == "y":
            try:
                with open("to_do.json", "r", encoding="UTF-8") as file:
                    items = json.load(file)
                    for index, item in enumerate(items, start=1):
                        status = "DONE" if item["done"] else "NOT DONE"
                        print(f"{index}- {item['title']} - {item['date_n_time']} - {status}")
            except (FileNotFoundError, json.JSONDecodeError):
                print("No to-do items found.")
    
    elif user_input.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon")
        break