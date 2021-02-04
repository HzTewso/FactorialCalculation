import tkinter as tk
import random

def calculated(fact=1):
    if num.get().isdigit():
        n = int(num.get())
        for i in range(1, n):
            fact *=i
        return fact

def texter():
    if num.get().isdigit():
        n = int(num.get())
        write2.configure(text="Belirlediğiniz sayının \n faktöriyeli {}'dir.".format(calculated(n)))

screen = tk.Tk()
screen.title('Faktöriyel Hesaplama')
screen.geometry('450x250')

write = tk.Label(screen, text='Hesaplanacak bir sayı girin!', font='Courier 14 bold', width=40, justify='center')
write.place(x=15, y=20)
num = tk.Entry(screen, font='Courier 14 bold', width=15, justify='center')
num.place(x=130, y=90)
control = tk.Button(screen, text='Hesapla', font='Courier 14', width=10, command=texter)
control.place(x=150, y=130)
write2 = tk.Label(screen, text='', font='Courier 14', width=25, justify='center')
write2.place(x=90, y=180)

screen.mainloop()