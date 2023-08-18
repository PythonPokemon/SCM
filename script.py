import tkinter as tk
import sqlite3

class SCMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Einfache SCM App")

        # Verbindung zur Datenbank herstellen
        self.conn = sqlite3.connect('scm_app.db')
        self.cursor = self.conn.cursor()

        # Tabelle erstellen, falls nicht vorhanden
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS demand_forecast (
                id INTEGER PRIMARY KEY,
                product_name TEXT,
                forecasted_demand INTEGER
            )
        ''')
        self.conn.commit()

        # GUI-Elemente erstellen
        self.product_label = tk.Label(root, text="Produkt:")
        self.product_label.pack()

        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.pack()

        self.forecast_label = tk.Label(root, text="Prognostizierte Nachfrage:")
        self.forecast_label.pack()

        self.forecast_entry = tk.Entry(root)
        self.forecast_entry.pack()

        self.add_forecast_button = tk.Button(root, text="Prognose hinzufügen", command=self.add_forecast)
        self.add_forecast_button.pack()

        self.show_forecasts_button = tk.Button(root, text="Prognosen anzeigen", command=self.show_forecasts)
        self.show_forecasts_button.pack()

    def add_forecast(self):
        product_name = self.product_name_entry.get()
        forecast = int(self.forecast_entry.get())

        # Hier fügen Sie die Prognose in die Datenbank ein
        self.cursor.execute("INSERT INTO demand_forecast (product_name, forecasted_demand) VALUES (?, ?)", (product_name, forecast))
        self.conn.commit()

        self.product_name_entry.delete(0, tk.END)  # Felder leeren nach dem Hinzufügen
        self.forecast_entry.delete(0, tk.END)

    def show_forecasts(self):
        self.cursor.execute("SELECT * FROM demand_forecast")
        forecasts = self.cursor.fetchall()
        for forecast in forecasts:
            print(forecast)  # Hier könnten Sie die Prognosen in einem separaten Fenster anzeigen

if __name__ == "__main__":
    root = tk.Tk()
    app = SCMApp(root)
    root.mainloop()
