import itertools

from pytest import raises

from src.chords import Chord, generate_note_sequence


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
    def test__Aflat__as_expected(self):
        chord_symbol = 'Ab'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Ab', 'C', 'Eb')

    def test__Bflat__as_expected(self):
        chord_symbol = 'Bb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Bb', 'D', 'F')

    def test__Cflat__as_expected(self):
        chord_symbol = 'Cb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('B', 'Eb', 'Gb')

    def test__Dflat__as_expected(self):
        chord_symbol = 'Db'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Db', 'F', 'Ab')

    def test__Eflat__as_expected(self):
        chord_symbol = 'Eb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('Eb', 'G', 'Bb')

    def test__Fflat__as_expected(self):
        chord_symbol = 'Fb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'
        assert chord.semitones == (0, 4, 7)
        assert chord.notes == ('E', 'Ab', 'B')

    def test__Gflat__as_expected(self):
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
    def test__Aflatm__as_expected(self):
        chord_symbol = 'Abm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Ab'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Ab', 'B', 'Eb')

    def test__Bflatm__as_expected(self):
        chord_symbol = 'Bbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Bb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Bb', 'Db', 'F')

    def test__Cflatm__as_expected(self):
        chord_symbol = 'Cbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Cb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('B', 'D', 'Gb')

    def test__Dflatm__as_expected(self):
        chord_symbol = 'Dbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Db'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Db', 'E', 'Ab')

    def test__Eflatm__as_expected(self):
        chord_symbol = 'Ebm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Eb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('Eb', 'Gb', 'Bb')

    def test__Fflatm__as_expected(self):
        chord_symbol = 'Fbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == 'Fb'
        assert chord.quality == 'minor'
        assert chord.semitones == (0, 3, 7)
        assert chord.notes == ('E', 'G', 'B')

    def test__Gflatm__as_expected(self):
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
    def test__A7__as_expected(self):
        chord_symbol = 'AM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'A'
        assert chord.quality == 'major seventh'

    def test__B7__as_expected(self):
        chord_symbol = 'BM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'B'
        assert chord.quality == 'major seventh'

    def test__C7__as_expected(self):
        chord_symbol = 'CM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'C'
        assert chord.quality == 'major seventh'

    def test__D7__as_expected(self):
        chord_symbol = 'DM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'D'
        assert chord.quality == 'major seventh'

    def test__E7__as_expected(self):
        chord_symbol = 'EM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'E'
        assert chord.quality == 'major seventh'

    def test__F7__as_expected(self):
        chord_symbol = 'FM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'F'
        assert chord.quality == 'major seventh'

    def test__G7__as_expected(self):
        chord_symbol = 'GM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == 'G'
        assert chord.quality == 'major seventh'


class TestMinorSeventhChords:
    def test__Am7__as_expected(self):
        chord_symbol = 'Am7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'A'
        assert chord.quality == 'minor seventh'

    def test__Bm7__as_expected(self):
        chord_symbol = 'Bm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'B'
        assert chord.quality == 'minor seventh'

    def test__Cm7__as_expected(self):
        chord_symbol = 'Cm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'C'
        assert chord.quality == 'minor seventh'

    def test__Dm7__as_expected(self):
        chord_symbol = 'Dm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'D'
        assert chord.quality == 'minor seventh'

    def test__Em7__as_expected(self):
        chord_symbol = 'Em7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'E'
        assert chord.quality == 'minor seventh'

    def test__Fm7__as_expected(self):
        chord_symbol = 'Fm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'F'
        assert chord.quality == 'minor seventh'

    def test__Gm7__as_expected(self):
        chord_symbol = 'Gm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == 'G'
        assert chord.quality == 'minor seventh'


class TestScales:
    def test__force_note_sequence_flat__flat_root__return_True(self):
        chord = Chord('Eb')

        assert chord.force_note_sequence_flat == True

    def test__force_note_sequence_flat__normal_root__return_False(self):
        chord = Chord('E')

        assert chord.force_note_sequence_flat == False

    def test__force_note_sequence_flat__sharp_root__return_False(self):
        chord = Chord('E#')

        assert chord.force_note_sequence_flat == False

    def test__generate_note_sequence__starting_C__returns_expected(self):
        generator = generate_note_sequence(starting_note='C', force_notes_flat=False)
        first_4_notes = [x for x in itertools.islice(generator, 4)]
        assert first_4_notes == ['C', 'C#', 'D', 'D#']

    def test__generate_note_sequence__with_flat_notes__returns_expected(self):
        generator = generate_note_sequence(starting_note='Db', force_notes_flat=True)
        first_4_notes = [x for x in itertools.islice(generator, 4)]
        assert first_4_notes == ['Db', 'D', 'Eb', 'E']
