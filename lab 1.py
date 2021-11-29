import tkinter as tk
import numpy as np

def make_button(method, mat, res, index):
    return tk.Button(text=method, bd=5, font=('Arial', 15), bg='yellow', command=lambda : Frame(method, mat, res, index))

def make_label(label, fr):
    return tk.Label(fr, text=label, bd=5, font=('Arial', 17), borderwidth=3, relief="solid")

def choose(method):
    res_mat = []
    if method == "Метод Вальда:":
        res_mat = Wald(input_matrix)
        Frame(method, res_mat)

def Frame(method, mat, res, index):
    wind = tk.Tk()
    wind.geometry("540x500")
    wind.resizable(0,0)
    wind.title(method)
    
    make_label("A1", wind).grid(row=1, column=1, stick='wens', padx=3, pady=3)
    make_label("A2", wind).grid(row=1, column=2, stick='wens', padx=3, pady=3)
    make_label("A3", wind).grid(row=1, column=3, stick='wens', padx=3, pady=3)
    
    ctr_row = 0
    for i in range(2,5):
        ctr_col = 0
        for j in range(1,4):
            make_label(input_matrix[ctr_row][ctr_col], wind).grid(row=i, column=j, stick='wens', padx=3, pady=3)
            ctr_col += 1
        ctr_row += 1
    
    make_label(method, wind).grid(row=1, column=4, columnspan=6, stick='wens', padx=3, pady=3)
    
    for i in range(0, len(mat)):
        make_label(mat[i], wind).grid(row=i+2, column=4, columnspan=6, stick='wens', padx=3, pady=3)
    
    str_res1 = "Для цього методу максимальне\n значення: " + str(res)
    str_res2 = "Це стратегія під номером: " + str(index)
    str_res = str_res1 + "\n" + str_res2
    make_label(str_res, wind).grid(row=6, column=1, columnspan=6, stick='wens', padx=3, pady=3)
    
    wind.grid_columnconfigure(0, minsize = 60)
    wind.grid_columnconfigure(1, minsize = 60)    
    wind.grid_columnconfigure(2, minsize = 60)
    wind.grid_columnconfigure(3, minsize = 60)
    wind.grid_columnconfigure(4, minsize = 50)
    wind.grid_columnconfigure(5, minsize = 100)
    wind.grid_columnconfigure(6, minsize = 100)
    
    wind.grid_rowconfigure(0, minsize = 60)
    wind.grid_rowconfigure(1, minsize = 60)
    wind.grid_rowconfigure(2, minsize = 60)
    wind.grid_rowconfigure(3, minsize = 60)
    wind.grid_rowconfigure(4, minsize = 60)
    wind.grid_rowconfigure(5, minsize = 60)
    wind.grid_rowconfigure(6, minsize = 60)
    wind.grid_rowconfigure(7, minsize = 60)
    wind.grid_rowconfigure(8, minsize = 60)
    
    wind.mainloop()
    
def Wald(matrix):
    minimum = []
    for el in matrix:
        minimum.append(min(el))  
    return minimum    

def Max(matrix):
    maximum = []
    for el in matrix:
        maximum.append(max(el))    
    return maximum

def Laplace(matrix):
    result = []
    for el in matrix:
        result.append(sum(el) / 3)
    return result

def Hurwitz(matrix):
    y = 0.25
    result = []
    for el in matrix:
        result.append(y * min(el) + (1 - y) * max(el))
    return result

def Bayes_Laplace(matrix):
    p = np.array([0.5, 0.35, 0.15])
    result = []
    for el in matrix:
        result.append(sum(el * p))
    return result

window = tk.Tk()
window.geometry("360x442")
window.resizable(0,0)
window.title('Прийняття рішення в умовах не визначеності')

input_matrix = np.loadtxt("lab 1.txt", dtype=int)

res_Wald = Wald(input_matrix)
m_Wald = max(res_Wald)
i_Wald = res_Wald.index(m_Wald) + 1
o_Wald = res_Wald.index(m_Wald, i_Wald, len(res_Wald)) + 1
_Wald = str(i_Wald) + " i " + str(o_Wald)

res_Max = Max(input_matrix)
m_Max = max(res_Max)
i_Max = res_Max.index(m_Max) + 1
res_Laplace = Laplace(input_matrix)
m_Laplace = max(res_Laplace)
i_Laplace = res_Laplace.index(m_Laplace) + 1
res_Hurwitz = Hurwitz(input_matrix)
m_Hurwitz = max(res_Hurwitz)
i_Hurwitz = res_Hurwitz.index(m_Hurwitz) + 1
res_Bayes_Laplace = Bayes_Laplace(input_matrix)
m_Bayes_Laplace = max(res_Bayes_Laplace)
i_Bayes_Laplace = res_Bayes_Laplace.index(m_Bayes_Laplace) + 1        

make_button("Метод Вальда", res_Wald, m_Wald, _Wald).grid(row=1, column=1, columnspan=3, stick='wens', padx=3, pady=3)
make_button("Метод Максимуму",res_Max, m_Max, i_Max).grid(row=2, column=1, columnspan=3, stick='wens', padx=3, pady=3)
make_button("Метод Гурвіца", res_Hurwitz, m_Hurwitz, i_Hurwitz).grid(row=3, column=1, columnspan=3, stick='wens', padx=3, pady=3)
make_button("Метод Лапласа", res_Laplace, m_Laplace, i_Laplace).grid(row=4, column=1, columnspan=3, stick='wens', padx=3, pady=3)
make_button("Метод Байеса-Лапласа",res_Bayes_Laplace, m_Bayes_Laplace, i_Bayes_Laplace).grid(row=5, column=1, columnspan=3, stick='wens', padx=3, pady=3)

window.grid_columnconfigure(0, minsize = 60)
window.grid_columnconfigure(1, minsize = 60)
window.grid_columnconfigure(2, minsize = 60)
window.grid_columnconfigure(3, minsize = 60)

window.grid_rowconfigure(0, minsize = 60)
window.grid_rowconfigure(1, minsize = 60)
window.grid_rowconfigure(2, minsize = 60)
window.grid_rowconfigure(3, minsize = 60)
window.grid_rowconfigure(4, minsize = 60)
window.grid_rowconfigure(5, minsize = 60)
window.grid_rowconfigure(6, minsize = 60)

window.mainloop()