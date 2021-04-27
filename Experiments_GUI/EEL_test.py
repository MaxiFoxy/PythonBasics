from tkinter import filedialog
import eel
import tk as tk

eel.init("test_gui")

@eel.expose
def btn_ResimyoluClick():
    root = tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    folder = filedialog.askdirectory()
    return folder

eel.start("index.html", size=(300, 600))
