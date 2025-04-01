try:
    #asks users to input their filename
    filename = input("Enter the filename to read: ")

    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file you are trying to read does not exist. Please check the file path and try again.")