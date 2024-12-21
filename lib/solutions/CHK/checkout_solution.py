import numpy as np


# noinspection PyUnusedLocal
# skus = unicode string

def discount(counts, special_n, d_price, price):
    # checks amount of special prices they can get
    special_price = (counts // special_n) * d_price
    # gets left overs from special prices
    remaining = (counts % special_n) * price
    return special_price + remaining


def checkout(skus):
    items = ["A", "B", "C", "D", "E"]
    item_prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    special_prices = {"A": [{"type": "d", "n": 3, "p": 130}, {"type": "d", "n": 5, "p": 200}],
                      "B": [{"type": "d", "n": 2, "p": 45}],
                      "E": [{"type": "f", "n": 2, "i": "B", "q": 1}],
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
                    if free_product in special_prices.keys():
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
                offers = np.ones(n_offers) * 1000

                for offer in range(n_offers):
                    # assuming only discount offers for this
                    offers[offer] = discount(letter_counts[char], special_prices[char][offer]["n"],
                                             special_prices[char][offer]["p"], item_prices[char])
                best_offer = np.min(offers)
                total += best_offer

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
    "Test 7: ": {"t": "AAAAAAAAA", "r": 390},

}
if __name__ == "__main__":
    for test in test_dic:
        print(f"{test} {checkout(test_dic[test]['t']) == test_dic[test]['r']}")

