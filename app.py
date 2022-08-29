import constants
import copy
import random

#sudo
#take existing data from players and add it to a new dictionary in a list
#while doing that clean the height, experiance, gaurdian


new_players = copy.deepcopy(constants.PLAYERS)
new_teams = copy.deepcopy(constants.TEAMS)
experience_yes = []
experience_no = []


def clean_data():
    for player in new_players:
        player['guardians'] = (','.join(player['guardians'].split(" and")))
        
        #cant figure out how to split the first two characters of the string
        height = player["height"].split()
        player["height"] = int(height[0])

        if player["experience"] == "YES":
            player["experience"] = True
            experience_yes.append(player)
            
        else:
            player["experience"] = "NO"
            player["experience"] = False
            experience_no.append(player)


clean_data()


#print(num_players_team)

def balance_teams():
    panthers = []
    bandits = []
    warriors = []
    random.shuffle(experience_yes)
    random.shuffle(experience_no)
    while experience_yes:
        warriors.append(experience_yes.pop())
        bandits.append(experience_yes.pop())
        panthers.append(experience_yes.pop())

    while experience_no:
        warriors.append(experience_no.pop())
        bandits.append(experience_no.pop())
        panthers.append(experience_no.pop())

    return panthers, warriors, bandits

balance_teams()
balanced_teams = balance_teams()
print(balanced_teams)

def main_menu():
    print("---MENU---")
    menu1 = input("Here are your choices: \n A) Display Team Stats \n B) Quit\n")
    print(menu1)
