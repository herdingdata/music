import itertools

from pytest import raises

from src.chords import Chord, generate_note_sequence

"""
CHECKLIST
Main ones               example notation
    YES Major           C
    YES Minor           Cm
    YES Diminished      Cdim
    • Augmented
    • Suspended 2nd
    • Suspended 4th
    • Flat 5th
    • 6th
    • Minor 6th
    YES Dominant 7th    C7
    YES Minor 7th       Cm7
    • Diminished 7th
    YES Major 7th       CM7 (CMaj7)
    • Minor, Major 7th
    • 7/6

Jazzy chords
    • 9th
    • Minor 9th
    • Flat 9th
    • Minor, Flat 9th
    • Augmented 9th
    • 9/6
    • Minor 9/6
    • 11th
    • Minor 11th
    • Augmented 11th
    • Minor, Augmented 11th
    • 13th
    • Minor 13th
    • 13th, Augmented 11th
    • Minor 13th, Augmented 11th
"""


class TestValidation:
    def test__lcase_maj_in_chord_symbol__raises_ValueError(self):
        with raises(ValueError):
            Chord('Cmaj')


class TestMajorChords:
    def test__A__as_expected(self):
        chord_symbol = 'A'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('A', 'C#', 'E')

    def test__B__as_expected(self):
        chord_symbol = 'B'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('B', 'D#', 'F#')

    def test__C__as_expected(self):
        chord_symbol = 'C'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('C', 'E', 'G')

    def test__D__as_expected(self):
        chord_symbol = 'D'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('D', 'F#', 'A')

    def test__E__as_expected(self):
        chord_symbol = 'E'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('E', 'G#', 'B')

    def test__F__as_expected(self):
        chord_symbol = 'F'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('F', 'A', 'C')

    def test__G__as_expected(self):
        chord_symbol = 'G'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('G', 'B', 'D')


class TestMinorChords:
    def test__Am__as_expected(self):
        chord_symbol = 'Am'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'A'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('A', 'C', 'E')

    def test__Bm__as_expected(self):
        chord_symbol = 'Bm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'B'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('B', 'D', 'F#')

    def test__Cm__as_expected(self):
        chord_symbol = 'Cm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'C'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('C', 'D#', 'G')

    def test__Dm__as_expected(self):
        chord_symbol = 'Dm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'D'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('D', 'F', 'A')

    def test__Em__as_expected(self):
        chord_symbol = 'Em'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'E'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('E', 'G', 'B')

    def test__Fm__as_expected(self):
        chord_symbol = 'Fm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'F'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('F', 'G#', 'C')

    def test__Gm__as_expected(self):
        chord_symbol = 'Gm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'G'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('G', 'A#', 'D')


class TestMajorSharpChords:
    def test__Asharp__as_expected(self):
        chord_symbol = 'A#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('A#', 'D', 'F')

    def test__Bsharp__as_expected(self):
        chord_symbol = 'B#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('C', 'E', 'G')

    def test__Csharp__as_expected(self):
        chord_symbol = 'C#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('C#', 'F', 'G#')

    def test__Dsharp__as_expected(self):
        chord_symbol = 'D#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('D#', 'G', 'A#')

    def test__Esharp__as_expected(self):
        chord_symbol = 'E#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('F', 'A', 'C')

    def test__Fsharp__as_expected(self):
        chord_symbol = 'F#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('F#', 'A#', 'C#')

    def test__Gsharp__as_expected(self):
        chord_symbol = 'G#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('G#', 'C', 'D#')


class TestSharpMinorChords:
    def test__Asharpm__as_expected(self):
        chord_symbol = 'A#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'A#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('A#', 'C#', 'F')

    def test__Bsharpm__as_expected(self):
        chord_symbol = 'B#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'B#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('C', 'D#', 'G')

    def test__Csharpm__as_expected(self):
        chord_symbol = 'C#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'C#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('C#', 'E', 'G#')

    def test__Dsharpm__as_expected(self):
        chord_symbol = 'D#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'D#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('D#', 'F#', 'A#')

    def test__Esharpm__as_expected(self):
        chord_symbol = 'E#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'E#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('F', 'G#', 'C')

    def test__Fsharpm__as_expected(self):
        chord_symbol = 'F#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'F#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('F#', 'A', 'C#')

    def test__Gsharpm__as_expected(self):
        chord_symbol = 'G#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'G#'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('G#', 'B', 'D#')


class TestMajorFlatChords:
    def test__Ab__as_expected(self):
        chord_symbol = 'Ab'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Ab', 'C', 'Eb')

    def test__Bb__as_expected(self):
        chord_symbol = 'Bb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Bb', 'D', 'F')

    def test__Cb__as_expected(self):
        chord_symbol = 'Cb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('B', 'Eb', 'Gb')

    def test__Db__as_expected(self):
        chord_symbol = 'Db'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Db', 'F', 'Ab')

    def test__Eb__as_expected(self):
        chord_symbol = 'Eb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Eb', 'G', 'Bb')

    def test__Fb__as_expected(self):
        chord_symbol = 'Fb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('E', 'Ab', 'B')

    def test__Gb__as_expected(self):
        chord_symbol = 'Gb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Gb', 'Bb', 'Db')


class TestMinorFlatChords:
    def test__Abm__as_expected(self):
        chord_symbol = 'Abm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Ab'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Ab', 'B', 'Eb')

    def test__Bbm__as_expected(self):
        chord_symbol = 'Bbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Bb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Bb', 'Db', 'F')

    def test__Cbm__as_expected(self):
        chord_symbol = 'Cbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Cb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('B', 'D', 'Gb')

    def test__Dbm__as_expected(self):
        chord_symbol = 'Dbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Db'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Db', 'E', 'Ab')

    def test__Ebm__as_expected(self):
        chord_symbol = 'Ebm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Eb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Eb', 'Gb', 'Bb')

    def test__Fbm__as_expected(self):
        chord_symbol = 'Fbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Fb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('E', 'G', 'B')

    def test__Gbm__as_expected(self):
        chord_symbol = 'Gbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Gb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Gb', 'A', 'Db')


class TestMajorSeventhChords:
    def test__AMaj7__as_expected(self):
        chord_symbol = 'AMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'A'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('A', 'C#', 'E', 'G#')

    def test__AM7_alternative_notation__still_as_expected(self):
        chord_symbol = 'AM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'A'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('A', 'C#', 'E', 'G#')

    def test__BMaj7__as_expected(self):
        chord_symbol = 'BMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'B'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('B', 'D#', 'F#', 'A#')

    def test__CMaj7__as_expected(self):
        chord_symbol = 'CMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'C'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('C', 'E', 'G', 'B')

    def test__DMaj7__as_expected(self):
        chord_symbol = 'DMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'D'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('D', 'F#', 'A', 'C#')

    def test__EMaj7__as_expected(self):
        chord_symbol = 'EMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'E'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('E', 'G#', 'B', 'D#')

    def test__FMaj7__as_expected(self):
        chord_symbol = 'FMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'F'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('F', 'A', 'C', 'E')

    def test__GMaj7__as_expected(self):
        chord_symbol = 'GMaj7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'G'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('G', 'B', 'D', 'F#')


class TestMinorSeventhChords:
    def test__Am7__as_expected(self):
        chord_symbol = 'Am7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'A'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('A', 'C', 'E', 'G')

    def test__Bm7__as_expected(self):
        chord_symbol = 'Bm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'B'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('B', 'D', 'F#', 'A')

    def test__Cm7__as_expected(self):
        chord_symbol = 'Cm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'C'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('C', 'D#', 'G', 'A#')

    def test__Dm7__as_expected(self):
        chord_symbol = 'Dm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'D'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('D', 'F', 'A', 'C')

    def test__Em7__as_expected(self):
        chord_symbol = 'Em7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'E'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('E', 'G', 'B', 'D')

    def test__Fm7__as_expected(self):
        chord_symbol = 'Fm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'F'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('F', 'G#', 'C', 'D#')

    def test__Gm7__as_expected(self):
        chord_symbol = 'Gm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'G'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('G', 'A#', 'D', 'F')


# From this point we probs don't need to write out every single as we have enough confidence
class TestFlatMajorSeventhChords:
    """
    Ab major seventh – Ab C Eb G
    Bb major seventh – Bb D F A
    Eb major seventh – Eb G Bb D
    """
    def test__AbM7__as_expected(self):
        chord_symbol = 'AbM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Ab'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('Ab', 'C', 'Eb', 'G')

    def test__BbM7__as_expected(self):
        chord_symbol = 'BbM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Bb'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('Bb', 'D', 'F', 'A')

    def test__EbM7__as_expected(self):
        chord_symbol = 'EbM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Eb'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('Eb', 'G', 'Bb', 'D')


class TestSharpMajorSeventhChords:
    """
    C# major seventh – C# E#(F) G# B#(C)
    F# major seventh – F# A# C# E#(F)
    """
    def test__CSharpM7__as_expected(self):
        chord_symbol = 'C#M7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'C#'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('C#', 'F', 'G#', 'C')

    def test__FSharpM7__as_expected(self):
        chord_symbol = 'F#M7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'F#'
        assert chord.quality == 'major seventh'
        assert chord.semitones == (0, 4, 7, 11)
        assert chord.notes == ('F#', 'A#', 'C#', 'F')


class TestFlatMinorSeventhChords:
    """
    Ab minor seventh – Ab Cb(B) Eb Gb
    Bb minor seventh – Bb Db F Ab
    Eb minor seventh – Eb Gb Bb Db
    """
    def test__AbMinorSeventh__as_expected(self):
        chord_symbol = 'Abm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Ab'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('Ab', 'B', 'Eb', 'Gb')

    def test__BbMinorSeventh__as_expected(self):
        chord_symbol = 'Bbm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Bb'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('Bb', 'Db', 'F', 'Ab')

    def test__EbMinorSeventh__as_expected(self):
        chord_symbol = 'Ebm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Eb'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('Eb', 'Gb', 'Bb', 'Db')


class TestSharpMinorSeventhChords:
    """
    C# minor seventh – C# E G# B
    F# minor seventh – F# A C# E
    """
    def test__CSharpMinorSeventh__as_expected(self):
        chord_symbol = 'C#m7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'C#'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('C#', 'E', 'G#', 'B')

    def test__FSharpMinorSeventh__as_expected(self):
        chord_symbol = 'F#m7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == 'F#'
        assert chord.quality == 'minor seventh'
        assert chord.semitones == (0, 3, 7, 10)
        assert chord.notes == ('F#', 'A', 'C#', 'E')


class TestDominantSeventh:
    """
    A dominant seventh – A C# E G
    B dominant seventh – B D# F# A
    C dominant seventh – C E G Bb
    D dominant seventh – D F# A C
    E dominant seventh – E G# B D
    F dominant seventh – F A C Eb
    G dominant seventh – G B D F
    """
    def test__A7__as_expected(self):
        chord_symbol = 'A7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'A'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('A', 'C#', 'E', 'G')

    def test__B7__as_expected(self):
        chord_symbol = 'B7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'B'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('B', 'D#', 'F#', 'A')

    def test__C7__as_expected(self):
        chord_symbol = 'C7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'C'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('C', 'E', 'G', 'A#')

    def test__D7__as_expected(self):
        chord_symbol = 'D7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'D'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('D', 'F#', 'A', 'C')

    def test__E7__as_expected(self):
        chord_symbol = 'E7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'E'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('E', 'G#', 'B', 'D')

    def test__F7__as_expected(self):
        chord_symbol = 'F7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'F'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('F', 'A', 'C', 'D#')

    def test__G7__as_expected(self):
        chord_symbol = 'G7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'G'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('G', 'B', 'D', 'F')


class TestSharpDominantSeventh:
    """
    C# dominant seventh – C# E#(F) G# B
    F# dominant seventh – F# A# C# E
    """
    def test__CSharpDominantSeventh__as_expected(self):
        chord_symbol = 'C#7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'C#'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('C#', 'F', 'G#', 'B')

    def test__FSharpDominantSeventh__as_expected(self):
        chord_symbol = 'F#7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'F#'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('F#', 'A#', 'C#', 'E')


class TestFlatDominantSeventh:
    """
    Ab dominant seventh – Ab C Eb Gb
    Bb dominant seventh – Bb D F Ab
    Eb dominant seventh – Eb G Bb Db
    """
    def test__AbDominantSeventh__as_expected(self):
        chord_symbol = 'Ab7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Ab'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('Ab', 'C', 'Eb', 'Gb')

    def test__BbDominantSeventh__as_expected(self):
        chord_symbol = 'Bb7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Bb'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('Bb', 'D', 'F', 'Ab')

    def test__EbDominantSeventh__as_expected(self):
        chord_symbol = 'Eb7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Eb'
        assert chord.quality == 'dominant seventh'
        assert chord.semitones == (0, 4, 7, 10)
        assert chord.notes == ('Eb', 'G', 'Bb', 'Db')


class TestDiminuishedChords:
    """
    Adim – A C Eb
    Bdim – B D F
    Cdim – C Eb Gb
    Ddim – D F Ab
    Edim – E G Bb
    Fdim – F Ab Cb
    Gdim – G Bb Db
    """
    def test__Adim__as_expected(self):
        chord_symbol = 'Adim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'A'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('A', 'C', 'Eb')

    def test__Bdim__as_expected(self):
        chord_symbol = 'Bdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'B'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('B', 'D', 'F')

    def test__Cdim__as_expected(self):
        chord_symbol = 'Cdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'C'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('C', 'Eb', 'Gb')

    def test__Ddim__as_expected(self):
        chord_symbol = 'Ddim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'D'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('D', 'F', 'Ab')

    def test__Edim__as_expected(self):
        chord_symbol = 'Edim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'E'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('E', 'G', 'Bb')

    def test__Fdim__as_expected(self):
        chord_symbol = 'Fdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'F'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('F', 'Ab', 'B')

    def test__Gdim__as_expected(self):
        chord_symbol = 'Gdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'G'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('G', 'Bb', 'Db')


class TestSharpDiminuishedChords:
    """
    A#dim – A# C# E
    C#dim – C# E G
    D#dim – D# F# A
    F#dim  – F# A C
    G#dim – G# B D
    """
    def test__Asharpdim__as_expected(self):
        chord_symbol = 'A#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'A#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('A#', 'C#', 'E')

    def test__Bsharpdim__as_expected(self):
        chord_symbol = 'B#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'B#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('C', 'D#', 'F#')

    def test__Csharpdim__as_expected(self):
        chord_symbol = 'C#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'C#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('C#', 'E', 'G')

    def test__Dsharpdim__as_expected(self):
        chord_symbol = 'D#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'D#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('D#', 'F#', 'A')

    def test__Esharpdim__as_expected(self):
        chord_symbol = 'E#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'E#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('F', 'G#', 'B')

    def test__Fsharpdim__as_expected(self):
        chord_symbol = 'F#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'F#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('F#', 'A', 'C')

    def test__Gsharpdim__as_expected(self):
        chord_symbol = 'G#dim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'G#'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('G#', 'B', 'D')


class TestFlatDiminuishedChords:
    """
    Abdim – Ab Cb (B)  Ebb (D)
    Bbdim – Bb Db Fb (E)
    Dbdim – Db Fb Abb (G)
    Ebdim – Eb Gb Bbb
    Gbdim – Gb Bbb (A) Dbb (C)
    """
    def test__Abdim__as_expected(self):
        chord_symbol = 'Abdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Ab'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('Ab', 'B', 'D')

    def test__Bbdim__as_expected(self):
        chord_symbol = 'Bbdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Bb'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('Bb', 'Db', 'E')

    def test__Cbdim__as_expected(self):
        chord_symbol = 'Cbdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Cb'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('B', 'D', 'F')

    def test__Dbdim__as_expected(self):
        chord_symbol = 'Dbdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Db'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('Db', 'E', 'G')

    def test__Ebdim__as_expected(self):
        chord_symbol = 'Ebdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Eb'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('Eb', 'Gb', 'A')

    def test__Fbdim__as_expected(self):
        chord_symbol = 'Fbdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Fb'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('E', 'G', 'Bb')

    def test__Gbdim__as_expected(self):
        chord_symbol = 'Gbdim'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Gb'
        assert chord.quality == 'diminuished'
        assert chord.semitones == (0, 3, 6)
        assert chord.notes == ('Gb', 'A', 'C')


class TestDiminuishedSeventhChords:
    """
    Adim7 – A C Eb Gb
    Bdim7 – B D F Ab
    Cdim7 – C Eb Gb Bbb (A)
    Ddim7 – D F Ab Cb (B)
    Edim7 – E G Bb Db
    Fdim7 – F Ab Cb (B) Ebb (D)
    Gdim7 – G Bb Db Fb (E)
    """
    def test__Adim7__as_expected(self):
        chord_symbol = 'Adim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'A'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('A', 'C', 'Eb', 'Gb')

    def test__Bdim7__as_expected(self):
        chord_symbol = 'Bdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'B'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('B', 'D', 'F', 'Ab')

    def test__Cdim7__as_expected(self):
        chord_symbol = 'Cdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'C'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('C', 'Eb', 'Gb', 'A')

    def test__Ddim7__as_expected(self):
        chord_symbol = 'Ddim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'D'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('D', 'F', 'Ab', 'B')

    def test__Edim7__as_expected(self):
        chord_symbol = 'Edim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'E'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('E', 'G', 'Bb', 'Db')

    def test__Fdim7__as_expected(self):
        chord_symbol = 'Fdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'F'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('F', 'Ab', 'B', 'D')

    def test__Gdim7__as_expected(self):
        chord_symbol = 'Gdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'G'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('G', 'Bb', 'Db', 'E')


class TestSharpDiminuishedSeventhChords:
    """
    A#dim7 – A# C# E G
    C#dim7 – C# E G Bb
    D#dim7 – D# F# A C
    F#dim7  – F# A C Eb
    G#dim7 – G# B D F
    """
    def test__Asharpdim7__as_expected(self):
        chord_symbol = 'A#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'A#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('A#', 'C#', 'E', 'G')

    def test__Bsharpdim7__as_expected(self):
        chord_symbol = 'B#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'B#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('C', 'D#', 'F#', 'A')

    def test__Csharpdim7__as_expected(self):
        chord_symbol = 'C#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'C#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('C#', 'E', 'G', 'A#')

    def test__Dsharpdim7__as_expected(self):
        chord_symbol = 'D#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'D#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('D#', 'F#', 'A', 'C')

    def test__Esharpdim7__as_expected(self):
        chord_symbol = 'E#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'E#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('F', 'G#', 'B', 'D')

    def test__Fsharpdim7__as_expected(self):
        chord_symbol = 'F#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'F#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('F#', 'A', 'C', 'D#')

    def test__Gsharpdim7__as_expected(self):
        chord_symbol = 'G#dim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == 'G#'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('G#', 'B', 'D', 'F')


class TestFlatDiminuishedSeventhChords:
    """
    Abdim7 – Ab Cb (B) Ebb (D) Gbb (F)
    Bbdim7 – Bb Db Fb (E) Abb (G)
    Dbdim7 – Db Fb Abb (G) Cbb (Bb)
    Ebdim7 – Eb Gb Bbb (A) Dbb (C)
    Gbdim7 – Gb Bbb (A) Dbb (C) Fbb (Eb)
    """
    def test__Abdim7__as_expected(self):
        chord_symbol = 'Abdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Ab'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('Ab', 'B', 'D', 'F')

    def test__Bbdim7__as_expected(self):
        chord_symbol = 'Bbdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Bb'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('Bb', 'Db', 'E', 'G')

    def test__Cbdim7__as_expected(self):
        chord_symbol = 'Cbdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Cb'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('B', 'D', 'F', 'Ab')

    def test__Dbdim7__as_expected(self):
        chord_symbol = 'Dbdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Db'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('Db', 'E', 'G', 'Bb')

    def test__Ebdim7__as_expected(self):
        chord_symbol = 'Ebdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Eb'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('Eb', 'Gb', 'A', 'C')

    def test__Fbdim7__as_expected(self):
        chord_symbol = 'Fbdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Fb'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('E', 'G', 'Bb', 'Db')

    def test__Gbdim7__as_expected(self):
        chord_symbol = 'Gbdim7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == 'Gb'
        assert chord.quality == 'diminuished seventh'
        assert chord.semitones == (0, 3, 6, 9)
        assert chord.notes == ('Gb', 'A', 'C', 'Eb')


class TestScales:
    def test__force_note_sequence_flat__flat_root__return_True(self):
        chord = Chord('Eb')

        assert chord.force_note_sequence_flat is True

    def test__force_note_sequence_flat__normal_root__return_False(self):
        chord = Chord('E')

        assert chord.force_note_sequence_flat is False

    def test__force_note_sequence_flat__sharp_root__return_False(self):
        chord = Chord('E#')

        assert chord.force_note_sequence_flat is False

    def test__generate_note_sequence__starting_C__returns_expected(self):
        generator = generate_note_sequence(starting_note='C', force_notes_flat=False)
        first_4_notes = [x for x in itertools.islice(generator, 4)]
        assert first_4_notes == ['C', 'C#', 'D', 'D#']

    def test__generate_note_sequence__with_flat_notes__returns_expected(self):
        generator = generate_note_sequence(starting_note='Db', force_notes_flat=True)
        first_4_notes = [x for x in itertools.islice(generator, 4)]
        assert first_4_notes == ['Db', 'D', 'Eb', 'E']
