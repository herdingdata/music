seconds_to_guess = 20
seconds_with_hint = 10
play_some_notes_number_notes = 4

# notes to include
include_sharps = True
include_flats = True

# chords to include
include_minors = False
include_major_7th = False
include_minor_7th = False
include_dominant_7th = False
include_diminuished = False
include_diminuished_7th = False


# --------------- workings only below here, no need to tweak these manually ------------
# now turn those include options into possible lists
possible_accidentals = ['']  # no accidental
if include_sharps:
    possible_accidentals.append('#')  # sharp
if include_flats:
    possible_accidentals.append('b')  # flat

possible_modifiers = ['']  # major
if include_minors:
    possible_modifiers.append('m')  # minor
if include_major_7th:
    possible_modifiers.append('Maj7')  # major seventh  (M7 also works, but is less explicit)
if include_minor_7th:
    possible_modifiers.append('m7')  # minor seventh
if include_dominant_7th:
    possible_modifiers.append('7')  # dominant seventh
if include_diminuished:
    possible_modifiers.append('dim')  # diminuished
if include_diminuished_7th:
    possible_modifiers.append('dim7')  # diminuished seventh
