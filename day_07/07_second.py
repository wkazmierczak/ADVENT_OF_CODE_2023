def second_07(file):
    lines = [line.rstrip() for line in file]
    cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
             '2': 2}

    tab_of_decks = []

    for line in lines:
        deck, bid = line.split(' ')
        n_cards_in_deck = {}
        for c in deck:
            if c == 'J':
                continue
            if c not in n_cards_in_deck:
                n_cards_in_deck[c] = 1
            else:
                n_cards_in_deck[c] += 1

        n_J = deck.count('J')

        values_of_cards = sorted(n_cards_in_deck.values(), reverse=True)
        if values_of_cards:
            values_of_cards[0] += n_J
        else:
            values_of_cards = [n_J]

        if values_of_cards[0] == 5:
            tab_of_decks.append((6, deck, bid))
        elif values_of_cards[0] == 4:
            tab_of_decks.append((5, deck, bid))
        elif values_of_cards[0] == 3 and values_of_cards[1] == 2:
            tab_of_decks.append((4, deck, bid))
        elif values_of_cards[0] == 3:
            tab_of_decks.append((3, deck, bid))
        elif values_of_cards[0] == 2 and values_of_cards[1] == 2:
            tab_of_decks.append((2, deck, bid))
        elif values_of_cards[0] == 2:
            tab_of_decks.append((1, deck, bid))
        else:
            tab_of_decks.append((0, deck, bid))

    merge_sort(tab_of_decks, cards)

    res = 0
    n = len(tab_of_decks)

    for _, dec, bid in tab_of_decks:
        res += int(bid) * n
        n -= 1

    print(tab_of_decks)

    return res


def merge_sort(A, cards):
    n = len(A)

    if n > 1:

        left = A[:n // 2]
        right = A[n // 2:]

        merge_sort(left, cards)
        merge_sort(right, cards)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:
                A[k] = left[i]
                i += 1
            elif left[i][0] == right[j][0]:
                for c1, c2 in zip(left[i][1], right[j][1]):
                    if cards[c1] == cards[c2]:
                        continue
                    if cards[c1] > cards[c2]:
                        A[k] = left[i]
                        i += 1
                        break
                    else:
                        A[k] = right[j]
                        j += 1
                        break

            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

    return A


if __name__ == '__main__':
    with open("07_input") as f:
        res = second_07(f)
        print(res)
