# #activate command : source .venv/bin/activate 
# #run command for debugging 
# #textual run --dev /home/nickumami/Work/ITSS/itss.py(personal terminal) , textual console(debug terminal)


from pathlib import Path
import os
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header , Static , Button
from textual.containers import HorizontalGroup , VerticalGroup
from textual.app import RenderResult
from textual.reactive import reactive

## gets all items in the current directory , and returns them in a hashmap
def get_items_in_folder(current_path : str , get_hidden = False) -> dict:
    
    items = {}
    for i , file in enumerate(os.listdir(path=current_path)):
            if not get_hidden:
                if file.startswith(".") == False:
                    items[i] = file
    return items

class Folder(Button):

     itemName : str
     def __init__(self, label = None, variant = "default", *, 
                  name = None, id = None, classes = None, 
                  disabled = False, tooltip = None, action = 
                  None, compact = False, flat = False , itemName):
          super().__init__( variant, name=name,id=id,
                            classes=classes, disabled=disabled, 
                            tooltip=tooltip, action=action, 
                            compact=compact, flat=flat)
          self.itemName = itemName
          self.label = itemName

class FolderContainer(HorizontalGroup):

    current_dir = reactive(str(Path.cwd()) , recompose=True)
    items_in_folder = {}

    def compose(self)-> ComposeResult:
         self.items_in_folder = get_items_in_folder(self.current_dir)
         yield Button(".." , variant="primary" , id="back-btn")
         # item is index to get the actual value in the hashmap. Think of it as a ticket that gets claimed when we yield static 
         for item in self.items_in_folder.keys():
              yield Folder(itemName = self.items_in_folder[item] )


    def on_button_pressed(self , event :  Folder.Pressed):
        print("This works")
        #update path and dict with items in the new folder
        if event.button.id == "back-btn":
            self.current_dir = str(Path(self.current_dir).parent)
            print(self.current_dir)
        else:
            pathToAppend = event.button.itemName
            self.current_dir = str(Path(self.current_dir) / pathToAppend)
            print("I got to folders btn")
        
      
              
              


class ITSS(App):

    CSS_PATH = "app.tcss"
    # main application , will mainly be for calling different widgets and just running the app 
    def compose(self) -> ComposeResult:
         yield FolderContainer()
        
       
       

    
   

    
if __name__ == "__main__":
    # main()
    app = ITSS()
    app.run()
