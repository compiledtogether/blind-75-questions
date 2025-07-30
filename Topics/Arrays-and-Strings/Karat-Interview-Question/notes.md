# Karat Interview Question

## Problem:
```yaml
A new singer is looking for songs to perform. To be able to perform a song all the notes in the song must be within the singer's range, which is given by the lowest and highest notes the singer is able to sing.

A note is represented by:

A letter for its pitch, ordered (lowest) C D E F G A B (highest)
A number for its octave, ordered (lowest) 0 1 2 3 4 5 6 7 (highest)
For example, C5 is a note with pitch C and octave 5.

A note with a larger octave number is always higher than a note with a smaller octave number. If the octave number is the same, then a note with a later pitch letter is higher.

For example, here are some notes in order from lower to higher:
... G3 A3 B3 C4 D4 E4 F4 G4 A4 B4 C5 D5 …

A3 is higher than G3 because A comes after G in the ordering above
C4 is higher than B3 because its octave number is larger

The lowest possible note is C0 and the highest possible note is B7.

You will be given as input a list of notes in a song, the lowest note the singer can sing, and the highest note the singer can sing. Write a function that returns whether the singer can sing the song.

Examples:
song1 = ["F4", "B4", "C5"] #List[string]
singable(song1, "F4", "C5") => True #range representing the lowest and highest note they can sing
Every note in the song is between F4 and C5, so the singer can sing this song.
Note that B4 is higher than F4, since notes are ordered C D E F G A B

singable(song1, "A4", "C5") => False
F4 is lower than A4, so the singer cannot sing this song

song2 = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
singable(song2, "B2", "C5") => True
singable(song2, "C3", "B4") => False
B2 is lower than C3. A note with a smaller octave number is always lower than a note with a larger octave number. Similarly, B4 is lower than C5

Additional input data:
song3 = [ "B4", "F5", "B5" ]

song4 = ["B4", "E4", "G4", "G4", "A4", "B4", "E4",
"B4", "E4", "G4", "G4", "A4", "C5", "B4",
"E5", "G4", "G4", "A4", "B4", "C5", "D5",
"C5", "B4", "C5", "E5", "D5", "C5", "C5",
"B4", "B4", "E5", "E4", "G4", "G4", "A4",
"B4", "B4", "B4", "C5", "E5", "A5", "E5",
"C5", "A4", "E5", "D5", "C5", "B4"]

song5 = [ "F4" ]

All test cases:
singable(song1, "F4", "C5") => True
singable(song1, "A4", "C5") => False
singable(song2, "B2", "C5") => True
singable(song2, "C3", "B4") => False
singable(song3, "B4", "B5") => True
singable(song3, "B4", "C5") => False
singable(song4, "D4", "A5") => True
singable(song4, "D4", "G5") => False
singable(song4, "D4", "C6") => True
singable(song4, "F4", "C6") => False
singable(song5, "D4", "E4") => False

Complexity Variables:
N = length of the song

song1 = ["F4", "B4", "C5"]
song2 = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
song3 = [ "B4", "F5", "B5" ]
song4 = ["B4", "E4", "G4", "G4", "A4", "B4", "E4",
"B4", "E4", "G4", "G4", "A4", "C5", "B4",
"E5", "G4", "G4", "A4", "B4", "C5", "D5",
"C5", "B4", "C5", "E5", "D5", "C5", "C5",
"B4", "B4", "E5", "E4", "G4", "G4", "A4",
"B4", "B4", "B4", "C5", "E5", "A5", "E5",
"C5", "A4", "E5", "D5", "C5", "B4"]
song5 = ["F4"]
```

---

## Topic:

- Array
- Strings

---

## Explanation

1. Create a dict of pitches
2. Create a helper function for convert note to a value, in which extract pitch and octave (int form) 
3. return a value using `octave * 7 + pitches[pitch]`
4. Iterate the song, for each convert it into corresponding value
5. Check if the note value is greater than low note value and smaller than high note value
6. If yes, continue, else return false
7. Finally, return True

---

# Test Cases:

# Test Case 1
song = ["F4", "B4", "C5"]
lowNote = "F4"
highNote = "C5"
output = True

# Test Case 2
song = ["F4", "B4", "C5"]
lowNote = "A4"
highNote = "C5"
output = False

# Test Case 3
song = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
lowNote = "B2"
highNote = "C5"
output = True

# Test Case 4
song = ["C3", "E3", "G3", "C4", "E4", "G4", "C5"]
lowNote = "C3"
highNote = "B4"
output = False

# Test Case 5
song = ["B4", "F5", "B5"]
lowNote = "B4"
highNote = "B5"
output = True

# Test Case 6
song = ["B4", "F5", "B5"]
lowNote = "B4"
highNote = "C5"
output = False

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

# Test Case 11
song = ["F4"]
lowNote = "D4"
highNote = "E4"
output = False

---

# Time and Space Complexity:

| Complexity | Value        |
|------------|--------------|
| Time       | O(N) |
| Space      | O(1) |