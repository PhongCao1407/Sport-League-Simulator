'''
This file is for drafting purpose only. It is to be replace with the front end later
'''
from .models import Sports, Leagues

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
    league_name = input('Please provide a league name: ') 

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
    num_of_teams = input('\nPlease choose the number of teams for the league: ')
    print('\nGenerating teams\n')
    create_teams_random(num_of_teams)


def create_teams_manual():
    # TODO
    print()

def create_teams_random(num_of_teams):
    # TODO
    print()



'''
Utilities functions
'''
def print_list(list):
    for item in list:
        print(item)


    

    