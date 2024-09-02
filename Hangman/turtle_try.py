import turtle, random  

screen = turtle.Screen()
screen.title('game')
screen.setup(width=800, height=800)
t = turtle.Turtle() 

t.speed(50)

t.penup()  
t.goto(0, 200)  
t.pendown()

t.write("HANGMAN GAME", align = 'center', font=("Times New Roman", 30, "bold"))
t.penup()
t.goto(100, 100)
t.pendown()


t.forward(140)
t.right(180)
t.forward(70)
t.left(90)
t.forward(70)
t.right(90)

t.circle(30)

# line below head
t.seth(270)
t.penup()
t.forward(60)
t.pendown()
t.forward(50)

# left arm
t.right(130)
t.forward(50)
t.right(180)
t.forward(50)

# right arm
t.left(80)
t.forward(50)
t.left(180)
t.forward(50)

# body
t.left(50)
t.forward(50)

# left leg
left_leg1 = 50
left_leg2 = 180
t.right(50)
t.forward(50)
t.right(180)
t.forward(50)

# right leg
right_leg1 = 80
right_leg2 = 50
t.right(right_leg1)
t.forward(right_leg2)
# t.right(80)
# t.forward(50)

t.penup()
t.goto(-350, 100)
t.write('Guess the word', font=("Times New Roman", 25, "bold"))
t.goto(-340, 50)


# ------------------------------------------------------------------------

def display_text(text):
    t.penup()
    t.goto(0, 0)  
    t.pendown()
    t.write(text, align="center", font=("Arial", 24, "bold"))

easy = ["Ant", "Age", "Axe"]
generate_word = random.choice(easy)
generate = generate_word.lower()
length_generate = len(generate)
dashes = ('_') * length_generate
t.write(dashes, font=("Times New Roman", 25, "bold"))

game_continue = True
tries = 3
y = -20
while(game_continue):
    user_input = input('Guess: ')
    user_guess = user_input.lower()

    if len(user_guess) == 1:
        char_found = generate.find(user_guess)
        if char_found != -1:
            dashes = ''.join(
                user_guess if generate[i] == user_guess else dashes[i] 
                for i in range(length_generate))
            t.goto(-340, 50)
            t.write(dashes, font=("Times New Roman", 25, "bold"))
            if dashes == generate:
                t.goto(-340, -20)
                t.write('YES! YOU GUESSED IT CORRECT!!!', font=("Times New Roman", 25, "bold"))
                game_continue = False
        else:
            tries = tries - 1
            t.goto(-340, y)
            t.write(f'Try Again! {tries} tries left!', font=("Times New Roman", 25, "bold"))
            y = y - 30
            if tries == 0:
                t.goto(-340, y -30)
                t.write(f'The word was: {generate_word}', font=("Times New Roman", 25, "bold"))
                print(generate_word)
                game_continue = False
# else:
#     tries = tries - 1
#     print(f'Try Again! {tries} tries left!')
#     print("Enter a single character!")
display_text(user_input)

turtle.done() 

