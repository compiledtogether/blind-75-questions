# https://leetcode.com/discuss/post/7020178/paypal-karat-interview-by-anonymous_user-a5nb/
from typing import List
def singable(song: List[str], lowNote: str, highNote: str) -> bool:
    pitches = {'C':1, 'D':2, 'E':3, 'F':4, 'G':5, 'A':6, 'B':7}

    def note_value(note: str) -> int:
        pitch, octave = note[0], int(note[1])
        return octave * 7 + pitches[pitch]
    
    low = note_value(lowNote)
    high = note_value(highNote)

    for note in song:
        val = note_value(note)

        if not (low <= val <= high):
            return False

    return True

# Test Case:

# Test Case 1
song = ["F4", "B4", "C5"]
lowNote = "F4"
highNote = "C5"
output = True
print(singable(song, lowNote, highNote) == output)

# Test Case 2
song = ["F4", "B4", "C5"]
lowNote = "A4"
highNote = "C5"
output = False
print(singable(song, lowNote, highNote) == output)

# Test Case 3
song = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
lowNote = "B2"
highNote = "C5"
output = True
print(singable(song, lowNote, highNote) == output)

# Test Case 4
song = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
lowNote = "C3"
highNote = "B4"
output = False
print(singable(song, lowNote, highNote) == output)

# Test Case 5
song = ["B4", "F5", "B5"]
lowNote = "B4"
highNote = "B5"
output = True
print(singable(song, lowNote, highNote) == output)

# Test Case 6
song = ["B4", "F5", "B5"]
lowNote = "B4"
highNote = "C5"
output = False
print(singable(song, lowNote, highNote) == output)

# Test Case 7
song = ["B4", "E4", "G4", "G4", "A4", "B4", "E4",
        "B4", "E4", "G4", "G4", "A4", "C5", "B4",
        "E5", "G4", "G4", "A4", "B4", "C5", "D5",
        "C5", "B4", "C5", "E5", "D5", "C5", "C5",
        "B4", "B4", "E5", "E4", "G4", "G4", "A4",
        "B4", "B4", "B4", "C5", "E5", "A5", "E5",
        "C5", "A4", "E5", "D5", "C5", "B4"]
lowNote = "D4"
highNote = "A5"
output = True
print(singable(song, lowNote, highNote) == output)

# Test Case 8
song = ["B4", "E4", "G4", "G4", "A4", "B4", "E4",
        "B4", "E4", "G4", "G4", "A4", "C5", "B4",
        "E5", "G4", "G4", "A4", "B4", "C5", "D5",
        "C5", "B4", "C5", "E5", "D5", "C5", "C5",
        "B4", "B4", "E5", "E4", "G4", "G4", "A4",
        "B4", "B4", "B4", "C5", "E5", "A5", "E5",
        "C5", "A4", "E5", "D5", "C5", "B4"]
lowNote = "D4"
highNote = "G5"
output = False
print(singable(song, lowNote, highNote) == output)

# Test Case 9
song = ["B4", "E4", "G4", "G4", "A4", "B4", "E4",
        "B4", "E4", "G4", "G4", "A4", "C5", "B4",
        "E5", "G4", "G4", "A4", "B4", "C5", "D5",
        "C5", "B4", "C5", "E5", "D5", "C5", "C5",
        "B4", "B4", "E5", "E4", "G4", "G4", "A4",
        "B4", "B4", "B4", "C5", "E5", "A5", "E5",
        "C5", "A4", "E5", "D5", "C5", "B4"]
lowNote = "D4"
highNote = "C6"
output = True
print(singable(song, lowNote, highNote) == output)

# Test Case 10
song = ["B4", "E4", "G4", "G4", "A4", "B4", "E4",
        "B4", "E4", "G4", "G4", "A4", "C5", "B4",
        "E5", "G4", "G4", "A4", "B4", "C5", "D5",
        "C5", "B4", "C5", "E5", "D5", "C5", "C5",
        "B4", "B4", "E5", "E4", "G4", "G4", "A4",
        "B4", "B4", "B4", "C5", "E5", "A5", "E5",
        "C5", "A4", "E5", "D5", "C5", "B4"]
lowNote = "F4"
highNote = "C6"
output = False
print(singable(song, lowNote, highNote) == output)

# Test Case 11
song = ["F4"]
lowNote = "D4"
highNote = "E4"
output = False
print(singable(song, lowNote, highNote) == output)
