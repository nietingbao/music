from mido import MidiFile, MidiTrack
import music

# 粉刷匠
def fsj():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    bpm = 90
    program = 24
    verse5(track,bpm,program)
    verse2(track,bpm,program)
    music.play_note(5, 1, track, bpm, program)
    music.play_note(5, 1, track, bpm, program, velocity=0)
    verse5(track,bpm,program)
    verse2(track,bpm,program)
    music.play_note(1, 1, track, bpm, program)
    music.play_note(5, 1, track, bpm, program, velocity=0)
    mid.save('fsj.mid')
    
def verse5(track, bpm, program):
    music.play_note(5, 0.5, track, bpm, program)
    music.play_note(3, 0.5, track, bpm, program)
    music.play_note(5, 0.5, track, bpm, program)
    music.play_note(3, 0.5, track, bpm, program)
    music.play_note(5, 0.5, track, bpm, program)
    music.play_note(3, 0.5, track, bpm, program)
    music.play_note(1, 1, track, bpm, program)

def verse2(track, bpm, program):
    music.play_note(2, 0.5, track, bpm, program)
    music.play_note(4, 0.5, track, bpm, program)
    music.play_note(3, 0.5, track, bpm, program)
    music.play_note(2, 0.5, track, bpm, program)

def main():
    fsj()
    music.play_midi('fsj.mid')

if __name__ == '__main__':
    main()
    