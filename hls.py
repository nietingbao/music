from mido import MidiFile, MidiTrack
import music

# 欢乐颂
def hls():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    bpm = 120
    program = 1
    verse3(track, bpm, program)
    music.play_note(3, 1.5, track, bpm, program)
    music.play_note(2, 0.5, track, bpm, program)
    music.play_note(2, 1, track, bpm, program)
    # We use velocity=0 to play a stop
    music.play_note(5, 1, track, bpm, program, velocity=0)
    verse3(track,bpm,program)
    music.play_note(2, 1.5, track, bpm, program)
    music.play_note(1, 0.5, track, bpm, program)
    music.play_note(1, 1, track, bpm, program)
    music.play_note(5, 1, track, bpm, program, velocity=0)
    
    music.play_note(2, 1, track, bpm, program)
    music.play_note(2, 1, track, bpm, program)
    music.play_note(3, 1, track, bpm, program)
    music.play_note(1, 1, track, bpm, program)
    
    music.play_note(2, 1, track, bpm, program)
    music.play_note(3, 0.5, track, bpm, program)
    music.play_note(4, 0.5, track, bpm, program)
    music.play_note(3, 1, track, bpm, program)
    music.play_note(1, 1, track, bpm, program)
    
    music.play_note(2, 1, track, bpm, program)
    music.play_note(3, 0.5, track, bpm, program)
    music.play_note(4, 0.5, track, bpm, program)
    music.play_note(3, 1, track, bpm, program)
    music.play_note(2, 1, track, bpm, program)
    
    music.play_note(1, 1, track, bpm, program)
    music.play_note(2, 1, track, bpm, program)
    music.play_note(5, 1, track, bpm, program, octachord=-1)
    music.play_note(5, 1, track, bpm, program, velocity=0)
    
    verse3(track,bpm,program)
    music.play_note(2, 1.5, track, bpm, program)
    music.play_note(1, 0.5, track, bpm, program)
    music.play_note(1, 1, track, bpm, program)
    music.play_note(5, 1, track, bpm, program, velocity=0)
    mid.save('hls.mid')
    
def verse3(track, bpm, program):
    music.play_note(3, 1, track, bpm, program)
    music.play_note(3, 1, track, bpm, program)
    music.play_note(4, 1, track, bpm, program)
    music.play_note(5, 1, track, bpm, program)
    
    music.play_note(5, 1, track, bpm, program)
    music.play_note(4, 1, track, bpm, program)
    music.play_note(3, 1, track, bpm, program)
    music.play_note(2, 1, track, bpm, program)
    
    music.play_note(1, 1, track, bpm, program)
    music.play_note(1, 1, track, bpm, program)
    music.play_note(2, 1, track, bpm, program)
    music.play_note(3, 1, track, bpm, program)
    
def main():
    hls()
    music.play_midi('hls.mid')

if __name__ == '__main__':
    main()
    