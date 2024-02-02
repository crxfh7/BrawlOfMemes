##### THIS FILE IS FOR CREATING NEW CHAMPIONS #####

# IMPORTS
import pandas as pa

# GLOBES
path_champion_list = 'champion_list.xlsx'

# This class is for creating a champion
# function __str__(self) is for outputting the current champion
class create_Character:
    def __init__(self, name, level, effective, fight, maxhp, curhp, atk, defence, shield, speed, kquote, kdamage, gen, wid, lifesteal, maxturnmeter, turnmeter):
        self.name = name
        self.level = level
        self.effective = effective
        self.fight = fight
        self.maxhp = maxhp
        self.curhp = curhp
        self.atk = atk
        self.defence = defence
        self.shield = shield
        self.speed = speed
        self.kquote = kquote
        self.kdamage = kdamage
        self.gen = gen
        self.wid = wid
        self.lifesteal = lifesteal
        self.maxturnmeter = maxturnmeter
        self.turnmeter = turnmeter

    def __str__(self):
        return f"""Character(Name = {self.name}, Level = {self.level}, Effective = {self.effective}, Type = {self.fight}, 
        MaxHP = {self.maxhp}, CurHP = {self.curhp}, ATK = {self.atk}, DEF = {self.defence} SHIELD = {self.shield}, SPEED = {self.speed},
        kQuote = {self.kquote}, kDamage = {self.kdamage}, GEN = {self.gen}, WID = {self.wid}, LIFESTEAL = {self.lifesteal},
        MaxTurnmeter = {self.maxturnmeter}, Turnmeter = {self.turnmeter})"""

# this function saves the selected champion in a specific Excel file
# double names are not allowed and get denied
def saveToExcel(create_Character):
    
    try:
        df = pa.read_excel(path_champion_list)
    except FileNotFoundError:
        df = pa.DataFrame(columns=['Name', 'Level', 'Effective', 'Type', 'MaxHP', 'CurHP', 'ATK', 'DEF', 'Shield', 'Speed', 'kQuote', 'kDamage', 'Gen', 'Wid', 'Lifesteal', 'MaxTurnmeter', 'Turnmeter'])
    
    if create_Character.name in df['Name'].values:
        print(f"Der Name '{create_Character.name}' ist bereits in der Liste vorhanden. Das Objekt wird nicht hinzugefügt.")
        return
    else:
        data = {
            'Name': [create_Character.name],
            'Level': [create_Character.level],
            'Effective': [create_Character.effective],
            'Type': [create_Character.fight],
            'MaxHP': [create_Character.maxhp],
            'CurHP': [create_Character.curhp],
            'ATK': [create_Character.atk],
            'DEF': [create_Character.defence],
            'Shield': [create_Character.shield],
            'Speed': [create_Character.speed],
            'kQuote': [create_Character.kquote],
            'kDamage': [create_Character.kdamage],
            'Gen': [create_Character.gen],
            'Wid': [create_Character.wid],
            'Lifesteal': [create_Character.lifesteal],
            'MaxTurnmeter': [create_Character.maxturnmeter],
            'Turnmeter': [create_Character.turnmeter]
        }

    new_character_df = pa.DataFrame(data)
    df = pa.concat([df, new_character_df], ignore_index=True)
    df.to_excel('champion_list.xlsx', index= False)
    print(f"Der Charakter '{create_Character.name}' wurde erfolgreich zur Liste hinzugefügt.")

# this function reads from the Excel file with champions and creates a character object out of the variables
### REWORK ###
def loadCharacter(path, charater_name):
    df = pa.read_excel(path)
    character_data = df[df['Name'] == charater_name].iloc[0]
    character = create_Character(
        character_data['Name'],
        character_data['Level'],
        character_data['Effective'],
        character_data['Type'],
        character_data['MaxHP'],
        character_data['CurHP'],
        character_data['ATK'],
        character_data['DEF'],
        character_data['Shield'],
        character_data['Speed'],
        character_data['kQuote'],
        character_data['kDamage'],
        character_data['Gen'],
        character_data['Wid'],
        character_data['Lifesteal'],
        character_data['MaxTurnmeter'],
        character_data['Turnmeter'],
    )

    return character
