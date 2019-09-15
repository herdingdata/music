"""
This structure is way over the top for now, but the reason it's here is
as a precursor for adding this together with src.visualise.
In other words, to understand exactly which notes are in each chord
"""
import random
from itertools import cycle, islice


class Chord:
    _accidental = None
    _quality = None
    _semitones = None

    def __init__(self, chord_symbol):
        self.chord_symbol = chord_symbol
        if 'maj' in self.chord_symbol:
            raise ValueError("if you're using a major chord then use a capital M instead of "
                             "lowercase 'maj'")

    def __repr__(self):
        return self.chord_symbol

    @property
    def accidental(self):
        if self._accidental is None:
            self._accidental = ''
            if len(self.chord_symbol) >= 2:
                second_char = self.chord_symbol[1]
                if second_char in ('b', '#'):
                    self._accidental = second_char
        return self._accidental

    @property
    def modifier(self):
        return 'm' if 'm' in self.chord_symbol else ''

    @property
    def root(self):
        if self.accidental != '':
            return self.chord_symbol[:2]
        else:
            return self.chord_symbol[:1]

    @property
    def quality(self):
        if self._quality is None:
            self._quality = 'major' if self.modifier == '' else 'minor'
            if self.chord_symbol.endswith('7'):
                if self.accidental == '' and len(self.chord_symbol) == 2 or \
                        len(self.accidental) == 1 and len(self.chord_symbol) == 3:
                    self._quality = 'dominant seventh'
                else:
                    self._quality = self._quality + ' seventh'
        return self._quality

    @property
    def notes(self):
        """
        calculate all the notes in this chord

        :return: tuple(str)
        """
        sequence = generate_note_sequence(self.root, self.force_note_sequence_flat)
        notes = []
        # for semitone_idx in self.semitones:
        #     notes.append(next(islice(sequence, semitone_idx, semitone_idx + 1)))
        for idx, note in enumerate(islice(sequence, max(self.semitones) + 1)):
            if idx in self.semitones:
                notes.append(note)
        return tuple(notes)


    @property
    def semitones(self):
        """
        calculate all the semitones that will be used for the notes

        :return: tuple(int)
        """
        if self._semitones is None:
            if self.quality == 'major':
                # 1st, 3rd, 5th notes of the major scale
                self._semitones = (0, 4, 7)
            elif self.quality == 'minor':
                # 1st, 3rd, 5th notes of the natural minor scale
                self._semitones = (0, 3, 7)
            elif self.quality == 'major seventh':
                # 1st, 3rd, 5th, 7th notes of the major scale
                self._semitones = (0, 4, 7, 11)
            elif self.quality == 'minor seventh':
                # 1st, 3rd, 5th, 7th notes of the natural minor scale
                self._semitones = (0, 3, 7, 10)
            elif self.quality == 'dominant seventh':
                # 1st, 3rd, 5th, flat 7th notes of the major scale
                self._semitones = (0, 4, 7, 10)
        return self._semitones

    @property
    def force_note_sequence_flat(self):
        """
        if we have a flat as the root then we should ensure that any
        scale we use includes flat notes. If not then default to sharp.
        :return: bool
        """
        return self.accidental == 'b'


def generate_note_sequence(starting_note, force_notes_flat):
    """
    get a generator that will go through all the notes on the piano

    :param starting_note: where to start the sequence from
    :param force_notes_flat: the sequence should use flat notes, not sharps
    :return: generator
    """
    if force_notes_flat:
        possible_notes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
        # if starting note is one of these then rename the note
        # this is probably not the right music theory way to do it, but it works
        bump_notes = {'Cb': 'B', 'Fb': 'E'}
    else:
        possible_notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        bump_notes = {'E#': 'F', 'B#': 'C'}
    if starting_note in bump_notes:
        starting_note = bump_notes[starting_note]
    in_sequence = False

    for note in cycle(possible_notes):
        if in_sequence:
            yield note
        else: # we're looking for the start note
            if note == starting_note:
                in_sequence = True
                yield note


def generate_random_chord():
    possible_notes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
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
    note = random.choice(possible_notes)
    accidental = random.choice(possible_accidentals)
    modifier = random.choice(possible_modifiers)
    finisher = random.choice(possible_finishers)
    return Chord(f'{note}{accidental}{modifier}{finisher}')
