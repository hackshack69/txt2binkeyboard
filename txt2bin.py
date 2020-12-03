import tkinter as tk
from tkinter import ttk

key = tk.Tk()              
# key window name
 
key.title('Keyboard Shukla')
# key window title

exp = " "         
# global variable 

# showing all data in display 
def press(num):
    global exp
    exp=exp + str(num)
    equation.set(exp)
# end 

# clear button
def clear():
	global exp
	exp = ""
	equation.set(exp)
#end


# Enter Button Work Next line Function

def action():
  exp = " Next Line : "
  equation.set(exp)

# end function coding

# Tab Button Function 
def Tab():
  exp = " TAB : "
  equation.set(exp)
# END Tab Button Fucntion





key.geometry('1010x250')         
# normal size

key.maxsize(width=1010, height=250)   # maximum size

key.minsize(width= 1010 , height = 250)     
# minimum size

key.configure(bg = 'blue')    
#  add background color

# entry box

equation = tk.StringVar()

Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)

Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)

# entry box end

# keyboard 

# letter q
q = ttk.Button(key,text = 'Q' , width = 2, command = lambda : press('Q'))
q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)

# letter w
w = ttk.Button(key,text = 'W' , width = 2, command = lambda : press('W'))
w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

# letter e
e = ttk.Button(key,text = 'E' , width = 2, command = lambda : press('E'))
e.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)

# letter r
r = ttk.Button(key,text = 'R' , width = 2, command = lambda : press('R'))
r.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)

# letter t 
t = ttk.Button(key,text = 'T' , width = 2, command = lambda : press('T'))
t.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)

# letter y
y = ttk.Button(key,text = 'Y' , width = 2, command = lambda : press('Y'))
y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)

# letter u
u = ttk.Button(key,text = 'U' , width = 2, command = lambda : press('U'))
u.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)

# letter i
i = ttk.Button(key,text = 'I' , width = 2, command = lambda : press('I'))
i.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)

# letter o 
o = ttk.Button(key,text = 'O' , width = 2, command = lambda : press('O'))
o.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)

# letter p
p = ttk.Button(key,text = 'P' , width = 2, command = lambda : press('P'))
p.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)

# curly brackets bro
cur = ttk.Button(key,text = '{' , width = 2, command = lambda : press('{'))
cur.grid(row = 1 , column = 10 , ipadx = 6 , ipady = 10)

# curly brackers close bro
cur_c = ttk.Button(key,text = '}' , width = 2, command = lambda : press('}'))
cur_c.grid(row = 1 , column = 11, ipadx = 6 , ipady = 10)

# back slash bro
back_slash = ttk.Button(key,text = '\\' , width = 2, command = lambda : press('\\'))
back_slash.grid(row = 1 , column = 12, ipadx = 6 , ipady = 10)




#-----ROW 2 OF KEYBOARD---------------

# letter a
a = ttk.Button(key,text = 'A' , width = 2, command = lambda : press('A'))
a.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)

# letter s 
s = ttk.Button(key,text = 'S' , width = 2, command = lambda : press('S'))
s.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

# letter d
d = ttk.Button(key,text = 'D' , width = 2, command = lambda : press('D'))
d.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

# letter f
f = ttk.Button(key,text = 'F' , width = 2, command = lambda : press('F'))
f.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)

# letter g
# puchna mat yeh letter hr jagah q likha maine , samajh nhi aa rha tha kidhar kya likhu isliye ⊂(・﹏・⊂)

g = ttk.Button(key,text = 'G' , width = 2, command = lambda : press('G'))
g.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)

# letter h
h = ttk.Button(key,text = 'H' , width = 2, command = lambda : press('H'))
h.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)

# letter j
j = ttk.Button(key,text = 'J' , width = 2, command = lambda : press('J'))
j.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)

# letter k
k = ttk.Button(key,text = 'K' , width = 2, command = lambda : press('K'))
k.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

# letter l
l = ttk.Button(key,text = 'L' , width = 2, command = lambda : press('L'))
l.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)

semi_co = ttk.Button(key,text = ';' , width = 6, command = lambda : press(';'))
semi_co.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)


d_colon = ttk.Button(key,text = '"' , width = 6, command = lambda : press('"'))
d_colon.grid(row = 2 , column = 10, ipadx = 6 , ipady = 10)

#-------ROW 3 OF KEYBOARD ------------

z = ttk.Button(key,text = 'Z' , width = 2, command = lambda : press('Z'))
z.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)

x = ttk.Button(key,text = 'X' , width = 2, command = lambda : press('X'))
x.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)

c = ttk.Button(key,text = 'C' , width = 2, command = lambda : press('C'))
c.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)

v = ttk.Button(key,text = 'V' , width = 2, command = lambda : press('V'))
v.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)

b = ttk.Button(key,text = 'B' , width = 2, command = lambda : press('B'))
b.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)

n = ttk.Button(key,text = 'N' , width = 2, command = lambda : press('N'))
n.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)

m = ttk.Button(key,text = 'M' , width = 2, command = lambda : press('M'))
m.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)



# clear button bro
clear = ttk.Button(key,text = 'Clear' , width = 6, command = clear)
clear.grid(row = 4 , column = 0, ipadx = 20 , ipady = 10)

enter = ttk.Button(key,text = 'Enter' , width = 6, command = action)
enter.grid(row = 2 , columnspan = 75, ipadx = 85 , ipady = 10)




key.mainloop()               
# using ending point 