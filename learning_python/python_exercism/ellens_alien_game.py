class Alien:
    health = 3
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health != 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, alien_object):
        pass

def new_aliens_collection(alien_start_positions):
    aliens_list = []
    for alien in alien_start_positions:
        new_alien = Alien(alien[0], alien[1])
        aliens_list.append(new_alien)

    return aliens_list