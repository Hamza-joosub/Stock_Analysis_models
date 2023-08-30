import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime as dt
import tkinter as tk
#from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure
import ttkbootstrap as ttk


def GUI():
    storage = []
    def get_plot_Entry():
        x,y = entryx.get(),entryy.get()
        timeSeriesPlot(x,y)
    
    def get_data_entry():
        input = filename_entry.get()
        final_data = getData(input)
        storeData(final_data)
    
    def storeData(input_data):
        storage.append(input_data)
        
        
    def getData(filename): 
        
        raw = [ ]
        with open(filename) as f:
            for line in f:
                line = line.strip('\n')
                raw.append(list(line.split(";")))       
            data = np.array(raw)
        return data
        
    
    def timeSeriesPlot(inx,iny):
        data = getData("Book2.csv")
        figure = plt.Figure(figsize=(6,5), dpi=100)
        x = data[1:,inx]
        y = data[1:,iny]
        xlabel = data[0,inx]
        ylabel = data[0,iny]
        plot = figure.add_subplot(111)
        plot.plot(x,y)
        plot.set_title(f"{xlabel} vs {ylabel}")
        canvas = FigureCanvasTkAgg(figure, master = window)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
        
    def dataLegend(data):
        data = getData("Book2.csv")
        legend = ""
        total = data.shape[1]
        for i in range(0,total):
            label = data[0,i]
            legend = legend + f"Column{i}: {label}" + "\n"
        return legend
        
        
        
        
    window = ttk.Window("Journal")
    window.title("Tracker")
    window.geometry("1000x1000")
    #data = getData("Book2.csv")

    
    
    data_frame = ttk.Frame(master = window)
    data_frame.pack()
    filename_entry = tk.StringVar()
    data_entry = ttk.Entry(master = data_frame, textvariable=filename_entry)
    data_entry.pack()
    data_label = ttk.Label(master = data_frame, text = "Enter File Name")
    data_label.pack()
    data_button = ttk.Button(master = data_frame, text = "OK", command = get_data_entry)
    data_button.pack()
    data1 = get_data_entry()
    
    
    
    plot_frame = ttk.Frame(master = window)
    d_label = ttk.Label(text = "Choose dataset", master = plot_frame)
    d_label.pack()
    x_label = ttk.Label(text = "Choose X", master = plot_frame)
    x_label.pack()
    entryx = tk.IntVar()
    x_entry = ttk.Entry(master = plot_frame, textvariable=entryx)
    x_entry.pack()
    y_label = ttk.Label(text = "Choose Y", master = plot_frame)
    y_label.pack()
    entryy = tk.IntVar()
    y_entry = ttk.Entry(master = plot_frame, textvariable=entryy)
    y_entry.pack()
    
    
    
    
    plot_Button = ttk.Button(text = "Plot", master = plot_frame, command = get_plot_Entry)
    plot_Button.pack()
    plot_frame.pack()
    
    
    
    
    window.mainloop()



    
def main():
    #df = getData("Book2.csv")
    #print(timeSeriesPlot(df,0,2))
    #print(dataLegend(df))
    GUI()
    #plt.plot(x,y)
    
    
    
    
    
    
if __name__ == "__main__":
    main()
    
