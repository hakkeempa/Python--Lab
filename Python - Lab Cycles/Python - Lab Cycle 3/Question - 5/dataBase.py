from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter.ttk import Style, Treeview
import pickle

global listOfVehicles
listOfVehicles = list()
vehicle_attributes = ["ownerName","vendor","model","type","registrationNumber","engineNumber","mileage"]
vehicleDetails = dict.fromkeys(vehicle_attributes, None)

def addList():
    treeList.insert(parent='', index='end', text="", values=(owner.get(), vendor.get(),model.get(),typeClass.get(),regNumber.get(),engNumber.get(),mileage.get()))
    vehicleDetails['ownerName'] = owner.get()
    vehicleDetails['vendor'] = vendor.get()
    vehicleDetails['model'] = model.get()
    vehicleDetails['type'] = typeClass.get()
    vehicleDetails['registrationNumber'] = int(regNumber.get())
    vehicleDetails['engineNumber'] = int(engNumber.get())
    vehicleDetails['mileage'] = float(mileage.get())
    listOfVehicles.append(vehicleDetails.copy())

def delete():
   # Get selected item to Delete
   selected_item = treeList.selection()[0]

def update():
   # Get selected item to Edit
   selected_item = treeList.selection()[0]
   treeList.item(selected_item, text="blub", values=("foo", "bar"))

def loadFile():
    filetypes = (
        ('Picle files', '*.pkl'),
        ('All files', '*.*')
    )
    filename = askopenfilename(title="Open Pickle",initialdir='/',filetypes=filetypes)
    listOfVehicles = pickle.load(open(filename,"rb"))
    showinfo(title="Selected File",message=filename)
    for i in listOfVehicles:
        treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))

def sortMileage():
    sortedList = sorted(listOfVehicles,key= lambda i:i['mileage'])
    for i in sortedList:
        treeList.insert(parent='', index='end', text="", values=(i['ownerName'],i['vendor'],i['model'],i['type'],i['registrationNumber'],i['engineNumber'],i['mileage']))

def createPickle():
    pickle.dump(listOfVehicles,open("vehicleDetails.pkl","wb"))

#window configuration.
window = Tk()
window.geometry("750x400")
window.title("Vehicle Data")

#variables to take input from screen.
owner = StringVar()
vendor = StringVar()
model = StringVar()
typeClass = StringVar()
regNumber = StringVar()
engNumber = StringVar()
mileage = StringVar()


#row-0
label1 = Label(window,text="Owner Name ")
label1.grid(row=0,column=0)

entry1 = Entry(window,width=25,textvariable=owner)
entry1.grid(row=0,column=1)

label2 = Label(window,text="Vendor Name ")
label2.grid(row=0,column=2)

entry2 = Entry(window,width=25,textvariable=vendor)
entry2.grid(row=0,column=3)

#row-1
label3 = Label(window,text="Model Name ")
label3.grid(row=1,column=0)

entry3 = Entry(window,width=25,textvariable=model)
entry3.grid(row=1,column=1)

label4 = Label(window,text="Type  ")
label4.grid(row=1,column=2)

entry4 = Entry(window,width=25,textvariable=typeClass)
entry4.grid(row=1,column=3)

#row-2
label5 = Label(window,text="Registration Number  ")
label5.grid(row=2,column=0)

entry5 = Entry(window,width=25,textvariable=regNumber)
entry5.grid(row=2,column=1)

label6 = Label(window,text="Engine Number ")
label6.grid(row=2,column=2)

entry6 = Entry(window,width=25,textvariable=engNumber)
entry6.grid(row=2,column=3)

#row - 3
label7 = Label(window,text="Mileage")
label7.grid(row=3,column=0)

entry7 = Entry(window,width=25,textvariable=mileage)
entry7.grid(row=3,column=1)

button1=Button(window,width=10,text="Load Pickle",bg='#99CCAA',command=loadFile)
button1.grid(row=3,column=4)

button8=Button(window,width=10,text="Display",bg='#99CCAA',)
button8.grid(row=3,column=5)

#second section 
#row - 0
button2=Button(window,width=10,text="Add",bg='#99CCAA',command=addList)
button2.grid(row=0,column=4)

button3=Button(window,width=10,text="Update",bg='#99CCAA',command=update)
button3.grid(row=0,column=5)

#row - 1
button4=Button(window,width=10,text="Delete",bg='#99CCAA',command=delete)
button4.grid(row=1,column=4)

button5=Button(window,width=10,text="Sort Mileage",bg='#99CCAA',command=sortMileage)
button5.grid(row=1,column=5)

#row - 2
button6=Button(window,width=10,text="Filter",bg='#99CCAA')
button6.grid(row=2,column=4)

button7=Button(window,width=10,text="Create Pickle",bg='#99CCAA',)
button7.grid(row=2,column=5)


style = Style()
style.theme_use("alt")
style.configure("Treeview",
    background="silver",
    foreground='green'
)
style.map('Treeview',background=[('selected','#FF1800')])
treeList = Treeview(columns=("Owner","Vendor","Model","Type","Reg Number","Eng Number","Mileage"),show='headings')

treeList.heading("Owner",text="Owner")
treeList.heading("Vendor",text="Vendor")
treeList.heading("Model",text="Model")
treeList.heading("Type",text="Type")
treeList.heading("Reg Number",text="Reg Number")
treeList.heading("Eng Number",text="Eng Number")
treeList.heading("Mileage",text="Mileage")

treeList['show']='headings'

treeList.column("Owner",width=90, anchor="center")
treeList.column("Vendor",width=50, anchor="center")
treeList.column("Model",width=50, anchor="center")
treeList.column("Type",width=40, anchor="center")
treeList.column("Reg Number",width=80, anchor="center")
treeList.column("Eng Number",width=80, anchor="center")
treeList.column("Mileage",width=50, anchor="center")

treeList.grid(row=4,column=0,columnspan=6)
window.mainloop()