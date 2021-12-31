import tkinter as tk
from tkinter.constants import ANCHOR, W
import main
from tkinter import messagebox
  
root=tk.Tk()
root.title("Miller Indices Representer")
 
# setting the windows size
root.geometry("600x400")
 

def plot():

    try:

        neg = True
        x=abs(int(x_txt.get("1.0","end")))
        y=abs(int(y_txt.get("1.0","end")))
        z=abs(int(z_txt.get("1.0","end")))

        if int(x_txt.get("1.0","end"))==x:
            if int(y_txt.get("1.0","end"))==y:
                if int(z_txt.get("1.0","end"))==z:
                    neg = False

        main.clear()
        main.cube()
    
        main.Plot(x, y, z, neg)
    except:
        messagebox.showerror("Error", "Please provide valid input")

     
     
pro_title = tk.Label(root, text="Miller Representer", padx=5, pady=5, font=('Arial',20, 'bold'))

member = tk.Label(root, text="Contributors", padx=5, pady=5, font=('calibre',10, 'bold'))
members1 = tk.Label(root, text="41. Mehul Phatangare", padx=5, pady=5, font=('calibre',10, 'bold'))
members2 = tk.Label(root, text="42. Vansh Purohit", padx=5, pady=5, font=('calibre',10, 'bold'))
members3 = tk.Label(root, text="43. Moiz Rajkotwala", padx=5, pady=5, font=('calibre',10, 'bold'))
members4 = tk.Label(root, text="44. Rajeshwari Raorane", padx=5, pady=5, font=('calibre',10, 'bold'))
members5 = tk.Label(root, text="45. Ravi Rathod", padx=5, pady=5, font=('calibre',10, 'bold'))




x_label = tk.Label(root, text = 'Provide the x intercept', padx=5, pady=5, font=('calibre',10, 'bold'))
x_txt = tk.Text(root, height=1, width=20)
  

y_label = tk.Label(root, text = 'Provide the y intercept', padx=5, pady=5, font = ('calibre',10,'bold'))
y_txt = tk.Text(root, height=1, width=20)


z_label = tk.Label(root, text = 'Provide the z intercept', padx=5, pady=5, font = ('calibre',10,'bold'))
z_txt = tk.Text(root, height=1, width=20)

  

pos_btn=tk.Button(root,text = 'Plot', padx=10, pady=10, command = plot)
  
pro_title.grid(row=0, column=1)
x_label.grid(row=3,column=0)
x_txt.grid(row=3,column=1)
y_label.grid(row=4,column=0)
y_txt.grid(row=4,column=1)
z_label.grid(row=5,column=0)
z_txt.grid(row=5,column=1)
pos_btn.grid(row=10,column=1)
member.grid(row=13,column=0,sticky=W)
members1.grid(row=14,column=0,sticky=W)
members2.grid(row=15,column=0,sticky=W)
members3.grid(row=16,column=0,sticky=W)
members4.grid(row=17,column=0,sticky=W)
members5.grid(row=18,column=0,sticky=W)


root.mainloop()