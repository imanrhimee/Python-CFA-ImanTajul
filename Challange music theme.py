#! /usr/bin/env python3
 
import random as rnd
 
musicgenre = {
    'pop': 'Ariana Grande',
    'jazz': 'Billie Holiday',
    'rock': 'Awie',
    'rapper': 'Joe Flizzow',
    'blues': 'Albert King'
}

score = 0;
tries = 3
 
while tries > 0:
    try:
        random_song = rnd.choice(list(musicgenre.items()))
        intials = []
        for first_letter in random_song[0].split():
            intials.append(first_letter[0].capitalize())

        """Start a music guessing game"""

        print(f'The intials for the MUSIC GENRE are {" ".join(intials)} and the singer is {random_song[1].title()}')
        print('Clues: (POP, JAZZ, ROCK, RAPPER, BLUES, PUNK, JPOP, BEBOP)')
        print('Can you guess the MUSIC GENRE?')
        genre = input('>> ')
        if genre.lower().strip() == random_song[0].lower().strip():
            print(f'Congratulations! You have {tries - 1} tries left. Your score is {score + 1}')
            tries -= 1
            score += 1
            continue
        else:
            print(f'That is incorrect. You have {tries - 1} tries left.')
            tries -= 1
            continue
        
        break
    except ValueError as error:
        print(error)