# python-tkinter-matplotlib
Data Visualization using Tkinter and Matplotlib
You can visualize any data by just using this GUI and you don't have to write code
for any specific task.

## Instructions to Use
1. Upload a csv[Comma Separated File] and make sure that file is available in the same folder
    where the program is located and also you must have all the images of the repository in you folder, because
    I have used them in my GUI.
2. You can now see name of columns in your csv file, you can type any column name in Entry box
    to view details of that columns
3. You can enter X and Y Parameters in their respective Entry Boxes and enter which type of 
    plot you want to plot [Line,Bar,Histogram,Scatter] and then click on Plot Button to see the plot.
4. You can plot data according to a specific species using "Filter plot" button, for ex:- In 
    iris dataset, you can filter according to it's species [setosa,versicolor,virginica].
5. You can view details like [Min, Max, Mean, Median] of the data by clicking on "Details" button.
6. You can use Beautiful features of Seaborn i.e. Pairplot and Heatmap in this GUI just by
    clicking on "Pairplot" and "Heatplot" Button respectively.
6 (a). After clicking on "Pairplot" button you can see all the available datasets in Seaborn,
        you have to enter the name of any of the datasets.
6 (b). After entering a dataset,you have to enter name of the column whose unique values you want 
        want to compare. For ex:- If you select "species" in "iris" dataset, it will pairplot according to it's species [setosa,virginica,versicolor].It selects unique value of that 
        column and plot it.
7. You can click on "Exit" Button to exit.

# Here's how it looks like
##### First Page
<img src="screenshots\Screenshot_20230223_221231.png" />

##### Second Page
<img src="screenshots\Screenshot_20230223_222954.png" />

##### Details of column you enter
<img src="screenshots\Screenshot_20230223_221324.png" />

##### Plot for given x and y parameters 

Normal Plot :- <img src="screenshots\Screenshot_20230223_221544.png" />

Zoomed Plot :- <img src="screenshots\Screenshot_20230223_223817.png" />

##### Details of the file [Min,Max,Count,Percentile]

#### Data 1:- <img src="screenshots\Screenshot_20230223_230633.png" />

#### Data 2:- <img src="screenshots\Screenshot_20230223_230743.png" />


##### Screen which shows available datasets in Seaborn

<img src="screenshots\Screenshot_20230223_223836.png" />
<img src="screenshots\Screenshot_20230223_223836.png" />

##### Pairplot filtered by Species

<img src="screenshots\Screenshot_20230223_223911.png" />

##### Heatmap

<img src="screenshots\Screenshot_20230223_223926.png" />