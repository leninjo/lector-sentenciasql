from tkinter import * 

reservadas = ("SELECT", "FROM", "UPDATE", "DELETE", "INSERT", "INTO", "TABLE", "COLUMN", "WHERE")
operadores = ("=", ",", "*", "+", "-", "(", ")", "&")


ventana = Tk()
ventana.title("LECTOR DE SENTENCIAS SQL")
ventana.geometry('500x460')
ventana.configure(bg="#0D1321")

label = Label(ventana, text="Ingresa la sentencia SQL que deseas analizar", bg="#0D1321", fg="#F0EBD8", font=("Nunito", 15))
label.grid(column=0, columnspan=4, row=0, pady=10)

cadena = Entry(ventana, width=38, borderwidth=0, bg="#3E5C76", fg="#F0EBD8", font=("Nunito", 15, "bold italic"))
cadena.grid(column=0, columnspan=4, row=1, padx=18)

def leer():
      res = cadena.get().upper().split(" ")
      list = Listbox(ventana, borderwidth=0, bg="#3E5C76", fg="#F0EBD8", font=("Nunito", 14))

      for i in res: 
            if i in reservadas:
                  list.insert(END, "  RESERVADA: " + i)
            elif i in operadores:
                  list.insert(END, "  OPERADOR: " + i)
            elif i.isnumeric():
                  list.insert(END, "  NÚMERO: " + i)
            elif i == "":
                  list.insert(END, "")
            elif i:
                  if i[0] == '"':
                        list.insert(END, "  CADENA : " + i)
                  else:
                        list.insert(END, "  IDENTIFICADOR: " + i)
            
      list.grid(column=0, columnspan=4, row=4, padx=15, pady=5, sticky=S+N+E+W)

def limpiar():
      cadena.delete(0, END)
      leer()

boton = Button(ventana, text="Analizar", command=leer, borderwidth=0, bg="#52BE80", fg="#0D1321", activebackground="#229954", activeforeground="#F0EBD8", font=("Nunito", 14))
boton.grid(column=0, columnspan=2, row=3, pady=18)

limpiar = Button(ventana, text="Limpiar", command=limpiar, borderwidth=0, bg="#F1948A", fg="#0D1321", activebackground="#B03A2E", activeforeground="#F0EBD8", font=("Nunito", 14))
limpiar.grid(column=2, columnspan=2, row=3, pady=18)

ventana.mainloop()




