import random

choices = word_list = [
    "car", "farm", "nigeria", "alden", "ezbon", "fox", "apple", "banana", "cherry", "dog",
    "elephant", "fish", "grape", "house", "ice", "jack", "kite", "lemon", "monkey", "notebook",
    "orange", "parrot", "queen", "rose", "snake", "tree", "umbrella", "violet", "whale", "xylophone",
    "yellow", "zebra", "airplane", "ball", "cat", "dinosaur", "eggplant", "flower", "giraffe", "hat",
    "ink", "jungle", "kiwi", "lion", "mountain", "net", "octopus", "piano", "question", "rabbit",
    "star", "tiger", "unicorn", "volcano", "watermelon", "x-ray", "yarn", "zoo", "ant", "butterfly",
    "cow", "dolphin", "elephant", "fish", "grapes", "hippopotamus", "iceberg", "jellyfish", "kangaroo",
    "lemonade", "mango", "night", "octagon", "penguin", "quail", "rocket", "sun", "tree", "universe",
    "vulture", "water", "xmas", "yellowstone", "zinnia", "air", "balloon", "cloud", "desk", "elephant",
    "fire", "green", "heron", "insect", "jelly", "koala", "lighthouse", "moon", "nectar", "orange",
    "pumpkin", "quilt", "ring", "sunflower", "toy", "underwater", "violet", "wizard", "xenon", "year",
    "zigzag", "apple", "bread", "candy", "daisy", "earth", "flame", "grapes", "harbor", "iris", "jewel"
]
choice = random.choice(choices)
guessed_word = []
progress = ["-"] * len(choice)
lives = 7
correct = False
not_g_word = []

print(f"Progress: {progress}")

while lives != 0 and "".join(progress) != choice:
    guess = input("Choose a letter: ")
    
    if len(guess) != 1:
        print("a word aldi smh")
        continue
    
    if guess in guessed_word:
        print("Already chosen")
        continue
    
    if guess in not_g_word:
        print("Already chosen, wrong answer tho stewpid")
    
    for index in range(len(choice)):
        if choice[index] == guess:
            progress[index] = guess
            guessed_word.append(guess)
            correct = True

    if correct == False and guess not in "".join(not_g_word):
        print(not_g_word)
        lives -= 1
        not_g_word.append(guess)
    else:
        correct = False
            
    print(f"Your lives: {lives}, Your progress: {progress}")
    print(lives)
    print("".join(progress))
    
if lives > 0 and "".join(progress) == choice:
    print(f"You won! Word was {choice}")
else:
    print(f"You lost LOSER, the word was {choice}")
