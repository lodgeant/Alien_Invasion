import sys
import pygame

from settings import Settings

# Global variables
GAME_VERSION = "v0.1"


# Main game loop
def run_game():
    """ Init game, settings and screen object """
    pygame.init()
    ai_settings = Settings()    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion " + GAME_VERSION)
    
    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()


# Main entry point for game
run_game()