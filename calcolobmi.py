import tkinter as tk
from tkinter import messagebox

def calcola_bmi(peso, altezza):
    bmi = peso / (altezza ** 2)
    return bmi

def descrizione_bmi(bmi):
    if bmi < 18.5:
        return "Sottopeso"
    elif 18.5 <= bmi < 25:
        return "Normopeso"
    elif 25 <= bmi < 30:
        return "Sovrappeso"
    else:
        return "Obesità"

def calcola():
    try:
        peso = float(peso_entry.get())
        altezza = float(altezza_entry.get())
        bmi = calcola_bmi(peso, altezza)
        descrizione = descrizione_bmi(bmi)
        risultato_label.config(text="Il tuo BMI è: {:.2f} ({})".format(bmi, descrizione))
    except ValueError:
        messagebox.showerror("Errore", "Inserisci valori validi per peso e altezza!")

root = tk.Tk()
root.title("Calcolatrice BMI")
root.geometry("800x600")

# Font più grande
font_label = ("Helvetica", 12)
font_entry = ("Helvetica", 12)

# Creazione di un frame per contenere tutti i widget
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

peso_label = tk.Label(frame, text="Peso (kg):", font=font_label)
peso_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

peso_entry = tk.Entry(frame, font=font_entry)
peso_entry.grid(row=0, column=1, padx=10, pady=5)

altezza_label = tk.Label(frame, text="Altezza (m):", font=font_label)
altezza_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

altezza_entry = tk.Entry(frame, font=font_entry)
altezza_entry.grid(row=1, column=1, padx=10, pady=5)

calcola_button = tk.Button(frame, text="Calcola BMI", command=calcola, font=font_label)
calcola_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Risultato centrato
risultato_label = tk.Label(root, text="", font=font_label, anchor="center")
risultato_label.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()