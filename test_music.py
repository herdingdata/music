import music as m
import pytest


# Note
def test_Note__init__invalid_letter__raises_ValueError():
    # Arrange
    invalid_letter = 'H'

    # Act/ Assert
    with pytest.raises(ValueError):
        note = m.Note(invalid_letter, 1)


def test_Note__init__invalid_index__raises_ValueError():
    # Arrange
    invalid_index = 9

    # Act/ Assert
    with pytest.raises(ValueError):
        note = m.Note('A', invalid_index)


def test_Note__numeric_value__a1__equals_0():
    note = m.Note('A', 1)
    result_val = note.numeric_value
    assert result_val == 0


def test_Note__numeric_value__a2__equals_7():
    note = m.Note('A', 2)
    result_val = note.numeric_value
    assert result_val == 7


def test_Note__numeric_value__f2__equals_12():
    note = m.Note('F', 2)
    result_val = note.numeric_value
    assert result_val == 12

def test_Note__subtraction__a1_from_a2__returns_7():
    note_1 = m.Note('A', 1)
    note_2 = m.Note('A', 2)

    result = note_2 - note_1

    assert result == 7

def test_Note__addition__a1_plus_a2__returns_7():
    note_1 = m.Note('A', 1)
    note_2 = m.Note('A', 2)

    result = note_2 + note_1

    assert result == 7

def test_Note__addition__a1_plus_something_invalid__raises_ValueError():
    note_1 = m.Note('A', 1)
    note_2 = 'not a note'

    with pytest.raises(TypeError):
        note_1 + note_2


def test_Note__addition__a1_subtract_something_invalid__raises_ValueError():
    note_1 = 'not a note'
    note_2 = m.Note('A', 2)

    with pytest.raises(TypeError):
        note_2 - note_1

# Staff
def test_TrebleStaff__row_indices__return_expected():
    # Arrange
    expected_row_indices = {
        0: 25,
        1: 26,
        2: 27,
        3: 28,
        4: 29,
        5: 30,
        6: 31,
        7: 32,
        8: 33
    }
    note = m.Note('C', 1)  # doesn't matter here
    staff = m.TrebleStaff(note)

    # Act
    result_row_indices = staff.row_indices

    # Assert
    assert result_row_indices == expected_row_indices


def test_TrebleStaff__init__C5__returns_expected():
    # Arrange
    letter = 'C'
    index = 5
    expected_note = \
        "---\n" \
        "   \n" \
        "---\n" \
        " O \n" \
        "---\n" \
        "   \n" \
        "---\n" \
        "   \n" \
        "---"
    note = m.Note(letter, index)

    # Act
    staff = m.TrebleStaff(note)

    # Assert
    assert staff.display_as == expected_note


def test_TrebleStaff__init__E5__returns_expected():
    # Arrange
    letter = 'E'
    index = 5
    expected_note = \
        "---\n" \
        " O \n" \
        "---\n" \
        "   \n" \
        "---\n" \
        "   \n" \
        "---\n" \
        "   \n" \
        "---"
    note = m.Note(letter, index)

    # Act
    staff = m.TrebleStaff(note)

    # Assert
    assert staff.display_as == expected_note


def test_TrebleStaff__init__G4__returns_expected():
    # Arrange
    letter = 'G'
    index = 4
    expected_note = \
        "---\n" \
        "   \n" \
        "---\n" \
        "   \n" \
        "---\n" \
        "   \n" \
        "-O-\n" \
        "   \n" \
        "---"
    note = m.Note(letter, index)

    # Act
    staff = m.TrebleStaff(note)

    # Assert
    assert staff.display_as == expected_note
#
# def test_TrebleStaff_generate_staff__no_notes__returns_empty():
#     # Arrange
#     expected_staff = \
#         "---\n" \
#         "   \n" \
#         "---\n" \
#         "   \n" \
#         "---\n" \
#         "   \n" \
#         "---\n" \
#         "   \n" \
#         "---"
#     staff = m.TrebleStaff(None)
#
#     # Act
#     staff_repr = staff.generate_staff()
#
#     # Assert
#     assert staff_repr == expected_staff

