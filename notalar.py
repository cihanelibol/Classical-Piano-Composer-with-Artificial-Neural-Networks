
import glob
import pickle
import numpy
from music21 import converter, instrument, note, chord

def get_notes():
   
    notes = []

    for file in glob.glob("midiler/*.mid"):
        midi = converter.parse(file)

        print("ayristir %s" % file)


        try: 
            s2 = instrument.partitionByInstrument(midi)
            notes_to_parse = s2.parts[0].recurse() 
        except: 
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    with open('veri/notes', 'wb') as filepath:
        pickle.dump(notes, filepath)
     
        return notes

get_notes()
a = get_notes()
print(numpy.shape(a))
print(get_notes())



   









