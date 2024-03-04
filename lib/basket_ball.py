

def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


# - Where in the dictionary will you find a player's `points_per_game`? What are
#   the steps you need to complete to iterate down to that level?
# - How can you check and see if a player's name matches the name that has been
#   passed into the method as an argument?
# - What does the function's return value need to be?
# - Is there a helper function you can write to break down the process into
#   smaller chunks and avoid repetitive code?

# To get a player's number of points I need to:
# game_dict['home/away'][players][indexofplyer][name]
# For the home and away we should have a for loop. This loop must use the items() method on the dict
# Players does not require a for loop
# players index of player will require another for loop when the user index['name'] == user_inp then I will return
# the number of point per game for the given player.
# get_detail_for_player() will be the reusable function. Because other functions use the same concept.

def get_detail_for_player(detail,player_name):
    information = game_dict()
    for place,details in information.items():
         for player in details['players']:
                if player['name'] == player_name:
                    return player.get(detail,player)
                

def num_points_per_game(player_name):
    return get_detail_for_player('points_per_game',player_name)
num_points_per_game('Jarrett Allen')
    


### `player_age()`

# Build a function, `player_age()`, that takes in an argument of a player's name
# and returns that player's age.

# This will be just be like num_points_per_game() but now I will return the player's age and not the 
# players points per game

# Threfore the whole body of the function can be made into a reusable function
# get_detail_for_player() will be the reusable function

def player_age(player_name):
    return get_detail_for_player('age',player_name)


player_age('Jarrett Allen')
    


### `team_colors()`

# Build a function, `team_colors()`, that takes in an argument of the team name
# and returns a `list` of that team's colors.

# Looking through data:
# We can see that to get to the colors we have to loop over the dict.items() and say if value['colors'] == user_inp

def team_colors(team_name):
    information = game_dict()
    for place,details in information.items():
        if details['team_name'] == team_name:
            return details['colors']
team_colors('Cleveland Cavaliers')



### `team_names()`

# Build a function, `team_names()`, that operates on the dictionary to return a
# `list` of the team names.

# I just need to loop over the information in the same way as above but now there should be no if
# i should just staright away and append() team_name to the team_names list

def team_names():
    info = game_dict()
    team_names = []
    for place,details in info.items():
        team_name = details['team_name']
        team_names.append(team_name)
    return team_names

         
team_names()


# Build a function, player_numbers(), that takes 
# in an argument of a team name and returns a list of the jersey numbers for that team.

def player_numbers(team_name):
    jersey_numbers_list = []
    info = game_dict()

    for place,details in info.items():
        if details['team_name'] == team_name:
            players = details['players']
            for player in players:
                player_jersy_num = player['number']
                jersey_numbers_list.append(player_jersy_num)
    return  jersey_numbers_list
player_numbers('Cleveland Cavaliers')
    

### `player_stats()`

# Build a function, `player_stats()`, that takes in an argument of a player's name
# and returns a dictionary of that player's stats.

# The player status could just be thought of as all the information for the given player
# I have refactored the code for the function get_player_details
# so now player details does the main work.

def player_stats(player_name):
    return get_detail_for_player('status',player_name)
player_stats('Kristaps Porzingis')

 



# `average_rebounds_by_shoe_brand()`

# Build a function, `average_rebounds_by_shoe_brand()`, that will calculate the
# average number of rebounds for players who wear a particular shoe brand. The
# function should print out a message for each brand using the following format:

# So for this we can clearly see that this is going to be an iterative process.
# We will need to to loop over the players list
# So first we need to point out the things we need:
# I will need to know what brand of shoe the player wears
# I will need to know the number of rebounds the player has per game

# I can make the ccondition during the iteration be e.g if player['shoe_brand'] == 'Nike' then do
# total_Nike_reb += player['rebounds_per_game']
# Then since the shoe brands are: 'Nike','Puma','Addidas','Jordan'
# I can just cover all the conditions using ifs and elifs and an else if the shoe_brand has no matches
# Just before end of function I can compute the averages and print them

def average_rebounds_by_shoe_brand():
    info = game_dict()
    total_nike_reb = 0
    total_nike_players = 0
    
    total_puma_reb = 0
    total_puma_players = 0
    
    total_adidas_reb = 0
    total_adidas_players = 0
    
    total_jordan_reb = 0
    total_jordan_players = 0
    
    for place,details in info.items():
        for player in details['players']:
            shoe_brand = player['shoe_brand']
            if shoe_brand == 'Nike':
                total_nike_reb += player['rebounds_per_game']
                total_nike_players += 1
                
            elif shoe_brand == 'Puma':
                total_puma_reb += player['rebounds_per_game']
                total_puma_players  += 1
                
            elif shoe_brand == 'Adidas':
                total_adidas_reb += player['rebounds_per_game']
                total_adidas_players += 1
                
            elif shoe_brand == 'Jordan':
                total_jordan_reb += player['rebounds_per_game']
                total_jordan_players += 1
                
    av_nike_reb = total_nike_reb / total_nike_players
    # Because the average should be a float correct to two decimal places
    # The round() function returns a floating point number that 
    # is a rounded version of the specified number, with the specified number of decimals.

    # The default number of decimals is 0, meaning that the function will return the nearest integer.
    # Syntax: round(number, digits) 
    av_nike_reb_deci =   round(av_nike_reb,2)


    
    av_puma_reb = total_puma_reb / total_puma_players 
    av_puma_reb_deci =   round(av_puma_reb,2)
    
    av_adidas_reb = total_adidas_reb / total_adidas_players
    av_adidas_reb_deci =   round(av_adidas_reb,2)
    
    av_jordan_reb = total_jordan_reb / total_jordan_players
    av_jordan_reb_deci =   round(av_jordan_reb,2)
    
    print(f'Nike:  {av_nike_reb_deci:.2f}\nAdidas:  {av_adidas_reb_deci:.2f}\nPuma:  {av_puma_reb_deci:.2f}\nJordan:  {av_jordan_reb_deci:.2f}')
    # print(f'Puma:  {av_puma_reb_deci:.2f}')
    # print(f'Adidas:  {av_adidas_reb_deci:.2f}')
    # print(f'Jordan:  {av_jordan_reb_deci:.2f}')
    # print("Nike:  4.93\nAdidas:  7.07\nPuma:  8.50\nJordan:  3.80\n")
       
       

average_rebounds_by_shoe_brand()


# 1. Which player has the most career points?
# 2. Are there any jersey numbers that are worn by players on both teams?
# 3. Which player has the longest name?

# Number One:
# For this I could simply loop over the players for each place both home and away.
# For each place (home and away) I can loop over the players array and get .add each career_points to a set 
# I will call career_points
# After thsi I will get the heighest member of career_points using the max(set) method
# After that I can loop over the players for both places once again and say:
# If player['career_points'] == max_num:
# Return the player['name']

def most_career_points():
    info = game_dict()
    all_career_points = set()
    for place,details in info.items():
        for player in details['players']:
            player_career_points = player['career_points']
            all_career_points.add(player_career_points)
    highest_career_points = max(all_career_points)
    for place,details in info.items():
        for player in details['players']:
            if player['career_points'] == highest_career_points:
                return player['name']
most_career_points()
            
            