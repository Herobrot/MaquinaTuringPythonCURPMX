import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random as rd
class TuringMachine:
    def __init__(self, input_string):
        self.tape = list(input_string) + ['B'] 
        self.state = 'q0' 
        self.head = 0
    
    def process(self):
        while self.state != 'q101' and self.state != 'qr':
            print(f"Current state: {self.state} with head at position {self.head} and char {self.tape[self.head]}")
            if self.state == 'q0':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z'):
                    self.state = 'q1'
                    self.head += 1
                else:
                    self.state = 'qr'

            elif self.state == 'q1':
                if self.tape[self.head] == 'A' or self.tape[self.head] == 'E' or self.tape[self.head] == 'I' or self.tape[self.head] == 'O' or self.tape[self.head] == 'U':
                    self.state = 'q2'
                    self.head += 1
                else:
                    self.state = 'qr'
            
            elif self.state == 'q2':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z'):
                    self.state = 'q3'
                    self.head += 1
                else:
                    self.state = 'qr'
            
            elif self.state == 'q3':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z'):
                    self.state = 'q4'
                    self.head += 1
                else:
                    self.state = 'qr'
            
            elif self.state == 'q4':
                if self.is_numeric_par(self.tape[self.head]):
                    self.state = 'q102'
                    self.head += 1
                elif self.is_numeric_impar(self.tape[self.head]):
                    self.state = 'q103'
                    self.head += 1
                else:
                    self.state = 'qr'
            
            elif self.state == 'q5':
                if self.is_numeric(self.tape[self.head], '0', '9'):
                    self.state = 'q107'
                    self.head += 1
                else:
                    self.state = 'qr'    
                
            elif self.state == 'q6':
                if self.tape[self.head] == '1':
                    self.state = 'q8'
                    self.head += 1
                elif self.tape[self.head] == '0':
                    self.state = 'q7'
                    self.head += 1
                else:
                    self.state = 'qr'

            elif self.state == 'q7':
                if self.is_numeric_impar(self.tape[self.head]):
                    self.state = 'q9'
                    self.head += 1
                elif self.is_numeric_par(self.tape[self.head]) and self.tape[self.head] != '2':
                    self.state = 'q10'
                    self.head += 1
                elif self.tape[self.head] == '2':
                    self.state = 'q13'
                    self.head += 1
                else:
                    self.state = 'qr'

            elif self.state == 'q8':
                if self.tape[self.head] == '2' or self.tape[self.head] == '0':
                    self.state = 'q10'
                    self.head += 1
                else:
                    self.state = 'qr'

            elif self.state == 'q9':
                if self.tape[self.head] == '0':
                    self.state = 'q21'
                    self.head += 1
                elif self.tape[self.head] == '2' or self.tape[self.head] == '1':
                    self.state = 'q14'
                    self.head += 1
                elif self.tape[self.head] == '3':
                    self.state = 'q15'
                    self.head += 1
                else:
                    self.state = 'qr'

            elif self.state == 'q10':
                if self.tape[self.head] == '1' or self.tape[self.head] == '2':
                    self.state = 'q27'
                    self.head += 1
                elif self.tape[self.head] == '3':
                    self.state = 'q26'
                    self.head += 1
                else:
                    self.state = 'qr'

            elif self.state == 'q11':
                if self.tape[self.head] == 'B':
                    self.state = 'qB'
                    self.head += 1
                elif self.tape[self.head] == 'S':
                    self.state = 'qS'
                    self.head += 1
                elif self.tape[self.head] == 'N':
                    self.state = 'qN'
                    self.head += 1
                elif self.tape[self.head] == 'C':
                    self.state = 'qC'
                    self.head += 1
                elif self.tape[self.head] == 'Q':
                    self.state = 'qQ'
                    self.head += 1
                elif self.tape[self.head] == 'D':
                    self.state = 'qD'
                    self.head += 1
                elif self.tape[self.head] == 'G':
                    self.state = 'qG'
                    self.head += 1
                elif self.tape[self.head] == 'Z':
                    self.state = 'qZ'
                    self.head += 1
                elif self.tape[self.head] == 'P':
                    self.state = 'qP'
                    self.head += 1
                elif self.tape[self.head] == 'J':
                    self.state = 'qJ'
                    self.head += 1
                elif self.tape[self.head] == 'M':
                    self.state = 'qM'
                    self.head += 1
                elif self.tape[self.head] == 'T':
                    self.state = 'qT'
                    self.head += 1
                elif self.tape[self.head] == 'V':
                    self.state = 'qV'
                    self.head += 1
                elif self.tape[self.head] == 'O':
                    self.state = 'qO'
                    self.head += 1
                elif self.tape[self.head] == 'H':
                    self.state = 'qH'
                    self.head += 1
                elif self.tape[self.head] == 'A':
                    self.state = 'qA'
                    self.head += 1
                elif self.tape[self.head] == 'Y':
                    self.state = 'qY'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q13':
                if self.tape[self.head] == '2':
                    self.state = 'q19'
                    self.head += 1
                elif self.tape[self.head] == '0':
                    self.state = 'q23'
                    self.head += 1
                elif self.tape[self.head] == '1':
                    self.state = 'q18'
                else:
                    self.state = 'qr'
            elif self.state == 'q14':
                if self.is_numeric(self.tape[self.head], 0, 9):
                    self.state = 'q16'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q15':
                if self.is_numeric(self.tape[self.head], 0, 1):
                    self.state = 'q17'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q17' or self.state == 'q20' or self.state == 'q30' or self.state == 'q31' or self.state == 'q29' or self.state == 'q16'  or self.state == 'q25' or self.state == 'q24' or self.state == 'q22' or self.state == 'q107':
                if self.is_gender(self.tape[self.head]):
                    self.state = 'q11'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q18':
                if self.is_numeric(self.tape[self.head], 0, 9):
                    self.state = 'q20'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q19':
                if self.is_numeric(self.tape[self.head], 0, 8):
                    self.state = 'q25'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q21':
                if self.is_numeric(self.tape[self.head], 1, 9):
                    self.state = 'q22'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q23':
                if self.is_numeric(self.tape[self.head], 1, 9):
                    self.state = 'q24'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q26':
                if self.tape[self.head] == '0':
                    self.state = 'q31'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q27':
                if self.is_numeric(self.tape[self.head], 0, 9):
                    self.state = 'q30'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q28':
                if self.is_numeric(self.tape[self.head], 1, 9):
                    self.state = 'q29'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q102':
                if self.is_numeric_par(self.tape[self.head]) and self.tape[self.head] != '6':
                    self.state = 'q104'
                    self.head += 1
                elif self.is_numeric_impar(self.tape[self.head]):
                    self.state = 'q6'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q103':
                if self.is_numeric(self.tape[self.head], '0', '9') and (self.tape[self.head] != '2' or self.tape[self.head] != '6'):
                    self.state = 'q6'
                    self.head += 1
                elif (self.tape[self.head] == '2' or self.tape[self.head] == '6'):
                    self.state = 'q106'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q104':
                if self.tape[self.head] == '0':
                    self.state = 'q105'
                    self.head += 1
                elif self.is_numeric_impar(self.tape[self.head]):
                    self.state = 'q9'
                    self.head += 1
                elif self.is_numeric_par(self.tape[self.head]) and self.tape[self.head] != '0' and self.tape[self.head] != '2':
                    self.state = 'q10'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q105':
                if self.is_numeric_impar(self.tape[self.head]):
                    self.state = 'q9'
                    self.head += 1
                elif self.is_numeric_par(self.tape[self.head]) and self.tape[self.head] != '0' and self.tape[self.head] != '2':
                    self.state = 'q10'
                    self.head += 1
                elif self.tape[self.head] == '2':
                    self.state = 'q109'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q106':
                if self.tape[self.head] == '1':
                    self.state = 'q8'
                    self.head += 1
                elif self.tape[self.head] == '0':
                    self.state = 'q105'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q109':
                if self.tape[self.head] == '0':
                    self.state = 'q23'
                    self.head += 1
                elif self.tape[self.head] == '1':
                    self.state = 'q18'
                    self.head += 1
                elif self.tape[self.head] == '2':
                    self.state = 'q5'
                    self.head += 1
                else:
                    self.state = 'qr'            
            elif self.state == 'qB':
                if self.tape[self.head] == 'C':
                    self.state = 'qBC'
                    self.head += 1
                elif self.tape[self.head] == 'S':
                    self.state = 'qBS'
                    self.head += 1
                else: 
                    self.state = 'qr'
            elif self.state == 'qA':
                if self.tape[self.head] == 'S':
                    self.state = 'qAS'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qC':
                if self.tape[self.head] == 'C':
                    self.state = 'qCC'
                    self.head += 1
                elif self.tape[self.head] == 'H':
                    self.state = 'qCH'
                    self.head += 1
                elif self.tape[self.head] == 'L':
                    self.state = 'qCL'
                    self.head += 1
                elif self.tape[self.head] == 'M':
                    self.state = 'qCM'
                    self.head += 1
                elif self.tape[self.head] == 'S':
                    self.state = 'qCS'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qD':
                if self.tape[self.head] == 'F':
                    self.state = 'qDF'
                    self.head += 1
                elif self.tape[self.head] == 'G':
                    self.state = 'qDG'
                    self.head += 1
                else: 
                    self.state = 'qr'
            elif self.state == 'qG':
                if self.tape[self.head] == 'T':
                    self.state = 'qGT'
                    self.head += 1
                elif self.tape[self.head] == 'R':
                    self.state = 'qGR'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qH':
                if self.tape[self.head] == 'G':
                    self.state = 'qHG'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qJ':
                if self.tape[self.head] == 'C':
                    self.state = 'qJC'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qM':
                if self.tape[self.head] == 'C':
                    self.state = 'qMC'
                    self.head += 1
                elif self.tape[self.head] == 'N':
                    self.state = 'qMN'
                    self.head += 1
                elif self.tape[self.head] == 'S':
                    self.state = 'qMS'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qN':
                if self.tape[self.head] == 'E':
                    self.state = 'qNE'
                    self.head += 1
                elif self.tape[self.head] == 'L':
                    self.state = 'qNL'
                    self.head += 1
                elif self.tape[self.head] == 'T':
                    self.state = 'qNT'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qO':
                if self.tape[self.head] == 'C':
                    self.state = 'qOC'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qP':
                if self.tape[self.head] == 'L':
                    self.state = 'qPL'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qQ':
                if self.tape[self.head] == 'R':
                    self.state = 'qQR'
                    self.head += 1
                elif self.tape[self.head] == 'T':
                    self.state = 'qQT'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qS':
                if self.tape[self.head] == 'L':
                    self.state = 'qSL'
                    self.head += 1
                elif self.tape[self.head] == 'P':
                    self.state = 'qSP'
                    self.head += 1
                elif self.tape[self.head] == 'R':
                    self.state = 'qSR'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qT':
                if self.tape[self.head] == 'L':
                    self.state = 'qTL'
                    self.head += 1
                elif self.tape[self.head] == 'S':
                    self.state = 'qTS'
                    self.head += 1
                elif self.tape[self.head] == 'C':
                    self.state = 'qTC'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qV':
                if self.tape[self.head] == 'Z':
                    self.state = 'qVZ'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qY':
                if self.tape[self.head] == 'N':
                    self.state = 'qYN'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qZ':
                if self.tape[self.head] == 'S':
                    self.state = 'qZS'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qAS' or self.state == 'qBC' or self.state == 'qBS' or self.state == 'qCC' or self.state == 'qCH' or self.state == 'qCL' or self.state == 'qCM' or self.state == 'qCS' or self.state == 'qDF' or self.state == 'qDG' or self.state == 'qGT' or self.state == 'qGR' or self.state == 'qHG' or self.state == 'qJC' or self.state == 'qMC' or self.state == 'qMN' or self.state == 'qMS' or self.state == 'qNE' or self.state == 'qNL' or self.state == 'qNT' or self.state == 'qOC' or self.state == 'qPL' or self.state == 'qQR' or self.state == 'qQT' or self.state == 'qSL' or self.state == 'qSP' or self.state == 'qSR' or self.state == 'qTC' or self.state == 'qTL' or self.state == 'qTS' or self.state == 'qVZ' or self.state == 'qYN' or self.state == 'qZS':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z'):
                    self.state = 'qConsonant1'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qConsonant1':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z'):
                    self.state = 'qConsonant2'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qConsonant2':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z'):
                    self.state = 'qConsonant3'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'qConsonant3':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z') or self.is_numeric(self.tape[self.head], '0', '9'):
                    self.state = 'q12'
                    self.head += 1
                else:
                    self.state = 'qr'
            elif self.state == 'q12':
                if self.is_uppercase_alpha(self.tape[self.head], 'A', 'Z') or self.is_numeric(self.tape[self.head], '0', '9'):
                    self.state = 'q101'
                    self.head += 1
                else:
                    self.state = 'qr'            


        return self.state == 'q101'
    
    def is_numeric(self, char, min, max):
        return char.isdigit() and int(min) <= int(char) <= int(max)
    
    def is_numeric_par(self, char):
        return char.isdigit() and (char == '0' or char == '2' or char == '4' or char == '6' or char == '8')
    
    def is_numeric_impar(self, char):        
        return char.isdigit() and (char == '1' or char == '3' or char == '5' or char == '7' or char == '9')

    def is_uppercase_alpha(self, char, min, max):        
        return char.isalpha() and min <= char <= max
    
    def is_gender(self, char):
        return char == 'H' or char == 'M'


def validate_string():
    input_string = entry.get()
    turing = TuringMachine(input_string=input_string)
    resultado = turing.process()

    if resultado: 
        messagebox.showinfo("Resultado", "¡Cadena válida!")
        result_entry.config(state='normal')

    else:
        messagebox.showwarning("Resultado", "Cadena inválida.")
        result_entry.config(state='normal')


def generate_curp():
    nombre = nombre_entry.get().strip().upper()
    apellido_paterno = apellido_paterno_entry.get().strip().upper()
    apellido_materno = apellido_materno_entry.get().strip().upper()
    fecha_nacimiento = fecha_nacimiento_entry.get().strip()
    sexo = sexo_entry.get().strip().upper()
    estado = estado_var.get().strip()
    clave = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    if not (nombre and apellido_paterno and apellido_materno and fecha_nacimiento and sexo and estado):
        result_var.set("Por favor, llena todos los campos.")
        return

    try:
        fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        anio = fecha.strftime("%y")
        mes = fecha.strftime("%m")
        dia = fecha.strftime("%d")
    except ValueError:
        result_var.set("Fecha de nacimiento inválida. Usa el formato DD/MM/AAAA.")
        return

    curp = (
        apellido_paterno[0] + get_first_internal_vowel(apellido_paterno) +
        apellido_materno[0] +
        nombre[0] +
        anio + mes + dia +
        sexo[0] +
        estado[0:2] +
        get_first_internal_consonant(apellido_paterno) +
        get_first_internal_consonant(apellido_materno) +
        get_first_internal_consonant(nombre) + 
        "".join(rd.choice(clave) for _ in range(2))
    )

    result_var.set(curp)


def get_first_internal_vowel(word):
    for letter in word[1:]:
        if letter in "AEIOU":
            return letter
    return "X"

def get_first_internal_consonant(word):
    for letter in word[1:]:
        if letter in "BCDFGHJKLMNPQRSTVWXYZ":
            return letter
    return "X"

def validate_string():
    curp = result_var.get()
    print(curp)
    if len(curp) == 18:
        validation_result.set("CURP válida.")
    else:
        validation_result.set("CURP no válida.")

root = tk.Tk()
root.title("Generador y Validador de CURP")
root.geometry("600x450")

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20, expand=True)

fields = [
    ("Nombre", "nombre"),
    ("Apellido Paterno", "apellido_paterno"),
    ("Apellido Materno", "apellido_materno"),
    ("Fecha de Nacimiento (DD/MM/AAAA)", "fecha_nacimiento"),
    ("Sexo (H/M)", "sexo")
]

entries = {}

for i, (label_text, var_name) in enumerate(fields):
    label = tk.Label(main_frame, text=label_text)
    label.grid(row=i, column=0, pady=5, sticky='e')
    entry = tk.Entry(main_frame, width=30)
    entry.grid(row=i, column=1, pady=5)
    entries[var_name] = entry

nombre_entry = entries["nombre"]
apellido_paterno_entry = entries["apellido_paterno"]
apellido_materno_entry = entries["apellido_materno"]
fecha_nacimiento_entry = entries["fecha_nacimiento"]
sexo_entry = entries["sexo"]

label_estado = tk.Label(main_frame, text="Estado")
label_estado.grid(row=len(fields), column=0, pady=5, sticky='e')

estado_var = tk.StringVar(value="Selecciona un estado")
estados = [
    "AS - Aguascalientes", "BC - Baja California", "BS - Baja California Sur", "CC - Campeche", "CH - Chihuahua", "CL - Coahuila", "CM - Colima", "CS - Chiapas", "DF - Ciudad de México", "DG - Durango", "GT - Guanajuato", "GR - Guerrero", "HG - Hidalgo", 
    "JC - Jalisco", "MC - México", "MN - Michoacán", "MS - Morelos", "NE - Nacido en el Extranjero", "NL - Nuevo León", "NT - Nayarit", "OC - Oaxaca", "PL - Puebla", "QR - Querétaro", "QT - Quintana Roo", "SL - Sinaloa", "SP - San Luis Potosí", 
    "SR - Sonora", "TC - Tabasco", "TL - Tlaxcala", "TS - Tamaulipas", "VZ - Veracruz", "YN - Yucatán", "ZS - Zacatecas"
]
estado_menu = tk.OptionMenu(main_frame, estado_var, *estados)
estado_menu.config(width=27)
estado_menu.grid(row=len(fields), column=1, pady=5)

generate_button = tk.Button(main_frame, text="Generar CURP", command=generate_curp)
generate_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(main_frame, text="CURP generada:")
result_label.grid(row=len(fields)+2, column=0, pady=5)
result_entry = tk.Entry(main_frame, width=30, textvariable=result_var, state='readonly')
result_entry.grid(row=len(fields)+2, column=1, pady=5)

validate_button = tk.Button(main_frame, text="Validar CURP", command=validate_string)
validate_button.grid(row=len(fields)+3, column=0, columnspan=2, pady=10)

validation_result = tk.StringVar()
validation_label = tk.Label(main_frame, text="Resultado de validación:")
validation_label.grid(row=len(fields)+4, column=0, pady=5)
validation_entry = tk.Entry(main_frame, width=30, textvariable=validation_result, state='readonly')
validation_entry.grid(row=len(fields)+4, column=1, pady=5)

root.mainloop()
