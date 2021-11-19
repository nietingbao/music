# Use Python MIDI to write songs
本项目使用python的MIDI库和pygame库实现了用计算机演奏音乐
## 目录结构

music.py中定义了弹奏单个音符和弹奏和弦的函数，play_midi用于演奏音乐；fsj.py和hls.py分别实现了《我是一个粉刷匠》和《欢乐颂》的片段；
chord.py实现了一个非常通用的和弦旋律 CAFG，可以使用该旋律作为大部分流行歌曲的伴奏。如《传奇》，《好久不见》，《菊花台》，《感恩的心》，《听海》等。

## 单轨音乐
函数play_note定义了如何弹出一个音符
```python
# note表示音高，length表示拍子的长度，base_note是do开始的音高，octachord表示跨越几个八度, velocity表示音乐击打的速度，表现为强度
play_note(note, length, track, bpm, program, base_note=60, octachord=0, velocity=64, channel=0)
```

## 和弦
函数play_chord定义了如何弹奏出一个大三和弦
```python
# 大三和弦（全全半全全全半）
def play_chord(note, track, track1, track2, track3, bpm, program, octachord=0, base_note=60, length=1):
```
