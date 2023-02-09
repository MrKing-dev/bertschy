# "Vader Awaits" Star Wars Text Adventure Game by Matt Bertschy

import time

print("Welcome to VADER AWAITS!")
#time.sleep(3)
print("You are Luke Skywalker and the very fate of the galaxy rests in your hands.")
#time.sleep(2)
print("You must defeat the evil Lord Vader.")
#time.sleep(2)
print("Bothan spies have located the Sith Lord on Mustafar.")
#time.sleep(2)
print("Before you face him, you must collect various items across the galaxy.")
#time.sleep(2)
print("You will start your journey on Tatooine. From there, you will fly your X-Wing to other planets.")
#time.sleep(3)
print("After you have collected all items from all planets, you will be able to face the Sith Lord on Mustafar.")
#time.sleep(4)
print("Is the Force with you, or will you turn to the Dark Side?")

print('Move commands: South, North, East, West.')
print('You can also type "quit" or "q" to exit the game.')

# Create dictionary of planets

planets = {
          'Tatooine': {'north': 'Coruscant', 'west': 'Dagobah', 'south': 'Bespin', 'east': 'Kamino'},
          'Alderaan': {'west': 'Coruscant'},
          'Coruscant': {'east': 'Alderaan', 'south': 'Tatooine'},
          'Dagobah': {'east': 'Tatooine'},
          'Bespin': {'north': 'Tatooine', 'east': 'Hoth'},
          'Hoth': {'west': 'Bespin'},
          'Kamino': {'west': 'Tatooine', 'north': 'Mustafar'},
          'Mustafar': {'south': 'Kamino'}
}

current_planet = 'Tatooine'

if __name__ == '__main__':
    while True:
        print(f"\nYou are on planet {current_planet}")
        command = input('\nWhat direction do you want to fly? ').lower()
        if command in planets[current_planet]:
            print(f'You have flown to planet {planets[current_planet][command]}')
            current_planet = planets[current_planet][command]    
        elif command == 'quit' or command == 'q':
            break
        else:
            print("You cannot go that way.")
    print('Thanks for playing!')

