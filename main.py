# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# set1 = set({})
# with open("cs.txt",'r') as file:
#     data = file.readlines()
#     for i in data:
#         words = i.split()
#         for word in words:
#             set1.add(word)
# print(set1)

# import pytube
#
# link = input("Youtube video linke: ")
# video_download = pytube.YouTube(link)
# video_download.streams.first().download()
#
# print("Downloaded",link)

# from stegano import lsb
#
# secret = lsb.hide("images.png",
#                   "Be careful python is dangerous")
# secret.save("sample_secret.png")
# lsb.reveal("sample_secret.png")

import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show','profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

for i in profiles:
    result = subprocess.check_output(['netsh', 'wlan', 'show','profiles',i,'key=clear']).decode('utf-8').split('\n')

    result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]
    try:
        print("{:<30}  {:}".format(i,result[0]))
    except IndexError:
        print("{:<30}  {:}".format(i, ""))
