import cards


def main():
    screen = cards.Window("The Space Electricity", (1270, 790))
    # picture1 = pygame.image.load('images//blue-5457731_640.jpg', "diamond")
    # picture2 = pygame.transform.scale(picture1, (150, 100))
    # screen.screen.blit(picture2,(50,480))
    card1 = cards.Card('Diamond', 'images//blue-5457731_640.jpg', "+3 cards on hand")
    card2 = cards.Card('CityLight', 'images//architecture-1868667_640.jpg', '+1card +1M')

    def draw(screen):
        card1.draw(screen, 50, 450)
        card2.draw(screen, 200, 450)

    def draw_picture(screen):
        card1.draw_picture(screen, 50, 450)
        card2.draw_picture(screen, 200, 450)
    screen.start(draw,draw_picture)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cards.create_lorem_ipsum_card_csv(20)
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#     print()