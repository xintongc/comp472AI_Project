import Half
import Card

card_Position = input("Please input your card position:")
print(card_Position)


half1 = Half.Half('R', 'X')
half2 = Half.Half('L', 'O')
card = Card.Card(half1, half2)
print(card.name())
