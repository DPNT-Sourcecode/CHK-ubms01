

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = ["A", "B", "C", "D", "E"]
    item_prices = {"A": 50 , "B":30, "C": 20, "D": 15, "E": 40}
    special_prices = {"A": [{"type": "", "n": 3, "p": 130}, {"n": 5, "p": 200}], "B": {"n": 2, "p": 45}}

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
            # checks amount of special prices they can get
            special_price = (letter_counts[char] // special_prices[char]["n"]) * special_prices[char]["p"]
            # gets left overs from special prices
            remaining = (letter_counts[char] % special_prices[char]["n"]) * item_prices[char]

            total += (special_price + remaining)
        else:
            total += (item_prices[char] * letter_counts[char])

    return total


test_dic = {
    "Test 1: ": {"t": "AABCDA", "r": 195},
    "Test 2: ": {"t": "BBCX", "r": -1},
    "Test 3: ": {"t": "BBCDA", "r": 130},
    "Test 4: ": {"t": "DCBA", "r": 115},

            }
if __name__ == "__main__":
    for test in test_dic:
        print(f"{test} {checkout(test_dic[test]['t']) == test_dic[test]['r']}")



