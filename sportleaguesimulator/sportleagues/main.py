'''
This file is for drafting purpose only. It is to be replace with the front end later
'''
# Database
from .models import Sports, Leagues, Teams, Players

# Package
from faker import Faker
fake = Faker()

# Utilities
from .utils.utils import print_list, generate_random_letter, generate_random_jersey_number


def main():
    INPUT_TEXT = """\nPlease choose an option:\n
    1) Create new sport\n
    2) Create new league\n
    """
    option = int(input(INPUT_TEXT))
    
    options = set([1, 2])
    
    while option in options:
        if option == 1:
            create_sport()
        elif option == 2:
            create_league()
        else:
            break

        option = input(INPUT_TEXT)



'''
CREATE Operations
'''

def create_sport():
    # Print existing sports
    sports = Sports.objects.all()
    print('Sports\n')
    print_list(sports)

    # Get sport name
    sport_name = input('Please provide a sport name: ')

    # Create new sport
    try:
        new_sport = Sports(name=sport_name)
        new_sport.save()
        print('Create sport successful.')
    except:
        print('There was an error.')
        return
    

def create_league():
    # Get league name
    league_name = input('\nPlease provide a league name: ') 

    # To get a sport for the league
    sports = Sports.objects.all()

    print("\nSports\n")
    print_list(sports)
    
    chosen_sport_input = input("\nPlease choose a sport: ")
    chosen_sport = None

    # Get sport instance
    for sport in sports:
        if sport.name == chosen_sport_input:
            chosen_sport = sport
            break
    
    # Error handling
    if chosen_sport == None:
        print('That is not a valid sport.\n')
        return 

    # Add new sport to db
    try:
        new_league = Leagues(sport=chosen_sport, name=league_name)
        new_league.save()
        print('\nCreate team successful\n')
    except: # Need to add the error here
        print('There was an error.')


    # Generating teams
    num_of_teams = int(input('\nPlease choose the number of teams for the league: '))
    create_teams_random(new_league, num_of_teams)


def create_team(team_name, team_league, team_city):
    team = Teams(name=team_name, location=team_city, league=team_league)
    team.save()
    return team


def create_teams_random(team_league, num_of_teams):
    # TODO
    print('\nGenerating teams...\n')

    num_of_players = int(input('\nHow many players do you want in a team?\n'))

    # To keep track of used team name
    team_names = set()

    for _ in range(num_of_teams):
        # Generate team name
        random_letter = generate_random_letter()
        while random_letter in team_names:
            random_letter = generate_random_letter()

        team_name = random_letter
        team_names.add(team_name)

        # Generate random city
        team_city = fake.city()

        # Create team
        team = create_team(team_name, team_league, team_city)

        # Create players for team
        print('\nCreated team', team_name)
        print('\nGenerating players...\n')
        create_players_random(team, num_of_players)


def create_player(player_first_name, player_last_name, player_jersey_number, player_team):
    player = Players(first_name=player_first_name, last_name=player_last_name, jersey_number=player_jersey_number, team=player_team)
    player.save()
    return player


def create_players_random(player_team, num_of_players):
    player_names = set()
    for _ in range(num_of_players):
        # Get player details
        player_first_name = fake.first_name_male()
        player_last_name = fake.last_name_male()
        player_jersey_number = generate_random_jersey_number()

        # Create players
        player = create_player(player_first_name, player_last_name, player_jersey_number, player_team)
        


        






    