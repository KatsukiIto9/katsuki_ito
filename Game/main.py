import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JRPG Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Character Classes and Skills
class Character:
    def __init__(self, name, char_class, level=1):
        self.name = name
        self.char_class = char_class
        self.level = level
        self.hp = 100 + (level * 10)  # HP increases with level
        self.skills = self.get_skills(char_class)

    def get_skills(self, char_class):
        skills = {
            "Warrior": ["Slash", "Heavy Attack", "Taunt", "Rush", "Shield Defense"],
            "Mage": ["Arcane Blast", "Fire Wall", "Ice Arrow", "Lightning", "Heal"],
            "Rogue": ["Stab", "Blink", "Smoke Screen", "Critical Hit", "Poison", "Assassinate"],
        }
        return skills[char_class]

    def level_up(self):
        self.level += 1
        self.hp += 1000  # Increase HP on level up

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 80 + (level * 8)

# Game Functionality
def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    
    while enemy.hp > 0 and player.hp > 0:
        # Player's turn
        print(f"{player.name}'s turn! HP: {player.hp}")
        print("Choose a skill:")
        for idx, skill in enumerate(player.skills):
            print(f"{idx + 1}. {skill}")
        
        choice = int(input("Select your skill (1-5): ")) - 1
        damage = player.level * 40
        enemy.hp -= damage
        print(f"{player.name} uses {player.skills[choice]} and deals {damage} damage!")
        
        # Enemy's turn
        if enemy.hp > 0:
            enemy_damage = enemy.level * 5
            player.hp -= enemy_damage
            print(f"{enemy.name} attacks and deals {enemy_damage} damage!")

    if player.hp <= 0:
        print("You have been defeated!")
        return False
    else:
        print(f"{enemy.name} has been defeated!")
        player.level_up()
        return True

def main():
    running = True
    player_name = input("Enter your character's name: ")
    player_class = input("Choose your class (Warrior, Mage, Rogue): ")
    player = Character(player_name, player_class)
    
    while running:
        screen.fill(WHITE)
        print(f"\n{player.name} (Level {player.level}, HP {player.hp})")
        
        # Random enemy encounter
        enemy_name = random.choice(["Goblin", "Skeleton", "Demon Lord"])
        enemy_level = random.randint(1, player.level + 5) if player.level < 100 else 100
        enemy = Enemy(enemy_name, enemy_level)

        if battle(player, enemy) is False:
            running = False
        
        if player.level >= 100:
            print("You are ready to face the Demon Lord!")
            enemy = Enemy("Demon Lord", 100)
            if not battle(player, enemy):
                running = False
            else:
                print("You have defeated the Demon Lord! Congratulations!")

        # Game Loop Control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
