#_______Description_____

#https://projecteuler.net/problem=54
#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#High Card: Highest value card.
#One Pair: Two cards of the same value.
#Two Pairs: Two different pairs.
#Three of a Kind: Three cards of the same value.
#Straight: All cards are consecutive values.
#Flush: All cards of the same suit.
#Full House: Three of a kind and a pair.
#Four of a Kind: Four cards of the same value.
#Straight Flush: All cards are consecutive values of same suit.
#Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#The cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
#Consider the following five hands dealt to two players:
#
#Hand Player 1 Player 2 Winner
#1 5H 5C 6S 7S KDPair of Fives 2C 3S 8S 8D TDPair of Eights Player 2
#2 5D 8C 9S JS ACHighest card Ace 2C 5C 7D 8S QHHighest card Queen Player 1
#3 2D 9C AS AH ACThree Aces 3D 6D 7D TD QDFlush  with Diamonds Player 2
#4 4D 6S 9H QH QCPair of QueensHighest card Nine 3D 6D 7H QD QSPair of QueensHighest card Seven Player 1
#5 2H 2D 4C 4D 4SFull HouseWith Three Fours 3C 3D 3S 9S 9DFull Housewith Three Threes Player 1
#
#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#How many hands does Player 1 win?
##_______end_description_____:
                  
# Current solution too long, will improve.

from collections import Counter as C
values={'T':10,'J':11,'Q':12,'K':13,'A':14}

def hand_winner(l):
    def card_value(l):
        values_list=[]
        for i in l:
            if i[0].isdigit():values_list.append(int(i[0]))
            else:values_list.append(values[i[0]])
        return values_list

    def same_suit(l):#takes raw
        if len(set([l[i][1] for i in range(5)]))==1:return True
        else:return False
        
    def highest_card(l,l2):#takes values
        player1=sorted(l, reverse=True)
        player2=sorted(l2, reverse=True)
        for i in range(len(l)):
            if player1[i] == player2[i]:
                continue
            else:
                if player1[i]>player2[i]:return 1
                else:return 2
        return 0
            
    def is_consecutive(l):#takes values
        values_set=set(l)
        if values_set == set(range(min(values_set), max(values_set)+1)) and len(values_set)==5:
            return True
        else:return False
    
    def royal_flush(l):#takes raw
        royal_set={'T','J','Q','K','A'}
        if royal_set==set([l[i][0] for i in range(5)]) and same_suit(l):
                return True
        else: return False
    
    def straigh_flush(raw,values):#takes raw
        if same_suit(raw) and is_consecutive(values):return True,max(values)
        else:return False
    
    def four(l):#takes values
        pair_values=list(i for i in C(l) if C(l)[i]==4)
        if 4 in C(l).values(): return True,pair_values[0]
        else: return False
        
    def three(l):#takes values
        pair_values=list(i for i in C(l) if C(l)[i]==3)
        if 3 in C(l).values(): return True,pair_values[0],[item for item in l if item not in set(pair_values)]
        else: return False
    def pair(l):#takes values
        pair_values=list(i for i in C(l) if C(l)[i]==2)
        if 2 in C(l).values(): return True,pair_values,[item for item in l if item not in set(pair_values)]
        else: return False
        
    def full_house(l):#takes values
        if three(l) and pair(l) and len(pair(l)[1])==1:return True,three(l)[1],pair(l)[1][0]
        else:return False
    p1=l[0:5];p2=l[5:10]
    p1_v=card_value(p1);p2_v=card_value(p2)
    royal=royal_flush(p1);royal2=royal_flush(p2)
    if royal and not royal2:return 1
    if royal2 and not royal:return 2
    straight=straigh_flush(p1,p1_v);straight2=straigh_flush(p2,p2_v)
    if straight and not straight2:return 1
    if straight2 and not straight:return 2
    if straight and straight2:
        if straight[1]>straight2[1]:return 1
        else:return 2
    four1=four(p1_v);four2=four(p2_v)
    if four1 and not four2:return 1
    if four2 and not four1:return 2
    if four1 and four2:
        if four1[1]>four2[1]:return 1
        if four1[1]<four2[1]:return 2
    full1=full_house(p1_v);full2=full_house(p2_v)
    if full1 and not full2:return 1
    if full2 and not full1:return 2
    if full1 and full2:
        if full1[1]>full2[1]:return 1
        if full1[1]<full2[1]:return 2
        else:
            if full1[2]>full2[2]: return 1
            else: return 2
    flush1=same_suit(p1);flush2=same_suit(p2)
    if flush1 and not flush2:return 1
    if flush2 and not flush1:return 2
    if flush1 and flush2:
        return highest_card(p1_v, p2_v)
    straight21=is_consecutive(p1_v);straight22=is_consecutive(p2_v)
    if straight21 and not straight22:return 1
    if straight22 and not straight21:return 2
    if straight21 and straight22:
        return highest_card(p1_v, p2_v)
    threep1=three(p1_v);threep2=three(p2_v)
    if threep1 and not threep2:return 1
    if threep2 and not threep1:return 2
    if threep1 and threep2:
        if threep1[1]>threep2[1]: return 1
        if threep1[1]<threep2[1]: return 2
        else: 
            return highest_card(threep1[2], threep2[2])
    pair1=pair(p1_v);pair2=pair(p2_v)
    if pair1 and not pair2:return 1
    if pair2 and not pair1:return 2
    if pair1 and pair2:
        if len(pair1[1])>len(pair2[1]): return 1
        if len(pair1[1])<len(pair2[1]): return 2
        else: #same amount pairs
            if highest_card(pair1[1],pair2[1])==0:
                return highest_card(pair1[2],pair2[2])
            else: return highest_card(pair1[1],pair2[1])
    return highest_card(p1_v, p2_v)
score=0
pokertxt =open('poker.txt', 'r')
hands=[i.split(' ') for i in pokertxt.read().split('\n')]
for i in hands[:1000]:
    if hand_winner(i) == 1:
        score+=1
        
print(score)
