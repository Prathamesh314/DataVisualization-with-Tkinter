import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tabulate import tabulate
import seaborn as sns

data = pd.read_csv("iris_nonull.csv")
# country_data = list(data["country"].unique())
# x_data = list(country_data["city"])
# y_data = list(country_data["lat"])
setosa_data = data[data.Species=="iris-setosa"]
dict1 = {}
# print(data["country"][0])
for i in setosa_data.columns:
    l1 = str(type(setosa_data[i][0]))
    if(l1[8:11]!="str"):
        dict1[i] = list(setosa_data[i])
# print(type(l1[1:6]))
# print(l1[6:12]=='clas')

# if(l1[6:12])
# print(str(type(country[0]))[6:12])
# df = pd.DataFrame(dict1)
# print(len(list(country_data["city"])))
# loop_idx = int(len(list(country_data["city"]))//40)
# gui = Tk()
# gui.config(width=200,bg="light blue")
# sb = Scrollbar(gui)
# sb.grid(row=3,column=4,sticky='w')

# my_list = Listbox(gui,height=40,width=20,yscrollcommand=sb.set,font=12)
# my_list.grid(row=1,column=2)
# for country in country_data:
#     my_list.insert(END,country)

# sb.config(command=my_list.yview)
# label = Label(text = f"{tabulate(df,tablefmt='fancy_grid')}",font=("Arial",12,"bold"))
# label.grid(row=0,column=2)

# next_button = Button(text="Next",font=("Arial",12,"bold"),width=20,bg="green")
# next_button.grid(row=19,column=4,columnspan=3,padx=10,pady=10)

# gui.mainloop()

# print(y_data)
# plt.figure(figsize=(50,50))
# plt.rcParams['figure.figsize']=[4,4]
# plt.figure().set_figwidth(20)
# plt.xticks(rotation=90,ha="right")
# plt.plot(x_data,y_data)
# plt.show()

# india_data = data[data.country=="India"]
# print(df.corr)
# sns.heatmap(df.corr())
# plt.show()
# plt.bar(data["country"],data["lng"])
# plt.show()
# print(dict1)

df = pd.DataFrame(dict1)
# print(df)
print(df.describe().transpose())
print(tabulate(df.describe().transpose()))
# print(df.corr())
# plt.plot(data["SepalLengthCm"],data["PetalWidthCm"])
# sns.heatmap(df.corr())
# plt.show()

