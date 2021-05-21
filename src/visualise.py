"""
each note is 3sp and 3 rows
-O- with an empty line above & below is a note which crosses a line

---
 O  is a note between two lines
---
"""
import abc
from typing import Iterable


class Note:
    """
    C4 is middle C; C1 is the lowest C
    """
    valid_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    def __init__(self, letter: str, index: int):
        letter = letter.upper()
        if letter not in self.valid_letters:
            raise ValueError(f'invalid note:{letter}')
        if index > 8:
            raise ValueError(f'invalid index:{index}')
        self.letter = letter
        self.index = index

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.numeric_value == other.numeric_value
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Note({self.letter}{self.index})'

    def __add__(self, other):
        if not isinstance(other, Note):
            raise TypeError(f'two Notes may be added together, '
                             f'but you tried to add a Note with a {type(other)}')
        return self.numeric_value + other.numeric_value

    def __sub__(self, other):
        if not isinstance(other, Note):
            raise TypeError(f'two Notes may be subtracted from one another, '
                             f'but you tried to subtract a {type(other)} from a Note')
        return self.numeric_value - other.numeric_value

    @property
    def numeric_value(self):
        """
        with A1 as 0, what number is this note on the scale?
        Just counting whole notes; flats and sharps are excluded
        In other words, counting the white keys of a piano starting from 0
        """
        values_within_set = dict(zip(self.valid_letters, range(7)))
        value_of_corresponding_a = (self.index * 7) - 7
        value_of_note_within_set = values_within_set[self.letter]
        return value_of_corresponding_a + value_of_note_within_set


class Staff(abc.ABC):
    _row_indices = None

    def __init__(self, note: Note = None):
        self.note = note

    @property
    @abc.abstractmethod
    def clef_symbol(self) -> list:
        """here we expect something resembling ascii art for the start of the row"""
        pass

    # def __repr__(self):
    #     return self.display_as

    @property
    @abc.abstractmethod
    def valid_notes(self) -> Iterable[Note]:
        """
        I've been pretty hacky so far in omitting to visualise notes above or below the staff
        so... middle C can't be represented (yet)
        For the time being, let's just limit what notes the quiz can generate
        """
        pass

    @property
    @abc.abstractmethod
    def base_note(self) -> Note:
        """
        what's the anchor note for this staff?
        i.e. the note that takes the position of `base_index`
        """
        pass

    @property
    @abc.abstractmethod
    def base_rowindex(self) -> int:
        """
        what's the row upon which the `base_note` appears
        the bottom line of the staff is 0, top line is 8
        notes can be <0 and >8

        e.g. the row indices look like this on a staff:
        --- 8
            7
        --- 6
            5
        --- 4
            3
        --- 2
            1
        --- 0
        """
        pass

    @property
    def row_indices(self):
        """:return: {row_index: numeric_value of the note that occupies it}"""
        if self._row_indices is None:
            self._row_indices = {}
            for row_index in range(9):
                self._row_indices[row_index] = self.base_note.numeric_value \
                                               - self.base_rowindex + row_index
        return self._row_indices

    def generate_staff(self) -> list:
        """returns a list of rows starting from the top"""
        rows = []
        for row_num in range(0, 9):
            rows.append(self._get_staff_row(row_num, self.note))
        # reverse rows so that we can append them from top to bottom
        rows.reverse()
        return rows

    def _get_staff_row(self, row_num: int, note: Note) -> str:
        line_char = self._get_row_char(row_num)
        if note is None:
            return line_char * 7
        if self._does_this_row_need_a_note(row_num, self.note):
            return line_char * 3 + 'O' + line_char * 3
        return line_char * 7

    def _get_row_char(self, row_num: int) -> str:
        """decide whether it's a - row or a space row"""
        # rownum 0 is the bottom row of the staff
        if row_num % 2 == 0:
            line_char = '-'
        else:
            line_char = ' '
            # rows.append(line_char + 'O' + line_char)
        return line_char

    def _does_this_row_need_a_note(self, row_num: int, note: Note) -> bool:
        return self.row_indices[row_num] == note.numeric_value

    @property
    def display_as(self):
        return '\n'.join([row for row in self.generate_staff()])


class TrebleStaff(Staff):
    @property
    def clef_symbol(self):
        return [
            r"---|\----|--",
            r"   ||    |  ",
            r"---|/----|--",
            r"   |     |  ",
            r"--/|-----|--",
            r" /  _    |  ",
            r"||-/-\\--|--",
            r"||   //  |  ",
            r"-\\=//---|--"
        ]

    @property
    def base_note(self):
        return Note('G', 4)  # crosses line 2 of 5 from the bottom

    @property
    def base_rowindex(self):
        return 2

    @property
    def valid_notes(self):
        notes = [('E', 4), ('F', 4), ('G', 4), ('A', 5), ('B', 5), ('C', 5),
                 ('D', 5), ('E', 5), ('F', 5)]
        return [Note(*n) for n in notes]


class BassStaff(Staff):
    @property
    def clef_symbol(self):
        return [
            r"---------|--",
            r" //  \\ .|  ",
            r"-\\--||--|--",
            r"     || .|  ",
            r"-----//--|--",
            r"    //   |  ",
            r"----/----|--",
            r"   /     |  ",
            r"---------|--"
        ]

    @property
    def base_note(self):
        return Note('F', 3)  # crosses line 2 of 5 from the bottom

    @property
    def base_rowindex(self):
        return 6

    @property
    def valid_notes(self):
        notes = [('G', 2), ('A', 3), ('B', 3), ('C', 3), ('D', 3), ('E', 3),
                 ('F', 3), ('G', 3), ('A', 4)]
        return [Note(*n) for n in notes]


def visualise_notes_on_a_treble_staff(notes: Iterable[Note]):
    staffs = [TrebleStaff(n) for n in notes]
    return _visualise_several_staffs(staffs)


def visualise_notes_on_a_bass_staff(notes: Iterable[Note]):
    staffs = [BassStaff(n) for n in notes]
    return _visualise_several_staffs(staffs)


def _visualise_several_staffs(staffs: Iterable[Staff]):
    """
    compose the entire line from your staffs.
    Assumes all are the same e.g. a collection of TrebleStaffs or a collection of BassStaffs
    If you pass a combination then it will just be wrong.
    """
    rows_to_return = ['', '', '', '', '', '', '', '', '']
    # first get a list of lists, each of which is 9 rows long
    items_to_display = [staffs[0].clef_symbol] + [s.generate_staff() for s in staffs]
    # here we break convention because row_num 0 is the top
    for row_num in range(9):
        for item in items_to_display:
            rows_to_return[row_num] = rows_to_return[row_num] + item[row_num]
    return '\n'.join(rows_to_return)


def visualise_notes(notes: Iterable[Note], empty_staff: Iterable[Staff]):
    if isinstance(empty_staff, TrebleStaff):
        print(visualise_notes_on_a_treble_staff(notes))
    else:
        print(visualise_notes_on_a_bass_staff(notes))
