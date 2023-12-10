import os

current_path = os.getcwd()

def list_files():
    files = os.listdir(current_path)
    for file in files:
        print(file)

def create_file():
    filename = input("Enter filename: ")
    data = input("Enter data: ")
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Data written to {filename}.")

def create_folder():
    foldername = input("Enter foldername: ")
    os.mkdir(foldername)
    print(f"Folder {foldername} created.")

def change_directory():
    foldername = input("Enter foldername: ")
    if foldername == "..":
        global current_path
        current_path = os.path.dirname(current_path)
    else:
        new_path = os.path.join(current_path, foldername)
        if os.path.isdir(new_path):
            current_path = new_path
        else:
            print("Invalid foldername.")

while True:
    command = input("Enter a command: ")

    if command == "ls":
        list_files()
    elif command == "touch":
        create_file()
    elif command == "mk":
        create_folder()
    elif command == "cd":
        change_directory()
    elif command == "exit":
        break
    else:
        print("Invalid command.")


