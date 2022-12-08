from tkinter import *
#Создаём главное окно
root = Tk()

#Задаём надпись, цвет и режим запуска
root.title("Матричный калькулятор")
root["bg"] = "gray15"
root.state('zoomed')
root.resizable(width=False, height=False)

#Функция для закрытия главного окна
def Exit():
    root.destroy()

#Функция вычитания двух матриц
def subtraction():
    #Создаём окно операции вычитания
    #Создаём кнопки, надписи и фунцкиона для них
    root1 = Tk()
    root1.title("Вычитание матриц")
    root1["bg"] = "gray15"
    root1.state('zoomed')
    root1.resizable(width=False, height=False)

    Frame(root1, height=20, bg="gray15").grid(row=0, column=0)
    Label(root1, text="Вычитание двух матриц", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=1, column=4)
    Frame(root1, height=140, bg="gray15").grid(row=2, column=0)
    Label(root1, text="Матрица А", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=W)
    Label(root1, text="Матрица В", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=E)
    Frame(root1, width=40, bg="gray15").grid(row=4, column=0)

    #Переменнык(поля ввода)
    a11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a11.grid(row=4, column=1)
    a12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a12.grid(row=4, column=2)
    a13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a13.grid(row=4, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=4, column=4)
    b11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b11.grid(row=4, column=5)
    b12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b12.grid(row=4, column=6)
    b13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b13.grid(row=4, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=4, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=5, column=0)
    a21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a21.grid(row=5, column=1)
    a22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a22.grid(row=5, column=2)
    a23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a23.grid(row=5, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=5, column=4)

    b21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b21.grid(row=5, column=5)
    b22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b22.grid(row=5, column=6)
    b23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b23.grid(row=5, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=5, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=6, column=0)
    a31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a31.grid(row=6, column=1)
    a32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a32.grid(row=6, column=2)
    a33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a33.grid(row=6, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=6, column=4)
    b31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b31.grid(row=6, column=5)
    b32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b32.grid(row=6, column=6)
    b33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b33.grid(row=6, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=6, column=8)
    Frame(root1, height=150, bg="gray15").grid(columnspan=9)

    #Фунцкия для подсчёта разности
    def suball(event):
        #Обработка исключений на случай, если поля ввода будут заполнены некорректно
        try:
            #Вычитаем элементы друг из друга и записываем результат в переменную
            c11 = int(a11.get()) - int(b11.get())
            c12 = int(a12.get()) - int(b12.get())
            c13 = int(a13.get()) - int(b13.get())
            c21 = int(a21.get()) - int(b21.get())
            c22 = int(a22.get()) - int(b22.get())
            c23 = int(a23.get()) - int(b23.get())
            c31 = int(a31.get()) - int(b31.get())
            c32 = int(a32.get()) - int(b32.get())
            c33 = int(a33.get()) - int(b33.get())
            root2 = Tk()
            root2.title("Результат")
            root2["bg"] = "gray15"
            root2.state('zoomed')
            root2.resizable(width=False, height=False)
            Frame(root2, height=20, bg="gray15").grid(row=0, column=0)
            Label(root2, text="Результат вычитания двух матриц", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=4)
            Frame(root2, height=100, bg="gray15").grid(columnspan=4)
            Label(root2, text="Матрица C", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=3)
            Label(root2, text=c11, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=0)
            Label(root2, text=c12, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=1)
            Label(root2, text=c13, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=2)
            Label(root2, text=c21, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=0)
            Label(root2, text=c22, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=1)
            Label(root2, text=c23, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=2)
            Label(root2, text=c31, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=0)
            Label(root2, text=c32, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=1)
            Label(root2, text=c33, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=2)
            Frame(root2, height=150, bg="gray15").grid(columnspan=4)

            #Функция выхода из окна операции вычитания
            def exit():
                root2.destroy()
                return 0
            #Кнопка выхода
            Button(root2, text="Понял, принял!", font=("Bebas Neue Cyrillic", 20), width=30, height=1, fg='gray15', bg='white', command=exit).grid(columnspan=3)
            root2.mainloop()
        except:
            return 0
    #Кнопка выхода
    buttonsum = Button(root1, text='Вычесть матрицы', font=("Bebas Neue Cyrillic", 20), width=50, height=1, fg='gray15',  bg='white')
    buttonsum.bind("<Button-1>", suball)
    buttonsum.grid(columnspan=9)
    Frame(root1, height=100, bg="gray15").grid(columnspan=4)

    #Функция закрытия окна операции вычитания
    def back():
        root1.destroy()
        return 0
    Button(root1, text='Назад', font=("Bebas Neue Cyrillic", 16), width=30, height=1, fg='gray15', bg='white', command=back).grid(columnspan=9)
    root1.mainloop()

#Функция сложения двух матриц
def sum():
    #Создаём окно для операции сложения
    #Задаём цвет, название, надписи и кнопки
    root1 = Tk()
    root1.title("Сложение матриц")
    root1["bg"] = "gray15"
    root1.state('zoomed')
    root1.resizable(width=False, height=False)

    Frame(root1, height=20, bg="gray15").grid(row=0, column=0)
    Label(root1, text="Сложение двух матриц", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=1, column=4)
    Frame(root1, height=140, bg="gray15").grid(row=2, column=0)
    Label(root1, text="Матрица А", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=W)
    Label(root1, text="Матрица В", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=E)
    Frame(root1, width=40, bg="gray15").grid(row=4, column=0)

    #Каждая переменная является полем ввода
    a11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a11.grid(row=4, column=1)
    a12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a12.grid(row=4, column=2)
    a13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a13.grid(row=4, column=3)
    Frame(root1, width=750, bg="gray15").grid(row=4, column=4)

    b11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b11.grid(row=4, column=5)
    b12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b12.grid(row=4, column=6)
    b13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b13.grid(row=4, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=4, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=5, column=0)
    a21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a21.grid(row=5, column=1)
    a22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a22.grid(row=5, column=2)
    a23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a23.grid(row=5, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=5, column=4)
    b21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b21.grid(row=5, column=5)
    b22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b22.grid(row=5, column=6)
    b23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b23.grid(row=5, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=5, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=6, column=0)
    a31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a31.grid(row=6, column=1)
    a32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a32.grid(row=6, column=2)
    a33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a33.grid(row=6, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=6, column=4)
    b31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b31.grid(row=6, column=5)
    b32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b32.grid(row=6, column=6)
    b33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b33.grid(row=6, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=6, column=8)
    Frame(root1, height=150, bg="gray15").grid(columnspan=9)

    #Фунцкия для вычисления суммы элементов матрицы
    def sumall(event):
        #Обработка исключений для того, чтобы не возникало ошибок, если поля не заполнены или заполнены некорректно
        try:
            c11 = int(a11.get()) + int(b11.get())
            c12 = int(a12.get()) + int(b12.get())
            c13 = int(a13.get()) + int(b13.get())
            c21 = int(a21.get()) + int(b21.get())
            c22 = int(a22.get()) + int(b22.get())
            c23 = int(a23.get()) + int(b23.get())
            c31 = int(a31.get()) + int(b31.get())
            c32 = int(a32.get()) + int(b32.get())
            c33 = int(a33.get()) + int(b33.get())
            root2 = Tk()
            root2.title("Результат")
            root2["bg"] = "gray15"
            root2.state('zoomed')
            root2.resizable(width=False, height=False)
            Frame(root2, height=20, bg="gray15").grid(row=0, column=0)
            Label(root2, text="Результат сложения двух матриц", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=4)
            Frame(root2, height=100, bg="gray15").grid(columnspan=4)
            Label(root2, text="Матрица C", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=3)
            Label(root2, text=c11, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=0)
            Label(root2, text=c12, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=1)
            Label(root2, text=c13, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=2)
            Label(root2, text=c21, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=0)
            Label(root2, text=c22, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=1)
            Label(root2, text=c23, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=2)
            Label(root2, text=c31, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=0)
            Label(root2, text=c32, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=1)
            Label(root2, text=c33, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=2)
            Frame(root2, height=150, bg="gray15").grid(columnspan=4)
            #Функция для закрытия окна с отображением результата
            def exit():
                root2.destroy()
                return 0
            #Кнопка выхода
            Button(root2, text="Понял, принял!", font=("Bebas Neue Cyrillic", 20), width=30, height=1, fg='gray15', bg='white', command=exit).grid(columnspan=3)
            root2.mainloop()
        except:
            return 0
    #Кнопка для подсчёта результата
    buttonsum = Button(root1, text='Cложить матрицы', font=("Bebas Neue Cyrillic", 20), width=50, height=1, fg='gray15',  bg='white')
    buttonsum.bind("<Button-1>", sumall)
    buttonsum.grid(columnspan=9)
    Frame(root1, height=100, bg="gray15").grid(columnspan=4)
    #Функция для закрытия окна операции сложения
    def back():
        root1.destroy()
        return 0
    Button(root1, text='Назад', font=("Bebas Neue Cyrillic", 16), width=30, height=1, fg='gray15', bg='white', command=back).grid(columnspan=9)
    root1.mainloop()

#Функция умножения матрицы на число
def multibynumber():
    #Создаём окно для операции умножения
    #Задаём цвет, название, надписи и кнопки
    root1 = Tk()
    root1.title("Умножение")
    root1["bg"] = "gray15"
    root1.state('zoomed')
    root1.resizable(width=False, height=False)

    Frame(root1, height=20, bg="gray15").grid(row=0, column=0)
    Label(root1, text="Умножение матрицы на число", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=1, column=4)
    Frame(root1, height=140, bg="gray15").grid(row=2, column=0)
    Label(root1, text="Матрица А", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=W)
    Label(root1, text="Число", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=E)
    Frame(root1, width=40, bg="gray15").grid(row=4, column=0)

    #Каждая переменная является полем ввода
    a11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a11.grid(row=4, column=1)
    a12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a12.grid(row=4, column=2)
    a13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a13.grid(row=4, column=3)
    Frame(root1, width=750, bg="gray15").grid(row=4, column=4)

    Frame(root1, width=50, bg="gray15").grid(row=4, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=5, column=0)
    a21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a21.grid(row=5, column=1)
    a22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a22.grid(row=5, column=2)
    a23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a23.grid(row=5, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=5, column=4)
    Frame(root1, width=50, bg="gray15").grid(row=5, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=6, column=0)
    a31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a31.grid(row=6, column=1)
    a32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a32.grid(row=6, column=2)
    a33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a33.grid(row=6, column=3)

    number = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    number.grid(row=4, column=5)
    Frame(root1, width=165, bg="gray15").grid(row=4, column=6)

    Frame(root1, width=750, bg="gray15").grid(row=6, column=4)
    Frame(root1, width=50, bg="gray15").grid(row=6, column=8)
    Frame(root1, height=150, bg="gray15").grid(columnspan=9)

    #Фунцкия для вычисления произведения матрицы на число
    def multiall(event):
        #Обработка исключений для того, чтобы не возникало ошибок, если поля не заполнены или заполнены некорректно
        try:
            c11 = int(a11.get()) * int(number.get())
            c12 = int(a12.get()) * int(number.get())
            c13 = int(a13.get()) * int(number.get())
            c21 = int(a21.get()) * int(number.get())
            c22 = int(a22.get()) * int(number.get())
            c23 = int(a23.get()) * int(number.get())
            c31 = int(a31.get()) * int(number.get())
            c32 = int(a32.get()) * int(number.get())
            c33 = int(a33.get()) * int(number.get())
            root2 = Tk()
            root2.title("Результат")
            root2["bg"] = "gray15"
            root2.state('zoomed')
            root2.resizable(width=False, height=False)
            Frame(root2, height=20, bg="gray15").grid(row=0, column=0)
            Label(root2, text="Результат умножения матрицы на число", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=4)
            Frame(root2, height=100, bg="gray15").grid(columnspan=4)
            Label(root2, text="Матрица C", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=3)
            Label(root2, text=c11, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=0)
            Label(root2, text=c12, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=1)
            Label(root2, text=c13, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=2)
            Label(root2, text=c21, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=0)
            Label(root2, text=c22, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=1)
            Label(root2, text=c23, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=2)
            Label(root2, text=c31, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=0)
            Label(root2, text=c32, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=1)
            Label(root2, text=c33, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=2)
            Frame(root2, height=150, bg="gray15").grid(columnspan=4)
            #Функция для закрытия окна с отображением результата
            def exit():
                root2.destroy()
                return 0
            #Кнопка выхода
            Button(root2, text="Понял, принял!", font=("Bebas Neue Cyrillic", 20), width=30, height=1, fg='gray15', bg='white', command=exit).grid(columnspan=3)
            root2.mainloop()
        except:
            return 0
    #Кнопка для подсчёта результата
    buttonsum = Button(root1, text='Умножить', font=("Bebas Neue Cyrillic", 20), width=50, height=1, fg='gray15',  bg='white')
    buttonsum.bind("<Button-1>", multiall)
    buttonsum.grid(row=8, columnspan=9)
    Frame(root1, height=100, bg="gray15").grid(columnspan=4)
    #Функция для закрытия окна операции умножения
    def back():
        root1.destroy()
        return 0
    Button(root1, text='Назад', font=("Bebas Neue Cyrillic", 16), width=30, height=1, fg='gray15', bg='white', command=back).grid(columnspan=9)
    root1.mainloop()

#Функция умножения двух матриц
def multi():
    #Создаём окно для операции умножения
    #Задаём цвет, название, надписи и кнопки
    root1 = Tk()
    root1.title("Умножение матриц")
    root1["bg"] = "gray15"
    root1.state('zoomed')
    root1.resizable(width=False, height=False)

    Frame(root1, height=20, bg="gray15").grid(row=0, column=0)
    Label(root1, text="Умножение двух матриц", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=1, column=4)
    Frame(root1, height=140, bg="gray15").grid(row=2, column=0)
    Label(root1, text="Матрица А", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=W)
    Label(root1, text="Матрица В", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, column=4, sticky=E)
    Frame(root1, width=40, bg="gray15").grid(row=4, column=0)

    #Каждая переменная является полем ввода
    a11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a11.grid(row=4, column=1)
    a12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a12.grid(row=4, column=2)
    a13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a13.grid(row=4, column=3)
    Frame(root1, width=750, bg="gray15").grid(row=4, column=4)

    b11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b11.grid(row=4, column=5)
    b12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b12.grid(row=4, column=6)
    b13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b13.grid(row=4, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=4, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=5, column=0)
    a21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a21.grid(row=5, column=1)
    a22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a22.grid(row=5, column=2)
    a23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a23.grid(row=5, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=5, column=4)
    b21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b21.grid(row=5, column=5)
    b22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b22.grid(row=5, column=6)
    b23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b23.grid(row=5, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=5, column=8)

    Frame(root1, width=50, bg="gray15").grid(row=6, column=0)
    a31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a31.grid(row=6, column=1)
    a32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a32.grid(row=6, column=2)
    a33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a33.grid(row=6, column=3)

    Frame(root1, width=750, bg="gray15").grid(row=6, column=4)
    b31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b31.grid(row=6, column=5)
    b32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b32.grid(row=6, column=6)
    b33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    b33.grid(row=6, column=7)
    Frame(root1, width=50, bg="gray15").grid(row=6, column=8)
    Frame(root1, height=150, bg="gray15").grid(columnspan=9)

    #Фунцкия для вычисления произведения элементов матриц
    def multiallmat(event):
        #Обработка исключений для того, чтобы не возникало ошибок, если поля не заполнены или заполнены некорректно
        try:
            c11 = int(a11.get()) * int(b11.get()) + int(a12.get()) * int(b21.get()) + int(a13.get()) * int(b31.get())
            c12 = int(a11.get()) * int(b12.get()) + int(a12.get()) * int(b22.get()) + int(a13.get()) * int(b32.get())
            c13 = int(a11.get()) * int(b13.get()) + int(a12.get()) * int(b23.get()) + int(a13.get()) * int(b33.get())
            c21 = int(a21.get()) * int(b11.get()) + int(a22.get()) * int(b21.get()) + int(a23.get()) * int(b31.get())
            c22 = int(a21.get()) * int(b12.get()) + int(a22.get()) * int(b22.get()) + int(a23.get()) * int(b32.get())
            c23 = int(a21.get()) * int(b13.get()) + int(a22.get()) * int(b23.get()) + int(a23.get()) * int(b33.get())
            c31 = int(a31.get()) * int(b11.get()) + int(a32.get()) * int(b21.get()) + int(a33.get()) * int(b31.get())
            c32 = int(a31.get()) * int(b12.get()) + int(a32.get()) * int(b22.get()) + int(a33.get()) * int(b32.get())
            c33 = int(a31.get()) * int(b13.get()) + int(a32.get()) * int(b23.get()) + int(a33.get()) * int(b33.get())
            root2 = Tk()
            root2.title("Результат")
            root2["bg"] = "gray15"
            root2.state('zoomed')
            root2.resizable(width=False, height=False)
            Frame(root2, height=20, bg="gray15").grid(row=0, column=0)
            Label(root2, text="Результат умножения двух матриц", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=4)
            Frame(root2, height=100, bg="gray15").grid(columnspan=4)
            Label(root2, text="Матрица C", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=3)
            Label(root2, text=c11, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=0)
            Label(root2, text=c12, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=1)
            Label(root2, text=c13, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=2)
            Label(root2, text=c21, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=0)
            Label(root2, text=c22, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=1)
            Label(root2, text=c23, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=2)
            Label(root2, text=c31, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=0)
            Label(root2, text=c32, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=1)
            Label(root2, text=c33, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=2)
            Frame(root2, height=150, bg="gray15").grid(columnspan=4)
            #Функция для закрытия окна с отображением результата
            def exit():
                root2.destroy()
                return 0
            #Кнопка выхода
            Button(root2, text="Понял, принял!", font=("Bebas Neue Cyrillic", 20), width=30, height=1, fg='gray15', bg='white', command=exit).grid(columnspan=3)
            root2.mainloop()
        except:
            return 0
    #Кнопка для подсчёта результата
    buttonsum = Button(root1, text='Умножить матрицы', font=("Bebas Neue Cyrillic", 20), width=50, height=1, fg='gray15',  bg='white')
    buttonsum.bind("<Button-1>", multiallmat)
    buttonsum.grid(columnspan=9)
    Frame(root1, height=100, bg="gray15").grid(columnspan=4)
    #Функция для закрытия окна операции сложения
    def back():
        root1.destroy()
        return 0
    Button(root1, text='Назад', font=("Bebas Neue Cyrillic", 16), width=30, height=1, fg='gray15', bg='white', command=back).grid(columnspan=9)
    root1.mainloop()

#Функция транспонирования матрицы
def transponation():
    # Создаём окно для операции транспонирования
    # Задаём цвет, название, надписи и кнопки
    root1 = Tk()
    root1.title("Транспонирование")
    root1["bg"] = "gray15"
    root1.state('zoomed')
    root1.resizable(width=False, height=False)
    Frame(root1, height=20, bg="gray15").grid(row=0, column=0)
    Label(root1, text="Транспонирование матрицы", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=1,
                                                                                                                  columnspan=8)
    Frame(root1, height=140, bg="gray15").grid(row=2, column=0)
    Label(root1, text="Матрица А", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, columnspan=8)
    Frame(root1, width=550, bg="gray15").grid(row=4, column=0)
    Frame(root1, width=550, bg="gray15").grid(row=4, column=4)
    a11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a11.grid(row=4, column=1)
    a12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a12.grid(row=4, column=2)
    a13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a13.grid(row=4, column=3)
    a21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a21.grid(row=5, column=1)
    a22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a22.grid(row=5, column=2)
    a23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a23.grid(row=5, column=3)
    a31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a31.grid(row=6, column=1)
    a32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a32.grid(row=6, column=2)
    a33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a33.grid(row=6, column=3)

    # Функция для закрытия окна операции сложения
    def back():
        root1.destroy()
        return 0

    # Фунцкия для транспонирования матрицы
    def transp(event):
        # Обработка исключений для того, чтобы не возникало ошибок, если поля не заполнены или заполнены некорректно
        try:
            c11 = int(a11.get())
            c12 = int(a21.get())
            c13 = int(a31.get())
            c21 = int(a12.get())
            c22 = int(a22.get())
            c23 = int(a32.get())
            c31 = int(a13.get())
            c32 = int(a23.get())
            c33 = int(a33.get())
            root2 = Tk()
            root2.title("Результат")
            root2["bg"] = "gray15"
            root2.state('zoomed')
            root2.resizable(width=False, height=False)
            Frame(root2, height=20, bg="gray15").grid(row=0, column=0)
            Label(root2, text="Результат транспонирования", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=4)
            Frame(root2, height=100, bg="gray15").grid(columnspan=4)
            Label(root2, text="Матрица A'", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=3)
            Label(root2, text=c11, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=0)
            Label(root2, text=c12, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=1)
            Label(root2, text=c13, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=4, column=2)
            Label(root2, text=c21, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=0)
            Label(root2, text=c22, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=1)
            Label(root2, text=c23, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=5, column=2)
            Label(root2, text=c31, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=0)
            Label(root2, text=c32, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=1)
            Label(root2, text=c33, font=("Bebas Neue Cyrillic", 25), bg="gray15", fg="white").grid(row=6, column=2)
            Frame(root2, height=150, bg="gray15").grid(columnspan=4)

            # Функция для закрытия окна с отображением результата
            def exit():
                root2.destroy()
                return 0

            # Кнопка выхода
            Button(root2, text="Понял, принял!", font=("Bebas Neue Cyrillic", 20), width=30, height=1, fg='gray15', bg='white', command=exit).grid(columnspan=3)
            root2.mainloop()
        except:
            return 0

    # Кнопка для подсчёта результата
    Frame(root1, height=150, bg="gray15").grid(columnspan=8)
    buttonsum = Button(root1, text='Транспонировать', font=("Bebas Neue Cyrillic", 20), width=50, height=1, fg='gray15', bg='white')
    buttonsum.bind("<Button-1>", transp)
    buttonsum.grid(columnspan=8)
    Frame(root1, height=100, bg="gray15").grid(columnspan=8)
    Button(root1, text='Назад', font=("Bebas Neue Cyrillic", 16), width=30, height=1, fg='gray15', bg='white', command=back).grid(columnspan=8)
    root1.mainloop()

#Функция нахождения определителя матрицы
def det():
    # Создаём окно для операции нахождение определителя матрицы
    # Задаём цвет, название, надписи и кнопки
    root1 = Tk()
    root1.title("Детерминант")
    root1["bg"] = "gray15"
    root1.state('zoomed')
    root1.resizable(width=False, height=False)
    Frame(root1, height=20, bg="gray15").grid(row=0, column=0)
    Label(root1, text="Определитель матрицы", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=1,
                                                                                                                  columnspan=8)
    Frame(root1, height=140, bg="gray15").grid(row=2, column=0)
    Label(root1, text="Матрица А", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(row=3, columnspan=8)
    Frame(root1, width=550, bg="gray15").grid(row=4, column=0)
    Frame(root1, width=550, bg="gray15").grid(row=4, column=4)
    a11 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a11.grid(row=4, column=1)
    a12 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a12.grid(row=4, column=2)
    a13 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a13.grid(row=4, column=3)
    a21 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a21.grid(row=5, column=1)
    a22 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a22.grid(row=5, column=2)
    a23 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a23.grid(row=5, column=3)
    a31 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a31.grid(row=6, column=1)
    a32 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a32.grid(row=6, column=2)
    a33 = Entry(root1, width=10, justify=CENTER, bd=7, font=("Bebas Neue Cyrillic", 12))
    a33.grid(row=6, column=3)

    # Функция для закрытия окна операции нахождение определителя матрицы
    def back():
        root1.destroy()
        return 0

    # Фунцкия для нахождение определителя матрицы
    def search(event):
        # Обработка исключений для того, чтобы не возникало ошибок, если поля не заполнены или заполнены некорректно
        try:
            det = int(a11.get())*int(a22.get())*int(a33.get()) + int(a12.get())*int(a23.get())*int(a31.get()) + int(a13.get())*int(a21.get())*int(a32.get()) - int(a13.get())*int(a22.get())*int(a31.get()) - int(a12.get())*int(a21.get())*int(a33.get()) - int(a11.get())*int(a23.get())*int(a32.get())
            root2 = Tk()
            root2.title("Результат")
            root2["bg"] = "gray15"
            root2.state('zoomed')
            root2.resizable(width=False, height=False)
            Frame(root2, height=20, bg="gray15").grid(row=0, column=0)
            Label(root2, text="Определитель матрицы равен", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=4)
            Frame(root2, height=100, bg="gray15").grid(columnspan=4)
            Label(root2, text=det, font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").grid(columnspan=3)
            Frame(root2, height=150, bg="gray15").grid(columnspan=4)

            # Функция для закрытия окна с отображением результата
            def exit():
                root2.destroy()
                return 0

            # Кнопка выхода
            Button(root2, text="Понял, принял!", font=("Bebas Neue Cyrillic", 20), width=30, height=1, fg='gray15', bg='white', command=exit).grid(columnspan=3)
            root2.mainloop()
        except:
            return 0

    # Кнопка для подсчёта результата
    Frame(root1, height=150, bg="gray15").grid(columnspan=8)
    buttonsum = Button(root1, text='Найти определитель', font=("Bebas Neue Cyrillic", 20), width=50, height=1, fg='gray15', bg='white')
    buttonsum.bind("<Button-1>", search)
    buttonsum.grid(columnspan=8)
    Frame(root1, height=100, bg="gray15").grid(columnspan=8)
    Button(root1, text='Назад', font=("Bebas Neue Cyrillic", 16), width=30, height=1, fg='gray15', bg='white', command=back).grid(columnspan=8)
    root1.mainloop()

#Создаём внешний вид главного окна
#Прописываем надписи, кнопки, их внешний вид и функционал
Frame(height=20, bg="gray15").pack(fill=X)
Label(root, text="Матричный калькулятор", font=("Bebas Neue Cyrillic", 35), bg="gray15", fg="white").pack(fill=X)
Frame(height=50, bg="gray15").pack(fill=X)
Label(root, text="Вы запустили матричный калькулятор. К сожалению, он не имеет функцию \nвыбора размерности матриц, поэтому матрицы будут размерностью 3 на 3!", font=("Bebas Neue Cyrillic", 20), bg="gray15", fg="white").pack(fill=X)
Frame(height=30, bg="gray15").pack(fill=X)
Label(root, text="Выберите математическую операцию:", font=("Bebas Neue Cyrillic", 20), bg="gray15", fg="white").pack(fill=X)
Button(root, text="Сложение матриц", font=("Bebas Neue Cyrillic", 15), width=80, height=1, fg="gray15", bg="white", command=sum).pack()
Button(root, text="Вычитание матриц", font=("Bebas Neue Cyrillic", 15), width=80, height=1, fg="gray15", bg="white", command=subtraction).pack()
Button(root, text="Умножение матрицы на число", font=("Bebas Neue Cyrillic", 15), width=80, height=1, fg="gray15", bg="white", command=multibynumber).pack()
Button(root, text="Умножение матриц", font=("Bebas Neue Cyrillic", 15), width=80, height=1, fg="gray15", bg="white", command=multi).pack()
Button(root, text="Транспонирование матрицы", font=("Bebas Neue Cyrillic", 15), width=80, height=1, fg="gray15", bg="white", command=transponation).pack()
Button(root, text="Определитель матрицы", font=("Bebas Neue Cyrillic", 15), width=80, height=1, fg="gray15", bg="white", command=det).pack()
Frame(height=180, bg="gray15").pack(fill=X)
Button(root, text='Выйти', font=("Bebas Neue Cyrillic", 15), width=40, height=1, fg='gray15', bg='white', command=Exit).pack()
root.mainloop()