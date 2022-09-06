import constants
import copy
import random

new_players = copy.deepcopy(constants.PLAYERS)
new_teams = copy.deepcopy(constants.TEAMS)
experience_yes = []
experience_no = []
panthers = []
bandits = []
warriors = []

def clean_data():
    for player in new_players:
        player['guardians'] = (','.join(player['guardians'].split(" and")))
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
    return panthers, bandits, warriors


def team_stats(team):
    player_count = len(team)
    experienced_count = 0
    inexperienced_count = 0
    total_height = 0
    names_players = []
    gaurdians_team = []
    for player in team:
        if player ["experience"] == True:
            experienced_count += 1
        elif player["experience"] == False:
            inexperienced_count += 1
    for player in team:
        total_height += player["height"]
    average_height = round(total_height / len(team))
    for player in team:
        names_players.append(player['name'])
        gaurdians_team.append(player['guardians'])

    


    print("\n-------------\n")
    print("Total Players: ", player_count)
    print("Total Experienced: ", experienced_count)
    print("Total Inexperienced: ", inexperienced_count)
    print("Average Height: ", average_height)
    print("Player Names: ")
    print(', '.join(names_players))
    print("Gaurdian Names: ")
    print(', '.join(gaurdians_team))
    print("\n")
    


def main_menu():
    
    while True:
        user_option = input("BASKETBALL TEAM STATS TOOL: \n\n"
                            "---MENU---\n\n"
                            "Here are your choices:\n"
                            "A) Display Team Stats\n"
                            "B) Quit\n\n Enter an option: \n").upper()
        if user_option == "A":
            print(
                "A) Panthers\n"
                "B) Warriors\n"
                "C) Bandits\n")
            
            team_option = input("Select a team from above\n").upper()
            if team_option == "A":
                print("\n\nDisplaying Panther Stats")
                team_stats(panthers)
            elif team_option == "B":
                print("\n\nDisplaying Warriors Stats")
                team_stats(warriors)
            elif team_option == "C":
                print("\n\nDisplaying Bandits Stats")
                team_stats(bandits)
            else:
                print("\n\nInvalid Selection, try again")
        elif user_option == "B":
            print("Okay bye...")
            break
        else:
            print("Invalid Selection")

if __name__ == "__main__":
    clean_data()
    balance_teams()
    main_menu()