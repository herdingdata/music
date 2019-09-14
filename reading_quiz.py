"""
In this module we generate a bunch of notes and challenge the user.
You don't need a piano for this one
"""
import random
from typing import Iterable
from src import visualise


def visualise_notes(notes: Iterable[visualise.Note], empty_staff: Iterable[visualise.Staff]):
    if isinstance(empty_staff, visualise.TrebleStaff):
        print(visualise.visualise_notes_on_a_treble_staff(notes))
    else:
        print(visualise.visualise_notes_on_a_bass_staff(notes))


def run_quiz_with_empty_staff(number_of_notes: int, empty_staff: visualise.Staff):
    chosen_notes = random.sample(empty_staff.valid_notes, number_of_notes)
    visualise_notes(chosen_notes, empty_staff)
    user_notes = input('\nWhat notes are these? Enter their letters in order:')
    user_notes = user_notes.upper()
    expected = ''.join([n.letter for n in chosen_notes])
    if user_notes == expected:
        print("Correct.")
    else:
        print(f"Wrong. The right answer was {expected}.")


def run_quiz():
    number_of_notes = 4
    treble_staff = visualise.TrebleStaff(None)
    run_quiz_with_empty_staff(number_of_notes, treble_staff)
    bass_staff = visualise.BassStaff(None)
    run_quiz_with_empty_staff(number_of_notes, bass_staff)


if __name__ == '__main__':
    run_quiz()
