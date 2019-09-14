from pytest import raises
from src.chords import Chord


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

    def test__B__as_expected(self):
        chord_symbol = 'B'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__C__as_expected(self):
        chord_symbol = 'C'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__D__as_expected(self):
        chord_symbol = 'D'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__E__as_expected(self):
        chord_symbol = 'E'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__F__as_expected(self):
        chord_symbol = 'F'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'


class TestMinorChords:
    def test__Am__as_expected(self):
        chord_symbol = 'Am'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Bm__as_expected(self):
        chord_symbol = 'Bm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Cm__as_expected(self):
        chord_symbol = 'Cm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Dm__as_expected(self):
        chord_symbol = 'Dm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Em__as_expected(self):
        chord_symbol = 'Em'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Fm__as_expected(self):
        chord_symbol = 'Fm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'


class TestMajorSharpChords:
    def test__Asharp__as_expected(self):
        chord_symbol = 'A#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Bsharp__as_expected(self):
        chord_symbol = 'B#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Csharp__as_expected(self):
        chord_symbol = 'C#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Dsharp__as_expected(self):
        chord_symbol = 'D#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Esharp__as_expected(self):
        chord_symbol = 'E#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Fsharp__as_expected(self):
        chord_symbol = 'F#'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'


class TestMinorSharpChords:
    def test__Asharpm__as_expected(self):
        chord_symbol = 'A#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Bsharpm__as_expected(self):
        chord_symbol = 'B#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Csharpm__as_expected(self):
        chord_symbol = 'C#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Dsharpm__as_expected(self):
        chord_symbol = 'D#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Esharpm__as_expected(self):
        chord_symbol = 'E#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Fsharpm__as_expected(self):
        chord_symbol = 'F#m'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == '#'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'


class TestMajorFlatChords:
    def test__Aflat__as_expected(self):
        chord_symbol = 'Ab'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Bflat__as_expected(self):
        chord_symbol = 'Bb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Cflat__as_expected(self):
        chord_symbol = 'Cb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Dflat__as_expected(self):
        chord_symbol = 'Db'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Eflat__as_expected(self):
        chord_symbol = 'Eb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'

    def test__Fflat__as_expected(self):
        chord_symbol = 'Fb'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major'


class TestMinorFlatChords:
    def test__Aflatm__as_expected(self):
        chord_symbol = 'Abm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Bflatm__as_expected(self):
        chord_symbol = 'Bbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Cflatm__as_expected(self):
        chord_symbol = 'Cbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Dflatm__as_expected(self):
        chord_symbol = 'Dbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Eflatm__as_expected(self):
        chord_symbol = 'Ebm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'

    def test__Fflatm__as_expected(self):
        chord_symbol = 'Fbm'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == 'b'
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor'


class TestMajorSeventhChords:
    def test__A7__as_expected(self):
        chord_symbol = 'AM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major seventh'

    def test__B7__as_expected(self):
        chord_symbol = 'BM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major seventh'

    def test__C7__as_expected(self):
        chord_symbol = 'CM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major seventh'

    def test__D7__as_expected(self):
        chord_symbol = 'DM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major seventh'

    def test__E7__as_expected(self):
        chord_symbol = 'EM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major seventh'

    def test__F7__as_expected(self):
        chord_symbol = 'FM7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == ''
        assert chord.root == chord_symbol
        assert chord.quality == 'major seventh'


class TestMinorSeventhChords:
    def test__Am7__as_expected(self):
        chord_symbol = 'Am7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor seventh'

    def test__Bm7__as_expected(self):
        chord_symbol = 'Bm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor seventh'

    def test__Cm7__as_expected(self):
        chord_symbol = 'Cm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor seventh'

    def test__Dm7__as_expected(self):
        chord_symbol = 'Dm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor seventh'

    def test__Em7__as_expected(self):
        chord_symbol = 'Em7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor seventh'

    def test__Fm7__as_expected(self):
        chord_symbol = 'Fm7'
        chord = Chord(chord_symbol)

        assert chord.__repr__() == chord_symbol
        assert chord.accidental == ''
        assert chord.modifier == 'm'
        assert chord.root == chord_symbol
        assert chord.quality == 'minor seventh'
