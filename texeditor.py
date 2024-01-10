import os
def command():
    while True:
        com = input("input your command> ")
        if com == "w":
            with open(filename, 'w') as file:
                while True:
                    a = input("input content(type end if finished)> ")
                    if a == "end":
                        break
                    file.write(a + "\n")
        elif com == "a":
            with open(filename, 'a') as file:
                while True:
                    a = input("what do you want to append?> ")
                    if a == "end":
                        break
                    file.write(a +"\n")
        elif com == "r":
            with open(filename, 'r') as orig_file:
                lines = orig_file.readlines()  # Read all lines into a list

            with open(filename, 'w') as file:
                while True:
                    origin = input("What do you want to replace? (type 'exit' if finished)> ")
                    if origin == "exit":
                        break
                    mod = input("what do you want to replace it with? ")
                    for line in lines:
                        new_line = line.replace(origin, mod)
                        file.write(new_line)
        elif com == "s":
            with open(filename, 'r') as file:
                print(file.read())
        elif com == "exit":
            break
        elif com == "h":
            print("w:write a:append r:replace s:show content")
        else:
            print("Wrong command")

filename = input("Type in the filename you want to open> ")

try:
    with open(filename, 'r') as file:
        print("the file is like this.")
        print(file.read())
        command()
        print("terminated")
except FileNotFoundError:
    with open(filename, 'w') as file:
        file.write('')
        command()
        print("terminated")
        