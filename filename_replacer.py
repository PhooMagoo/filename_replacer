### Primarily for dealing with downloaded seasons of shows. There's a lot of
### duplicate garbage text in the filename. This lets you target the duplicate
### text and replace it with whatever you want to clean it up.

# TODO: Nothing.

import os                   # For walking through a directory tree.
from pprint import pprint   # For displaying text nicely.

# Create our source variable.
source = r""
source = input(r"Enter directory: ") # Accept user specified directory.

# While we want to modify things...
while True:
    try:
        # ...Create a path to each file, and...
        pathiter = (os.path.join(root, filename)
        for root, _, filenames in os.walk(source)
        for filename in filenames)

        pprint(r"In " + source + ":")
        oldtxt = input("Current Text: ") # The current text of the filename.
        newtxt = input("Replace With: ") # What we want to change that text to.

        # For each relevant file...
        for path in pathiter:
            newname = path.replace(oldtxt, newtxt) # Store new name in variable.
            if newname != path: # If the name hasn't been switched out yet...
                os.rename(path, newname) # Rename the file.

        # Verify if user wants to modify more things.
        pprint(r"Would you like to modify another string in the current directory?")
        pprint(r"Y (yes) / N (no) / C (change directory): ")

        choice = input("> ") # User input.
        
        if choice.lower() == "y":
            continue
        elif choice.lower() == "n":
            break
        elif choice.lower() == "c":
            source = input("Enter directory: ")
            continue
        else:
            pprint("Invalid response.")

    except Exception as e:
        print (e + " : " + newname)
