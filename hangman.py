import random

# Word list with hints
words = {
    "python": "Programming language",
    "apple": "A fruit",
    "tiger": "Wild animal",
    "india": "A country",
    "computer": "Electronic device"
}

# Select random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
attempts = 6

# Hangman stages
stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("🎮 Welcome to Hangman!")
print("Hint:", hint)

# Game loop
while attempts > 0:
    display = ""
    
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print("\nWord:", display)
    print(stages[6 - attempts])
    
    if "_" not in display:
        print("🎉 You won!")
        break
    
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_letters:
        print("⚠️ Already guessed!")
        continue
    
    guessed_letters.append(guess)
    
    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)

if attempts == 0:
    print(stages[6])
    print("💀 Game Over! The word was:", word)