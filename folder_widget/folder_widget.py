# #activate command : source .venv/bin/activate
# #run command for debugging
# #textual run --dev /home/nickumami/Work/ITSS/itss.py(personal terminal) , textual console(debug terminal)


from pathlib import Path
import os
from textual.app import  ComposeResult
from textual.widgets import  Button , Switch , Static , DirectoryTree
from textual.containers import HorizontalGroup , VerticalGroup
from textual.app import RenderResult
from textual.reactive import reactive

## gets all items in the current directory , and returns them in a hashmap
def get_items_in_folder(current_path : str , get_hidden = False) -> dict:

    items = {}
    for i , file in enumerate(os.listdir(path=current_path)):
                if file.startswith(".") == True:
                     if get_hidden == False :
                          continue
                     elif get_hidden == True:
                          items[i] = file
                else:
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

#Universal file navigation that will be docked to the left 
class FolderHQ(DirectoryTree):

     def __init__(self, path, *, name = None, id = None, classes = None, disabled = False , showHidden : bool):
          super().__init__(path, name=name, id=id, classes=classes, disabled=disabled)
          self.showHidden : bool = showHidden

     #if get_hidden is toggled true , we show hidden files. Otherwise we don't
     def filter_paths(self, paths):
          if self.showHidden == False:
               return [path for path in paths if not path.name.startswith(".")]
          else:
               return super().filter_paths(paths)
          

class AtTheCrimeScene(HorizontalGroup):

    def __init__(self, *children, name = None, id = None, classes = None, disabled = False, markup = True , current_dir : str , get_hidden : bool):
         super().__init__(*children, name=name, id=id, classes=classes, disabled=disabled, markup=markup)

         self.current_dir = current_dir
         self.get_hidden = get_hidden
         self.items_in_folder = {}

    def compose(self)-> ComposeResult:

        # on compose , create dict for all items in the current directory
         self.items_in_folder = get_items_in_folder(self.current_dir , self.get_hidden)
         yield Button(".." , variant="primary" , id="back-btn" , name="back-btn")

         # item is index to get the actual value in the hashmap. Think of it as a ticket that gets claimed when we yield static
         for item in self.items_in_folder.keys():
              yield Folder(itemName = self.items_in_folder[item]  , name="folder")




class FolderContainer(HorizontalGroup):

    CSS_PATH = 'folder.tcss'
    current_dir = reactive(str(Path.cwd()) , recompose=True)
    get_hidden = reactive(False , recompose=True)

    def compose(self)-> ComposeResult:

         yield FolderHQ("/" , showHidden= self.get_hidden)
         yield AtTheCrimeScene(current_dir=self.current_dir , get_hidden= self.get_hidden)

    def on_switch_changed( self , event : Switch.Changed):

        if event.value == True:
             self.get_hidden = True
        else:
             self.get_hidden = False


    def on_button_pressed(self , event :  Folder.Pressed):
        #update path and dict with items in the new folder
        if event.button.name == "back-btn":
            self.goUpDir()
        elif event.button.name == "folder":
            self.goIntoDir(event.button.itemName)


    # functions to go up and down the file tree to keep button press
    # logic readable self.current_dir = str(Path(self.current_dir).parent)
    def goUpDir(self) -> None:
         self.current_dir = str(Path(self.current_dir).parent)

    def goIntoDir(self , itemName : str) -> None:
            self.current_dir = str(Path(self.current_dir) / itemName)
