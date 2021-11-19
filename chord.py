from mido import Message, MidiFile, MidiTrack
import music

# major 3 chord uses three tracks to play
def normal_chord():
    mid = MidiFile()
    track1 = MidiTrack()
    mid.tracks.append(track1)
    track2 = MidiTrack()
    mid.tracks.append(track2)
    track3 = MidiTrack()
    mid.tracks.append(track3)
    bpm = 75
    program = 1
    track = MidiTrack()
    mid.tracks.append(track)
    music.play_note(note=1, length=4, track=track, bpm=bpm, program=program, octachord=-1)
    music.play_chord(1, track, track1, track2, track3, bpm, program=program)
    music.play_chord(1, track, track1, track2, track3, bpm, program=program)
    music.play_chord(1, track, track1, track2, track3, bpm, program=program)
    music.play_chord(1, track, track1, track2, track3, bpm, program=program)
    
    music.play_note(note=6, length=4, track=track, bpm=bpm, program=program, octachord=-2)
    music.play_chord(6, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(6, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(6, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(6, track, track1, track2, track3, bpm, program=program, octachord=-1)
   
    music.play_note(note=4, length=4, track=track, bpm=bpm, program=program, octachord=-2)
    music.play_chord(4, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(4, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(4, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(4, track, track1, track2, track3, bpm, program=program, octachord=-1)
    
    music.play_note(note=5, length=4, track=track, bpm=bpm, program=program, octachord=-2)
    music.play_chord(5, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(5, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(5, track, track1, track2, track3, bpm, program=program, octachord=-1)
    music.play_chord(5, track, track1, track2, track3, bpm, program=program, octachord=-1)
    
    mid.save('normal.mid')
  
def main():
    normal_chord()
    music.play_midi('normal.mid')

if __name__ == '__main__':
    main()
    
    