import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Inventory: {', '.join(self.inventory)}")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You've acquired {item}!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Game Over - You have been defeated!")
            quit()

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        self.intro()
        self.create_character()
        self.main_quest()

    def intro(self):
        print("Welcome to 'Quest for the Lost Amulet'!")
        print("Your mission is to find the legendary Lost Amulet.")
        print("Are you ready to begin?\n")

    def create_character(self):
        name = input("Enter your character's name: ")
        self.player = Player(name)
        print(f"Welcome, {self.player.name}!")

    def main_quest(self):
        print("\nYou embark on your journey...")
        print("As you travel through the dense forest, you encounter a fork in the road.")
        choice = input("Do you take the left path or the right path? (left/right): ").lower()

        if choice == "left":
            print("\nYou chose the left path...")
            print("You discover an old temple deep within the woods.")
            self.explore_temple()
        elif choice == "right":
            print("\nYou chose the right path...")
            print("You encounter a band of thieves!")
            self.battle_thieves()
        else:
            print("Invalid choice. Please try again.")
            self.main_quest()

    def explore_temple(self):
        print("\nYou cautiously enter the temple...")
        print("You find a hidden chamber with a treasure chest.")
        loot = random.choice(["gold coins", "health potion", "sword"])
        self.player.add_to_inventory(loot)
        print("After exploring further, you find a mysterious inscription.")
        print("It hints at the location of the Lost Amulet.")

    def battle_thieves(self):
        print("\nYou prepare for battle with the thieves...")
        enemy_health = 50
        while enemy_health > 0 and self.player.health > 0:
            print(f"Your health: {self.player.health}")
            print(f"Enemy's health: {enemy_health}")
            attack = input("Do you attack (yes/no)? ").lower()
            if attack == "yes":
                damage = random.randint(10, 20)
                enemy_health -= damage
                print(f"You attack the thieves and deal {damage} damage!")
            else:
                print("You hesitated and took a hit!")
                self.player.take_damage(10)

        if self.player.health > 0:
            print("You defeated the thieves!")
            self.player.add_to_inventory("amulet fragment")
        else:
            print("You were defeated by the thieves. Game Over!")

        print("\nYou continue your quest...")
        self.main_quest()

# Main function to start the game
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
