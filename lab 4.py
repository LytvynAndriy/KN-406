import numpy as np
from tabulate import tabulate

def show_table(rait, head):
    show = tabulate(rait, headers=head, tablefmt='fancy_grid', 
                numalign='center', showindex=range(1,len(rait)+1))
    print(show)

def calculations(rait, imp, sub, sur):
    imp = np.reshape(imp, (len(imp), 1))
    imp__rait = rait * imp
    imp__rait = np.round(imp__rait, 3)
    
    sum_imp__rait = np.sum(imp__rait, axis=0)
    max_sum = max(sum_imp__rait)
    index = sum_imp__rait.tolist().index(max_sum)
    best_surname = sur[index]
    
    sur.insert(0, "Ваги")
    sur.insert(0, "Предмети")
    
    imp__rait = imp__rait.tolist()
    ctr = 0
    for el in imp__rait:
        el.insert(0, imp[ctr])
        el.insert(0, sub[ctr])
        ctr +=1
    sum_imp__rait = sum_imp__rait.tolist()
    sum_imp__rait.insert(0,sum(imp))
    sum_imp__rait.insert(0, "Сума")
    
    imp__rait.append(sum_imp__rait)
    
    print("Результати: ")
    show_table(imp__rait, sur)  
    print()
    print("В результаті оцінки було вибрано кращого студента - %s з оцінкою %.2f"
          %(best_surname , max_sum))

subject = []
file_sub = open('subject.txt', 'r', encoding="utf-8")
for line in file_sub:
    subject.append(line[:-1])
file_sub.close()

surnames = []
file_sur = open('surnames.txt', 'r', encoding="utf-8")
for line in file_sur:
    surnames.append(line[:-1])
file_sur.close()

importance = []
file_imp = open('importances.txt', 'r', encoding="utf-8")
for line in file_imp:
    importance.append(float(line[:-1]))
file_imp.close()

file_raiting = np.loadtxt("raiting.txt", dtype=int)

print("Вхідна таблиця: ")
input_table = file_raiting.tolist()
for i in range(0, len(input_table)):
    input_table[i].insert(0, subject[i])
show_table(input_table, surnames)

calculations(file_raiting, importance, subject, surnames)