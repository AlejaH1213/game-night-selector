#people who are attending game night
gamers = []
#function to add gamer to the gamers list 
def add_gamer(gamer,gamers_list):
  # conditional to check that the gamer is putting the information necessary 
  if gamer.get('name') and gamer.get('availability'):
    gamers_list.append(gamer)
  else:
    print('Gamer missing critical information')

#dictionaries with mock gamers
add_gamer({'name': 'Kimberly wagner','availability': ['Monday', 'Tuesday', 'Friday']}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

#this function takes no arguments and returns a dictionary with the days of the week as keys and 0 as values, this function will count the availability of gamers per night 
def build_daily_frequency_table():
  return{
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0,
    'Saturday': 0,
    'Sunday': 0,
  }
count_availability = build_daily_frequency_table()

#this function takes a list of gamers and the frequence table, the function iterates through each gamer, and then iterates through each day in the gamer's availability and then adds 1 to the frequency table
def calculate_availability(gamers_list, available_frequency):
  for gamer in gamers_list:
    for day in gamer['availability']:
      available_frequency[day] += 1
calculate_availability(gamers, count_availability)
print(count_availability)

#this function determines which is the night based on the highest number of gamers available
def find_best_night(availability_table):
  best_availability = 0
  for day, availability in availability_table.items():
    if availability > best_availability:
      best_night = day
      best_availability = availability
  return best_night
game_night = find_best_night(count_availability)
print(game_night)

#this function creates a list of gamers that are available on the best night
def available_on_night(gamers_list, day):
  return [gamer for gamer in gamers_list if day in gamer['availability']]
attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = """
Dear {name}, 

We are delighted to host "{game}" night and wish you will attend. Come by {day_of_week} and have a blast!
"""

#this function takes three parameters and will output an email form for each gamer that is available on the best day for game night
def send_email(gamers_who_can_attend, day, game):
  for gamer in gamers_who_can_attend:
    print(form_email.format(name=gamer['name'], day_of_week=day, game=game))
send_email(attending_game_night, game_night, 'Catan')

#here is the procedure to have a second game night
unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers,second_night)
send_email(available_second_game_night, second_night, 'Catan')