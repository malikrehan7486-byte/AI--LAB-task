"""Stateless reflex baseline from the Lab 2 classroom example."""


def target_mode(temp, occupied):
    if not occupied:
        return "ECO"
    if temp > 26:
        return "COOL"
    if temp < 20:
        return "WARM"
    return "IDLE"


if __name__ == "__main__":
    for percept in [(29, True), (24, True), (29, False)]:
        print(percept, target_mode(*percept))
