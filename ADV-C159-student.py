 from tkinter import *
 
 root=Tk()
 root.geometry("600x400")
 
 list_name = ["Will Smith", "General Grey", "President Whitemore", "Russeel Casse"]
 dict_student={"name" : "Shreya",
               "age":"10"}
 
 
 try:
     
     print(list_name[5])
     
     print(dict_student["mom"])
     
     
 except IndexError :
     messagebox.showinfo("Error", "This index is lost in space")
     
 except KeyError :
     messagebox.showinfo("Error", "This index is lost in space")
     
 root.mainloop()