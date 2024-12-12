type point = tuple[int, int]

with open("input") as f:
    garden = [list(l.strip()) for l in f.readlines()]

leny = len(garden) - 1
lenx = len(garden[0]) - 1
patches: list[tuple[set[point], tuple[point]]] = []


def in_patch(plant: point) -> bool:
    for patch in patches:
        if plant in patch[0]:
            return True
    return False


def get_bordering(plant: point) -> tuple[tuple[point, tuple[point]]]:
    i = plant[0]
    j = plant[1]
    plant_type = garden[i][j]
    plants = []
    fences = []
    # intentional that fences includes negative numbers
    (plants if i > 0 and garden[i - 1][j] == plant_type else fences).append((i - 1, j))
    (plants if j > 0 and garden[i][j - 1] == plant_type else fences).append((i, j - 1))
    (plants if i < leny and garden[i + 1][j] == plant_type else fences).append((i + 1, j))
    (plants if j < lenx and garden[i][j + 1] == plant_type else fences).append((i, j + 1))
    return plants, fences


def explore_patch(plant: point) -> tuple[tuple[point], tuple[point]]:
    to_visit = [plant]
    plants: set[point] = set()
    fences: list[point] = []
    while len(to_visit) > 0:
        focus = to_visit.pop()
        plants.add(focus)
        new_plants, new_fences = get_bordering(focus)
        for new_plant in new_plants:
            if new_plant in to_visit or new_plant in plants:
                continue
            to_visit.append(new_plant)
        fences.extend(new_fences)
    return plants, fences


for i, row in enumerate(garden):
    for j, plant_type in enumerate(row):
        plant: point = (i, j)
        if in_patch(plant):
            continue
        patches.append(explore_patch(plant))


# for patch in patches:
#     print(len(patch[0]), len(patch[1]))

print(sum(map(lambda x: len(x[0]) * len(x[1]), patches)))
