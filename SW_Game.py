# "Vader Awaits" Star Wars Text Adventure Game by Matt Bertschy

import time

inventory = []

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
#time.sleep(4)
print()
print('Move commands: South, North, East, West.') # Define available inputs for game
print('You can also type "quit" or "q" to exit the game.')

# Create dictionary of planets and corresponding items

planets = {
          'Tatooine': {'north': 'Coruscant', 'west': 'Dagobah', 'south': 'Bespin', 'east': 'Kamino', 'Item': 'Nothing'},
          'Alderaan': {'west': 'Coruscant', 'Item': 'Star Chart'},
          'Coruscant': {'east': 'Alderaan', 'south': 'Tatooine', 'Item': 'Jedi Text'},
          'Dagobah': {'east': 'Tatooine', 'Item': 'Knowledge'},
          'Bespin': {'north': 'Tatooine', 'east': 'Hoth', 'Item': 'Hyper Drive'},
          'Hoth': {'west': 'Bespin', 'Item': 'Lightsaber'},
          'Kamino': {'west': 'Tatooine', 'north': 'Mustafar', 'Item': 'Armor'},
          'Mustafar': {'south': 'Kamino', 'Vader': 'Darth Vader'}
}

current_planet = 'Tatooine'

if __name__ == '__main__':
    # Create loop for directional moves based on planet
    while True:
        
        if current_planet == 'Mustafar':
            print('You have arrived on Mustafar. Vader awaits!')
            if len(inventory) >= 6: 
                print("You have collected all items and are ready to face Darth Vader.")
                print("You have defeated Darth Vader and saved the galaxy!")
                again = input('Do you want to play again? ').lower()
                if again == 'yes' or again == 'y':
                    inventory = []
                    current_planet = 'Tatooine'
                
                #exit()
            else:
                print("You have not collected all items. The Force is not with you. You turn to the Dark Side!")
                again = input('Do you want to play again? ').lower()
                if again == 'yes' or again == 'y':
                    inventory = []
                    current_planet = 'Tatooine'
                
                #exit()
        print(f"\nYou are on planet {current_planet}") # Output location of current planet
        if current_planet != 'Tatooine':
            if planets[current_planet]['Item'] in inventory: # If item is in inventory, do not output item
                print("You have already collected this item.")
            else:
                print(f"The item available here is {planets[current_planet]['Item']}") # Output item available on current planet
                take_item = input('Do you want to take the item? ').lower() # Define variable for item input
                if take_item == 'yes' or take_item == 'y': # If input equals 'yes' or 'y', add item to inventory
                    inventory.append(planets[current_planet]['Item'])
                    print(f"You have added {planets[current_planet]['Item']} to your inventory.")
                    print(f"Your inventory is {inventory}")
        command = input('\nWhat direction do you want to fly? ').lower() # Define variable for directional input.
        if command in planets[current_planet]: # Is current direction available on current planet?
            print(f'You have flown to planet {planets[current_planet][command]}') # Output planet traveled to
            current_planet = planets[current_planet][command] # Change variable current_planet to current planet
        elif command == 'quit' or command == 'q': # If command input equals 'quit' or 'q', exit the game
            break
        else:
            print("You cannot go that way.") # Output if input is not recognized in dictionary
    print('Thanks for playing and May the Force be With You')

# Create blank list of items


