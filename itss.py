# #activate command : source .venv/bin/activate 
# #run command for debugging 
# #textual run --dev /home/nickumami/Work/ITSS/itss.py(personal terminal) , textual console(debug terminal)
# activate for windows : source .venv/Scripts/activate

#personal module import
from folder_widget import folder_widget
from toggle_widget import toggle_widget

#imports needed to run main 
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header  , Button , Switch , Static
from textual.containers import HorizontalGroup , VerticalGroup
from textual.app import RenderResult
from textual.reactive import reactive

class ITSS(App):

    CSS_PATH = "app.tcss"
    # main application , will mainly be for calling different widgets and just running the app 
    def compose(self) -> ComposeResult:
         yield Header()
         yield toggle_widget.HiddenToggle(id="toggle-switch")
         yield folder_widget.FolderContainer()
         yield Button( "Quit", id="quit" , variant="error")

    def on_button_pressed( self , event :  Button.Pressed):

         if event.button.id == "quit":
              quit()

    def on_switch_changed(self , event : Switch.Changed):
         self.query_exactly_one(folder_widget.FolderContainer).get_hidden = event.value
        
    
#actual main function running the code
if __name__ == "__main__":
    # main()
    app = ITSS()
    app.run()
