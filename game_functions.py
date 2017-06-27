import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events (ai_settings, screen, stats, play_button, ship, aliens,
                  bullets, sb):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            sys.exit ()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button (ai_settings, screen, stats, play_button,
            ship, aliens, bullets, sb, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events (event, ai_settings, screen, stats, ship, aliens, bullets, sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_button (ai_settings, screen, stats, play_button, ship, aliens,
                       bullets, sb, mouse_x, mouse_y):
    """Start a new game when the user clicks play."""
    button_clicked = play_button.rect.collidepoint (mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game (ai_settings, screen, stats, ship, aliens, bullets, sb)

def start_game (ai_settings, screen, stats, ship, aliens, bullets, sb):
    """Start a new game when prompted by the user."""
    #Hide the mouse cursor
    pygame.mouse.set_visible(False)
    #Reset the game statistics.
    stats.reset_stats()
    sb.prep_images ()
    sb.prep_images()
    stats.game_active = True
    #Empty the list of rapests and bullets
    aliens.empty()
    bullets.empty()
    #Create a new fleet and centre the ship.
    ai_settings.initialise_dynamic_settings()
    create_fleet (ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_keydown_events (event, ai_settings, screen, stats, ship, aliens,
                          bullets, sb):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet (ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit ()
    elif event.key == pygame.K_p:
        if stats.game_active == False:
            start_game (ai_settings, screen, stats, ship, aliens, bullets, sb)

def check_keyup_events(event,ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet (ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not yet reached."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet (ai_settings, screen, ship)
        bullets.add (new_bullet)

def get_number_aliens_x (ai_settings, alien_width):
    """Determine the number of aliens that fit on a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int (available_space_x / ( 2* alien_width))
    return number_aliens_x

def get_number_rows (ai_settings, ship_height, alien_height):
    """Determine the number of rows that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int (available_space_y / (2 * alien_height))
    return number_rows

def create_alien (ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row."""
    alien = Alien (ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + ((2 * alien_number) * alien_width)
    alien.rect.x = alien.x
    #This line is what moves each row down the screen when the fleet is
    #created in the create_fleet function.
    alien.rect.y = alien.rect.height + ((2 * row_number) * alien.rect.height)
    aliens.add (alien)

def create_fleet (ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    #Create a hypothetical alien and find the number of aliens in a row, and
    #the number of rows that fit on the screen.
    alien = Alien (ai_settings, screen)
    number_aliens_x = get_number_aliens_x (ai_settings, alien.rect.width)
    number_rows = get_number_rows (ai_settings, ship.rect.height, alien.rect.height)
    #Create the actual fleet of aliens.
    for row_number in range (number_rows):
        for alien_number in range (number_aliens_x):
            create_alien (ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges (ai_settings, aliens):
    """Respond appropriately if any aliens have reached the edge."""
    for alien in aliens.sprites():
        if alien.check_edges ():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction (ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_bullets (ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    #Update bullet positions
    bullets.update()
    #Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove (bullet)
    check_bullet_collisions (ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_collisions (ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to any bullet-rapest collisions."""
    #Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #Increase the score - Totals is the number of aliens in the dictionary
    #created by the collisions function above
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    #If all aliens have been destroyed, create a new fleet.
    if len(aliens) == 0:
        # If all aliens are destroyed, start a new level.
        start_new_level(bullets, ai_settings, stats, sb, screen, ship, aliens)
        bullets.empty()

def start_new_level (bullets, ai_settings, stats, sb, screen, ship, aliens):
    bullets.empty()
    ai_settings.increase_speed()
    stats.level += 1
    sb.prep_level()
    create_fleet (ai_settings, screen, ship, aliens)

def check_high_score (stats, sb):
    """Check to see if there is a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        filename = 'high_score.txt'
        with open (filename, 'w') as file_object:
            file_object.write (str(stats.high_score))

def update_aliens (ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Check if the fleet is at an edge and then update positions of all the
    rapests, also checking for impacts
    """
    check_fleet_edges (ai_settings, aliens)
    aliens.update()
    # Look for rapest-girl collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    check_aliens_bottom (ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_aliens_bottom (ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any rapests have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this as if the girl has been hit
            ship_hit (ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def ship_hit (ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to a girl being hit by a rapest"""
    if stats.ships_left > 0:
        #Lose a life
        stats.ships_left -=1
        #Update the scoreboard
        sb.prep_ships()
        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        #Create a new fleet and center the ship
        create_fleet (ai_settings, screen, ship, aliens)
        ship.center_ship()
        #Pause
        sleep (0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible (True)

def update_screen (ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    #alien.blitme()
    for bullet in bullets.sprites ():
        bullet.draw_bullet()
    ship.blitme()
    #THIS IS WHERE I FIGURED OUT WHY THE ALIENS DIDN'T APPEAR
    aliens.draw(screen)
    #aliens.blitme()
    #aliens.blitme()
    #Draw the score information
    sb.show_score()
    #Draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    #Make the most recently drawn screen visible.
    pygame.display.flip()

    

#15 seconds
    
