salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


need_money = 0  # количество денег, чтобы прожить 10 месяцев

sum_spend = spend
for i in range(2, months + 1):
     spend = spend * 1.03
     sum_spend = sum_spend + spend

need_money = ((sum_spend - salary * months) / 1)

print(round(need_money))
