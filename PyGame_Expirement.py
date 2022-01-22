"""
LESSON: 3.1 - Lines
WARMUP 1
"""

import random
import pygame
pygame.init()
window = pygame.display.set_mode([400, 300])
window.fill((72, 245, 15))

rand1 = random.randint(0, 300)
rand2 = random.randint(0, 300)

print(rand1)
print(rand2)

if rand1 > rand2:
    print(str(rand1) + " is the bigger number!")
elif rand2 > rand1:
    print(str(rand2) + " is the bigger number!")
else:
    print("Both numbers were the same! Incredible!")
pygame.draw.line(window, (15, 15, 242), (50, rand1), (350, rand2), 5)
pygame.display.flip()
input("Press enter to close the window ")