import tkinter as tk
import yf

def dl:
  try:
    code = ent.get()
    df = yf.YahooFinanceHistory().get_data(code)
  except:
    lbl['text'] = 'Fail'
  else:
    df.to_csv('./Record.csv')
    lbl['text'] = 'Success!'
    
window = tk.Tk()
window.geometry('800x800')
window.title('History record downloader')
tk.Label(window, text = 'Please input the num of the stock').pack()
ent = tk.Entry(window)
ent.pack()
tk.Button(window, text='Start to download', command = download).pack()
lbl = tk.Label(window, width = 60, height = 10)
lbl.pack()
window.mainloop()
