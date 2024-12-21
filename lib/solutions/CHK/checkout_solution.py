

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = ["A", "B", "C", "D"]
    item_prices = {"A": 50 , "B":30, "C": 20, "D": 15}
    special_prices = {"A": {"n": 3, "p": 130}, "B": {"n": 2, "p": 45}}

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
    for char in items:
        # check if special price
        if char in special_prices.keys():
            





