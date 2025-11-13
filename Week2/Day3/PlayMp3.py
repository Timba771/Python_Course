import pygame
import os

def play_file(file_name: str) -> None:
    if not os.path.exists(file_name):
        raise FileNotFoundError(file_name)
    
    pygame.mixer.init() # öffnet Audiodevice

    try:
        pygame.mixer.music.load(file_name) # Datei aus GeneratedMp3.py
        pygame.mixer.music.play()
       
        # kleines "Event-Loop", damit das Programm nicht sofort endet
        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(30)
    finally:
        pygame.mixer.quit()