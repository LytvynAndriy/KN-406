import numpy as np
from tabulate import tabulate
from pulp import LpVariable, LpProblem, LpMinimize, value, LpMaximize 
  
def show_table(data, head):
    show = tabulate(data, headers=head, tablefmt='fancy_grid', numalign='center')
    print(show)

def simplex(matrix, x_y):
    variables = []
    for i in range(0, len(matrix)):
        variables.append(LpVariable(x_y + str(i + 1), lowBound=0))
    
    function = ''    
    if x_y == "x":
        print("Система рівнянь для стратегії А: ")
        problem = LpProblem("Система рівнянь", LpMinimize)  
        for i in range(0, len(matrix)):
            changed = sum(matrix[i] * variables) >= 1
            print(changed)
            problem += changed
        function = sum(variables)
        print("Функція:")
        print("F(%s) = %s --> MIN" %(x_y, function))
    else:
        print("Система рівнянь для стратегії B: ")
        problem = LpProblem("Система рівнянь", LpMaximize)     
        for i in range(0, len(matrix)):
            changed = sum(matrix[i] * variables) <= 1
            print(changed)
            problem += changed
        function = sum(variables)
        print("Функція:")
        print("F(%s) = %s --> MAX" %(x_y, function))
    
    problem += function       
        
    problem.solve()
    res = []
    for variable in problem.variables():
        res.append(variable.varValue)
    F = value(problem.objective)        
    return res, F, variables
   
def Game_price_and_probability(res_x_y):
    V = 1 / sum(res_x_y)
    probability = []
    for element in res_x_y:
        probability.append(element * V)
    return V, probability

matrix = np.loadtxt("lab 5.txt", dtype=int)

matrix_list = matrix.tolist()
header = []
for i in range(0, len(matrix_list)):
    matrix_list[i].insert(0, "A" + str(i+1))
    header.append("B" + str(i+1))
header.insert(0, "Гравці")

print("Платіжна матриця:")
show_table(matrix_list, header)

transpose_matrix = np.transpose(matrix)
    
res_for_x, Function_x, head_x = simplex(transpose_matrix, "x")
head_x.append("F(x)")
print("Розв'язки для гравця A:")
show_table([res_for_x + [Function_x]], head_x)

res_for_y, Function_y, head_y = simplex(matrix, "y")
head_y.append("F(y)")
print("Розв'язки для гравця B:")
show_table([res_for_y + [Function_y]], head_y)

Price_X, p_x = Game_price_and_probability(res_for_x)
head_p = []
for i in range(0, len(p_x)):
    head_p.append("p" + str(i+1))
head_p.append("Ціна гри")
print("Ціна гри і ймовірності застосування стратегій для гравця А:")
show_table([p_x + [Price_X]], head_p)

Price_Y, p_y = Game_price_and_probability(res_for_y)
head_q = []
for i in range(0, len(p_y)):
    head_q.append("q" + str(i+1))
head_q.append("Ціна гри")
print("Ціна гри і ймовірності застосування стратегій для гравця B:")
show_table([p_y + [Price_Y]], head_q)
