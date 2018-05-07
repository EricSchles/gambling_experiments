import random
from collections import namedtuple
import IPython
import matplotlib.pyplot as plt


def generate_deck():
    deck = []
    Card = namedtuple("Card", ["number", "suit"])
    for suit in ["hearts", "clubs", "diamonds", "spades"]:
        # 13 is Ace
        for card_num in range(2,14):
            card = Card(card_num, suit)
            deck.append(card)
    return deck


def check_deck(deck):
    if len(deck) == 52 and deck[0].suit == "hearts" and deck[51].suit=="spades":
        return True
    else:
        return False


def draw_card(deck):
    """
    draw card samples without replacement
    """
    card = random.choice(deck)
    deck.remove(card)
    return card


def draw_hands(num_players, deck):
    number_cards = 5
    number_iterations = num_players * number_cards
    player_enumeration = list(range(num_players))
    hands = {key:[] for key in player_enumeration}
    for draw in range(number_iterations):
        player = draw % num_players
        hands[player].append(draw_card(deck))
    return hands, deck


def discard(player, card, hands):
    hands[player].remove(card)
    return hands


def is_straight(hand):
    hand.sort()
    min_card = min(hand)
    max_card = max(hand)
    run_hand = list(range(min_card, max_card+1))
    if hand == run_hand:
        True
    else:
        return False

    
def is_flush(suits):
    if len(set(suits)) == 1:
        return True
    else:
        return False

    
def determine_hand(hand):
    numbers = [card.number for card in hand]
    suits = [card.suit for card in hand]
    max_count = 0
    pair_exists = False
    three_of_a_kind_exists = False
    four_of_a_kind_exists = False
    num_pairs = 0
    for number in numbers:
        count = numbers.count(number)
        if count == 2:
            pair_exists = True
            num_pairs += 1
        if count == 3:
            three_of_a_kind_exists = True
        if count == 4:
            four_of_a_kind_exists = True
    if four_of_a_kind_exists:
        return "four of a kind"
    elif pair_exists and three_of_a_kind_exists:
        return "full house"
    elif three_of_a_kind_exists:
        return "three of a kind"
    elif num_pairs > 2:
        return "two pair"
    elif pair_exists:
        return "pair"
    elif is_straight(numbers) and is_flush(suits):
        return "straight flush"
    elif is_flush(suits):
        return "flush"
    elif is_straight(numbers):
        return "straight"
    else:
        return "high card"
     
        
def calculate_points(hand):
    hand_type = determine_hand(hand)
    if hand_type == "high card":
        numbers = [card.number for card in hand]
        return max(numbers)
    elif hand_type == "pair":
        numbers = [card.number for card in hand]
        return 14 + max([number for number in numbers if numbers.count(number) > 1])
    elif hand_type == "two pair":
        numbers = [card.number for card in hand]
        return 27 + max([number for number in numbers if numbers.count(number) > 1])
    elif hand_type == "three of a kind":
        numbers = [card.number for card in hand]
        return 40 + max([number for number in numbers if numbers.count(number) > 2])
    elif hand_type == "full house":
        numbers = [card.number for card in hand]
        return 69 + max([number for number in numbers if numbers.count(number) > 2])
    elif hand_type == "straight":
        numbers = [card.number for card in hand]
        return 53 + max(numbers)
    elif hand_type == "flush":
        numbers = [card.number for card in hand]
        return 61 + max(numbers)
    elif hand_type == "four of a kind":
        numbers = [card.number for card in hand]
        return 81 + max([number for number in numbers if numbers.count(number) > 3])
    elif hand_type == "straight flush":
        numbers = [card.number for card in hand]
        return 93 + max(numbers)
    
def determine_winner(hands):
    """
    How this works:
    We will use a point system.
    high_card -> 2 - 13
    pair -> 14 - 26
    2 pair -> 27 - 39
    3 of a kind -> 40 - 52
    straight -> 53 - 60
    flush -> 61 - 68
    full house -> 69 - 80
    four of a kind -> 81 - 92
    straight flush -> 93 - 100
    """
    player_scores = {} 
    for player in hands:
        player_scores[player] = calculate_points(hands[player]) 
    max_score = 0
    max_player = ''
    for player in player_scores:
        if player_scores[player] > max_score:
            max_score = player_scores[player]
            max_player = player
    return max_player


def experiment_one(num_players, num_iterations):
    """
    In this experiment, we ask the question:
    'Over n hands, what cards are most probable?'
    Of course, the long term probabilities are known,
    but what is the asymptotic behavior of the system?
    """
    experiments = []
    for _ in range(num_iterations):
        deck = generate_deck()
        hands, _ = draw_hands(num_players, deck)
        experiments.append(determine_winner(hands))
    players = list(set(experiments))
    win_proportion = {}.fromkeys(players, 0)
    for player in players:
        win_proportion[player] = experiments.count(player) / len(experiments)
    return win_proportion

for i in range(2, 5):
    print("For ", i, "players at", 1000, "experiments, the results were", experiment_one(i, 1000))
    print("For ", i, "players at", 10000, "experiments, the results were", experiment_one(i, 10000))
    print("For ", i, "players at", 100000, "experiments, the results were", experiment_one(i, 100000))

        
