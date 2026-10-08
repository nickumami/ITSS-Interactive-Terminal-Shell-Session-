#activate command : source .venv/bin/activate 
from pathlib import Path
import os
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header , Static , Button
from textual.containers import HorizontalGroup , VerticalGroup

## gets all items in the current directory , and returns them in a hashmap
def get_items_in_folder(current_path : str) -> dict:

    items = {}
    for i , file in enumerate(os.listdir(path=current_path)):
            items[i] = file
    return items




class FolderContainer(HorizontalGroup):

    current_dir = str(Path.cwd())
    items_in_folder = get_items_in_folder(current_dir)

    def compose(self):
         yield Button(".." , variant="primary")
         # item is index to get the actual value in the hashmap. Think of it as a ticket that gets claimed when we yield static 
         for item in self.items_in_folder.keys():
              yield Static(self.items_in_folder[item])
              
              
         






class ITSS(App):

    CSS_PATH = "app.tcss"
    # main application , will mainly be for calling different widgets and just running the app 
    def compose(self):
        yield FolderContainer()

    
   

    
if __name__ == "__main__":
    # main()
    app = ITSS()
    app.run()
