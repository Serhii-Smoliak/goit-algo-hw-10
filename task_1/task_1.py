from pulp import *

limonad = LpVariable("Лимонад", lowBound=0, cat='Integer')
frukt_sik = LpVariable("Фруктовий_сік", lowBound=0, cat='Integer')

model = LpProblem("Оптимізація_виробництва", LpMaximize)

model += 2 * limonad + frukt_sik <= 100
model += limonad + frukt_sik <= 50
model += limonad <= 30
model += 2 * frukt_sik <= 40

model += limonad + frukt_sik

solver = pulp.PULP_CBC_CMD(msg=False)
model.solve(solver)

print(f"Загальна кількість продуктів: {limonad.varValue + frukt_sik.varValue}")
print("а саме:")
print("Лимонаду: ", limonad.varValue)
print("Фруктового соку: ", frukt_sik.varValue)
