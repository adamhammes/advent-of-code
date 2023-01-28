import collections
import re
from typing import *

import lib

WORD = re.compile("[a-z]+")

Ingredient = str
Allergen = str

Recipes = Dict[Tuple[Ingredient, ...], Tuple[Allergen, ...]]
PossibleAllergens = Dict[Allergen, Set[Ingredient]]


def parse_input(raw: str) -> Recipes:
    recipes = {}
    for line in raw.strip().splitlines():
        raw_ingredients, raw_allergens = line.split("contains")
        ingredients = tuple(WORD.findall(raw_ingredients))
        allergens = tuple(WORD.findall(raw_allergens))

        recipes[ingredients] = allergens

    return recipes


def could_be(recipes: Recipes) -> PossibleAllergens:
    allergens_to_recipes: Dict[
        Allergen, List[Set[Ingredient, ...]]
    ] = collections.defaultdict(list)

    for ingredients, allergens in recipes.items():
        for allergen in allergens:
            allergens_to_recipes[allergen].append(set(ingredients))

    pruned: Dict[Allergen, Set[Ingredient]] = {}
    for allergen, ingredient_sets in allergens_to_recipes.items():
        pruned[allergen] = set.intersection(*ingredient_sets)

    return pruned


def solve(recipes: Recipes) -> List[Tuple[Allergen, Ingredient]]:
    possible_allergens = could_be(recipes)

    found_allergens: List[Tuple[Allergen, Ingredient]] = []
    while possible_allergens:
        new_known_allergens = [
            allergen
            for allergen, ingredients in possible_allergens.items()
            if len(ingredients) == 1
        ]
        for allergen in new_known_allergens:
            allergic_ingredient = lib.first(possible_allergens[allergen])
            found_allergens.append((allergen, allergic_ingredient))

            for other_allergen in possible_allergens:
                possible_allergens[other_allergen].discard(allergic_ingredient)

            possible_allergens.pop(allergen)

    return found_allergens


def part_1(raw: str):
    recipes = parse_input(raw)
    found_allergens = solve(recipes)

    found_allergens = list(sorted(found_allergens))
    all_ingredients = set(
        ingredient for ingredients in recipes for ingredient in ingredients
    )
    allergic_ingredients = set(ingredient for _, ingredient in found_allergens)

    non_allergic_ingredients = all_ingredients - allergic_ingredients

    count = 0
    for ingredient_list in recipes:
        count += len(non_allergic_ingredients.intersection(ingredient_list))

    return count


def part_2(raw: str):
    recipes = parse_input(raw)
    found_allergens = solve(recipes)
    return ",".join(ingredient for allergen, ingredient in found_allergens)


if __name__ == "__main__":
    print(part_1(lib.get_input(21)))
    print(part_2(lib.get_input(21)))
