"""
This quiz will generate chord symbols for you to play.
It's designed for when you're with your instrument, to practice playing
different chords.
"""
from datetime import datetime as dt

from src.chords import generate_random_chord
import config
from src.utils import countdown


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
    # intro
    input("This quiz is designed for you to play along with when you are with your instrument.\n\n"
          "At any time you can press CTRL + C to interrupt it.\n" \
          "To start, press ENTER.")
    while 1 == 1:
        chord = generate_random_chord()
        print('\n', chord, '\n\n Hint will be shown in')
        countdown(config.seconds_to_guess)
        print('\n\n', chord.hint, 'Next chord will be shown in')
        countdown(config.seconds_with_hint)
        print('\n\n\n\n')


if __name__ == '__main__':
    run_chord_quiz_autoproceed()
