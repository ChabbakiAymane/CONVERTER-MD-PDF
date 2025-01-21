# CHABBY-CONVERTER

## **Descrizione**

**Chabby Converter** è un'applicazione GUI che consente di convertire file Markdown (**.md**) in file PDF (**.pdf**) utilizzando:

- *markdown2* per la conversione da Markdown a HTML
- *pdfkit* per la conversione da HTML a PDF
- *tkinter* per l'interfaccia grafica

L'app supporta l'esecuzione multithreading per garantire che l'interfaccia utente rimanga reattiva durante la conversione.

## **Funzionalità**

- Selezione del file Markdown da convertire.
- Selezione del percorso di salvataggio del file PDF.
- Conversione in un thread separato per migliorare l'esperienza utente.
- Notifiche di successo o errore durante il processo di conversione.

## **Requisiti**

- Python 3.x
- Moduli Python:
  - tkinter
  - markdown2
  - pdfkit

## **Software esterno**:

- wkhtmltopdf (necessario per pdfkit)

## **Installazione**

  1. Installare [Python 3.x](https://www.python.org/downloads/)

  2. Moduli Python:

      ```bash pip install markdown2```

      ```bash pip install pdfkit```

  3. Installare [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

      Installa il software e annota il percorso dell'eseguibile (```C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe```).

  4. Aggiorna il percorso dell'eseguibile nel file Python (linea 70):

      ```config = pdfkit.configuration(wkhtmltopdf='Percorso\wkhtmltopdf.exe')```

## **Utilizzo**

Avvia il programma eseguendo il file Python:

  ```bash
    python md_converter.py
  ```

Segui questi passi nell'interfaccia grafica:

- Clicca su Browse accanto a "*Path File to Convert*" per selezionare il file **.md**.

- Clicca su Browse accanto a "*Path File to Save*" per scegliere dove salvare il file **.pdf**.

- Clicca su *CONVERT* per avviare la conversione.

---

Nella cartella *exe* vi è l'eseguibile già compilato ed pronto per l'utilizzo. 

## **Note**

Assicurati che il file *.md* sia valido e che il percorso di salvataggio abbia i permessi necessari.

Il percorso di **wkhtmltopdf** deve essere configurato correttamente per evitare errori.
