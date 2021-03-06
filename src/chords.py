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
        if 'm' in self.chord_symbol and 'dim' not in self.chord_symbol:
            return 'm'
        else:
            return ''

    @property
    def root(self):
        if self.accidental != '':
            return self.chord_symbol[:2]
        else:
            return self.chord_symbol[:1]

    @property
    def quality(self):
        if self._quality is None:
            if 'dim' in self.chord_symbol:
                self._quality = 'diminuished'
            elif self.modifier == '':
                self._quality = 'major'
            else:
                self._quality = 'minor'
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
                self._semitones = (0, 4, 7)
            elif self.quality == 'minor':
                self._semitones = (0, 3, 7)
            elif self.quality == 'major seventh':
                self._semitones = (0, 4, 7, 11)
            elif self.quality == 'minor seventh':
                self._semitones = (0, 3, 7, 10)
            elif self.quality == 'dominant seventh':
                self._semitones = (0, 4, 7, 10)
            elif self.quality == 'diminuished':
                self._semitones = (0, 3, 6)
            elif self.quality == 'diminuished seventh':
                self._semitones = (0, 3, 6, 9)
        return self._semitones

    @property
    def hint(self):
        hints = {
            'major': '1st, 3rd, 5th notes of the major scale',
            'minor': '1st, 3rd, 5th notes of the natural minor scale',
            'major seventh': '1st, 3rd, 5th, 7th notes of the major scale',
            'minor seventh': '1st, 3rd, 5th, 7th notes of the natural minor scale. '
                             'In other words, the 1st, flat 3rd, 5th and flat 7th notes of the '
                             'major scale.',
            'dominant seventh': '1st, 3rd, 5th, flat 7th notes of the major scale',
            'diminuished': '1st, flat 3rd, flat 5th notes of the major scale. '
                     'In other words, take the corresponding minor chord and flatten the fifth.',
            'diminuished seventh': '1st, flat 3rd, flat 5th and double-flat seventh notes of the '
                                   'major scale. In other words, take the corresponding minor '
                                   'seventh chord and flatten both the fifth and seventh.',
        }
        full_hint = f'{self.chord_symbol} is a {self.quality} chord. \n' \
                    f' It is made up of the {hints[self.quality]}. \n It has the notes ' \
                    f'{", ".join(self.notes)}. \n\n'
        return full_hint

    @property
    def force_note_sequence_flat(self):
        """
        if we have a flat as the root or a diminuished chord that's not a sharp then we should
        ensure that any scale we use includes flat notes. If not then default to sharp.
        There's probably a much better way of determining this.
        :return: bool
        """
        return self.accidental == 'b' or (self.quality.startswith('diminuished') and self.accidental != '#')


def generate_note_sequence(starting_note, force_notes_flat):
    """
    get a generator that will go through all the music notes

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
        '',  # no accidental
        '#',  # sharp
        'b',  # flat
    ]
    possible_modifiers = [
        '',  # major
        'm',  # minor
        'Maj7',  # major seventh  (M7 also works, but is less explicit)
        'm7',  # minor seventh
        '7',  # dominant seventh
        'dim',  # diminuished
        'dim7',  # diminuished seventh
    ]
    note = random.choice(possible_notes)
    accidental = random.choice(possible_accidentals)
    modifier = random.choice(possible_modifiers)
    return Chord(f'{note}{accidental}{modifier}')
