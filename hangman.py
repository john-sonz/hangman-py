import random
from string import ascii_letters

WORDLIST_PATH = "wordlist.txt"

with open("wordlist.txt") as f:
    lines = f.read().splitlines()
    target_word = random.choice(lines)

target_word_len = len(target_word)

guessed_str = ["_"] * target_word_len
used_chars = set()
errors_left = 5
letters_left = target_word_len

while errors_left > 0 and letters_left > 0:
    print(f'Word to guess: {" ".join(guessed_str)}')
    print(f'Letters left to guess: {letters_left}, errors_left: {errors_left}')
    letter = input("Guess a letter: ").lower()

    if letter == "" or letter not in ascii_letters:
        print("That's not a letter")
        continue

    if letter in used_chars:
        print("You already guessed this letter!")
    else:
        used_chars.add(letter)
        if letter in target_word:
            print("Good guess!")
            for i, char in enumerate(target_word):
                if char == letter:
                    guessed_str[i] = letter
                    letters_left -= 1
        else:
            print("Bad guess :(")
            errors_left -= 1


if letters_left == 0:
    print(f'You guessed the word! {target_word}')
else:
    print(f'Too many errors You lost! \"{target_word}\" was the answer')
