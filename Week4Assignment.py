def read_modify_file():
    filename = input("Enter the filename to read : ")
    
    try:
        with open(filename, "r") as infile:
            content = infile.read()
            print("Originale Content")
            print(content)
            
            modified_content = content.upper()
            
        with open("modified.txt", "w") as outfile:
            outfile.write(modified_content)
            print("\n Modified content has been written to 'modified.txt'")
            
    except FileNotFoundError:
        print("Error : The file " + filename + " does not exist.")
        
read_modify_file()