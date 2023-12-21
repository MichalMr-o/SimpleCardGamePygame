import random
import csv
import pygame

class Window:
    def __init__(self, title: object, size: object) -> object:
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    def start(self, draw, draw_picture):
        while True:      
            draw(self.screen)
            draw_picture(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

# TODO: creating cards from CSV:
# def createCardsFromCsv(self, file_name):

# Not works - want to create CSV with simple input.
# def create_lorem_ipsum_card_csv(number_of_cards_csv: int):
#     with open('cards.csv', 'a', newline='') as file_cards:
#         header = ['name', 'picture_url', 'description', 'name_of_deck']
#         writer = csv.writer(file_cards, delimiter=';')
#         writer.writerow(header)
#
#         for number in range(number_of_cards_csv):
#             writer.writerow([f'card{number}', f'pixabay', 'description', 'deck1'])
#         pass

# card class - single card.

CARD_SIZE = (150, 300)
class Card:
    def __init__(self, name: str, picture, description: str):
        self.name = name
        self.picture = picture
        self.description = description

    def draw(self, screen, x, y):
        pygame.draw.rect(screen, (0, 0, 255), (x, y, CARD_SIZE[0], CARD_SIZE[1]), 1)
        font = pygame.font.Font('Roboto-Light.ttf', 30)
        text = font.render(self.name, True, (255, 255, 255))
        size = text.get_size()

        tx = x + CARD_SIZE[0] / 2 - size[0] / 2

        screen.blit(text, (tx , y + 10))

        font = pygame.font.Font('Roboto-Light.ttf', 15)
        text = font.render(self.description, True, (255, 255, 255))
        size = text.get_size()

        tx = x + CARD_SIZE[0] / 2 - size[0] / 2
        screen.blit(text, (tx, y + 150))

    def draw_picture(self, screen, x, y):
        picture1 = pygame.image.load(self.picture, self.name)
        picture2 = pygame.transform.scale(picture1, (150, 100))
        screen.blit(picture2, (x, y + 45))

#TODO: Want to copy all cards with specific name_of_deck
class DeckOfCards:
    def __init__(self):
        self.list_of_cards = []
    
    def add_to_deck(self, card):
        self.list_of_cards.append(card)

class HandOfCards():
    pass



