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
