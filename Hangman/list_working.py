import random

easy = [
    "Ant", "Age", "Apple", "Ball", "Bear", "Bird", "Bold", "Cake",
    "Cat", "Coal", "Cold", "Desk", "Dog", "Drum", "Duck", "Easy",
    "Ear", "Exit", "Fast", "Fish", "Firm", "Frog", "Gate", "Gold"
]

medium = [
    "Apple", "Bright", "Candle", "Dance", "Eagle", "Forest", "Glove",
    "Happy", "Image", "Jewel", "Knife", "Lemon", "Magic", "Night",
    "Ocean", "Piano", "Queen", "River", "Shine", "Tiger", "Under"
]

hard = [
    "Abandoner", "Backbone", "Catalogs", "Defender", "Elevation", "Fascinate",
    "Generator", "Hospital", "Influence", "Journey", "Knowledge", "Liberated",
    "Magnificent", "Notorious", "Operator", "Peculiar", "Quadrant", "Recover"
]

def generate_dashes(level_type):
    generate_word = random.choice(level_type)
    generate = generate_word.lower()
    length_generate = len(generate)
    # print(generate, length_generate)
    
    dashes = '_' * length_generate
    print(dashes)
    
    tries = 3
    # for x in range(len(generate)):
    game_continue = True
    while(game_continue):
        user_guess = input('Guess the word: ').lower()
        if len(user_guess) == 1:
            char_found = generate.find(user_guess)
            if char_found != -1:
                # dashes = dashes[ : char_found] + user_guess + dashes[char_found + 1 : ]
                dashes = ''.join(
                    user_guess if generate[i] == user_guess else dashes[i] 
                    for i in range(length_generate))
                print(dashes)
                if dashes == generate:
                    print("=== YES! YOU GUESSED IT CORRECT!!! ===")
                    game_continue = False
            else:
                tries = tries - 1
                print(f'Try Again! {tries} tries left!')
                if tries == 0:
                    print('The word was: ', generate)
                    # exit()
                    game_continue = False
        else:
            tries = tries - 1
            print(f'Try Again! {tries} tries left!')
            print("Enter a single character!")
        
def easy_level():
    generate_dashes(easy)

def medium_level():
    generate_dashes(medium)

def hard_level():
    generate_dashes(hard)
    


