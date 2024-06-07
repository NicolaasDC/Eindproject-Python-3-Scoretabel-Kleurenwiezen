from Source.klassen import Kleurenwiezen
import tkinter as tk
from tkinter import simpledialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Maak het hoofdvenster aan met ttkbootstrap
root = ttk.Window(themename="superhero")
root.withdraw()  # Verberg het hoofdvenster

#speler1 = simpledialog.askstring(title="Speler", prompt="Geef de naam van speler 1:", parent=root)
#speler2 = simpledialog.askstring(title="Speler", prompt="Geef de naam van speler 2:", parent=root)
#speler3 = simpledialog.askstring(title="Speler", prompt="Geef de naam van speler 3:", parent=root)
#speler4 = simpledialog.askstring(title="Speler", prompt="Geef de naam van speler 4:", parent=root)

speler1 = 'speler1'
speler2 = 'speler2'
speler3 = 'speler3'
speler4 = 'speler4'

# Sluit het hoofdvenster
root.destroy()

kleurenwiezen = Kleurenwiezen(speler1, speler2, speler3, speler4)

kleurenwiezen.update_score('speler1', 'Samen 9', vrager=True, gelukt=True, overslagen=0)

print(kleurenwiezen.score())