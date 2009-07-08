import orca.input_event
import orca.keybindings
import orca.orca
import orca.speech
import orca.braille
import re
 
myKeyBindings = orca.keybindings.KeyBindings()
 
def sayTime(script, inputEvent=None):
    import time
    message = time.strftime("%A, %l:%M", time.localtime())
    orca.speech.speak(message)
    orca.braille.displayMessage(message)
    return True
 
sayTimeHandler = orca.input_event.InputEventHandler(
    sayTime,
    "Presents the time.")
 
myKeyBindings.add(orca.keybindings.KeyBinding(
    "n",
    1 << orca.settings.MODIFIER_ORCA,
    1 << orca.settings.MODIFIER_ORCA,
    sayTimeHandler))
 
orca.settings.keyBindingsMap["default"] = myKeyBindings

