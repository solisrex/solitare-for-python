#https://stackoverflow.com/questions/11469025/how-to-implement-a-subscriptable-class-in-python-subscriptable-class-not-subsc
#https://stackoverflow.com/questions/152580/whats-the-canonical-way-to-check-for-type-in-python
#https://bicyclecards.com/how-to-play/solitaire/
#https://stackoverflow.com/questions/6087484/how-to-capture-pygame-screen
import pygame, sys, math
from pygame.locals import *
from Deck import *

def create_value_text(red, suit, value):
    return fontObj.render(value_dict[value]+suit_unicode[suit],True, color_dict[red])

def return_card_value(card, red, suit, value):
    pos = card.get_height()//15
    value_text = create_value_text(red,suit,value)
    card.blit(value_text,(pos,pos))
    card.blit(value_text,(card.get_width()-pos-value_text.get_width(),card.get_height()-pos-value_text.get_height()))
    return card

def alternate_ascending(card1,card2):
    if (card1.red != card2.red) and (card1.value+1 == card2.value):
        return True
    else:
        return False

def ascending_suit(card1, card2):
    if (card1.suit == card2.suit) and (card1.value +1 == card2.value):
        return True
    else:
        return False

def blit_back_card(x,y):
    DISPLAYSURF.blit(card_back,(x,y))

def draw_lower_piles():
    for j in range(len(piles_lower)):
        if piles_lower[j] != []:
            for i in range(len(piles_lower[j])):
                card = piles_lower[j][i]
                blit_back_card(card_back.get_width()*(j+35/168)*12//7, (card_back.get_height()//5)*i)
        else:
            pygame.draw.rect(DISPLAYSURF, (0,0,0), [card_back.get_width()*(j+35/168)*12//7, 0, card_back.get_width(), card_back.get_height()], 2)
def draw_upper_piles():
    for j in range(len(piles_upper)):
        for i in range(len(piles_upper[j])):
            card = piles_upper[j][i]
            DISPLAYSURF.blit(blit_dict[card],(card_back.get_width()*(j+35/168)*12//7, (card_back.get_height()//5*(len(piles_lower[j])+i))))

def draw_selected(cards, x, y):
    for i in range(len(cards)):
        DISPLAYSURF.blit(blit_dict[cards[i]], (x, y+i*card_back.get_height()//5))

def draw_stock():
    if deck.deck != []:
        DISPLAYSURF.blit(card_back,(35/168*card_back.get_width()*12//7,height-card_back.get_height()-35/168*card_back.get_width()*12//7))
    else:
        pygame.draw.rect(DISPLAYSURF, (0,0,0), [35/168*card_back.get_width()*12//7,height-card_back.get_height()-35/168*card_back.get_width()*12//7, card_back.get_width(), card_back.get_height()], 2)

def draw_waste():
    if waste != []:
        DISPLAYSURF.blit(blit_dict[waste[-1]], (card_back.get_width()*(1+35/168)*12//7, height-card_back.get_height()-35/168*card_back.get_width()*12//7))
    else:
        pygame.draw.rect(DISPLAYSURF, (0,0,0), (card_back.get_width()*(1+35/168)*12//7, height-card_back.get_height()-35/168*card_back.get_width()*12//7, card_back.get_width(), card_back.get_height()), 2)

def draw_foundations():
    if heart_foundation == []:
        pygame.draw.rect(DISPLAYSURF, (255,0,0), [card_back.get_width()*(3+35/168)*12//7, height-card_back.get_height()-35/168*card_back.get_width()*12//7, card_back.get_width(), card_back.get_height()], 2)
        DISPLAYSURF.blit(heart, (card_back.get_width()*(3+35/168+7/24)*12//7-heart.get_width()//2, height-1/2*card_back.get_height()-35/168*card_back.get_width()*12//7-heart.get_height()//2))
    else:
        DISPLAYSURF.blit(blit_dict[heart_foundation[-1]],((3+35/168)*card_back.get_width()*12//7,height-card_back.get_height()-35/168*card_back.get_width()*12//7))

    if diamond_foundation == []:
        pygame.draw.rect(DISPLAYSURF, (255,0,0), [card_back.get_width()*(4+35/168)*12//7, height-card_back.get_height()-35/168*card_back.get_width()*12//7, card_back.get_width(), card_back.get_height()], 2)
        DISPLAYSURF.blit(diamond, (card_back.get_width()*(4+35/168+7/24)*12//7-heart.get_width()//2, height-1/2*card_back.get_height()-35/168*card_back.get_width()*12//7-heart.get_height()//2))
    else:
        DISPLAYSURF.blit(blit_dict[diamond_foundation[-1]],((4+35/168)*card_back.get_width()*12//7,height-card_back.get_height()-35/168*card_back.get_width()*12//7))

    if spade_foundation == []:
        pygame.draw.rect(DISPLAYSURF, (0,0,0), [card_back.get_width()*(5+35/168)*12//7, height-card_back.get_height()-35/168*card_back.get_width()*12//7, card_back.get_width(), card_back.get_height()], 2)
        DISPLAYSURF.blit(spade, (card_back.get_width()*(5+35/168+7/24)*12//7-heart.get_width()//2, height-1/2*card_back.get_height()-35/168*card_back.get_width()*12//7-heart.get_height()//2))
    else:
        DISPLAYSURF.blit(blit_dict[spade_foundation[-1]],((5+35/168)*card_back.get_width()*12//7,height-card_back.get_height()-35/168*card_back.get_width()*12//7))

    if clubs_foundation == []:
        pygame.draw.rect(DISPLAYSURF, (0,0,0), [card_back.get_width()*(6+35/168)*12//7, height-card_back.get_height()-35/168*card_back.get_width()*12//7, card_back.get_width(), card_back.get_height()], 2)
        DISPLAYSURF.blit(club, (card_back.get_width()*(6+35/168+7/24)*12//7-heart.get_width()//2, height-1/2*card_back.get_height()-35/168*card_back.get_width()*12//7-heart.get_height()//2))
    else:
        DISPLAYSURF.blit(blit_dict[clubs_foundation[-1]],((6+35/168)*card_back.get_width()*12//7,height-card_back.get_height()-35/168*card_back.get_width()*12//7))
        
def scale_x(x):
    return  7*x/(card_face.get_width()*12)-35/168

def scale_y(y):
    return  5*y/card_back.get_height()

def check_xbounds(x):
    x_scaled = scale_x(x)
    x_floored = math.floor(x_scaled)
    if x_scaled - x_floored < 1-5/12:
        return True
    else:
        return False

def check_ybounds(x,y):
    x_floored = math.floor(scale_x(x))
    y_floored = math.floor(scale_y(y))
    
    lower_col = piles_lower[x_floored]
    upper_col = piles_upper[x_floored]
    max_lower = len(lower_col)
    max_upper = len(upper_col)
    max_y = max_lower + max_upper
    if y_floored < max_y+4:
        return True
    else:
        return False

def check_both_bounds(x,y):
    if check_xbounds(x) and check_ybounds(x,y) is True:
        return True
    else:
        return False

def check_empty(x,y):
    if check_both_bounds(x,y):
        pass

def check_stock(x,y):
    if 0 < scale_x(x) < 1-5/12:
        return True

def empty_col(col_num):
    if len(piles_upper[col_num]) == 0 and len(piles_lower[col_num]) == 0:
        return True
    else:
        return False
    
def get_cards(x,y):
    #Only to be run after checking xbounds.
    x_floored = math.floor(scale_x(x))
    y_floored = math.floor(scale_y(y))

    lower_col = piles_lower[x_floored]
    upper_col = piles_upper[x_floored]

    max_lower = len(lower_col)
    max_upper = len(upper_col)
    max_y = max_lower + max_upper

    if y_floored < max_lower:
        return [[lower_col[y_floored:]], False, x_floored, y_floored]
    elif max_lower <= y_floored < max_y:
        return [upper_col[y_floored-max_lower:], True, x_floored, y_floored]
    elif max_y <= y_floored < max_y+4 and max_upper > 0:
        return [[upper_col[-1]], True, x_floored, y_floored]
    elif max_y <= y_floored < max_y+4 and max_lower > 0 and max_upper == 0:
        return [[lower_col[-1]], False, x_floored, y_floored]

def check_foundation_bound(x,y):
    if 1 <= scale_y(height-y)-35/168 <= 6 and 3 <= scale_x(x) < 7-5/12:
        return True
    else:
        return False

def get_foundation_suit(x, y):
    if 3 < scale_x(x) < 4-5/12:
        return "Hearts"
    elif 4 < scale_x(x) < 5-5/12:
        return "Diamonds"
    elif 5 < scale_x(x) < 6-5/12:
        return "Spades"
    elif 6 < scale_x(x) < 7-5/12:
        return "Clubs"

def check_waste_bound(x,y):
    if 1 <= scale_y(height-y)-35/168 <= 6 and 1 <= scale_x(x) < 2-5/12:
        return True
    else:
        return False

def handle_last_event():
    global selected_stack, dragging, last_col, waste
    if last_foundation == True:
        found_dict[selected_stack[0].suit] += selected_stack
        selected_stack = None
        dragging = False
    elif last_tableau == True :
        if type(selected_stack) != list:
            piles_upper[last_col]+=[selected_stack]
        else:
            piles_upper[last_col]+=selected_stack
            elected_stack = None
            dragging = False
    elif last_waste == True:
            waste += selected_stack
            selected_stack = None
            dragging = False

def set_last_events_negative():
    global last_foundation, last_tableau, last_waste
    last_foundation = False
    last_tableau = False
    last_waste = False

def check_win():
    if piles_lower == [[]]*7:
        return True
    else:
        return False

suit_unicode = {"Spades": u"♠", "Hearts" : u"♥", "Diamonds" : u"♦", "Clubs" : u"♣"}
value_dict = {1 : u"A", 2 : u"2", 3 : u"3", 4 : u"4", 5 : u"5", 6 : u"6", 7 : u"7", 8 : u"8", 9 : u"9", 10 : u"10", 11 : u"J", 12 : u"Q", 13 : u"K"}
color_dict = {True : (244,7,56), False : (0,0,0)}

pygame.init()
fontObj = pygame.font.SysFont("arial", 40)
win_text = fontObj.render("You Win!",True, (255,255,255))
heart = fontObj.render(suit_unicode["Hearts"],True, color_dict[True])
diamond = fontObj.render(suit_unicode["Diamonds"],True, color_dict[True])
spade = fontObj.render(suit_unicode["Spades"],True, color_dict[False])
club = fontObj.render(suit_unicode["Clubs"],True, color_dict[False])
fontObj = pygame.font.SysFont("arial", 20)
height = 750
width = 4*height//3
LIGHT_GOLD = (240, 238, 203)
GREY = (200, 200, 200)
DARK_BLUE = (3, 13, 43)
BLACK = (0,0,0)
card_back = pygame.image.load("../Solitare/Images/Card_Back_Black_and_White.png")
card_back = pygame.transform.scale(card_back, (width//12, (7*width//(5 * 12))))
card_face = pygame.image.load("../Solitare/Images/Card_Face_Black_and_White.png")
card_face = pygame.transform.scale(card_face, (width//12, (7*width//(5 * 12))))

deck = Deck()
deck.shuffle()
waste = []
heart_foundation = []
diamond_foundation = []
spade_foundation = []
clubs_foundation = []

found_dict = {"Hearts" : heart_foundation, "Diamonds" : diamond_foundation, "Spades" : spade_foundation, "Clubs" : clubs_foundation}

piles_lower = [deck.draw_n(i) for i in range(0,7)]
piles_upper = [[deck.draw()] for i in range(0,7)]
total_upper = [card[0] for card in piles_upper]
pile_dict = {True : piles_upper, False : piles_lower}

blit_upper = [return_card_value(card_face.copy(),pile.red,pile.suit,pile.value) for pile in total_upper]
blit_dict = dict(zip(total_upper,blit_upper))
DISPLAYSURF =  pygame.display.set_mode((width,height))
        
def main():
    global waste, last_foundation, last_tableau, last_waste, dragging, selected_stack, last_col
    FPSCLOCK = pygame.time.Clock()
    selected_stack = None
    dragging = False
    last_foundation = False
    last_tableau = False
    last_waste = False
    win = False
    while True:
        DISPLAYSURF.fill((36,158,89))
        draw_lower_piles()
        draw_upper_piles()
        draw_stock()
        draw_waste()
        draw_foundations()
        if dragging == True:
            draw_selected(selected_stack, mousex-card_face.get_width()//2, mousey)
        if win == True:
            DISPLAYSURF.blit(win_text,(width//2-win_text.get_width()//2,height//2-win_text.get_height()))
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            if event.type ==  MOUSEBUTTONUP:

                if dragging == True and check_both_bounds(event.pos[0],event.pos[1]) == True:
                    if empty_col(math.floor(scale_x(mousex))) == False:
                        _, is_upper, col, _ = get_cards(event.pos[0],event.pos[1])

                    else:
                        is_upper = False
                        col = math.floor(scale_x(mousex))

                    if is_upper is True and alternate_ascending(selected_stack[0],piles_upper[col][-1]) is True:
                        piles_upper[col]+=selected_stack
                        selected_stack = None
                        dragging = False
                        if last_tableau:
                            if len(piles_upper[last_col]) == 0 and len(piles_lower[last_col]) != 0:
                                new_card = piles_lower[last_col].pop()
                                piles_upper[last_col].append(new_card)
                                blit_dict[new_card] = return_card_value(card_face.copy(),new_card.red,new_card.suit,new_card.value)
                                if check_win():
                                    win = True
                        set_last_events_negative()

                    elif is_upper is False and selected_stack[0].value == 13:
                        piles_upper[col]+=selected_stack
                        selected_stack = None
                        dragging = False
                        if len(piles_upper[last_col]) == 0 and len(piles_lower[last_col]) != 0 and last_tableau == True:
                            new_card = piles_lower[last_col].pop()
                            piles_upper[last_col].append(new_card)
                            blit_dict[new_card] = return_card_value(card_face.copy(),new_card.red,new_card.suit,new_card.value)
                            if check_win():
                                win = True
                        set_last_events_negative()

                    else:
                        handle_last_event()
                        set_last_events_negative()
                        
                elif dragging == True and check_foundation_bound(event.pos[0], event.pos[1]) == True and len(selected_stack) == 1:
                    found_suit = get_foundation_suit(event.pos[0], event.pos[1])

                    if found_dict[found_suit] != []:
                        found_card = found_dict[found_suit]

                        if ascending_suit(found_dict[found_suit][-1], selected_stack[0]) ==  True:
                            found_dict[found_suit] += selected_stack
                            selected_stack = None
                            dragging = False

                            if len(piles_upper[last_col]) == 0 and len(piles_lower[last_col]) != 0 and last_tableau == True:
                                new_card = piles_lower[last_col].pop()
                                piles_upper[last_col].append(new_card)
                                blit_dict[new_card] = return_card_value(card_face.copy(),new_card.red,new_card.suit,new_card.value)
                                if check_win():
                                    win = True
                            set_last_events_negative()

                    elif (found_suit == selected_stack[0].suit and selected_stack[0].value == 1):
                        found_dict[found_suit] += selected_stack
                        selected_stack = None
                        dragging = False
                        if last_tableau == True:
                            if len(piles_upper[last_col]) == 0 and len(piles_lower[last_col]) != 0:
                                new_card = piles_lower[last_col].pop()
                                piles_upper[last_col].append(new_card)
                                blit_dict[new_card] = return_card_value(card_face.copy(),new_card.red,new_card.suit,new_card.value)
                                if check_win():
                                    win = True
                        set_last_events_negative()
                    else:
                        handle_last_event()
                        set_last_events_negative()
                elif dragging == True:
                    handle_last_event()
                    set_last_events_negative()

                elif dragging == False and check_both_bounds(event.pos[0],event.pos[1]) == True:
                        cards, is_upper, col, row = get_cards(event.pos[0],event.pos[1])
                        last_col = col
                        if is_upper:
                            selected_stack = cards
                            print(selected_stack)
                            dragging = not dragging
                            last_tableau = True
                            for card in selected_stack:
                                pile_dict[True][col].remove(card)

                elif dragging == False and check_stock(event.pos[0],event.pos[1]) == True:
                    if deck.deck != []:
                        waste += [deck.draw()]
                        if waste[-1] not in blit_dict:
                            blit_dict[waste[-1]] = return_card_value(card_face.copy(),waste[-1].red,waste[-1].suit,waste[-1].value)
                    else:
                        deck.deck = waste
                        waste = []
                elif dragging == False and check_foundation_bound(event.pos[0], event.pos[1]) == True:
                    print(get_foundation_suit(event.pos[0],event.pos[1]))
                    found_suit = get_foundation_suit(event.pos[0], event.pos[1])
                    if found_suit != None:
                        if found_dict[found_suit] != []:
                            selected_stack = [found_dict[found_suit].pop()]
                            dragging = not dragging
                            last_foundation = True
                elif dragging == False and check_waste_bound(event.pos[0],event.pos[1]) == True:
                    if waste != []:
                        selected_stack = [waste.pop()]
                        print(selected_stack)
                        dragging = not dragging
                        last_waste = True
        
        pygame.display.update()
        FPSCLOCK.tick(30)
main()
