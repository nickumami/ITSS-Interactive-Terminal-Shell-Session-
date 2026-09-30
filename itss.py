from pathlib import Path


# To print the current dir and its contents 
def print_current_dir(currentPath):

    itemsInDir = {}
    index = 0

    print(f"The current dir is '{currentPath}'")
    print(f"It's contents are :\n")

    
    for  item in currentPath.iterdir():
        

        if item.name.startswith('.') == False :
            #index only goes up if we find a hit for a none .dot file
            index += 1 
            print(f"\t * {item.name} ({index})")
            itemsInDir[str(index)] = str(item.name)

    print("\t")
    return itemsInDir


# listens to input on what directory the user wants to go into 
#need current path to update path and return it. alongside out hashmap to actually choose

def selection_mode(currentPath , current_directory_selection):
    selectionMade = False
    while not selectionMade: 

        selection = input(f"Selection Mode : choose a number between 1 - {len(current_directory_selection)}\nOr q to quit \n")
        if selection == 'q':
            #don't update list , just return path again because user changed their mind
            selection_mode = True
            return currentPath
        elif current_directory_selection.get(selection):
            
            currentPath = currentPath / current_directory_selection[selection]
            selectionMade = True
            return currentPath
        else: 
            print("That key doesn't exist boss , try again ")

        
        


def print_actions():
    print("u : go up")
    print("d : enter selection mode and go down into file tree") 
    print("q : quit program\n")      

def main():
    

    quit = False;
    currentPath = Path(__file__).parent

    #A list of the current files in the directory , used and updated for moving down the file tree

    current_directory_selection = {}
    while not quit:
        
        #Change afterwards to check if user put in an int 
        current_directory_selection = print_current_dir(currentPath)
        print_actions()
        choice = input("What would you like to do ?\n")
        

        #switch case depending on user choice 
        match choice : 
            case 'u':
                 currentPath = currentPath.parent

            case 'd':
                #enter into selection mode and returns the new path 
                 currentPath = selection_mode(currentPath , current_directory_selection)
            case 'q':
                quit = True
                 

    
if __name__ == "__main__":
    main()
