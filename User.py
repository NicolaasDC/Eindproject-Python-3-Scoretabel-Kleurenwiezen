from Source.klassen import Kleurenwiezen
import tkinter as tk
from tkinter import simpledialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Initialiseer de globale variabelen
Speler1 = ""
Speler2 = ""
Speler3 = ""
Speler4 = ""


def create_window(player_num, submit_command):
    root = ttk.Window(themename="superhero")
    root.geometry('300x150')

    label = ttk.Label(root, text=f"Voer speler {player_num} in:")
    label.pack(pady=10)

    global entry
    entry = ttk.Entry(root, bootstyle=PRIMARY)
    entry.pack(pady=10)

    button = ttk.Button(root, text="Submit", command=lambda: submit_command(root), bootstyle=SUCCESS)
    button.pack(pady=10)

    root.mainloop()


def speler1(root):
    global Speler1
    Speler1 = entry.get()
    root.destroy()


def speler2(root):
    global Speler2
    Speler2 = entry.get()
    root.destroy()


def speler3(root):
    global Speler3
    Speler3 = entry.get()
    root.destroy()


def speler4(root):
    global Speler4
    Speler4 = entry.get()
    root.destroy()


# Maak vensters voor elke speler
# create_window(1, speler1)
# create_window(2, speler2)
# create_window(3, speler3)
# create_window(4, speler4)

# Print de namen van de spelers
Speler1 = 'Nico'
Speler2 = 'Jelle'
Speler3 = 'Brecht'
Speler4 = 'Jonas'

kleurenwiezen = Kleurenwiezen(Speler1, Speler2, Speler3, Speler4)


# kleurenwiezen.update_score('speler1', 'Grote miserie', vrager=True, gelukt=True)
# kleurenwiezen.update_score('speler2', 'Grote miserie', vrager=False, gelukt=True)
# kleurenwiezen.update_score('speler3', 'Grote miserie', vrager=False, gelukt=True)
# kleurenwiezen.update_score('speler4', 'Grote miserie', vrager=False, gelukt=True)


# print(kleurenwiezen.score())


def nieuw_spel():
    def selecteer_spel():
        selected_value = combo.get()
        global spel
        spel = selected_value
        root.destroy()  # Close the window

    # Create the main application window
    root = tk.Tk()
    root.title("Welk spel")
    root.geometry("300x200")

    # Create a label
    label = tk.Label(root, text="Selecteer een spel:")
    label.pack(pady=10)

    # Create a combobox (drop-down menu)
    options_spel = ["Samen 8", "Solo 5", "Samen 9", "Solo 6", "Samen 10", "Solo 7", "Samen 11", 'Kleine miserie',
                    "Samen 12", "Solo 8", "Samen 13", "Abondance 9", "Troel voor 8", "Troel voor 9", "Grote miserie",
                    "Abondance 10", "Abondance 11", "Abondance 12", "Solo slim"]
    combo = ttk.Combobox(root, values=options_spel)
    combo.pack(pady=10)

    # Create a button to select the option and close the window
    button = tk.Button(root, text="Select", command=selecteer_spel)
    button.pack(pady=10)

    # Run the application
    root.mainloop()

    twee_spelers = ["Samen 8", "Samen 9", "Samen 10", "Samen 11", "Samen 12", "Samen 13", "Troel voor 8",
                    "Troel voor 9"]
    options = [Speler1, Speler2, Speler3, Speler4]
    # After the window is closed, you can use the selected_option variable
    if spel in twee_spelers:
        def selecteer_speler1():
            selected_value = combo.get()
            global speler1
            speler1 = selected_value
            options.remove(speler1)
            root.destroy()  # Close the window

        # Create the main application window
        root = tk.Tk()
        root.title("Welk speler")
        root.geometry("300x200")

        # Create a label
        label = tk.Label(root, text="Selecteer speler 1:")
        label.pack(pady=10)

        # Create a combobox (drop-down menu)
        combo = ttk.Combobox(root, values=options)
        combo.pack(pady=10)

        # Create a button to select the option and close the window
        button = tk.Button(root, text="Select", command=selecteer_speler1)
        button.pack(pady=10)

        # Run the application
        root.mainloop()

        def selecteer_speler2():
            selected_value = combo.get()
            global speler2
            speler2 = selected_value
            root.destroy()  # Close the window

        # Create the main application window
        root = tk.Tk()
        root.title("Welk speler")
        root.geometry("300x200")

        # Create a label
        label = tk.Label(root, text="Selecteer speler 2:")
        label.pack(pady=10)

        # Create a combobox (drop-down menu)
        combo = ttk.Combobox(root, values=options)
        combo.pack(pady=10)

        # Create a button to select the option and close the window
        button = tk.Button(root, text="Select", command=selecteer_speler2)
        button.pack(pady=10)

        # Run the application
        root.mainloop()

    else:
        def selecteer_speler1():
            selected_value = combo.get()
            global speler1
            speler1 = selected_value
            root.destroy()  # Close the window

        # Create the main application window
        root = tk.Tk()
        root.title("Welk speler")
        root.geometry("300x200")

        # Create a label
        label = tk.Label(root, text="Selecteer speler 1:")
        label.pack(pady=10)

        # Create a combobox (drop-down menu)
        options = [Speler1, Speler2, Speler3, Speler4]
        combo = ttk.Combobox(root, values=options)
        combo.pack(pady=10)

        # Create a button to select the option and close the window
        button = tk.Button(root, text="Select", command=selecteer_speler1)
        button.pack(pady=10)

        # Run the application
        root.mainloop()

    def selecteer_geslaagd():
        selected_value = combo.get()
        global geslaagd
        geslaagd = selected_value
        if geslaagd == "Ja":
            geslaagd = True
        else:
            geslaagd = False
        root.destroy()  # Close the window

    # Create the main application window
    root = tk.Tk()
    root.title("Spel geslaagd")
    root.geometry("300x200")

    # Create a label
    label = tk.Label(root, text="Spel geslaagd?")
    label.pack(pady=10)

    # Create a combobox (drop-down menu)
    options_geslaagd = ["Ja", "Nee"]
    combo = ttk.Combobox(root, values=options_geslaagd)
    combo.pack(pady=10)

    # Create a button to select the option and close the window
    button = tk.Button(root, text="Select", command=selecteer_geslaagd)
    button.pack(pady=10)

    # Run the application
    root.mainloop()

    spellen_overslagen = ["Samen 8", "Solo 5", "Samen 9", "Solo 6", "Samen 10", "Solo 7", "Samen 11", "Samen 12",
                          "Troel voor 8", "Troel voor 9"]

    if geslaagd == True and spel in spellen_overslagen:
        def on_submit():
            try:
                # Get the input value and convert it to an integer
                input_value = int(entry.get())
                global overslagen
                overslagen = input_value
                root.destroy()  # Close the window
            except ValueError:
                # Show an error message if the input is not a valid integer
                messagebox.showerror("Invalid Input", "Please enter a valid integer.")

        # Create the main application window
        root = tk.Tk()
        root.title("Vul de overslagen in")
        root.geometry("300x150")

        # Create a label
        label = tk.Label(root, text="Overslagen:")
        label.pack(pady=10)

        # Create an entry widget to input the integer
        entry = tk.Entry(root)
        entry.pack(pady=10)

        # Create a button to submit the input and close the window
        button = tk.Button(root, text="Submit", command=on_submit)
        button.pack(pady=10)

        # Run the application
        root.mainloop()

    if geslaagd == False and spel in spellen_overslagen:
        def on_submit():
            try:
                # Get the input value and convert it to an integer
                input_value = int(entry.get())
                global overslagen
                overslagen = input_value
                root.destroy()  # Close the window
            except ValueError:
                # Show an error message if the input is not a valid integer
                messagebox.showerror("Invalid Input", "Please enter a valid integer.")

        # Create the main application window
        root = tk.Tk()
        root.title("Hoeveel slagen er in?")
        root.geometry("300x150")

        # Create a label
        label = tk.Label(root, text="Aantal slagen er in:")
        label.pack(pady=10)

        # Create an entry widget to input the integer
        entry = tk.Entry(root)
        entry.pack(pady=10)

        # Create a button to submit the input and close the window
        button = tk.Button(root, text="Submit", command=on_submit)
        button.pack(pady=10)

        # Run the application
        root.mainloop()



nieuw_spel()
