# Iterative
house = ["Raymund's house", "Mela's house", "Dokie's house"]


def deliver_presents(houses):
    for house in houses:
        print(f"Delivering presents to {house}")


# deliver_presents(house)

# Recursive (Quicksort)


def deliver_presents_recursively(houses):
    if len(houses) == 1:
        house = houses[0]
        print(f"Delivering presents to {house}")
    else:
        mid = len(houses) // 2
        lower_half = houses[:mid]
        upper_half = houses[mid:]
        deliver_presents_recursively(upper_half)
        # deliver_presents_recursively(mid)
        deliver_presents_recursively(lower_half)


houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]
deliver_presents_recursively(houses)
