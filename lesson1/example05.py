Profit=int(input("Прибыль фирмы: "))
Costs=int(input("Расход фирмы: "))
if Profit > Costs:
    print("У фирмы прибыль: ", Profit - Costs, "руб.")
elif Profit == Costs:
    print("Фирма работает в 0")
else:
    print("Фирма уходит в убыток на", Costs- Profit, "руб.")