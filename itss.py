from pathlib import Path


# To print the current dir and its contents 
def print_current_dir(currentPath):

    print(f"The current dir is '{currentPath}'")
    print(f"It's contents are :")

    for item in currentPath.iterdir():
        if item.name.startswith('.') == False :
            print(f"\t + {item.name}")





        

def main():
    

    quit = False;
    currentPath = Path(__file__).parent
    while not quit:
        
        #Change afterwards to check if user put in an int 
        print_current_dir(currentPath)
        choice = input("What would you like to do ?\n")

        #switch case depending on user choice 
        match choice : 
            case '1':
                 currentPath = currentPath.parent
                 

    
if __name__ == "__main__":
    main()
