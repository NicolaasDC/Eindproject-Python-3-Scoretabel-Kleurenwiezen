import streamlit as st
import pandas as pd
import ast
from Source.klassen import Kleurenwiezen
from datetime import date

# Initialize global variables
if 'rondes' not in st.session_state:
    st.session_state['rondes'] = []
if 'players' not in st.session_state:
    st.session_state['players'] = ["", "", "", ""]
if 'kleurenwiezen' not in st.session_state:
    st.session_state['kleurenwiezen'] = None
if 'page' not in st.session_state:
    st.session_state['page'] = 'set_player_names'  # Default page

# Function to set player names
def set_player_names():
    st.title("Welkom beste kleurenwiezers, geef de 4 spelers in")
    for i in range(4):
        # Pre-fill text input with the existing player name
        name_input = st.text_input(f"Voer speler {i + 1} in:", key=f"player_{i}", value=st.session_state['players'][i])

        # Check if the name is already entered by another player
        if name_input and name_input in st.session_state['players'][:i]:
            st.warning(f"De naam '{name_input}' is al ingevoerd. Kies een andere naam.")
        
        # Update the session state for the player name
        st.session_state['players'][i] = name_input
    if st.button("Submit"):
        if "" in st.session_state['players']:
            st.error("Vul alle 4 spelersnamen in voordat je verdergaat!")
        else:
            # Create the game object with player names from session state
            st.session_state['kleurenwiezen'] = Kleurenwiezen(*st.session_state['players'])
            
            # Navigate to the main menu page
            st.session_state['page'] = 'main_menu'

# Function to start a new game
def nieuw_spel():
    st.title("Nieuw Spel")
    spellen = ["Samen 8", "Solo 5", "Samen 9", "Solo 6", "Samen 10", "Solo 7", "Samen 11", 'Kleine miserie',
               "Samen 12", "Solo 8", "Samen 13", "Abondance 9", "Troel voor 8", "Troel voor 9", "Grote miserie",
               "Abondance 10", "Abondance 11", "Abondance 12", "Solo slim"]

    max_overslagen = {
        "Samen 8": [0, 1, 2, 3, 4, 5], 
        "Solo 5": [0, 1, 2, 3], 
        "Samen 9": [0, 1, 2, 3, 4],
        "Solo 6": [0, 1, 2], 
        "Samen 10": [0, 1, 2, 3], 
        "Solo 7": [0, 1], 
        "Samen 11": [0, 1, 2],
        "Samen 12": [0, 1],
        "Troel voor 8": [0, 1, 2, 3, 4, 5], 
        "Troel voor 9": [0, 1, 2, 3, 4]
    }

    hoeveel_verliesslagen = {
        "Samen 8": [1, 2, 3, 4, 5, 6, 7], "Solo 5": [1, 2, 3, 4],
        "Samen 9": [1, 2, 3, 4, 5, 6, 7],
        "Solo 6": [1, 2, 3, 4, 5], "Samen 10": [1, 2, 3, 4, 5, 6, 7],
        "Solo 7": [1, 2, 3, 4, 5, 6], "Samen 11": [1, 2, 3, 4, 5, 6, 7],
        "Solo 8": [1, 2, 3, 4, 5, 6, 7],
        "Samen 12": [1, 2, 3, 4, 5, 6, 7], "Samen 13": [1, 2, 3, 4, 5, 6, 7],
        "Troel voor 8": [1, 2, 3, 4, 5, 6, 7], "Troel voor 9": [1, 2, 3, 4, 5, 6, 7]
    }

    spel = st.selectbox("Selecteer een spel:", spellen, key="spel_selectie")
    twee_spelers = ["Samen 8", "Samen 9", "Samen 10", "Samen 11", "Samen 12", "Samen 13", "Troel voor 8", "Troel voor 9"]

    vrager1 = st.selectbox("Selecteer vrager 1:", st.session_state['players'])
    vrager2 = None

    if spel in twee_spelers:
        vrager2 = st.selectbox("Selecteer vrager 2:", [p for p in st.session_state['players'] if p != vrager1])

    geslaagd = st.radio("Spel geslaagd?", ["Ja", "Nee"], key="geslaagd_selectie") == "Ja"

    # Dynamisch overslagen/verliesslagen bijwerken
    if geslaagd and spel in max_overslagen:
        overslagen = st.selectbox("Hoeveel overslagen?", max_overslagen[spel], key="overslagen_selectie")
    elif not geslaagd and spel in hoeveel_verliesslagen:
        overslagen = st.selectbox("Hoeveel verliesslagen?", hoeveel_verliesslagen[spel], key="verliesslagen_selectie")
    else:
        overslagen = 0

    if st.button("Bevestig spel"):
        kleurenwiezen = st.session_state['kleurenwiezen']
        spelers = st.session_state['players'].copy()

        if vrager2:
            kleurenwiezen.update_score(vrager1, spel, True, geslaagd, overslagen)
            kleurenwiezen.update_score(vrager2, spel, True, geslaagd, overslagen)
            spelers.remove(vrager1)
            spelers.remove(vrager2)
        else:
            kleurenwiezen.update_score(vrager1, spel, True, geslaagd, overslagen)
            spelers.remove(vrager1)

        for speler in spelers:
            kleurenwiezen.update_score(speler, spel, False, geslaagd, overslagen)

        huidige_score = kleurenwiezen.score()
        if spel == "Solo slim" and geslaagd:
            st.title(f"Proficiat {vrager1}! Levensdoel bereikt! Kader die solo slim maar in!")
        st.session_state['rondes'].append(ast.literal_eval(huidige_score))
        st.success("Spel toegevoegd!")
        st.session_state['page'] = 'main_menu'  # Navigate back to main menu


# Function to save score table
def write_to_csv():
    st.title("Score Opslaan")
    df = pd.DataFrame(st.session_state['rondes'])
    st.download_button("Download Scoretabel", df.to_csv(index=False), file_name=f"{date.today()}-{st.session_state['players'][0]}-{st.session_state['players'][1]}-{st.session_state['players'][2]}-{st.session_state['players'][3]}.csv", mime="text/csv")    

    # Voeg een knop toe om terug te gaan naar het hoofdmenu
    if st.button("Terug naar hoofdmenu"):
        st.session_state['page'] = 'main_menu'    

# Main menu
def main_menu():
    st.title("Wat wil je doen?")
    opties = ["Een spelletje kaarten", "Laatste spelletje wissen", "Scoretabel opslaan"]
    keuze = st.radio("Selecteer een optie:", opties)

    if st.button("Bevestig keuze"):
        if keuze == "Een spelletje kaarten":
            st.session_state['page'] = 'new_game'
        elif keuze == "Scoretabel opslaan":
            st.session_state['page'] = 'save_scores'
        elif keuze == "Laatste spelletje wissen":
            rondes = st.session_state['rondes']
            kleurenwiezen = st.session_state['kleurenwiezen']
            if len(rondes) == 1:
                kleurenwiezen.scores = {kleurenwiezen.speler1: 0, kleurenwiezen.speler2: 0, kleurenwiezen.speler3: 0, kleurenwiezen.speler4: 0}
                rondes.pop()
                st.success("Laatste spelletje gewist!")
            if len(rondes) > 1:
                kleurenwiezen.scores = {kleurenwiezen.speler1: rondes[-2][kleurenwiezen.speler1], kleurenwiezen.speler2: rondes[-2][kleurenwiezen.speler2], kleurenwiezen.speler3: rondes[-2][kleurenwiezen.speler3], kleurenwiezen.speler4: rondes[-2][kleurenwiezen.speler4]}
                rondes.pop()
                st.success("Laatste spelletje gewist!")
            else:
                st.error("Er zijn nog geen spelletjes gespeeld om te wissen!")


    st.title("Scoretabel")

    # Display the DataFrame with the custom index
    if 'rondes' in st.session_state and len(st.session_state['rondes']) == 0:
        st.write("Er zijn nog geen spelletjes gespeeld.")
        
    if 'rondes' in st.session_state and len(st.session_state['rondes']) > 0:
        df = pd.DataFrame(st.session_state['rondes'])
        df.index = range(1, len(df) + 1)
        st.dataframe(df, use_container_width=True)
        

# Page navigation logic
if st.session_state['page'] == 'set_player_names':
    set_player_names()
elif st.session_state['page'] == 'main_menu':
    main_menu()
elif st.session_state['page'] == 'new_game':
    nieuw_spel()
elif st.session_state['page'] == 'save_scores':
    write_to_csv()

