"""
each note is 3sp and 3 rows
-O- with an empty line above & below is a note which crosses a line

---
 O  is a note between two lines
---
"""
import abc


class Note:
    """
    C4 is middle C; C1 is the lowest C
    """
    def __init__(self, letter: str, index: int):
        if letter not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            raise ValueError(f'invalid note:{letter}')
        if index > 8:
            raise ValueError(f'invalid index:{index}')
        self.letter = letter
        self.index = index

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.letter == other.letter and self.index == other.index
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Note({self.letter}{self.index})'


class Staff(abc.ABC):
    def __init__(self, note: Note=None):
        self.note = note

    # def __repr__(self):
    #     return self.display_as

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
    def base_index(self) -> int:
        """
        what's the row upon which the `base_note` appears
        the bottom line of the staff is 0, top line is 8
        notes can be <0 and >8
        """
        pass

    def generate_staff(self) -> str:
        rows = []
        for row_num in range(0, 9):
            rows.append(self._get_staff_row(row_num, self.note))
        # reverse rows so that we can append them from top to bottom
        rows.reverse()
        return '\n'.join(rows)

    def _get_staff_row(self, row_num: int, note: Note) -> str:
        line_char = self._get_row_char(row_num)
        if note is None:
            return line_char * 3
        if self._does_this_row_need_a_note(row_num, self.note):
            return line_char + 'O' + line_char
        return line_char * 3

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
        # if row_num == 5:
        #     print('hi')
        if row_num == self.base_index and note == self.base_note:
            return True
        if row_num

    @property
    def display_as(self):
        return self.generate_staff()


class TrebleStaff(Staff):
    @property
    def base_note(self):
        return Note('C', 5)

    @property
    def base_index(self):
        return 5
