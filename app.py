import constants
import copy


#sudo
#take existing data from players and add it to a new dictionary in a list
#while doing that clean the height, experiance, gaurdian


new_players = copy.deepcopy(constants.PLAYERS)
new_teams = copy.deepcopy(constants.TEAMS)

def clean_data():
    for player in new_players:
        player['guardians'] = (','.join(player['guardians'].split(" and")))
        
        #cant figure out how to split the first two characters of the string
        height = player["height"].split()
        player["height"] = int(height[0])

        if player["experience"] == "YES":
            player["experience"] = True
        else:
            player["experience"] = "NO"
        player["experience"] = False
        
