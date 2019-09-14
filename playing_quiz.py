"""
This quiz will generate chord symbols for you to play.
It's designed for when you're sitting at a piano, to practice playing
different chords.
"""
import random
from datetime import datetime as dt


possible_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
possible_accidentals = [
    '',  # normal
    '#',  # sharp
    'b',
]
possible_modifiers = [
    '',  # major
    'm',  # minor
]
possible_finishers = [
    '',  # normal
    # '7',
]


def generate_chord():
    note = random.choice(possible_notes)
    accidental = random.choice(possible_accidentals)
    modifier = random.choice(possible_modifiers)
    finisher = random.choice(possible_finishers)
    return f'{note}{accidental}{modifier}{finisher}'


def run_chord_quiz():
    """
    generate a bunch of random chords to see if you can play them
    """
    cont = True
    while cont is True:
        start_time = dt.now()
        print ('\n', generate_chord(), '\n')
        result = input('press enter to continue or Q then enter to quit')
        if result == 'q' or result == 'Q':
            cont = False
        finish_time = dt.now()
        print(int(round((finish_time-start_time).total_seconds(), 0)), ' seconds')


if __name__ == '__main__':
    run_chord_quiz()
