import pygame
import networkx as nx
import matplotlib.pyplot as plt
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Global Trade Route Simulation")
clock = pygame.time.Clock()

# Define trade hubs with positions
trade_hubs = {
    "Shanghai": (650, 300),
    "Rotterdam": (300, 200),
    "Los Angeles": (100, 350),
    "Dubai": (500, 350),
    "Singapore": (600, 450),
    "New York": (200, 150),
    "Tokyo": (700, 250)
}

# Define trade routes (ships & planes)
trade_routes = [
    ("Shanghai", "Los Angeles"),
    ("Shanghai", "Rotterdam"),
    ("Rotterdam", "New York"),
    ("Los Angeles", "Tokyo"),
    ("Dubai", "Singapore"),
    ("Singapore", "Shanghai"),
    ("New York", "Dubai")
]


# Load assets
ship_img = pygame.image.load("ship.png")  # Add a small ship image
plane_img = pygame.image.load("plane.png")  # Add a small plane image
ship_img = pygame.transform.scale(ship_img, (30, 30))
plane_img = pygame.transform.scale(plane_img, (30, 30))

# Define moving cargo objects
class Cargo:
    def __init__(self, start, end, image):
        self.start = start
        self.end = end
        self.image = image
        self.x, self.y = trade_hubs[start]
        self.target_x, self.target_y = trade_hubs[end]
        self.speed = random.uniform(1, 2)
        self.active = True

    def move(self):
        if self.active:
            dx = self.target_x - self.x
            dy = self.target_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance > 1:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed
            else:
                self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))

# Generate moving cargo
cargo_list = [Cargo(start, end, ship_img if random.random() > 0.5 else plane_img) for start, end in trade_routes]

# Game loop
running = True
while running:
    screen.fill((0, 0, 30))  # Dark blue background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw trade hubs
    for hub, pos in trade_hubs.items():
        pygame.draw.circle(screen, (0, 255, 0), pos, 8)  # Green hubs

    # Draw trade routes
    for start, end in trade_routes:
        pygame.draw.line(screen, (255, 255, 255), trade_hubs[start], trade_hubs[end], 2)

    # Move & draw cargo
    for cargo in cargo_list:
        cargo.move()
        cargo.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()