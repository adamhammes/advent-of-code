from day21 import *

SAMPLE_1 = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


def test_parse_input():
    recipes = parse_input(SAMPLE_1)

    assert len(recipes) == 4

    assert recipes[("mxmxvkd", "kfcds", "sqjhc", "nhms")] == ("dairy", "fish")
