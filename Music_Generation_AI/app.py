from music21 import stream, note
import random

s = stream.Stream()

for i in range(20):
    pitch = random.choice([
        "C4",
        "D4",
        "E4",
        "F4",
        "G4",
        "A4",
        "B4"
    ])

    n = note.Note(pitch)
    n.quarterLength = 1
    s.append(n)

s.write('midi', fp='generated_music.mid')

print("Music generated successfully!")