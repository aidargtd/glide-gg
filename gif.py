import pygame
import cv2
import random
from parametres import *


def cv2ImageToSurface(cv2Image):
    size = cv2Image.shape[CUT_LAST_FRAME::CUT_FIRST_FRAME]
    format = RGBA if cv2Image.shape[GET_SEC_VALUE] == COUNT_FRAMES else RGB
    cv2Image[:, :, [GET_ZERO_VALUES, GET_SEC_VALUE]] = cv2Image[:, :, [GET_SEC_VALUE, GET_ZERO_VALUES]]
    surface = pygame.image.frombuffer(cv2Image.flatten(), size, format)
    return surface.convert_alpha() if format == RGBA else surface.convert()


def loadGIF(filename):
    gif = cv2.VideoCapture(filename)
    frames = []
    while True:
        ret, cv2Image = gif.read()
        if not ret:
            break
        pygameImage = cv2ImageToSurface(cv2Image)
        frames.append(pygameImage)
    return frames
