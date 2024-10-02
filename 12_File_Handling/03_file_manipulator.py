import os

def file_manipulator():
    while True:
        command = input()
        if command == "End":
            break

        parts = command.split('-')
        action = parts[0]

        if action == "Create":
            file_name = parts[1]
            with open(file_name, 'w') as f:
                pass

        elif action == "Add":
            file_name = parts[1]
            content = parts[2]
            with open(file_name, 'a') as f:
                f.write(content + '\n')

        elif action == "Replace":
            file_name = parts[1]
            old_string = parts[2]
            new_string = parts[3]
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    file_content = f.read()
                new_content = file_content.replace(old_string, new_string)
                with open(file_name, 'w') as f:
                    f.write(new_content)
            else:
                print("An error occurred")

        elif action == "Delete":
            file_name = parts[1]
            if os.path.exists(file_name):
                os.remove(file_name)
            else:
                print("An error occurred")

        else:
            print("Invalid command")


file_manipulator()
