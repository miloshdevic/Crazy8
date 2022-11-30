# Chaima Boussora 20159909
# Milosh Devic 20158232
import copy
import math
import random


class LinkedList:
    class _Node:
        def __init__(self, v, n):
            self.value = v
            self.next = n

    def __init__(self):
        self._head = None
        self._size = 0

    def __str__(self):
        # TO DO
        list = "["
        node = self._head

        if self.isEmpty():
            list += "]"
            return list

        elif type(self._head.value) is Card:
            while node.next:
                list += str(node.value) + ", "
                node = node.next
            list += str(node.value) + "]"
            return list

        while node.next:
            list += str(node.value) + ", "
            node = node.next

        list += str(node.value) + "]"
        return list

    def __len__(self):
        return self._size

    def isEmpty(self):
        # TO DO
        return self._head is None

    # Adds a node of value v to the beginning of the list
    def add(self, v):
        # TO DO
        node = self._Node(v, self._head)  # node.value = v et node.next = head
        self._head = node
        self._size += 1

    # Adds a node of value v to the end of the list
    def append(self, v):
        # TO DO
        node_to_add = self._Node(v, None)  # noeud qu'on ajoute dans la liste

        if self.isEmpty():
            self._head = node_to_add
        else:
            node = self._head
            while node.next:
                node = node.next
            node.next = node_to_add

        self._size += 1

    # Removes and returns the first node of the list
    def pop(self):
        # TO DO
        if self.isEmpty():
            return None
        else:  # changer les pointeurs
            node = self._head
            value = node.value
            self._head = node.next
            self._size -= 1
            return value

    # Returns the value of the first node of the list
    def peek(self):
        # TO DO
        return self._head.value

    # Removes the node of the list with value v and return v
    def remove(self, v):
        # TO DO
        if self.isEmpty():
            return None

        node = self._head
        # s'il n'y a qu'un seul noeud et que c'est ≠ de v
        if node.next is None and node.value != v:
            return None
        # retirer le 1er noeud
        elif node.value == v:
            self.pop()
            return v

        # trouver l'élément
        while node.next.value != v:
            node = node.next
            # si l'élément n'existe pas
            if node.next is None:
                return None

        # retirer l'élément
        if node.next.next is None:
            node.next = None
        else:
            node.next = node.next.next

        self._size -= 1
        return v


class CircularLinkedList(LinkedList):
    def __init__(self):
        super().__init__()

    def __str__(self):
        # TO DO
        list = "["
        node = self._head

        while (node.next is not self._head):
            list += str(node.value) + ", "
            node = node.next

        list += str(node.value) + "]"
        return list

    def __iter__(self):
        # TO DO
        node = self._head
        while node.next is not self._head:
            yield node.value
            node = node.next
        yield node.value

    # Moves head pointer to next node in list
    def next(self):
        # TO DO
        self._head = self._head.next  # changer le noeud auquel on pointe "head"

    # Adds a node of value v to the end of the list
    def append(self, v):
        # TO DO
        node_to_add = self._Node(v, self._head)  # noeud qu'on ajoute dans la liste

        if self.isEmpty():
            self._head = node_to_add
            node_to_add.next = self._head  # il faut remettre car la premiere fois, head = None
        else:
            node = self._head
            while node.next is not self._head:
                node = node.next
            node.next = node_to_add

        self._size += 1

    # Reverses the next pointers of all nodes to previous node
    def reverse(self):
        # TO DO
        if self.isEmpty():
            return None

        prev = None  # pointeur du noeud précédent
        node = self._head

        # changer les pointeurs
        temp = node.next
        node.next = prev
        prev = node
        node = temp

        while node is not self._head:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        self._head.next = prev

    # Removes head node and returns its value
    def pop(self):
        # TO DO
        node = self._head
        popped_value = self._head.value

        if self.isEmpty() or (self._head.next == self._head):
            self._head = None
            return None

        while node.next is not self._head:
            node = node.next

        node.next = self._head.next
        self._head = self._head.next
        return popped_value


class Card:
    def __init__(self, r, s):
        self._rank = r
        self._suit = s

    suits = {'s': '\U00002660', 'h': '\U00002661', 'd': '\U00002662', 'c': '\U00002663'}

    def __str__(self):
        # print(self._rank + self.suits[self._suit])
        return self._rank + self.suits[self._suit]

    def __eq__(self, other):
        # TO DO
        if type(self) is not type(other):
            return False

        if self._rank == other._rank and self._suit == other._suit:
            return True
        elif self._suit == other._suit:
            return (self._rank == 'A' or self._rank == '1') and (other._rank == 'A' or other._rank == '1')
        else:
            return False


class Hand:
    def __init__(self):
        self.cards = {'s': LinkedList(), 'h': LinkedList(), 'd': LinkedList(), 'c': LinkedList()}

    def __str__(self):
        result = ''
        for suit in self.cards.values():
            result += str(suit)
        return result

    def __getitem__(self, item):
        return self.cards[item]

    def __len__(self):
        result = 0
        for suit in list(self.cards):
            result += len(self.cards[suit])

        return result

    def add(self, card):
        self.cards[card._suit].add(card)

    def get_most_common_suit(self):
        return max(list(self.cards), key=lambda x: len(self.cards[x]))

    # Returns a card included in the hand according to
    # the criteria contained in *args and None if the card
    # isn't in the hand. The tests show how *args must be used.
    def play(self, *args):
        # TO DO
        if len(args) == 2:
            # si le 1er argument passé est le suit
            if args[0] in self.cards:
                rank = args[1]
                if rank == '1':
                    rank = 'A'
                list_rank = self.__getitem__(args[0])  # prendre la liste de rank pour le suit correspondant
                if not list_rank.isEmpty():
                    card_to_find = Card(rank, args[0])
                    return list_rank.remove(card_to_find)

            # si le 1er argument passé est le rank
            elif args[1] in self.cards:
                rank = args[0]
                if rank == '1':
                    rank = 'A'
                list_rank = self.__getitem__(args[1])  # prendre la liste de rank pour le suit correspondant
                if not list_rank.isEmpty():
                    card_to_find = Card(rank, args[1])
                    return list_rank.remove(card_to_find)

        # un seul argument
        else:
            # si c'est un suit en paramètre
            if args[0] in self.cards:
                list_rank = self.__getitem__(args[0])  # prendre la liste de rank pour le suit correspondant
                if not list_rank.isEmpty():
                    return list_rank.pop()

            # si c'est un rank en paramètre
            else:
                rank = args[0]
                if rank == '1':
                    rank = 'A'
                for suit in self.cards:
                    list_rank = self.__getitem__(suit)
                    if not list_rank.isEmpty():
                        card_to_find = Card(rank, suit)
                        card_in_hand = list_rank.remove(card_to_find)
                        if card_in_hand:
                            return card_in_hand
        return None


class Deck(LinkedList):
    def __init__(self, custom=False):
        super().__init__()
        if not custom:
            # for all suits
            for i in range(4):
                # for all ranks
                for j in range(13):
                    s = list(Card.suits)[i]
                    r = ''
                    if j == 0:
                        r = 'A'
                    elif j > 0 and j < 10:
                        r = str(j + 1)
                    elif j == 10:
                        r = 'J'
                    elif j == 11:
                        r = 'Q'
                    elif j == 12:
                        r = 'K'
                    self.add(Card(r, s))

    def draw(self):
        return self.pop()

    def shuffle(self, cut_precision=0.05):
        # Cutting the two decks in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision * len(self)))
        # other_deck must point the kth node in self
        # (starting at 0 of course)
        other_deck = self._head
        original_deck = self._head

        # faire pointer au kième noeud
        for i in range(k):
            other_deck = other_deck.next
            if i != k - 1:
                original_deck = original_deck.next

        # TO DO: seperate both lists
        original_deck.next = None
        original_deck = self._head
        # trouver les tailles
        original_deck_size = k
        other_deck_size = self._size - k

        # Merging the two decks together
        if random.uniform(0, 1) < 0.5:
            temp1 = original_deck.next
            temp2 = other_deck.next
            self._head = other_deck
            # switch self._head and other_deck pointers
            for i in range(min(original_deck_size, other_deck_size)):
                other_deck.next = original_deck
                original_deck.next = temp2
                original_deck = temp1
                other_deck = temp2
                temp1 = temp1.next
                temp2 = temp2.next
                if temp1 is None:
                    other_deck.next = original_deck
                    original_deck.next = temp2
                    break
                if temp2 is None:
                    other_deck.next = original_deck
                    break

        # TO DO
        else:
            temp1 = original_deck.next
            temp2 = other_deck.next
            # switch self._head and other_deck pointers
            for i in range(min(original_deck_size, other_deck_size)):
                original_deck.next = other_deck
                other_deck.next = temp1
                original_deck = temp1
                other_deck = temp2
                temp1 = temp1.next
                temp2 = temp2.next
                if temp1 is None:
                    original_deck.next = other_deck
                    break
                if temp2 is None:
                    original_deck.next = other_deck
                    other_deck.next = temp1
                    break


class Player():
    def __init__(self, name, strategy='naive'):
        self.name = name
        self.score = 8
        self.hand = Hand()
        self.strategy = strategy

    def __str__(self):
        return self.name

    # This function must modify the player's hand,
    # the discard pile, and the game's declared_suit
    # attribute. No other variables must be changed.
    # The player's strategy can ONLY be based
    # on his own cards, the discard pile, and
    # the number of cards his opponents hold.
    def play(self, game):
        if (self.strategy == 'naive'):
            top_card = game.discard_pile.peek()
            # TO DO
            # si la carte est un '2' et qu'elle n'est ni une wildcard ni du même rank du score du joueur
            if top_card._rank == '2' and game.draw_count != 0 and game.declared_suit == '':
                card1 = self.hand.play('2')
                if card1:
                    game.discard_pile.add(card1)
                    if self.score == 2:
                        game.declared_suit = self.hand.get_most_common_suit()
                    return game
                card2 = self.hand.play('s', 'Q')
                if card2:
                    game.discard_pile.add(card2)
                return game  # s'il ne peut pas jouer alors il va piger "draw_count" fois

            elif top_card == Card('Q', 's') and game.draw_count != 0:
                card = self.hand.play('2')
                if card:
                    game.discard_pile.add(card)
                return game  # même principe que pour '2'

            else:
                # si la top card est une wildcard
                if game.declared_suit in self.hand.cards:
                    if top_card._rank == '2' and game.draw_count != 0:
                        card = self.hand.play(game.declared_suit, '2')
                        if card:
                            game.discard_pile.add(card)
                        return game
                    card = self.hand.play(game.declared_suit)  # chercher un suit commun en premier
                else:
                    card = self.hand.play(top_card._suit)  # chercher un suit commun en premier
                if card:
                    # la carte prise est une wildcard
                    if card._rank == str(self.score):
                        # rechercher car wildcard en dernier recours
                        if game.declared_suit == '':
                            new_card = self.hand.play(top_card._suit)
                        else:
                            new_card = self.hand.play(game.declared_suit)
                        self.hand.add(card)
                        # ajouter la carte, update "declared_suit" puis update "draw_count" au besoin
                        if new_card:
                            game.discard_pile.add(new_card)
                            game.declared_suit = ''
                            return game
                    else:
                        # ajouter la carte, update "declared_suit" puis update "draw_count" au besoin
                        game.discard_pile.add(card)
                        game.declared_suit = ''
                        return game

                # si c'est une wildcard et qu'on a pas le suit voulu -> mettre notre wildcard (si on a)
                if game.declared_suit != '':
                    card = self.hand.play(str(self.score))
                    if card:
                        game.discard_pile.add(card)
                        game.declared_suit = self.hand.get_most_common_suit()
                    return game

                # chercher le rank commun
                card = self.hand.play(top_card._rank)
                if card and (card._rank != str(self.score)):
                    game.discard_pile.add(card)
                    game.declared_suit = ''
                    if card._rank == str(self.score) or card._rank == 'A' and self.score == 1:
                        game.declared_suit = self.hand.get_most_common_suit()
                    return game
                elif card:
                    self.hand.add(card)

                # si on a rien donc on cherche une wildcard
                if self.score == 1:
                    possible_wildcard = self.hand.play('A')
                else:
                    possible_wildcard = self.hand.play(str(self.score))
                if possible_wildcard:
                    game.discard_pile.add(possible_wildcard)
                    game.declared_suit = self.hand.get_most_common_suit()
                    return game
            return game

        else:
            # TO DO(?): Custom strategy (Bonus)
            pass


class Game:
    def __init__(self):
        self.players = CircularLinkedList()

        for i in range(1, 5):
            self.players.append(Player('Player ' + str(i)))

        self.deck = Deck()
        self.discard_pile = LinkedList()

        self.draw_count = 0
        self.declared_suit = ''

    def __str__(self):
        result = '--------------------------------------------------\n'
        result += 'Deck: ' + str(self.deck) + '\n'
        result += 'Declared Suit: ' + str(self.declared_suit) + ', '
        result += 'Draw Count: ' + str(self.draw_count) + ', '
        result += 'Top Card: ' + str(self.discard_pile.peek()) + '\n'

        for player in self.players:
            result += str(player) + ': '
            result += 'Score: ' + str(player.score) + ', '
            result += str(player.hand) + '\n'
        return result

    # Puts all cards from discard pile except the
    # top card back into the deck in reverse order
    # and shuffles it 7 times
    def reset_deck(self):
        # TO DO

        if self.discard_pile._head:

            cards_to_shuffle = self.discard_pile._head.next
            while cards_to_shuffle.next:
                removed = self.discard_pile.remove(cards_to_shuffle.value)
                self.deck.append(removed)
                cards_to_shuffle = self.discard_pile._head.next
            removed = self.discard_pile.remove(cards_to_shuffle.value)
            self.deck.append(removed)
        # "riffle shuffle" les cartes 7 fois
        for i in range(7):
            self.deck.shuffle()

    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):
        # TO DO
        player = self.players.peek()  # joueur à qui c'est le tour de jouer est tjrs indiqué par le head
        if num < self.deck._size:
            for i in range(num):
                player.hand.add(self.deck.draw())
        else:
            reste = num - self.deck._size
            for i in range(self.deck._size):
                player.hand.add(self.deck.draw())
            self.reset_deck()
            for i in range(reste):
                player.hand.add(self.deck.draw())

    def start(self, debug=False):
        # Ordre dans lequel les joueurs gagnent la partie
        result = LinkedList()

        self.reset_deck()

        # Each player draws 8 cards
        for player in self.players:
            for i in range(8):
                player.hand.add(self.deck.draw())

        self.discard_pile.add(self.deck.draw())

        transcript = open('result.txt', 'w')
        if debug:
            transcript = open('result_debug.txt', 'w')

        while (not self.players.isEmpty()):
            if debug:
                transcript.write(str(self))

            # player plays turn
            player = self.players.peek()

            old_top_card = self.discard_pile.peek()

            self = player.play(self)

            new_top_card = self.discard_pile.peek()

            # Player didn't play a card => must draw from pile
            if new_top_card == old_top_card:
                # TO DO
                message = ''
                if self.draw_count > 0:
                    self.draw_from_deck(self.draw_count)
                    message += player.name + " draws " + str(self.draw_count) + " cards\n"
                    self.draw_count = 0
                else:
                    self.draw_from_deck(1)
                    message += player.name + " draws 1 card\n"

                transcript.write(message)
            # Player played a card
            else:
                # TO DO
                message = player.name + " plays " + str(new_top_card) + "\n"
                transcript.write(message)

                if new_top_card._rank == 'J':
                    if len(player.hand) == 0:
                        player.score -= 1
                        self.draw_from_deck(player.score)
                        message = player.name + " is out of cards to play! " + player.name + \
                                  " draws " + str(player.score) + " card"
                        if player.score > 1:
                            message += "s"
                        message += "\n"
                        transcript.write(message)
                    self.players.next()
                elif new_top_card._rank == '1' or new_top_card._rank == 'A':
                    self.players.reverse()
                elif new_top_card._rank == '2':
                    self.draw_count += 2
                elif new_top_card == Card('Q', 's'):
                    self.draw_count += 5
            # Handling player change
            # Player has finished the game
            if len(player.hand) == 0 and player.score == 1:
                # TO DO
                message = player.name
                player_done = self.players.pop()
                result.append(player_done)
                message += " finishes in position " + str(result._size) + "\n"
                transcript.write(message)
                if new_top_card._rank == 'A':
                    #si le joueur finit avec un ace -> random suit déclaré
                    random_suit = random.randint(0, 3)
                    self.declared_suit = ['s', 'h', 'c', 'd'][random_suit]
                if result._size == 3:
                    message = str(self.players._head.value) + " finishes last\n"
                    result.append(self.players._head.value)
                    self.players.pop()
                    transcript.write(message)

            else:
                # Player is out of cards to play
                if len(player.hand) == 0:
                    # TO DO
                    player.score -= 1
                    self.draw_from_deck(player.score)
                    message = player.name + " is out of cards to play! " + player.name + \
                              " draws " + str(player.score) + " cards\n"
                    transcript.write(message)
                # Player has a single card left to play
                elif len(player.hand) == 1:
                    # TO DO
                    message = "*Knock, knock* - " + player.name + " has a single card left!\n"
                    transcript.write(message)
                self.players.next()

        transcript.close()
        return result


if __name__ == '__main__':

    random.seed(420)
    game = Game()
    print(game.start(debug=True))

    # TESTS
    # LinkedList
    l = LinkedList()
    l.append('b')
    l.append('c')
    l.add('a')

    assert(str(l) == '[a, b, c]')
    assert(l.pop() == 'a')
    assert(len(l) == 2)
    assert(str(l.remove('c')) == 'c')
    assert(l.remove('d') == None)
    assert(str(l) == '[b]')
    assert(l.peek() == 'b')
    assert(l.pop() == 'b')
    assert(len(l) == 0)
    assert(l.isEmpty())

    # CircularLinkedList
    l = CircularLinkedList()
    l.append('a')
    l.append('b')
    l.append('c')

    assert(str(l) == '[a, b, c]')
    l.next()
    assert(str(l) == '[b, c, a]')
    l.next()
    assert(str(l) == '[c, a, b]')
    l.next()
    assert(str(l) == '[a, b, c]')
    l.reverse()
    assert(str(l) == '[a, c, b]')
    assert(l.pop() == 'a')
    assert(str(l) == '[c, b]')

    # Card
    c1 = Card('A','s')
    c2 = Card('A','s')
    # Il est pertinent de traiter le rang 1
    # comme étant l'ace
    c3 = Card('1','s')
    assert(c1 == c2)
    assert(c1 == c3)
    assert(c3 == c2)

    # Hand
    h = Hand()
    h.add(Card('A','s'))
    h.add(Card('8','s'))
    h.add(Card('8','h'))
    h.add(Card('Q','d'))
    h.add(Card('3','d'))
    h.add(Card('3','c'))

    assert(str(h) == '[8♠, A♠][8♡][3♢, Q♢][3♣]')
    assert(str(h['d']) == '[3♢, Q♢]')
    assert(h.play('3','d') == Card('3','d'))
    assert(str(h) == '[8♠, A♠][8♡][Q♢][3♣]')
    assert(str(h.play('8')) == '8♠')
    assert(str(h.play('c')) == '3♣')
    assert(str(h) == '[A♠][8♡][Q♢][]')
    assert(h.play('d','Q') == Card('Q','d'))
    assert(h.play('1') == Card('A','s'))
    assert(h.play('J') == None)

    # Deck
    d = Deck(custom=True)
    d.append(Card('A','s'))
    d.append(Card('2','s'))
    d.append(Card('3','s'))
    d.append(Card('A','h'))
    d.append(Card('2','h'))
    d.append(Card('3','h'))

    random.seed(15)

    temp = copy.deepcopy(d)
    assert(str(temp) == '[A♠, 2♠, 3♠, A♡, 2♡, 3♡]')
    temp.shuffle()
    assert(str(temp) == '[A♠, A♡, 2♠, 2♡, 3♠, 3♡]')
    temp = copy.deepcopy(d)
    temp.shuffle()
    assert(str(temp) == '[A♡, A♠, 2♡, 2♠, 3♡, 3♠]')
    assert(d.draw() == Card('A','s'))
