import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

clock = pygame.time.Clock()

songs = [
    "Miyagi_JEndshpil_Mav-d_-_Aphrodisiac_78725692.mp3",
    "Tones_and_I_-_Dance_Monkey_66175914.mp3",
    "Kayrat_Nurtas_-_MY_UNIVERSE_62847935.mp3"
]

current_song_index = 0

def play_song(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song(current_song_index)

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song(current_song_index)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_song(current_song_index)
            if event.key == pygame.K_s:
                stop_music()
            if event.key == pygame.K_n:
                next_song()
            if event.key == pygame.K_b:
                previous_song()
        
    screen.fill("white")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()