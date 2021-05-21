"""
A bigger quiz for sitting at your instrument

Choose between 1 of the following 3 at random

1) Play a chord

2) Play a scale

3) Play these 4 notes
"""
import random

import config
from src.chords import generate_random_chord
from src import visualise
from src.utils import countdown


def play_chord():
    print("Play a chord")
    chord = generate_random_chord()
    print('\n', chord, '\n\n Hint will be shown in')
    countdown(config.seconds_to_guess)
    print('\n\n', chord.hint, 'Next question will be shown in')
    countdown(config.seconds_with_hint)
    print('\n\n\n\n\n\n\n\n')


# def play_scale():
#     print("Play a scale")  # TODO
#     pass


def play_some_notes():
    print("Play some notes")
    random_staff = random.choice((visualise.TrebleStaff, visualise.BassStaff))(None)
    chosen_notes = random.sample(random_staff.valid_notes, config.play_some_notes_number_notes)
    visualise.visualise_notes(chosen_notes, random_staff)
    expected = ', '.join([n.letter for n in chosen_notes])
    print('\n\n Hint will be shown in')
    countdown(config.seconds_to_guess)
    print('\n\n The notes are', expected, '\n\n', 'Next question will be shown in')
    countdown(config.seconds_with_hint)
    print('\n\n\n\n\n\n\n\n')


def run_quiz_autoproceed():
    """
    once started this quiz will keep going until interrupted
    """
    # intro
    input("This quiz is designed for you to play along with when you are with your instrument.\n"
          "You'll be asked to play either a chord, a scale, or some random notes.\n"
          "You can tweak some of the parameters in config.py. "
          "If you change them then make sure to restart this quiz.\n\n"
          "At any time you can press CTRL + C to interrupt.\n" \
          "To start, press ENTER.")
    while 1 == 1:
        quiz_function = random.choice((
            play_chord,
            # play_scale,
            play_some_notes
        ))
        quiz_function()


if __name__ == '__main__':
    run_quiz_autoproceed()
