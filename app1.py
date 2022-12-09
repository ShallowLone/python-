import tkinter as tk
import requests
from bs4 import BeautifulSoup

class YahooFinanceHistory:
    # URL for the Yahoo Finance page for a given stock code
    _url = 'https://hk.finance.yahoo.com/quote/{code}.HK/history?p={code}.HK'

    def __init__(self):
        # Initialize the GUI window
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Yahoo股票历史数据转换器")

        # Initialize GUI widgets
        self.code_label = tk.Label(self.root, text="股票代码：")
        self.code_entry = tk.Entry(self.root)
        self.get_data_button = tk.Button(self.root, text="获取数据", command=self.get_data)

        # Layout the widgets
        self.code_label.pack()
        self.code_entry.pack()
        self.get_data_button.pack()

        # Start the GUI event loop
        self.root.mainloop()

    def get_data(self):
        # Get the stock code entered by the user
        code = self.code_entry.get()

        # Construct the URL for the Yahoo Finance page for the stock code
        url = self._url.format(code=code)

        # Make a web request to the URL
        web = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15(KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'})

        # Check if the request was successful
        if web.status_code == 200:
            # Parse the HTML response
            soup = BeautifulSoup(web.text, "lxml")

            # Find the table containing the historical stock data
            table = soup.find("div", {"id":"Main"}).find("table", {"class": "historical-prices"})

            # Extract the data from the table
            data = []
            trs = table.find_all("tr")
            for tr in trs:
                cells = tr.find_all(["th", "td"])
                row = []
                for cell in cells:
                    row.append(cell.text.strip("*"))
                data.append(row)

            # Print the data to the console
            print(data)
