from tabulate import tabulate

def calculations_5_year(mat, year):
    earn = year * mat[1]
    waste = year * mat[3]
    win = earn * mat[2] + waste * mat[4] - mat[0]
    result = [earn, waste, win]
    return result

def calculations_4_year(mat1, mat2, year):
    earn = year * mat1[1]
    waste = year * mat1[3]
    win = earn * mat2[2] + waste * mat2[3] - mat1[0]
    result = [earn, waste, win]
    return result

def show_res(mat1, mat2, year):
    mat1.insert(0, "Великий завод")
    mat2.insert(0, "Малий завод")
    header = ["План", 'M', 'D1', 'P1', 'D2', 'P2',
              "Дохід за " + str(year) + " Років",
                      "Витрати за " + str(year) + " Років",
                      "Виграш за " + str(year) + " Років"]
    table = [mat1, mat2]
    show = tabulate(table, headers=header, tablefmt='fancy_grid', showindex=range(1, len(table)+1))
    print(show)

file = open("lab 2.txt", "r")

A = file.readline()
B = file.readline()
C = file.readline()

file.close()

A = [float(i) for i in A.split(' ')]
B = [float(i) for i in B.split(' ')]
C = [float(i) for i in C.split(' ')]

A_res_5 = calculations_5_year(A, 5)
B_res_5 = calculations_5_year(B, 5)

to_table_A5 = A + A_res_5
to_table_B5 = B + B_res_5
print("Обчислення для стратегії А і B:")
show_res(to_table_A5, to_table_B5, 5)

A_res_4 = calculations_4_year(A, C, 4)
B_res_4 = calculations_4_year(B, C, 4)

to_table_A4 = [A[0], A[1], C[2], A[3], C[3]] + A_res_4
to_table_B4 = [B[0], B[1], C[2], B[3], C[3]] + B_res_4
print("Обчислення для стратегії C:")
show_res(to_table_A4, to_table_B4, 4)

win_AB_4 = max([A_res_4[-1], B_res_4[-1]])

win_C1_4 = C[0] * win_AB_4
win_C2_4 = C[1] * 0
win_C_5 = max([win_C1_4, win_C2_4])

data_C = [[C[0], C[1], A_res_4[2], B_res_4[2], win_C1_4, win_C2_4, win_C_5]]
head_C = ['P3', 'P4', 'Виграш за 4 роки А', 'Виграш за 4 роки B', 'Виграш за 5 років С1', 'Виграш за 5 років С2', 'Виграш С']
prnt_C = tabulate(data_C, headers=head_C, tablefmt='fancy_grid')
print(prnt_C)

data = [[A_res_5[-1], B_res_5[-1], win_C_5]]
res_head = ["Виграш стратегії А", "Виграш стратегії Б", "Виграш стратегії В"]
prnt = tabulate(data, headers=res_head, tablefmt='fancy_grid')
print(prnt)

win_strategy = max(data[0])

if win_strategy == A_res_5[-1]:
    print('Стратегія A виграшна:', win_strategy)
    print('Бується великий завод!')
elif win_strategy == B_res_5[-1]:
    print('Стратегія Б виграшна:', win_strategy)
    print('Бується малий завод!')
elif win_strategy == win_C_5:
    print('Стратегія В виграшна::', win_strategy)
    print('Відладається будівництво')