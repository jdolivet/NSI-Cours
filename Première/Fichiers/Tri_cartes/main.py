"""
               GLWT(Good Luck With That) Public License
                 Copyright (c) Everyone, except Author

Everyone is permitted to copy, distribute, modify, merge, sell, publish,
sublicense or whatever they want with this software but at their OWN RISK.

                            Preamble

The author has absolutely no clue what the code in this project does.
It might just work or not, there is no third option.


                GOOD LUCK WITH THAT PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION, AND MODIFICATION

  0. You just DO WHATEVER YOU WANT TO as long as you NEVER LEAVE A
TRACE TO TRACK THE AUTHOR of the original product to blame for or hold
responsible.

IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

Good luck and Godspeed.

You can get a copy of this license at https://github.com/me-shaon/GLWTPL

"""


# import of needed libraries
import pygame
import random
from pygame import Vector2

from sys import exit as sexit

# constants
BG_COLOR = (10, 70, 10)

# pygame init
pygame.init()

pygame.display.set_caption('Card Game')

width, height = (1000, 300)
screen = pygame.display.set_mode((width, height),
                                 flags=pygame.SCALED)

f = random.choice(('co', 'ca', 'p', 't'))
cards = [
    pygame.image.load(f"assets/{f}{i}.gif")
    for i in range(2, 15)
]
random.shuffle(cards)

pos = [
    Vector2(x * width / 13, height / 16)
    for x in range(13)
]


card_surf = pygame.Surface((71, 96))
rectdet = [screen.blit(card_surf, (x, y)) for (x, y) in pos]

click = False
running = True
clicked_card = -1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sexit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            position_souris = event.pos
            for a in range(13):
                if rectdet[a].collidepoint(position_souris):
                    clicked_card = a
                    click = True
            #pos.append(pos.pop(clicked_card))
            rectdet = [screen.blit(card_surf, (x, y)) for (x, y) in pos]
            #cards.append(cards.pop(clicked_card))

        if event.type == pygame.MOUSEBUTTONUP:
            click = False

        if event.type == pygame.MOUSEMOTION:
            if click == True and clicked_card != -1:
                try:
                    pos[clicked_card] += event.rel
                except AttributeError:
                    pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass

    rectdet = [screen.blit(card_surf, p) for p in pos]
    screen.fill(BG_COLOR)
    for i, card in enumerate(cards):
        screen.blit(card, pos[i])
    pygame.display.flip()

pygame.quit()

# thanks https://iteroni.com/watch?v=dQw4w9WgXcQ for helping