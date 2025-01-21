"""
    @Author: Aymane Chabbaki
    @Date: 2021-05-10
    @Title: MD Converter
    @Description: 
        - Converte un file Markdown (.md) in un file PDF (.pdf) utilizzando la libreria markdown2 e pdfkit.
        - Richiede l'installazione di wkhtmltopdf.
        - Utilizza threading per eseguire la conversione in un thread separato.
        - Utilizza tkinter per l'interfaccia grafica.
"""

import tkinter
from tkinter import messagebox, filedialog
import markdown2
import pdfkit
import threading

# Funzione per aggiornare il messaggio di stato
def update_status(message):
    status_label.config(text=message)

# Funzione per selezionare il file .md
def select_md_file():
    md_file_path.set(filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")]))
    
# Funzione per selezionare il percorso di salvataggio del file .pdf
def select_pdf_save_path():
    pdf_save_path.set(filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")]))
    
# Funzione per convertire il file .md in .pdf
def convert_md_to_pdf():
    try:
        with open(md_file_path.get(), 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        html_content = markdown2.markdown(md_content)
        pdfkit.from_string(html_content, pdf_save_path.get(), configuration=config)
        messagebox.showinfo("Successo", "Il file è stato convertito con successo!")
    except Exception as e:
        messagebox.showerror("Errore", f"Si è verificato un errore durante la conversione: {str(e)}")

# Funzione per eseguire la conversione in un thread separato
def convert_md_to_pdf_threaded():
    threading.Thread(target=convert_md_to_pdf).start()
    update_status("Conversione in corso...")

# Creazione della finestra principale
window = tkinter.Tk()
window.title("MD Converter")
window.geometry('520x620')
window.configure(bg='#333333')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame = tkinter.Frame(window, bg='#333333')
frame.grid(sticky="nsew")
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_rowconfigure(4, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

# Variabili per i percorsi dei file
md_file_path = tkinter.StringVar()
pdf_save_path = tkinter.StringVar()

# Imposta manualmente il percorso dell'eseguibile di wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')  # Modifica questo percorso secondo la tua installazione

# Creazione dei widget
convert_label = tkinter.Label(frame, text="CONVERCHABBY", bg='#333333', fg="#FF3399", font=("Arial", 30))
pathConvert_label = tkinter.Label(frame, text="Path File to Convert", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
pathConvert_entry = tkinter.Entry(frame, textvariable=md_file_path, font=("Arial", 16))
pathConvert_button = tkinter.Button(frame, text="Browse", command=select_md_file, bg="#FF3399", fg="#FFFFFF", font=("Arial", 12))
pathSave_label = tkinter.Label(frame, text="Path File to Save", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
pathSave_entry = tkinter.Entry(frame, textvariable=pdf_save_path, font=("Arial", 16))
pathSave_button = tkinter.Button(frame, text="Browse", command=select_pdf_save_path, bg="#FF3399", fg="#FFFFFF", font=("Arial", 12))
convert_button = tkinter.Button(frame, text="CONVERT", command=convert_md_to_pdf_threaded, bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))
status_label = tkinter.Label(frame, text="", bg='#333333', fg="#FFFFFF", font=("Arial", 12))

# Posizionamento dei widget
convert_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40)
pathConvert_label.grid(row=1, column=0, pady=20, sticky="e")
pathConvert_entry.grid(row=1, column=1, pady=20, sticky="ew")
pathConvert_button.grid(row=1, column=2, pady=10, sticky="w")
pathSave_label.grid(row=2, column=0, pady=20, sticky="e")
pathSave_entry.grid(row=2, column=1, pady=20, sticky="ew")
pathSave_button.grid(row=2, column=2, pady=10, sticky="w")
convert_button.grid(row=3, column=0, columnspan=3, pady=20, sticky="news")
status_label.grid(row=4, column=0, columnspan=3, pady=10, sticky="news")

# Avvio del loop della finestra
window.mainloop()