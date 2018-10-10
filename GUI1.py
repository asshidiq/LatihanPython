#!/usr/bin/env python
# coding: utf-8

# In[21]:


from tkinter import *

app = Tk()
app.title("Python Desktop Application")
app.geometry("600x400")

judul = Label(app, text="Python Application", font="Calibri 20 bold", fg="blue")
judul.pack(side="top")

def ubahjudul():
    judul.configure(text="Thank you")

btn1 = Button(app, text="Click Me", command=ubahjudul)
btn1.pack(side="top")

btn2 = Button(app, text="Exit", command=quit)
btn2.pack()

app.mainloop()


# In[ ]:





# In[ ]:




