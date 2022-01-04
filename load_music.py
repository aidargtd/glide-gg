import pygame
# import pyttsx3
from deep_translator import GoogleTranslator
import requests
from gtts import gTTS
from parametres import *
from playsound import playsound


def quote_to_speech(l_id):
    url_for_quote = URL_FOR_QUOTE
    r = requests.get(url_for_quote)
    quote = r.json()
    text = GoogleTranslator(source=EN, target=RU).translate(quote[GET_QUOTE])
    language = RU
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save(f"{PATH_FOR_CREATE_QUOTES}{l_id}{FORMAT_OGG}")
    playsound(f"{PATH_FOR_CREATE_QUOTES}{l_id}{FORMAT_OGG}")


def sound(name, on, volume=USING_VOLUME):
    pygame.mixer.music.load(f'{PATH_FOR_SOUND_IN_LEVELS}{name}')
    pygame.mixer.music.set_volume(volume)
    if on:
        pygame.mixer.music.play(INFINITY_PLAYBACK)
    else:
        pygame.mixer.music.stop()


def sound_effects(name, on, volume=USING_VOLUME):
    effect = pygame.mixer.Sound(f'{PATH_MUSIC}{name}')
    effect.set_volume(volume)
    if on:
        pygame.mixer.Sound.play(effect)

# sound_collision = pygame.mixer.Sound('Samples/3816133910831170.ogg')
# sound_click = pygame.mixer.Sound('Samples/zapsplat_multimedia_button_click_005_68777.mp3')
# sound_click.set_volume(0.3)
# sound_restart = pygame.mixer.Sound('Samples/8476647490550829.ogg')
