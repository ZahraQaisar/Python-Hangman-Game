import list_working as lw

def main():
    game = True
    while(game):
        user_input = input('''                  
                           === HANGMAN GAME ===
            Select Level (EASY / MEDIUM / HARD)
            (To QUIT press 'q')
            Enter: ''')
        user = user_input.lower()
        
        if user == 'easy':
            print("You've selected level easy.")
            lw.easy_level()
                
        elif user == 'medium':
            print("You've selected level medium.")
            lw.medium_level()
                
        elif user == 'hard':
            print("You've selected level hard.")
            lw.hard_level()
            
        elif user == 'q':
            game = False
            
        else:
            print("Invalid Input!")
    
main()