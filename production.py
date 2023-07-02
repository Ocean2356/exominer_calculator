from data import *

def listIngredients(compo):
    ls = {}
    ls[compo.name] = 1
    if isinstance(compo, Ores):
        return ls
    for i in compo.ingredients:
        tmp = listIngredients(INGREDIENTS_LIST[i[0]])
        for j in tmp:
            if j not in ls:
                ls[j] = 0
            ls[j] += tmp[j] * i[1]
    return ls

def countIngredients(ingre_list, prod_list):
    time = 0
    gain = 0
    for i in prod_list:
        if i in ingre_list:
            print("{}, {} * {}".format(i, INGREDIENTS_LIST[i].time, ingre_list[i]))
            time += INGREDIENTS_LIST[i].time.toInt() * ingre_list[i]
            gain += INGREDIENTS_LIST[i].addedValue.toInt() * ingre_list[i]
    return time, gain

def calcGain(prod):
    ls = listIngredients(prod)
    print("Refined:")
    res_refined = countIngredients(ls, REFINED)
    print("Component:")
    res_compo = countIngredients(ls, COMPONENTS)
    return *res_refined, *res_compo

def showGain(prod, time_refined, gain_refined, time_component, gain_component):
    print("Avg:")
    print("Refined Avg Gain: {}/h, Total Time: {}".format(Value(gain_refined/time_refined*3600), Time(time_refined)))
    if time_component != 0:
        print("Component Avg Gain: {}/h, Total Time: {}".format(Value(gain_component/time_component*3600), Time(time_component)))
        print("Time Percentage: {}%".format(round(time_refined/time_component*100, 2)))

def main():
    prods = [
        FINAL_COMPONENT,
        FINAL_REFINED,
    ]
    # prods = {**refined, **components}
    res = {}
    for i in prods:
        print(i)
        res[i] = calcGain(INGREDIENTS_LIST[i])
        showGain(i, *res[i])
        print()
    c = res[FINAL_COMPONENT]
    r = res[FINAL_REFINED]
    final_gainPerSecond = c[3]/c[2] * NB_COMPONENT + (c[1]/c[2] + r[1]/(c[2]-c[0])) * NB_COMPONENT + r[1]/r[0] * (NB_REFINE - NB_COMPONENT)
    print("Final Avg Gain: {}/h".format(Value(final_gainPerSecond*3600)))
    print("Final Time: {}".format(Time(Value(b=10).toInt()/final_gainPerSecond)))

if __name__ == "__main__":
    main()