import os, shutil, vlc, time
from pydub import AudioSegment
from gtts import gTTS

vlc_instance = vlc.Instance('--aout=alsa')
audio_player = vlc_instance.media_player_new()

def read_text(text):
    #Generate Sound from Text
    tts = gTTS(text)
    tts.save('left.wav')
    shutil.copyfile("left.wav", "right.wav")
    left_channel = AudioSegment.from_file("left.wav")
    right_channel = AudioSegment.from_file("right.wav")
    stereo_sound = AudioSegment.from_mono_audiosegments(left_channel, right_channel)
    stereo_sound.export("stereo.wav", format="wav")
    os.remove("left.wav")
    os.remove("right.wav")

    #Play Sound
    play_sound('stereo.wav')
    os.remove('stereo.wav')

def play_sound(file_path):
    media = vlc_instance.media_new(file_path)
    audio_player.set_media(media)
    audio_player.play()
    time.sleep(1.5)
    duration = audio_player.get_length() / 1000
    time.sleep(duration)
