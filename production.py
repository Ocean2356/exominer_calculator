from data import *

def listIngredients(compo, ingre_list=INGREDIENTS_LIST):
    ls = {}
    ls[compo.name] = 1
    if isinstance(compo, Ores):
        return ls
    for i in compo.ingredients:
        tmp = listIngredients(ingre_list[i[0]])
        for j in tmp:
            if j not in ls:
                ls[j] = 0
            ls[j] += tmp[j] * i[1]
    return ls

def countIngredients(ingre_list, cond):
    time = 0
    gain = 0
    for i in ingre_list:
        if cond(i):
            print("{}, {} * {}".format(i, INGREDIENTS_LIST[i].time, ingre_list[i]))
            time += INGREDIENTS_LIST[i].time.toInt() * ingre_list[i]
            gain += INGREDIENTS_LIST[i].addedValue.toInt() * ingre_list[i]
    return time, gain

def calcGain(prod):
    ls = listIngredients(prod)
    print("Component:")
    res_compo = countIngredients(ls, lambda x: isinstance(INGREDIENTS_LIST[x], Component))
    print("Refined:")
    res_refined = countIngredients(ls, lambda x: isinstance(INGREDIENTS_LIST[x], Refined))
    return *res_refined, *res_compo

def showGain(prod, time_refined, gain_refined, time_component, gain_component):
    print("Refined Avg Gain: {}/h, Total Time: {}".format(Value(gain_refined/time_refined*3600), Time(time_refined)))
    if time_component != 0:
        print("Component Avg Gain: {}/h, Total Time: {}".format(Value(gain_component/time_component*3600), Time(time_component)))
        print("Time Percentage: {}%".format(round(time_refined/time_component*100, 2)))

def main():
    prods = [
        "Kriptonite Alloy",
        # "Laser blaster",
        "Surface Scanner",
    ]
    # prods = {**refined, **components}
    res = {}
    for i in prods:
        print(i)
        res[i] = calcGain(INGREDIENTS_LIST[i])
        showGain(i, *res[i])
        print()
    final_compo = "Surface Scanner"
    final_refined = "Kriptonite Alloy"
    c = res[final_compo]
    r = res[final_refined]
    final_gainPerSecond = c[3]/c[2] * 2 + (c[1]/c[2] + r[1]/(c[2]-c[0])) * 2 + r[1]/r[0] * 1
    print("Final Avg Gain: {}/h".format(Value(final_gainPerSecond*3600)))
    print("Final Time: {}".format(Time(Value(b=10).toInt()/final_gainPerSecond)))

if __name__ == "__main__":
    main()