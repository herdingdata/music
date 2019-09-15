"""
This quiz will generate chord symbols for you to play.
It's designed for when you're with your instrument, to practice playing
different chords.
"""
import sys
from datetime import datetime as dt
from time import sleep

from src.chords import generate_random_chord


def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(' ' + str(i))
        sys.stdout.flush()
        sleep(1)


def run_chord_quiz_manually_proceed():
    """
    manually proceed to the next chord
    """
    cont = True
    while cont is True:
        start_time = dt.now()
        print('\n', generate_random_chord(), '\n')
        result = input('press enter to continue or Q then enter to quit')
        if result == 'q' or result == 'Q':
            cont = False
        finish_time = dt.now()
        print(int(round((finish_time-start_time).total_seconds(), 0)), ' seconds')


def run_chord_quiz_autoproceed():
    """
    once started this quiz will keep going until interrupted
    """
    seconds_to_guess_the_chord = 20
    seconds_with_hint = 20
    # intro
    input("This quiz is designed for you to play along with when you are with your instrument.\n\n"
          "At any time you can press CTRL + C to interrupt it.\n" \
          "To start, press ENTER.")
    while 1 == 1:
        chord = generate_random_chord()
        print('\n', chord, '\n\n Hint will be shown in')
        countdown(seconds_to_guess_the_chord)
        print('\n\n', chord.hint, 'Next chord will be shown in')
        countdown(seconds_with_hint)
        print('\n\n\n\n')


if __name__ == '__main__':
    run_chord_quiz_autoproceed()
