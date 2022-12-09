 def __init__(self):
        # Initialize the window
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Yahoo Stock Data Crawler")

        # Initialize the widgets
        self.code_label = tk.Label(self.root, text="Stock Code:")
        self.code_entry = tk.Entry(self.root)
        self.get_data_button = tk.Button(self.root, text="Get Data", command=self.get_data)
        self.save_as_csv_button = tk.Button(self.root, text="Save as CSV", command=self.save_as_csv)
        self.local_time_label = tk.Label(self.root, text="")
        self.elapsed_time_label = tk.Label(self.root, text="")

        # Layout the widgets
        self.code_label.pack()
        self.code_entry.pack()
        self.get_data_button.pack()
        self.save_as_csv_button.pack()
        self.local_time_label.pack()
        self.elapsed_time_label.pack()

        # Start the window
        self.root.mainloop()
