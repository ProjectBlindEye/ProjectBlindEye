import os, shutil, vlc, time
from pydub import AudioSegment
from gtts import gTTS

vlc_instance = vlc.Instance('--aout=alsa')
audio_player = vlc_instance.media_player_new()

def read(text):

    #Print
    print(text)

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
    media = vlc_instance.media_new('stereo.wav')
    audio_player.set_media(media)
    audio_player.play()
    time.sleep(1.5)
    duration = audio_player.get_length() / 1000
    time.sleep(duration)
    os.remove('stereo.wav')
