from mido import Message,MidiFile, MidiTrack 
import pygame
import time

# 使用大调，可用其他调式
scale_list = [0, 2, 2, 1, 2, 2, 2, 1]

def play_midi(file):
    freq = 44100
    bitsize = -16
    channels = 0
    buffer = 1024
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(10)
    clock = pygame.time.Clock()
    try:
        pygame.mixer.music.load(file)
    except:
        import traceback
        print(traceback.format_exc())
    pygame.mixer.music.play()
    print("played")
    while  pygame.mixer.music.get_busy():
        clock.tick(30)

# note表示音高，length表示拍子的长度，base_note是do开始的音高，octachord表示跨越几个八度, velocity表示音乐击打的速度，表现为强度
def play_note(note, length, track, bpm, program, base_note=60, octachord=0, velocity=64, channel=0):
    time_per_beat = 60 * 1000 / bpm
    real_note = base_note + sum(scale_list[0:note]) + octachord * 12
    play_time = time_per_beat * length
   
    track.append(Message('program_change',channel=0,program=program,time=0))
    track.append(Message('note_on', note=real_note, time=0, velocity=velocity, channel=channel))
    track.append(Message('note_off', note=real_note, time=round(play_time), velocity=velocity, channel=channel))
    
def main():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track1 = MidiTrack()
    mid.tracks.append(track1)
    track2 = MidiTrack()
    mid.tracks.append(track2)
    track.append(Message('program_change',channel=0,program=1,time=0))
    track.append(Message('note_on', note=72, time=0, velocity=64, channel=0))
    track.append(Message('note_off', note=72, time=500, velocity=64, channel=0))
    # play_chord(0, track, track1, track2, 90, 1)
    mid.save("note.mid")
    play_midi("note.mid")

# 大三和弦（全全半全全全半）
def play_chord(note, track, track1, track2, track3, bpm, program, octachord=0, base_note=60, length=1):
    chord_array = [0, 4, 7]
    time_per_beat = 60 * 1000 / bpm
    play_time = time_per_beat * length
    track1.append(Message('program_change',channel=0,program=program,time=0))
    track2.append(Message('program_change',channel=0,program=program,time=0))
    track3.append(Message('program_change',channel=0,program=program,time=0))
     
    real_note1 = base_note + sum(scale_list[0:(note+chord_array[0])]) + octachord * 12
    track1.append(Message('note_on', note=real_note1, time=0))
    real_note2 = base_note + sum(scale_list[0:(note+chord_array[1])]) + octachord * 12
    track2.append(Message('note_on', note=real_note2, time=0))
    real_note3 = base_note + sum(scale_list[0:(note+chord_array[2])]) + octachord * 12
    track3.append(Message('note_on', note=real_note3, time=0))
    
        
    track1.append(Message('note_off', note=real_note1, time=round(play_time)))
    track2.append(Message('note_off', note=real_note2, time=round(play_time)))
    track3.append(Message('note_off', note=real_note3, time=round(play_time)))
         
    
if __name__ == '__main__':
    main()

