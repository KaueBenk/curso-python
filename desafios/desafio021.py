import pygame

print('='*10, 'Desafio 021', '='*10, '\nMúsica\n')
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
print('Ouça...')
while pygame.mixer.music.get_busy():
    pass
