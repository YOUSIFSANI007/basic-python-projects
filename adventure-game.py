import time
import os
from typing import Dict, List, Optional

class Player:
    def __init__(self, name: str):
        self.name = name
        self.inventory: List[str] = []
        self.visited_locations: List[str] = []
        self.health = 100

class Game:
    def __init__(self):
        self.player: Optional[Player] = None
        
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_slow(self, text: str, delay: float = 0.03):
        """Print text character by character"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def get_valid_input(self, prompt: str, valid_options: List[str]) -> str:
        """Get and validate user input"""
        while True:
            choice = input(prompt).lower().strip()
            if choice in valid_options:
                return choice
            print(f"Invalid choice. Please choose from: {', '.join(valid_options)}")
            
    def show_status(self):
        """Display player status"""
        print("\n" + "=" * 40)
        print(f"Health: {self.player.health}%")
        print("Inventory:", ", ".join(self.player.inventory) if self.player.inventory else "Empty")
        print("=" * 40 + "\n")
        
    def intro(self) -> None:
        """Game introduction"""
        self.clear_screen()
        self.print_slow("Welcome to the Enchanted Forest Adventure!")
        self.print_slow("\nIn this mysterious realm, your choices will shape your destiny...")
        
        name = input("\nWhat is your name, brave adventurer? ")
        self.player = Player(name)
        
        self.print_slow(f"\nWelcome, {self.player.name}! Your journey begins now...")
        time.sleep(1)
        
    def forest_entrance(self) -> str:
        """First game location"""
        self.clear_screen()
        self.print_slow("You stand at the entrance of an ancient forest.")
        self.print_slow("The air is thick with magic, and two paths lie before you:")
        self.print_slow("\n1. A well-worn path leading east")
        self.print_slow("2. A darker path heading north through dense trees")
        
        choice = self.get_valid_input("\nWhich path do you choose? (1/2): ", ["1", "2"])
        
        if choice == "1":
            return "meadow"
        return "dark_woods"
        
    def meadow(self) -> str:
        """Meadow location"""
        self.clear_screen()
        self.print_slow("You emerge into a sunlit meadow filled with colorful flowers.")
        
        if "meadow" not in self.player.visited_locations:
            self.print_slow("You notice a gleaming sword stuck in a nearby stone.")
            choice = self.get_valid_input("\nTry to pull out the sword? (y/n): ", ["y", "n"])
            
            if choice == "y":
                self.print_slow("\nWith a burst of strength, you pull the sword free!")
                self.player.inventory.append("Magic Sword")
                self.print_slow("The sword glows with magical energy.")
            
        self.player.visited_locations.append("meadow")
        
        self.print_slow("\nFrom here you can:")
        self.print_slow("1. Head to the mysterious cave")
        self.print_slow("2. Return to the forest entrance")
        
        choice = self.get_valid_input("\nWhat's your choice? (1/2): ", ["1", "2"])
        
        if choice == "1":
            return "cave"
        return "forest_entrance"
        
    def dark_woods(self) -> str:
        """Dark woods location"""
        self.clear_screen()
        self.print_slow("The trees loom overhead, blocking out most of the sunlight.")
        
        if "dark_woods" not in self.player.visited_locations:
            self.print_slow("\nSuddenly, a shadow creature appears!")
            
            if "Magic Sword" in self.player.inventory:
                self.print_slow("Your magic sword glows brightly, causing the creature to flee!")
            else:
                self.print_slow("The creature attacks! You barely escape, but are injured.")
                self.player.health -= 30
                if self.player.health <= 0:
                    return "game_over"
                
        self.player.visited_locations.append("dark_woods")
        
        self.print_slow("\nYou can:")
        self.print_slow("1. Press deeper into the woods")
        self.print_slow("2. Return to the forest entrance")
        
        choice = self.get_valid_input("\nWhat's your choice? (1/2): ", ["1", "2"])
        
        if choice == "1":
            return "ancient_temple"
        return "forest_entrance"
        
    def cave(self) -> str:
        """Cave location"""
        self.clear_screen()
        self.print_slow("You enter a dimly lit cave. Water drips from the ceiling.")
        
        if "cave" not in self.player.visited_locations:
            self.print_slow("\nYou find an old treasure chest!")
            self.player.inventory.append("Ancient Map")
            self.print_slow("Inside is an Ancient Map!")
            
        self.player.visited_locations.append("cave")
        
        self.print_slow("\nYou can:")
        self.print_slow("1. Explore deeper into the cave")
        self.print_slow("2. Return to the meadow")
        
        choice = self.get_valid_input("\nWhat's your choice? (1/2): ", ["1", "2"])
        
        if choice == "1":
            if "Ancient Map" in self.player.inventory:
                return "dragon_lair"
            self.print_slow("\nThe cave is too dark and complex to navigate without a map.")
            return "cave"
        return "meadow"
        
    def ancient_temple(self) -> str:
        """Temple location"""
        self.clear_screen()
        self.print_slow("You discover an ancient temple covered in mysterious runes.")
        
        if "Magic Sword" in self.player.inventory and "Ancient Map" in self.player.inventory:
            self.print_slow("\nThe sword and map begin to glow in unison...")
            return "victory"
            
        self.print_slow("\nYou sense that you're missing something important...")
        return "dark_woods"
        
    def dragon_lair(self) -> str:
        """Dragon's lair location"""
        self.clear_screen()
        self.print_slow("You enter a massive cavern. A dragon sleeps atop a pile of gold!")
        
        if "Magic Sword" not in self.player.inventory:
            self.print_slow("\nThe dragon awakens and attacks! Without a weapon, you stand no chance!")
            return "game_over"
            
        self.print_slow("\nThe dragon awakens, but your magic sword protects you.")
        self.print_slow("The dragon recognizes you as worthy and grants you passage.")
        return "victory"
        
    def victory(self) -> str:
        """Victory ending"""
        self.clear_screen()
        self.print_slow("Congratulations! You have completed your quest!")
        self.print_slow(f"\n{self.player.name}, you have proven yourself a true hero.")
        return "game_over"
        
    def game_over(self) -> str:
        """Handle game over state"""
        if self.player.health <= 0:
            self.print_slow("\nYou have been defeated... Game Over!")
        
        choice = self.get_valid_input("\nWould you like to play again? (y/n): ", ["y", "n"])
        
        if choice == "y":
            return "play_again"
        return "quit"
        
    def run(self):
        """Main game loop"""
        self.intro()
        
        # Game state machine
        current_location = "forest_entrance"
        locations = {
            "forest_entrance": self.forest_entrance,
            "meadow": self.meadow,
            "dark_woods": self.dark_woods,
            "cave": self.cave,
            "ancient_temple": self.ancient_temple,
            "dragon_lair": self.dragon_lair,
            "victory": self.victory,
            "game_over": self.game_over
        }
        
        while True:
            self.show_status()
            
            if current_location in locations:
                current_location = locations[current_location]()
                
            if current_location == "quit":
                self.print_slow("\nThank you for playing! Farewell, brave adventurer!")
                break
            elif current_location == "play_again":
                self.player = None
                self.intro()
                current_location = "forest_entrance"

if __name__ == "__main__":
    game = Game()
    game.run()
