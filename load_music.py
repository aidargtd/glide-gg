import pygame
import pyttsx3
from deep_translator import GoogleTranslator
import requests


def quote_to_speech():
    url_for_quote = 'https://api.quotable.io/random'
    r = requests.get(url_for_quote)
    quote = r.json()
    text = GoogleTranslator(source='en', target='ru').translate(quote['content'])
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def sound(name, on):
    pygame.mixer.music.load(name)
    pygame.mixer.music.set_volume(0.3)
    if on:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()


sound_collision = pygame.mixer.Sound('Samples/3816133910831170.ogg')
sound_click = pygame.mixer.Sound('Samples/zapsplat_multimedia_button_click_005_68777.mp3')
sound_click.set_volume(0.3)
sound_restart = pygame.mixer.Sound('Samples/8476647490550829.ogg')
