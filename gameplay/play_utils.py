import pygame

def player_is_bot(player):
    return player.type != "human"

# Handle sounds
game_start_sound = pygame.mixer.Sound("assets/sounds/game_start.mp3")
move_sound = pygame.mixer.Sound("assets/sounds/slot.mp3")

def play_sound(last_time, current_time, sound, move_delay=50):
    if current_time - last_time > move_delay:  # Cooldown of 100ms
        sound.play()
        return current_time
    return last_time
