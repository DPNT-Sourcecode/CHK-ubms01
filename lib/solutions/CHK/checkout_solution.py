import numpy as np
# very sorry thought I had restarted it in the chk_r4 challenge, I think I started making changes about 15:20
# but it would make sense to just continue the timer from when I paused it.

# noinspection PyUnusedLocal
# skus = unicode string

def discount(counts, special_n, d_price, price):
    # checks amount of special prices they can get
    special_price = (counts // special_n) * d_price
    # gets left overs from special prices
    remaining = (counts % special_n) * price
    return special_price + remaining


def checkout(skus):
    items = [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"]
    item_prices = {
        "A": 50, "B": 30, "C": 20, "D": 15, "E": 40,
        "F": 10, "G": 20, "H": 10, "I": 35, "J": 60,
        "K": 80, "L": 90, "M": 15, "N": 40, "O": 10,
        "P": 50, "Q": 30, "R": 50, "S": 30, "T": 20,
        "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50,

    }
    special_prices = {"A": [{"type": "d", "n": 3, "p": 130}, {"type": "d", "n": 5, "p": 200}],
                      "B": [{"type": "d", "n": 2, "p": 45}],
                      "E": [{"type": "f", "n": 2, "i": "B", "q": 1}],
                      "F": [{"type": "f", "n": 3, "i": "F", "q": 1}],
                      "H": [{"type": "d", "n": 5, "p": 45}, {"type": "d", "n": 10, "p": 80}],
                      "K": [{"type": "d", "n": 2, "p": 150}],
                      "N": [{"type": "f", "n": 3, "i": "M", "q": 1}],
                      "P": [{"type": "d", "n": 5, "p": 200}],
                      "Q": [{"type": "d", "n": 3, "p": 80}],
                      "R": [{"type": "f", "n": 3, "i": "Q", "q": 1}],
                      "U": [{"type": "f", "n": 4, "i": "U", "q": 1}],
                      "V": [{"type": "d", "n": 2, "p": 90}, {"type": "d", "n": 3, "p": 130}],
                      }

    letter_counts = {letter: 0 for letter in items}

    # iterate through items

    for char in skus:
        # if in list
        if char in items:
            letter_counts[char] += 1
        else:
            return -1

    # dict{A:1, B: 3...}

    # go through all the items
    total = 0
    for char in items:
        # check if special price
        if char in special_prices.keys():
            # checks number of offers
            if len(special_prices[char]) == 1:

                if special_prices[char][0]["type"] == "d":
                    total += discount(letter_counts[char], special_prices[char][0]["n"],
                                      special_prices[char][0]["p"], item_prices[char])

                elif special_prices[char][0]["type"] == "f":
                    # checks amount of special prices they can get
                    number_free = (letter_counts[char] // special_prices[char][0]["n"])
                    free_product = special_prices[char][0]["i"]

                    if letter_counts[free_product] < number_free:
                        number_free = letter_counts[free_product]

                    if free_product in special_prices.keys() and special_prices[free_product][0]["type"] == "d":
                        previous_price = discount(letter_counts[free_product], special_prices[free_product][0]["n"],
                                                  special_prices[free_product][0]["p"], item_prices[free_product])
                        new_price = discount((letter_counts[free_product] - number_free),
                                             special_prices[free_product][0]["n"],
                                             special_prices[free_product][0]["p"], item_prices[free_product])

                    else:
                        previous_price = letter_counts[free_product] * item_prices[free_product]
                        new_price = (letter_counts[free_product] - number_free) * item_prices[free_product]

                    price_char = letter_counts[char] * item_prices[char]
                    total += (new_price - previous_price + price_char)

                else:
                    print(f"error: {special_prices[char]}")
            else:
                n_offers = len(special_prices[char])
                list_n = np.zeros(n_offers)
                list_p = np.zeros(n_offers)
                list_ind = np.zeros(n_offers)

                for offer in range(n_offers):
                    list_n[offer] = special_prices[char][offer]["n"]
                    list_p[offer] = special_prices[char][offer]["p"]
                    list_ind[offer] = offer

                indices = np.argsort(list_n)[::-1]

                tot = 0
                rem = letter_counts[char]
                for i in indices:

                    groups_n = rem // list_n[i]
                    rem = rem % list_n[i]

                    tot += groups_n * list_p[i]


                tot += rem * item_prices[char]

                total += tot

                #sorted_n = [list_n[i] for i in indices]
                #sorted_p = [list_p[i] for i in indices]
                #sorted_ind = [list_ind[i] for i in indices]

                #for N_discount in

                #offers = np.ones(n_offers) * 1000


                #for offer in range(n_offers):
                    # assuming only discount offers for this
                #    offers[offer] = discount(letter_counts[char], special_prices[char][offer]["n"],
                #                             special_prices[char][offer]["p"], item_prices[char])
                #best_offer = np.min(offers)
                #total += best_offer

        else:
            total += (item_prices[char] * letter_counts[char])

    return total


test_dic = {
    "Test 1: ": {"t": "AABCDA", "r": 195},
    "Test 2: ": {"t": "BBCX", "r": -1},
    "Test 3: ": {"t": "BBCDA", "r": 130},
    "Test 4: ": {"t": "DCBA", "r": 115},
    "Test 5: ": {"t": "AAAAAA", "r": 250},
    "Test 6: ": {"t": "AAAAA", "r": 200},
    "Test 7: ": {"t": "AAAAAAAAA", "r": 380},
    "Test 8: ": {"t": "AAAAABBBEEDD", "r": 355},
    "Test 9: ": {"t": "F", "r": 10},
    "Test 10: ": {"t": "FF", "r": 20},
    "Test 11: ": {"t": "FFF", "r": 20},
    "Test 12: ": {"t": "FFFF", "r": 30},
    "Test 13: ": {"t": "FFFF", "r": 30},
    "Test 14: ": {"t": "AAAAABBBEEDDFFFF", "r": 385},
    "Test 15: ": {"t": "DCBAFFFF", "r": 145},
    "Test 16: ": {"t": "RRRQQQQQQQ", "r": 310},
    "Test 17: ": {"t": "RRRQQQQ", "r": 230},
    "Test 18: ": {"t": "UUUU", "r": 120},
    "Test 19: ": {"t": "UUU", "r": 120},

}
if __name__ == "__main__":
    for test in test_dic:
        res = checkout(test_dic[test]['t'])
        print(f"{test} {res == test_dic[test]['r']}, {res}")
