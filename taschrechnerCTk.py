import customtkinter as ctk

# --- Funktionen ---
def ende():
    main.destroy()

def res():
    text = lb.cget("text")
    for i, zeichen in enumerate(text):
        if zeichen in "+-*/":
            zahl1 = text[:i]
            op = zeichen
            zahl2 = text[i+1:]
            break
    try:
        ausdruck = zahl1 + op + zahl2
        ergebnis = eval(ausdruck)
        lb.configure(text=f"{ausdruck} = {ergebnis}")
    except Exception:
        lb.configure(text="Fehler")

def cl():
    lb.configure(text="")

def anz(eingabe):
    lb.configure(text=lb.cget("text") + str(eingabe))

def anzp():
    if "." not in lb.cget("text"):
        lb.configure(text=lb.cget("text") + ".")

# --- Fenster ---
ctk.set_appearance_mode("light")  # oder "dark"
ctk.set_default_color_theme("blue")

main = ctk.CTk()
main.title("CustomTkinter Rechner")

main.resizable(False, False)
ctk.set_appearance_mode("dark")
# --- Label (Anzeige) ---
lb = ctk.CTkLabel(main, text="", height=40, anchor="e", font=("Arial", 20), corner_radius=5, fg_color="#ffffff", text_color="black")
lb.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="we")

# --- Row 1 ---
ctk.CTkButton(main, text="+", width=70, command=lambda: anz("+")).grid(row=1, column=0, padx=5, pady=5)
ctk.CTkButton(main, text="-", width=70, command=lambda: anz("-")).grid(row=1, column=1, padx=5, pady=5)
ctk.CTkButton(main, text="*", width=70, command=lambda: anz("*")).grid(row=1, column=2, padx=5, pady=5)
ctk.CTkButton(main, text="/", width=70, command=lambda: anz("/")).grid(row=1, column=3, padx=5, pady=5)

# --- Row 2 ---
ctk.CTkButton(main, text="7", width=70, command=lambda: anz(7)).grid(row=2, column=0, padx=5, pady=5)
ctk.CTkButton(main, text="8", width=70, command=lambda: anz(8)).grid(row=2, column=1, padx=5, pady=5)
ctk.CTkButton(main, text="9", width=70, command=lambda: anz(9)).grid(row=2, column=2, padx=5, pady=5)
ctk.CTkButton(main, text="=", width=70, command=res).grid(row=2, column=3, padx=5, pady=5)

# --- Row 3 ---
ctk.CTkButton(main, text="4", width=70, command=lambda: anz(4)).grid(row=3, column=0, padx=5, pady=5)
ctk.CTkButton(main, text="5", width=70, command=lambda: anz(5)).grid(row=3, column=1, padx=5, pady=5)
ctk.CTkButton(main, text="6", width=70, command=lambda: anz(6)).grid(row=3, column=2, padx=5, pady=5)
ctk.CTkButton(main, text="CL", width=70, command=cl).grid(row=3, column=3, padx=5, pady=5)

# --- Row 4 ---
ctk.CTkButton(main, text="1", width=70, command=lambda: anz(1)).grid(row=4, column=0, padx=5, pady=5)
ctk.CTkButton(main, text="2", width=70, command=lambda: anz(2)).grid(row=4, column=1, padx=5, pady=5)
ctk.CTkButton(main, text="3", width=70, command=lambda: anz(3)).grid(row=4, column=2, padx=5, pady=5)

# --- Row 5 ---
ctk.CTkButton(main, text=".", width=70, command=anzp).grid(row=5, column=0, padx=5, pady=5)
ctk.CTkButton(main, text="0", width=70, command=lambda: anz(0)).grid(row=5, column=1, padx=5, pady=5)
ctk.CTkButton(main, text="Ende", width=70, command=ende).grid(row=5, column=2, padx=5, pady=5)

main.mainloop()


