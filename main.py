import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from tkinter import messagebox
import seaborn as sns
from tabulate import tabulate
# defining functions
sets = sns.get_dataset_names()
dict1 = {"Data":sets}
df = pd.DataFrame(dict1)

def save():
    file_name = file_input.get()
    per = 0
    try:
        data = pd.read_csv(file_name)
    except FileNotFoundError:
        per = messagebox.showerror("Missing","You haven't provided file name")
    if(not(per)):
        gui.geometry("700x500")
        t.destroy()
        file_text.destroy()
        file_input.destroy()
        upload_button.destroy()
        canvas.destroy()
        tk_label = Label(text="ITEMS OF YOUR FILE",font=("Arial",13,"bold"),bg="yellow")
        tk_label.grid(row=0,column=1)
        k,p,m = 2,2,2
        heading1 = Label(text="Columns of data",font=("Arial",13,"bold"),bg="red")
        heading1.grid(row=1,column=1,pady=10,padx=10)
        for i in data.columns:
            item_text = Label(text="{:<10}".format(f"{i}"),font=("Arial",12,"bold"),bg="sky blue")
            item_text.grid(row=k,column=1)
            k+=1
        graphs_type = ["Line","Bar","Histogram","Scatter"]
        heading3 = Label(text="Types of Graphs",font=("Arial",13,"bold"),bg="red")
        heading3.grid(row=1,column=2,pady=10,padx=10)
        for  j in graphs_type:
            graph_text = Label(text="{:<10}".format(f"{j}"),font=("Arial",12,"bold"),bg="sky blue")
            graph_text.grid(row=m,column=2)
            m+=1

        column_text = Label(text="Enter name of column : ",font=("Arial",13,"bold"),bg="light green")
        column_text.grid(row=8,column=1,pady=10,padx=10)
        column_entry = Entry(width=20,font=("Arial",13,"bold"))
        column_entry.grid(row=8,column=2,padx=10,pady=10)
        column_entry.focus()
        # heading2 = Label(text="Species of data", font=("Arial", 13, "bold"), bg="red")
        def ok():
            try:
                new_win = Toplevel(gui)
                column_input1 = column_entry.get()
                new_win.title(f"{column_input1} Information")
                # dt = {f"{column_input1}":data[column_input1]}
                column_d = data[column_input1].unique()
                sb = Scrollbar(new_win,orient="vertical",bg="red",width=30)
                sb.grid(row=1,column=3,sticky=NS)
                my_list = Listbox(new_win,height=30,width=20,yscrollcommand=sb.set,font=10)
                my_list.grid(row=1,column=2)
                for i in column_d:
                    my_list.insert(END,i)
                sb.config(command=my_list.yview)
            except KeyError:
                messagebox.showerror("Missing Arguements","Please fill the box")

        def heat_plot():
            heat_dict = {}
            for i in data.columns:
                l1 = str(type(data[i][0]))
                if(l1[8:11]!="str"):
                    heat_dict[i] = list(data[i])
            heat_df = pd.DataFrame(heat_dict)
            sns.heatmap(heat_df.corr())
            plt.show()

        def filter_plot():
            try:
                column_input = column_entry.get()
                species = species_entry.get()
                species_data = data[data[column_input] == species]
                x_cor = x_entry.get()
                y_cor = y_entry.get()
                graph = graph_entry.get()
                plt.title(f"{x_cor} VS {y_cor}")
                plt.xlabel(x_cor)
                plt.ylabel(y_cor)
                if (graph == "Bar"):
                    plt.bar(species_data[x_cor],species_data[y_cor])
                    plt.show()
                elif (graph == "Line"):
                    plt.plot(species_data[x_cor],species_data[y_cor])
                    plt.show()
                elif (graph == "Histogram"):
                    plt.hist(species_data[y_cor], bins=np.arange(4, 6, 0.5))
                    plt.show()
                else:
                    plt.scatter(species_data[x_cor], species_data[y_cor])
                    plt.show()
            except KeyError:
                messagebox.showerror("Missing Arguements","Please fill the box")


        def plot():
            try:
                # column_input = column_entry.get()
                x_cor = x_entry.get()
                y_cor = y_entry.get()
                graph = graph_entry.get()
                plt.title(f"{x_cor} VS {y_cor}")
                plt.xlabel(x_cor)
                plt.ylabel(y_cor)
                if (graph == "Bar"):
                    plt.bar(data[x_cor],data[y_cor])
                    plt.show()
                elif (graph == "Line"):
                    plt.plot(data[x_cor],data[y_cor])
                    plt.show()
                elif (graph == "Histogram"):
                    plt.hist(data[y_cor], bins=np.arange(4, 6, 0.5))
                    plt.show()
                else:
                    plt.scatter(data[x_cor], data[y_cor])
                    plt.show()
            except KeyError:
                messagebox.showerror("Missing Arguements","Please fill the box")
        y_para = Label(text="Enter Parameter on Y axis : ",font=("Arial",13,"bold"),bg="light green")
        y_para.grid(row=9,column=1,padx=10,pady=10)
        y_entry = Entry(width=20,font=("Arial",12,"bold"))
        y_entry.grid(row=9,column=2,padx=10,pady=10)

        x_para = Label(text="Enter Parameter on X axis : ",font=("Arial",13,"bold"),bg="light green")
        x_para.grid(row=10,column=1,padx=10,pady=10)
        x_entry = Entry(width=20,font=("Arial",12,"bold"))
        x_entry.grid(row=10,column=2,padx=10,pady=10)

        graph_head = Label(text="Enter Type of Graph : ",font=("Arial",13,"bold"),bg="light green")
        graph_head.grid(row=11,column=1,padx=10,pady=10)
        graph_entry = Entry(width=20,font=("Arial",13,"bold"))
        graph_entry.grid(row=11,column=2,pady=10,padx=10)

        species_text = Label(text="Enter filter by : ",font=("Arial",13,"bold"),bg="light green")
        species_text.grid(row=12,column=1,padx=10,pady=10)
        species_entry = Entry(width=20,font=("Arial",13,"bold"))
        species_entry.grid(row=12,column=2,pady=10,padx=10)

        ok_button = Button(text="Ok", font=("Arial", 13, "bold"),width=15, command=ok)
        ok_button.grid(row=7, column=3, columnspan=2, padx=10)

        plot_button = Button(text="Plot",font=("Arial",13,"bold"),width=15,command=plot)
        plot_button.grid(row=8, column=3, columnspan=2, padx=10)

        filter_button = Button(text="Filter",font=("Arial",12,"bold"),width=15,command=filter_plot)
        filter_button.grid(row=9,column=3,columnspan=2,padx=10)

        def pair_plot():
            def show_pair_plot():
                def final_plot():
                    hueds = columnds.get()
                    sns.pairplot(sns_ds,hue=hueds)
                    plt.show()

                sns_dataset = dataset_entry.get()
                new_new_window = Toplevel(gui)
                sns_ds = sns.load_dataset(sns_dataset)
                dict1 = {f"{sns_dataset}":sns_ds.columns}
                df1 = pd.DataFrame(dict1)
                window_level = Label(new_new_window,text=f"{df1}",font=("Arial",13,"bold"))
                window_level.grid(row=0,column=1,pady=10,padx=10)
                ds_text = Label(new_new_window,text="Enter Column : ",font=("Arial",13,"bold"))
                ds_text.grid(row=len(sns_ds.columns)+1,column=0,pady=10,padx=10)
                columnds = Entry(new_new_window,font=("Arial",13,"bold"),width=20)
                columnds.grid(row=len(sns_ds.columns)+1,column=1,padx=10,pady=10)
                final_button = Button(new_new_window,text="Plot",font=("Arial",13,"bold"),width=15,command=final_plot)
                final_button.grid(row=len(sns_ds.columns)+2,column=1,columnspan=2,pady=10)

            pair_window = Toplevel(gui)
            pair_window.title("Pair Plot")
            pair_window.config(bg="pink")
            # data_sets = sns.get_dataset_names()
            pair_window_label = Label(pair_window,text=f"{df}",font=("Arial",13,"bold"),bg="pink")
            pair_window_label.grid(row=0,column=1)
            dataset_text = Label(pair_window,text="Enter Dataset : ",font=("Arial",13,"bold"),bg="pink")
            dataset_text.grid(row=22,column=1,padx=10,pady=10)
            dataset_entry = Entry(pair_window,font=("Arial",13,"bold"),width=20)
            dataset_entry.grid(row=22,column=2,padx=10,pady=10)
            dataset_entry.focus()
            sns_button = Button(pair_window,text="Pair plot",font=("Arial",13,"bold"),width=15,command=show_pair_plot)
            sns_button.grid(row=23,column=1,columnspan=2,padx=10,pady=10)

        def detail():
            new_window = Toplevel(gui)
            new_window.config(width = 20,bg="black")
            ce = column_entry.get()
            se = species_entry.get()
            new_window.title(f"Details of {se}")
            s_data = data[data[ce] == se]
            dict1 = {}
            for i in data.columns:
                dict1[i] = s_data[i]
            df = pd.DataFrame(dict1)
            # messagebox.showinfo("More Details",f"{df.describe().transpose()}")
            txt1 = Label(new_window, text=f"{df.describe().transpose()}",font=("Arial",13,"bold"))
            txt1.grid(row=1,column=1)
        details_button = Button(text="Details",font=("Arial",13,"bold"),width=15,command=detail)
        details_button.grid(row=10,column=3,columnspan=2,padx=10)

        pair_plot_button = Button(text="Pair Plot",font=("Arial",13,"bold"),width=15,command=pair_plot)
        pair_plot_button.grid(row=11,column=3,columnspan=2,padx=10)

        heat_button = Button(text="Heatmap",font=("Arial",12,"bold"),width=15,command=heat_plot)
        heat_button.grid(row=12,column=3,columnspan=2,padx=10)

        exit_button = Button(text="Exit",font=("Arial",13,"bold"),width=15,command=gui.destroy)
        exit_button.grid(row=13,column=3,columnspan=2,padx=10)

gui = Tk(className = "Graphs interface")
gui.geometry("520x400")
gui.config(bg="sky blue")

t = Label(gui,text="Welcome to Graph viewer",font=("Arial",14,'italic'),bg="sky blue")
t.grid(row=0,column=1,pady=10,columnspan=2)

canvas = Canvas(width=260,height=200,bg="sky blue")
logo = PhotoImage(file="images.png")
canvas.create_image(130,100,image = logo)
canvas.grid(row=1,column=1,columnspan=2)

file_text = Label(text="Enter file name.csv : ",font=("Arial",13,'bold'),bg="sky blue")
file_text.grid(row=3,column=1,pady=20,padx=5)
file_input = Entry(width=30,font=("Arial",12,"bold"))
file_input.insert(0,".csv")
file_input.focus()
file_input.grid(row=3,column=2,pady=20)

upload_button = Button(text="Upload",font=("Arial",12,"bold"),command=save)
upload_button.config(width=15)
upload_button.grid(row=4,column=2,columnspan=2)


gui.mainloop()