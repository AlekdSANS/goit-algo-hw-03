import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < min or quantity > (max - min + 1):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers: ", lottery_numbers)

print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 49, 50))