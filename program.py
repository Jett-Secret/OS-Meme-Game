from pynput.keyboard import Key, KeyCode,Listener
from pynput.mouse import Button,Listener as mListener
import sys,datetime,time
import threading
from tkinter import Tk, Text,Label,StringVar,Button as Btn,ttk,IntVar,Checkbutton

global lasttime
global label	
	
def display():
	root.after(200, decrement_label )
def SetLabels(labs):
	global root
	for ele in root.winfo_children():
		ele.destroy()
	if len(labs)==0:
		lab = Label(root,text="Nothin'",font=("Courier", 11))
		lab.bind("<Button-1>",setmovable)
		lab.pack()
		return
	for l in labs:
		lab = Label(root,text=l,font=("Courier", 11))
		lab.bind("<Button-1>",setmovable)
		lab.pack()
		
		
def updateDisp():
	labels=[]
	for m in themap:
		if themap[m].get()==1:
			line = ""
			amt = 24
			i=1
			spl = m.split(' ')
			j=1
			for word in spl:
				line+=word
				if len(line)>amt*i:
					line+="\n"
					i+=1
				else:
					line+=" "
			j+=1
			if line.endswith("\n"):
				line=line[:-1]
			labels.append(line)
	SetLabels(labels)
global root
root = Tk()
root2 = Tk()
fi = open("./options.txt")
options = []
themap = {}
for line in fi.read().split("\n"):
	while line!="" and line[0]==" ":
		line=line[1:]
	if line=="" or line.startswith("#"): continue;
	
	options.append(line)
	themap[line] = IntVar(root2)
fi.close()

global movable
movable=False
def setmovable(e):
	global movable
	#print("hello!")
	movable=not movable
	root.resizable(movable, False)
	root.overrideredirect(not movable)
cbs = {}
global label
global labeltext
labeltext = StringVar()
label =None
def run():
	global labeltext
	global label

	lasttime = time.time();

	root.resizable(False, False)
	root.overrideredirect(True)
	root.title("")
	label = Label(root,text="Nothin'",font=("Courier", 11))
	label.grid(column=0, row=0)
	label.bind("<Button-1>",setmovable)
	#root.configure(bg='white')
	root.wm_attributes("-topmost", True)
	root.attributes('-toolwindow', True)
	#root.wm_attributes("-transparentcolor", "white")
	
	#x = threading.Thread(target=display)


	#x.start()
	
		
	root2.resizable(True, True)
	root2.title("Options")
	i=0
	
	for o in options:
		checkbox = Checkbutton(root2,
				text=o,
				variable=themap[o],
				command=updateDisp,
				onvalue=1,
				offvalue=0)
		#checkbox.grid(column=0, row=i)
		#newlabel = Label(root2,text=o, bg='gray',font=("Courier", 20))
		#newlabel.grid(column=1, row=i)
		#i+=1
		checkbox.deselect()
		checkbox.pack()
		cbs[o]=checkbox
	'''
	for o in options:
		checkbox_var = themap[o]
		checkbox = Checkbutton(root2,
                text="",
                variable=checkbox_var,
                onvalue=1,
                offvalue=0)
		checkbox.grid(column=0, row=i)
		newlabel = Label(root2,text=o, bg='gray',font=("Courier", 20))
		newlabel.grid(column=1, row=i)
		i+=1
		checkbox.deselect()
		#checkbox.pack()
		'''
	root.mainloop()
	root2.mainloop()
	quit()
run()