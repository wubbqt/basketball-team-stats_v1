from multiprocessing.sharedctypes import Value
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


def balance_teams():
    panthers = []
    bandits = []
    warriors = []
    all_teams = []
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
    all_teams = [warriors, bandits, panthers]
    return all_teams






def main_menu():
    print("BASKETBALL TEAM STATS TOOL\n\n\n")
    print("---MENU---\n\n")
    
    try:
        while True:
            menu1 = input(
                "Here are your choices: \n A) Display Team Stats \n B) Quit\n")
            if menu1 == "a" or "A":
                team_choice()
            if menu1 == "b" or "B":
                print("Quiting Application")
                break

    except ValueError:
        print("Invalid choicem, please try again.")
        
            



            
            
def team_choice():
    print("A) Panthers\nB) Bandits\nC) Warriors\n")

            
if __name__ == "__main__":
    clean_data()
    main_menu()
