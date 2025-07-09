import random

animals = [
    "tiger",
    "zebra",
    "horse",
    "koala",
    "sheep",
    "whale",
    "moose",
    "eagle",
    "otter",
    "panda"
]


fruits = [
    "apple",
    "mango",
    "grape",
    "guava",
    "lemon",
    "peach",
    "melon",
    "olive",
    "berry",
    "plums"
]


vegetables = [
    "onion",
    "radish",
    "chard",
    "beans",
    "leeks",
    "cress",
    "okra",
    "turnip",
    "kale",
    "yams"
]


interest=int(input("Enter in which list you gonna guess the word (1. animal, 2. fruits, 3. vegetables) :"))

if interest == 1:
    question = random.choice(animals)
elif interest == 2:
    question = random.choice(fruits)
elif interest == 3:
    question = random.choice(vegetables)
else:
    print("Enter the number of the list !!")
    
count=len(question)
list_question=list(question)

blank=[]
for i in range(0,count):
    blank.append("_")


hangman_stages = [
    """
     _______
    |       |
    |       
    |      
    |      
    |      
    |______
    """,  # 6 lives left
    """
     _______
    |       |
    |       O
    |      
    |      
    |      
    |______
    """,  # 5 lives left
    """
     _______
    |       |
    |       O
    |       |
    |      
    |      
    |______
    """,  # 4 lives left
    """
     _______
    |       |
    |       O
    |      /|
    |      
    |      
    |______
    """,  # 3 lives left
    """
     _______
    |       |
    |       O
    |      /|\\
    |      
    |      
    |______
    """,  # 2 lives left
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / 
    |      
    |______
    """,  # 1 life left
    """
     _______
    |       |
    |       O
    |      /|\\
    |      / \\
    |      
    |______
    """   # 0 lives left — game over
]

print("Let's start the hangman game")
print(hangman_stages[0])
print(list_question)
print(f"Guess the word to save the man with have {count} letters in it {blank} ")

lives=6
while lives>0 and "_" in blank:
    guess=input(f"Enter the word to fill the blanks :")
    match_found = False
    for find in range(0,count):
        if list_question[find] == guess:
            blank[find] = guess
            print(f"You guessed right {blank}")
            match_found=True
            
    if match_found :
        final_result=''.join(str(str_conv) for str_conv in blank )
    else:
        lives-=1
        print(hangman_stages[6-lives])
        print(f"You lost one live balance {lives} are left")

if "_" not in blank:
    print(f"\n You won! The word was '{final_result}'")
else:
    print(f"\n Game Over! The word was '{question}'")
    