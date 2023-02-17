import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# sets = sns.get_dataset_names()
# # print(sets[:11])
# # print(sets[11:])
#
# dict1 = {"Data":sets}
# df = pd.DataFrame(dict1)
# df = df
# print(df)

iris = sns.load_dataset("iris")
dict1 = {"iris":iris.columns}
# print(iris.columns)
# sns.pairplot(iris,hue="species")
# plt.show()
df = pd.DataFrame(dict1)
print(df)
