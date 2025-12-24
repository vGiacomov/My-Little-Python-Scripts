import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Toplevel
from math import pi
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class AirflowCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator przepływu powietrza i wizualizacja")
        self.root.geometry("850x640")
        self.root.resizable(False, False)

        self.create_input_fields()
        self.create_output_table()

    def create_input_fields(self):
        frame = ttk.LabelFrame(self.root, text="Parametry wejściowe")
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        fields = [
            ("Średnica wentylatora (cm):", "fan_diameter_entry"),
            ("Średnica rdzenia (cm):", "core_diameter_entry"),
            ("Prędkość powietrza dla każdego RPM (m/s, rozdzielone przecinkami):", "air_speeds_entry"),
            ("Od obrotów (RPM):", "rpm_start_entry"),
            ("Do obrotów (RPM):", "rpm_end_entry"),
            ("Krok obrotów (RPM):", "rpm_step_entry"),
        ]

        for row, (label_text, attr_name) in enumerate(fields):
            ttk.Label(frame, text=label_text).grid(
                row=row, column=0, padx=5, pady=5, sticky="w"
            )
            entry = ttk.Entry(frame)
            entry.grid(row=row, column=1, padx=5, pady=5)
            setattr(self, attr_name, entry)

        # Buttons
        ttk.Button(frame, text="Oblicz", command=self.calculate).grid(row=len(fields), column=0, pady=10)
        ttk.Button(frame, text="Zapisz do pliku", command=self.save_to_file).grid(row=len(fields), column=1, pady=10)
        ttk.Button(frame, text="Wygeneruj wykres", command=self.generate_plot).grid(row=9, column=0, columnspan=2, pady=10)



    def create_output_table(self):
        frame = ttk.LabelFrame(self.root, text="Wyniki")
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.tree = ttk.Treeview(frame, columns=("RPM", "Prędkość (m/s)", "Głośność (dB)", "Przepływ (m^3/h)", "Przepływ (CFM)"), show="headings")
        self.tree.heading("RPM", text="Obroty (RPM)")
        self.tree.heading("Prędkość (m/s)", text="Prędkość powietrza (m/s)")
        self.tree.heading("Głośność (dB)", text="Głośność (dB)")
        self.tree.heading("Przepływ (m^3/h)", text="Przepływ powietrza (m^3/h)")
        self.tree.heading("Przepływ (CFM)", text="Przepływ powietrza (CFM)")
        self.tree.pack(fill="both", expand=True)

    def calculate(self):
        # Get inputs
        try:
            fan_diameter_cm = float(self.fan_diameter_entry.get())
            core_diameter_cm = float(self.core_diameter_entry.get())
            air_speeds = list(map(float, self.air_speeds_entry.get().split(",")))
            sound_levels = list(map(float, self.sound_levels_entry.get().split(",")))
            rpm_start = int(self.rpm_start_entry.get())
            rpm_end = int(self.rpm_end_entry.get())
            rpm_step = int(self.rpm_step_entry.get())

            fan_radius = (fan_diameter_cm / 2) / 100  # Convert diameter to radius in meters
            core_radius = (core_diameter_cm / 2) / 100  # Convert diameter to radius in meters

            if fan_radius <= core_radius:
                raise ValueError("Średnica wentylatora musi być większa niż średnica rdzenia.")

        except ValueError as e:
            messagebox.showerror("Błąd danych wejściowych", f"Niepoprawne dane: {e}")
            return

        # Calculate airflow
        fan_area = pi * fan_radius ** 2
        core_area = pi * core_radius ** 2
        effective_area = fan_area - core_area

        if effective_area <= 0:
            messagebox.showerror("Błąd obliczeń", "Pole wentylatora musi być większe niż pole rdzenia.")
            return

        self.tree.delete(*self.tree.get_children())  # Clear previous results

        rpms = range(rpm_start, rpm_end + 1, rpm_step)
        if len(air_speeds) != len(rpms) or len(sound_levels) != len(rpms):
            messagebox.showerror("Błąd danych wejściowych", "Liczba prędkości i głośności musi odpowiadać liczbie obrotów RPM.")
            return

        self.results = []  # Store results for saving to file and plotting

        for rpm, air_speed, sound_level in zip(rpms, air_speeds, sound_levels):
            airflow_m3h = effective_area * air_speed * 3600  # m^3/h
            airflow_cfm = airflow_m3h * 0.58858   # Convert to CFM
            self.tree.insert("", "end", values=(rpm, air_speed, sound_level, round(airflow_m3h, 2), round(airflow_cfm, 2)))
            self.results.append((rpm, sound_level, round(airflow_cfm, 2)))

    def save_to_file(self):
        if not hasattr(self, 'results') or not self.results:
            messagebox.showerror("Błąd", "Brak wyników do zapisania. Proszę najpierw przeprowadzić obliczenia.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")])
        if not file_path:
            return  # User cancelled save dialog

        try:
            with open(file_path, "w") as f:
                rpms = [str(result[0]) for result in self.results]
                f.write("Prędkość wentylatora (RPM): [" + ", ".join(rpms) + "]\n")

                sound_levels = [str(result[1]) for result in self.results]
                f.write("Głośność (dB): [" + ", ".join(sound_levels) + "]\n")

                cfm_values = [str(result[2]) for result in self.results]
                f.write("Przepływ powietrza (CFM): [" + ", ".join(cfm_values) + "]\n")

            messagebox.showinfo("Sukces", f"Wyniki zostały zapisane do pliku {file_path}.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się zapisać pliku: {e}")

    def generate_plot(self):
        if not hasattr(self, 'results') or not self.results:
            messagebox.showerror("Błąd", "Brak wyników do wyświetlenia. Proszę najpierw przeprowadzić obliczenia.")
            return

        data = {
            "Prędkość wentylatora (RPM)": [result[0] for result in self.results],
            "Głośność (db)": [result[1] for result in self.results],
            "Przepływ powietrza (CFM)": [result[2] for result in self.results]
        }

        def prepare_data(data):
            df = pd.DataFrame(data)
            return df

        def set_styles_and_colors():
            sns.set(style="darkgrid")
            plt.style.use("dark_background")
            return sns.color_palette("afmhot", n_colors=3)

        df = prepare_data(data)

        fig, ax1 = plt.subplots(figsize=(19, 9), dpi=100)

        palette = set_styles_and_colors()

        ax1.plot(df["Prędkość wentylatora (RPM)"], df["Głośność (db)"], label="Sound Level (dB)", color=palette[2], linewidth=2, marker="o")
        ax1.set_xlabel("Prędkość wentylatora (RPM)", fontsize=10, color="white")
        ax1.set_ylabel("Głośność (db)", fontsize=10, color=palette[2])
        ax1.tick_params(axis='y', labelcolor=palette[2])
        ax1.tick_params(axis='x', colors="white")
        ax1.xaxis.set_major_locator(plt.MultipleLocator(100))
        ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
        ax1.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

        for x, y in zip(df["Prędkość wentylatora (RPM)"], df["Głośność (db)"]):
            ax1.text(x, y - 1, f"{y}", color=palette[2], fontsize=8, ha='center')

        ax2 = ax1.twinx()
        ax2.plot(df["Prędkość wentylatora (RPM)"], df["Przepływ powietrza (CFM)"], label="Airflow (CFM)", color=palette[1], linewidth=2, marker="s")
        ax2.set_ylabel("Przepływ powietrza (CFM)", fontsize=10, color=palette[1])
        ax2.tick_params(axis='y', labelcolor=palette[1])
        ax2.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
        ax2.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

        for x, y in zip(df["Prędkość wentylatora (RPM)"], df["Przepływ powietrza (CFM)"]):
            ax2.text(x, y + 1.75, f"{y:.1f}", color=palette[1], fontsize=8, ha='center')

        ax1.set_facecolor("#3C3C3C")
        fig.patch.set_facecolor("#3C3C3C")

        plot_title = self.plot_title_entry.get().strip() or "Głośność i przepływ powietrza wentylatorów"
        plt.title(plot_title, fontsize=12, color="white")

        # Create a new window for the plot
        plot_window = Toplevel(self.root)
        plot_window.title("Wykres")

        canvas = FigureCanvasTkAgg(fig, master=plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar_frame = tk.Frame(plot_window)
        toolbar_frame.pack(side=tk.BOTTOM, fill=tk.X)

        def save_plot():
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("Image files", "*.png"), ("All files", "*.*")])
            if file_path:
                fig.set_size_inches(1920/fig.dpi, 1080/fig.dpi)  # Set figure size to 3840x2160 pixels
                fig.savefig(file_path)
                messagebox.showinfo("Sukces", f"Wykres został zapisany do pliku {file_path}.")

        ttk.Button(toolbar_frame, text="Zapisz wykres", command=save_plot).pack(side=tk.RIGHT, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = AirflowCalculator(root)
    root.mainloop()
