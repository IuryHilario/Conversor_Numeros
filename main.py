from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Convertor(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(0, 0)
        self.title('Convertor')
        self.geometry('+550+250')

        self.values = ["Decimal para Binário", "Binário para Decimal", "Decimal para Hexadecimal",
                       "Hexadecimal para Decimal", "Decimal para Octal", "Octal para Decimal"]

        self.initial()

    def initial(self):
        # FASE INICIAL DE TUDO
        # LAYOUT DA GUI
        self.frase_inicial = StringVar()
        self.frase_final = StringVar()
        self.frase_resultado = StringVar()

        Label(self, text="Convertor de Números", font=("Comic Sans MS", 30), justify='center').grid(row=0, column=0,
                                                                                                    sticky="NEWS",
                                                                                                    columnspan=2)

        self.opcoes = ttk.Combobox(self, values=self.values, justify="center", font=('Comic Sans MS', 12),
                                   state="readonly")
        self.opcoes.grid(row=1, column=0, sticky="WE", padx=5, pady=5, columnspan=2)

        self.button = Button(self, text='Situar conversão', font=('Comic Sans MS', 12), bd=5, relief=RAISED,
                             command=self.button_conversor)
        self.button.grid(row=2, column=0, columnspan=2, sticky="NEWS", padx=5, pady=5)
        # relief: flat, groove, raised, ridge, solid, or sunken

        Label(self).grid(row=3, column=0, columnspan=2)

    def button_conversor(self):
        # INICIO DA FASE DE CONVERSÃO
        # LAYOUT
        if self.opcoes.get() == '':
            messagebox.showerror('ERROR', 'Escolha uma opção!!')

        else:

            self.label_inicial = Label(self, textvariable=self.frase_inicial, font=('Comic Sans MS', 12))
            self.label_inicial.grid(row=4, column=0)

            self.inicial_valor = Entry(self, font=('Comic Sans MS', 12))
            self.inicial_valor.grid(row=4, column=1)

            self.button_convert = Button(self, text='Converter', font=('Comic Sans MS', 12), command=self.converter,
                                         bd=5, relief=RAISED)
            self.button_convert.grid(row=5, column=0, columnspan=2, sticky="NEWS", padx=5, pady=5)

            self.label_final = Label(self, textvariable=self.frase_final, font=('Comic Sans MS', 12))
            self.label_final.grid(row=6, column=0)

            self.resultado_final = Label(self, textvariable=self.frase_resultado, font=('Comic Sans MS', 12))
            self.resultado_final.grid(row=6, column=1)


        # OPÇÕES ESCOLHIDAS PELO USÚARIO

        if self.opcoes.get() == self.values[0]:
            self.frase_inicial.set('Número Decimal: ')
            self.frase_final.set('Número Binário: ')

        elif self.opcoes.get() == self.values[1]:
            self.frase_inicial.set('Número Binário: ')
            self.frase_final.set("Número Decimal: ")

        elif self.opcoes.get() == self.values[2]:
            self.frase_inicial.set('Número Decimal: ')
            self.frase_final.set('Número Hexadecimal: ')

        elif self.opcoes.get() == self.values[3]:
            self.frase_inicial.set('Número Hexadecimal: ')
            self.frase_final.set("Número Decimal: ")

        elif self.opcoes.get() == self.values[4]:
            self.frase_inicial.set('Número Decimal: ')
            self.frase_final.set('Número Octal: ')

        elif self.opcoes.get() == self.values[5]:
            self.frase_inicial.set('Número Octal: ')
            self.frase_final.set("Número Decimal: ")

    def converter(self):
        if self.opcoes.get() == self.values[0]:
            # DECIMAL PARA BINÁRIO
            # MATH ACCOUNT
            try:
                decimal = int(self.inicial_valor.get())

            except:
                messagebox.showerror('ERROR', 'Existe valor não DECIMAL!!')

            else:
                if decimal == 0:
                    return "0"
                binario = ""
                while decimal > 0:
                    resto = decimal % 2
                    binario = str(resto) + binario
                    decimal //= 2

                self.frase_resultado.set(binario)


        elif self.opcoes.get() == self.values[1]:
            # BINÁRIO PARA DECIMAL
            # COMPUTACIONAL ACCOUNT

            binario = str(self.inicial_valor.get())

            if all(c in '01' for c in binario):
                binario = str(binario)

                decimal = 0
                for i in range(len(binario)):
                    decimal += int(binario[i]) * (2 ** (len(binario) - 1 - i))

                self.frase_resultado.set(decimal)


            else:
                messagebox.showerror('ERROR', 'Existe valor não BINÁRIO!!')


        elif self.opcoes.get() == self.values[2]:
            # DECIMAL PARA HEXADECIMAL
            # MATH ACCOUNT
            try:
                decimal = int(self.inicial_valor.get())

            except:
                messagebox.showerror('ERROR', 'Existe valor não DECIMAL!!')

            else:

                if decimal == 0:
                    return "0"
                hexadecimal = ""
                while decimal > 0:
                    resto = decimal % 16
                    if resto < 10:
                        hexadecimal = str(resto) + hexadecimal
                    else:
                        hexadecimal = chr(65 + resto - 10) + hexadecimal
                    decimal //= 16

                self.frase_resultado.set(hexadecimal)


        elif self.opcoes.get() == self.values[3]:
            # HEXADECIMAL PARA DECIMAL
            # COMPUTACIONAL ACCOUNT

            hexadecimal = str(self.inicial_valor.get()).upper()

            if all(c in '0123456789ABCDEF' for c in hexadecimal):

                decimal = 0
                for i in range(len(hexadecimal)):
                    if '0' <= hexadecimal[i] <= '9':
                        decimal += int(hexadecimal[i]) * (16 ** (len(hexadecimal) - 1 - i))
                    else:
                        decimal += (ord(hexadecimal[i]) - 55) * (16 ** (len(hexadecimal) - 1 - i))
                self.frase_resultado.set(decimal)

            else:
                messagebox.showerror('ERROR', 'Existe valor não HEXADECIMAL!!')


        elif self.opcoes.get() == self.values[4]:
            # DECIMAL PARA OCTAL
            # MATH ACCOUNT
            try:
                decimal = int(self.inicial_valor.get())

            except:
                messagebox.showerror('ERROR', 'Existe valor não DECIMAL!!')

            else:
                if decimal == 0:
                    return "0"
                octal = ""

                while decimal > 0:
                    resto = decimal % 8
                    octal = str(resto) + octal
                    decimal //= 8

                self.frase_resultado.set(octal)


        elif self.opcoes.get() == self.values[5]:
            # OCTAL PARA DECIMAL
            # COMPUTACIONAL ACCOUNT

            octal = str(self.inicial_valor.get())

            if all(c in '012345678' for c in octal):
                decimal = 0
                for i in range(len(octal)):
                    decimal += int(octal[i]) * (8 ** (len(octal) - 1 - i))

                self.frase_resultado.set(decimal)

            else:
                messagebox.showerror('ERROR', 'Existe valor não OCTAL!!')


if __name__ == "__main__":
    Convertor().mainloop()
