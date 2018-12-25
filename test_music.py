import music as m
import pytest


# Note
def test_Note__init__invalid_letter__raises_ValueError():
    # Arrange
    invalid_letter = "H"

    # Act/ Assert
    with pytest.raises(ValueError):
        note = m.Note(invalid_letter, 1)


def test_Note__init__invalid_index__raises_ValueError():
    # Arrange
    invalid_index = 9

    # Act/ Assert
    with pytest.raises(ValueError):
        note = m.Note("A", invalid_index)


# Staff
def test_TrebleStaff__init__C5__returns_expected():
    # Arrange
    letter = "C"
    index = 5
    expected_note = (
        "---\n" "   \n" "---\n" " O \n" "---\n" "   \n" "---\n" "   \n" "---"
    )
    note = m.Note(letter, index)

    # Act
    staff = m.TrebleStaff(note)

    # Assert
    assert staff.display_as == expected_note


def test_TrebleStaff__init__E5__returns_expected():
    # Arrange
    letter = "C"
    index = 5
    expected_note = (
        "---\n" " O \n" "---\n" "   \n" "---\n" "   \n" "---\n" "   \n" "---"
    )
    note = m.Note(letter, index)

    # Act
    staff = m.TrebleStaff(note)

    # Assert
    assert staff.display_as == expected_note


def test_TrebleStaff_generate_staff__no_notes__returns_empty():
    # Arrange
    expected_staff = (
        "---\n" "   \n" "---\n" "   \n" "---\n" "   \n" "---\n" "   \n" "---"
    )
    staff = m.TrebleStaff(None)

    # Act
    staff_repr = staff.generate_staff()

    # Assert
    assert staff_repr == expected_staff
