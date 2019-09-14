"""
This structure is way over the top for now, but the reason it's here is
as a precursor for adding this together with src.visualise.
In other words, to understand exactly which notes are in each chord
"""
import random

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


class Chord:
    def __init__(self, chord_symbol):
        self.chord_symbol = chord_symbol
        if 'maj' in self.chord_symbol:
            raise ValueError("if you're using a major chord then use a capital M")

    def __repr__(self):
        return self.chord_symbol

    @property
    def accidental(self):
        return ''

    @property
    def modifier(self):
        return 'm' if 'm' in self.chord_symbol else ''

    @property
    def root(self):
        return self.chord_symbol

    @property
    def quality(self):
        return 'major' if self.modifier == '' else 'minor'


def generate_random_chord():
    note = random.choice(possible_notes)
    accidental = random.choice(possible_accidentals)
    modifier = random.choice(possible_modifiers)
    finisher = random.choice(possible_finishers)
    return f'{note}{accidental}{modifier}{finisher}'
