"""
This quiz will generate chord symbols for you to play.
It's designed for when you're sitting at a piano, to practice playing
different chords.
"""
from datetime import datetime as dt

from src.chords import generate_random_chord


def run_chord_quiz():
    """
    generate a bunch of random chords to see if you can play them
    """
    cont = True
    while cont is True:
        start_time = dt.now()
        print ('\n', generate_random_chord(), '\n')
        result = input('press enter to continue or Q then enter to quit')
        if result == 'q' or result == 'Q':
            cont = False
        finish_time = dt.now()
        print(int(round((finish_time-start_time).total_seconds(), 0)), ' seconds')


if __name__ == '__main__':
    run_chord_quiz()
