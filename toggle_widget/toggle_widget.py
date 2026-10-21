from textual.containers import HorizontalGroup
from textual.widgets import Static, Switch
from textual.app import  ComposeResult


#Going to put a pin in this <- , because I want to see if I can 
#Create a custom header that shows the toggle button in the top
# If not , we like what this is . We'll dock it in the top right 
class HiddenToggle(HorizontalGroup):

    def compose(self) -> ComposeResult:
        yield Static("Toggle Hidden:")
        yield Switch( value=False)

