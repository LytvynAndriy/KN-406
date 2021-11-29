import tkinter as tk
from itertools import permutations

def make_button(method):
    return tk.Button(text=method, bd=5, font=('Arial', 17), bg='yellow', command=lambda : choose(method))

def choose(method):
    if method == "Метод Борда":
        frame_Borda(method)
    else:
        frame_Condorce(method)
    
def make_label_main(label):
    return tk.Label(text=label, bd=5, font=('Arial', 17), borderwidth=3, relief="solid")

def make_label_other(label, fr):
    return tk.Label(fr, text=label, bd=5, font=('Arial', 15), borderwidth=3, relief="solid")

def frame_Borda(method):
    A = method_Borda(input_matrix, 'A')
    B = method_Borda(input_matrix, 'B')
    C = method_Borda(input_matrix, 'C')
    
    window_calc = tk.Tk()
    window_calc.geometry("380x500")
    window_calc.resizable(0,0)
    window_calc.title(method)
    
    A_B_C = ["A", "B", "C"]
    res_A_B_C = [A, B, C]
    
    for i in range(0, len(A_B_C)):
        make_label_other(i+1, window_calc).grid(row=i+1, column=1, stick='wens', padx=3, pady=3)
        make_label_other(A_B_C[i], window_calc).grid(row=i+1, column=2, stick='wens', padx=3, pady=3)
        make_label_other(res_A_B_C[i], window_calc).grid(row=i+1, column=3, stick='wens', padx=3, pady=3)
    
    best = max(res_A_B_C)
    res_str = "Переможцем за методом\n Борда є кандидат " + A_B_C[res_A_B_C.index(best)] + "\nз результатом " + str(best)
    res = make_label_other(res_str, window_calc)
    res.grid(row=4, rowspan=5, column=1, columnspan=3, stick='wens', padx=3, pady=3)
    
    window_calc.grid_columnconfigure(0, minsize = 70)
    window_calc.grid_columnconfigure(1, minsize = 70)
    window_calc.grid_columnconfigure(2, minsize = 70)
    window_calc.grid_columnconfigure(3, minsize = 70)
    window_calc.grid_columnconfigure(4, minsize = 70)
    
    window_calc.grid_rowconfigure(0, minsize = 70)
    window_calc.grid_rowconfigure(1, minsize = 70)
    window_calc.grid_rowconfigure(2, minsize = 70)
    window_calc.grid_rowconfigure(3, minsize = 70)
    window_calc.grid_rowconfigure(4, minsize = 70)
    window_calc.grid_rowconfigure(5, minsize = 70)
    
    window_calc.mainloop()

def method_Borda(mat, candidate):
    Sum = 0
    for i in range(0, len(mat)):    
        for j in range(1, len(mat[i])):
            if mat[i][j] == candidate:
                if mat[i].index(candidate) == 1:
                    Sum += mat[i][0] * 2
                elif mat[i].index(candidate) == 2:
                    Sum += mat[i][0] * 1
                elif mat[i].index(candidate) == 3:
                    Sum += mat[i][0] * 0
    return Sum

def frame_Condorce(method):
    str_A_B, sum_A_B = method_Condorce(input_matrix, 'A', 'B')
    str_B_C, sum_B_C = method_Condorce(input_matrix, 'B', 'C')
    str_A_C, sum_A_C = method_Condorce(input_matrix, 'A', 'C')
    
    all_str = str_A_B + str_B_C + str_A_C
    all_digit = sum_A_B + sum_B_C + sum_A_C
    
    window_calc = tk.Tk()
    window_calc.geometry("340x500")
    window_calc.resizable(0,0)
    window_calc.title(method)
    
    for i in range(0, len(all_str)):
        make_label_other(all_str[i], window_calc).grid(row=i+1, column=1, stick='wens', padx=3, pady=3)
        make_label_other(all_digit[i], window_calc).grid(row=i+1, column=2, stick='wens', padx=3, pady=3)
    
    A_B = make_label_other(str_A_B[sum_A_B.index(max(sum_A_B))], window_calc)
    A_B.grid(row=1, rowspan=2, column=3, stick='wens', padx=3, pady=3)
    B_C = make_label_other(str_B_C[sum_B_C.index(max(sum_B_C))], window_calc)
    B_C.grid(row=3, rowspan=2, column=3, stick='wens', padx=3, pady=3)
    A_C = make_label_other(str_A_C[sum_A_C.index(max(sum_A_C))], window_calc)
    A_C.grid(row=5, rowspan=2, column=3, stick='wens', padx=3, pady=3)
    
    all_str_2d = [str_A_B[sum_A_B.index(max(sum_A_B))],
                  str_B_C[sum_B_C.index(max(sum_B_C))],
                  str_A_C[sum_A_C.index(max(sum_A_C))]]
    all_str_2d = list(permutations(all_str_2d))
    
    for i in range(0, len(all_str_2d)):
        determine_result(all_str_2d[i][0], all_str_2d[i][1], all_str_2d[i][2], window_calc)
    
    window_calc.grid_columnconfigure(0, minsize = 50)
    window_calc.grid_columnconfigure(1, minsize = 50)
    window_calc.grid_columnconfigure(2, minsize = 50)
    window_calc.grid_columnconfigure(3, minsize = 50)
    window_calc.grid_columnconfigure(4, minsize = 50)
    
    window_calc.grid_rowconfigure(0, minsize = 50)
    window_calc.grid_rowconfigure(1, minsize = 50)
    window_calc.grid_rowconfigure(2, minsize = 50)
    window_calc.grid_rowconfigure(3, minsize = 50)
    window_calc.grid_rowconfigure(4, minsize = 50)
    window_calc.grid_rowconfigure(5, minsize = 50)
    window_calc.grid_rowconfigure(6, minsize = 50)
    window_calc.grid_rowconfigure(7, minsize = 50)
    window_calc.grid_rowconfigure(8, minsize = 50)
    
    window_calc.mainloop()

def method_Condorce(mat, candidate1, candidate2):
    res1 = 0
    res2 = 0
    for i in range(0, len(mat)):
        if mat[i].index(candidate1) < mat[i].index(candidate2):
            res1 += mat[i][0]
        else:
            res2 += mat[i][0]
    res = [res1, res2]
    compare = [candidate1 + " > " + candidate2, candidate2 + " > " + candidate1]
    return compare, res

def determine_result(str1, str2, str3, fr):
    if str1[len(str1) - 1] == str2[0]:
        str1_str2 = str1 + ' > ' + str2[len(str2) - 1]
        if str1_str2[0] == str3[0] and str1_str2[len(str1_str2) - 1] == str3[len(str3) - 1]:
            make_label_other(str1_str2, fr).grid(row=7, column=1, columnspan=3, stick='wens', padx=3, pady=3)
            make_label_other('Переможцем за методом\nКондорсе є кандидат '+ str1_str2[0], fr).grid(row=8, column=1, columnspan=3, stick='wens', padx=3, pady=3)
        else:
            make_label_other('Разом ці твердження суперечливі.\nНеможливо прийняти якесь\nузгоджене рішення', fr).grid(row=7, rowspan=9, column=1, columnspan=3, stick='wens', padx=3, pady=3)

file = open('lab 3.txt', 'r')

input_matrix = []
for line in file:
        strip = line.strip()
        split = strip.split(' ')
        for i in range(0, len(split)):
            if split[i].isdigit():
                split[i] = int(split[i])
        input_matrix.append(split)
file.close()

window = tk.Tk()
window.geometry("300x550")
window.resizable(0,0)
window.title('Методи колективних рішень')

for i in range(2, 5):
    make_label_main(i-1).grid(row=1, column=i, stick='wens', padx=3, pady=3)

for i in range(2, len(input_matrix)+2):
    for j in range(2, len(input_matrix[i-3])+2):
        make_label_main(input_matrix[i-2][j-2]).grid(row=i, column=j-1, stick='wens', padx=3, pady=3)
    
make_button("Метод Борда").grid(row=len(input_matrix)+2, column=1, columnspan=4, stick='wens', padx=3, pady=3)
make_button("Метод Кондорсе").grid(row=len(input_matrix)+3, column=1, columnspan=4, stick='wens', padx=3, pady=3)

window.grid_columnconfigure(0, minsize = 50)
window.grid_columnconfigure(1, minsize = 50)
window.grid_columnconfigure(2, minsize = 50)
window.grid_columnconfigure(3, minsize = 50)
window.grid_columnconfigure(4, minsize = 50)
window.grid_columnconfigure(5, minsize = 50)

window.grid_rowconfigure(0, minsize = 50)
window.grid_rowconfigure(1, minsize = 50)
window.grid_rowconfigure(2, minsize = 50)
window.grid_rowconfigure(3, minsize = 50)
window.grid_rowconfigure(4, minsize = 50)
window.grid_rowconfigure(5, minsize = 50)
window.grid_rowconfigure(6, minsize = 50)
window.grid_rowconfigure(7, minsize = 50)
window.grid_rowconfigure(8, minsize = 50)

window.mainloop()