from model import *

NB_REFINE = 4
NB_COMPONENT = 3

FINAL_REFINED = "Coreium Alloy"
# FINAL_REFINED = "Kriptonite Alloy"
# FINAL_COMPO = "Surface Scanner"
FINAL_COMPONENT = "Planet Dust Collector"


ORES = {
    "Carbon": Ores("Carbon", 1),
    "Tin": Ores("Tin", 2),
    "Cobalt": Ores("Cobalt", 4),
    "Bismuth": Ores("Bismuth", 8),
    "Cerussite": Ores("Cerussite", 16),
    "Manganese": Ores("Manganese", 36),
    "Einherjer": Ores("Einherjer", 75),
    "Dark Matter": Ores("Dark Matter", 160),
    "Kriptonite": Ores("Kriptonite", 340),
    "Coreium": Ores("Coreium", 730),
}

refined_values = {
    "Refined Carbon": Value(k=1.67),
    "Refined Tin": Value(k=3.45),
    "Refined Cobalt": Value(k=7.01),
    "Refined Bismuth": Value(k=14.37),
    "Refined Cerussite": Value(k=31.74),
    "Refined Manganese": Value(k=69),
    "Refined Einherjer": Value(k=138),
    "Manganese Alloy": Value(k=269.1),
    "Cobalt Alloy": Value(k=391),
    "Kriptonite Alloy": Value(k=897),
    "Coreium Alloy": Value(m=1.87),
}

refined_ingredients = {
    "Refined Carbon": ([("Carbon", 1000)], Time(s=16)),
    "Refined Tin": ([("Tin", 1000)], Time(s=24)),
    "Refined Cobalt": ([("Cobalt", 1000)], Time(s=32)),
    "Refined Bismuth": ([("Bismuth", 1000)], Time(s=48)),
    "Refined Cerussite": ([("Cerussite", 1000)], Time(s=64)),
    "Refined Manganese": ([("Manganese", 1000)], Time(s=96)),
    "Refined Einherjer": ([("Einherjer", 1000)], Time(s=144)),
    "Manganese Alloy": ([("Refined Manganese", 2), ("Refined Carbon", 10)], Time(s=192)),
    "Cobalt Alloy": ([("Refined Cobalt", 15), ("Refined Carbon", 30)], Time(s=384)),
    "Kriptonite Alloy": ([("Refined Einherjer", 2), ("Kriptonite", 1000)], Time(s=480)),
    "Coreium Alloy": ([("Manganese Alloy", 2), ("Coreium", 1000)], Time(s=576)),
}

REFINED = {}
for i in refined_ingredients.keys():
    REFINED[i] = Refined(i, refined_values[i], refined_ingredients[i][0], refined_ingredients[i][1])

component_values = {
    "Cables": Value(k=11.5),
    "Fuse": Value(k=23),
    "Heat sensor": Value(k=80.5),
    "Ball bearing": Value(k=155.25),
    "Glass": Value(k=241.5),
    "Circuit": Value(k=690),
    "Lense": Value(m=1.15),
    "Laser Optic": Value(m=3.45),
    "Mini rover": Value(m=8.62),
    "Solar Panel": Value(m=14.37),
    "Laser blaster": Value(m=34.5),
    "Advanced Sensors": Value(m=40.25),
    "Surface Scanner": Value(m=82.22),
    "Planet Explorer": Value(m=207),
    "Planet Dust Collector": Value(b=1.10),
}

component_ingredients = {
    "Cables": ([("Refined Carbon", 5)], Time(s=48)),
    "Fuse": ([("Refined Tin", 5)], Time(s=96)),
    "Heat sensor": ([("Cables", 2), ("Refined Carbon", 10)], Time(s=192)),
    "Ball bearing": ([("Fuse", 2), ("Refined Cobalt", 5)], Time(s=384)),
    "Glass": ([("Refined Bismuth", 10)], Time(s=576)),
    "Circuit": ([("Refined Cerussite", 5), ("Refined Bismuth", 5), ("Cables", 10)], Time(s=960)),
    "Lense": ([("Glass", 1), ("Refined Manganese", 5)], Time(m=32)),
    "Laser Optic": ([("Refined Einherjer", 5), ("Refined Tin", 10), ("Lense", 1)], Time(m=48)),
    "Mini rover": ([("Refined Manganese", 5), ("Circuit", 5), ("Ball bearing", 4)], Time(m=64)),
    "Solar Panel": ([("Circuit", 5), ("Glass", 10)], Time(m=80)),
    "Laser blaster": ([("Manganese Alloy", 5), ("Laser Optic", 2), ("Lense", 5)], Time(m=96)),
    "Advanced Sensors": ([("Cobalt Alloy", 20), ("Heat sensor", 30)], Time(h=2)),
    "Surface Scanner": ([("Kriptonite Alloy", 5), ("Laser Optic", 2), ("Glass", 5)], Time(h=2, m=24)),
    "Planet Explorer": ([("Coreium Alloy", 5), ("Mini rover", 5)], Time(h=2, m=48)),
    "Planet Dust Collector": ([("Laser blaster", 2), ("Surface Scanner", 1), ("Manganese Alloy", 10)], Time(h=3)),
}

COMPONENTS = {}
for i in component_ingredients.keys():
    COMPONENTS[i] = Component(i, component_values[i], component_ingredients[i][0], component_ingredients[i][1])

INGREDIENTS_LIST = {**ORES, **REFINED, **COMPONENTS}

def calcAddedValue(ingre_list, prod_list):
    for i in prod_list:
        sum = 0
        for j in prod_list[i].ingredients:
            try:
                sum += ingre_list[j[0]].value * j[1]
            except:
                sum += ingre_list[j[0]].value.toInt() * j[1]
        prod_list[i].addedValue = Value(prod_list[i].value.toInt() - sum)
        prod_list[i].gainPerHour = Value(prod_list[i].addedValue.toInt() / prod_list[i].time.toInt() * 3600)

calcAddedValue(INGREDIENTS_LIST, REFINED)
calcAddedValue(INGREDIENTS_LIST, COMPONENTS)