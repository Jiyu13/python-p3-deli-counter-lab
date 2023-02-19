katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty." )
    else:
        place = "The line is currently:"
        for i in range(len(katz_deli)):
            place += f" {i + 1}. {katz_deli[i]}"
        print(place)

def take_a_number(katz_deli, people):
    katz_deli.append(people)
    print(f"Welcome, {people}. You are number {katz_deli.index(people) + 1} in line.")


def now_serving(katz_deli):
    if len(katz_deli) != 0:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]
    else:
        print("There is nobody waiting to be served!")