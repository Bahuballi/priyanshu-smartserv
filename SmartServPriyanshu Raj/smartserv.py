import tkinter as tk
from tkinter import filedialog
import csv

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk



address=""
delimitors=[".",',',';','|','^']
delimitoR=""
columns=[]

Data={}

def first_interface():
  root = tk.Tk()

  topFrame = tk.Frame(root)
  topFrame.pack()

  bottomFrame = tk.Frame(root)
  bottomFrame.pack(side='bottom')

  #row=0
  Upload = tk.Label(topFrame, text="Upload CSV File",bg='blue')
  Col_hand = tk.Label(topFrame, text = "Column Handling")
  Upload.grid(row=0,column=0,columnspan=4)
  Col_hand.grid(row=0,column=4,columnspan=4)

  #row=1
  space = tk.Label(topFrame, text="")
  space.grid(row=1)

  #row=2
  import_from_csv_file = tk.Label(topFrame, text="Import from CSV file")
  import_from_csv_file.grid(row=2,column=0,columnspan=2)

  #row=3
  space = tk.Label(topFrame, text="")
  space.grid(row=3)

  #row=4
  select_csv_file = tk.Label(topFrame, text="Select CSV file")
  select_csv_file.grid(row=4,column=0,columnspan=2)

  def browsefunc():
    global address
    address = filedialog.askopenfilename()

  file=tk.Button(topFrame, text='select from my computer', command=browsefunc)
  file.grid(row=4 ,column=3,columnspan=2)

  #row=5
  Header=tk.IntVar()
  has_header = tk.Label(topFrame,text='Has Header')
  has_header.grid(row=5,column=0,columnspan=2)

  header=tk.Checkbutton(topFrame,onvalue = 1, offvalue = 0,variable=Header, height=4,width = 20)
  header.grid(row=5,column=3)

  #row=6
  character_encoding = tk.Label(topFrame,text='Character Encoding')
  character_encoding.grid(row=6,column=0,columnspan=2)

  tkvar = tk.StringVar()
  choices = {'UTF-8','UTF-16','UTF-32'}
  tkvar.set('UTF-8')

  popupMenu=tk.OptionMenu(topFrame,tkvar,*choices)
  popupMenu.grid(row=6,column=3)

  #row=7
  delimiter = tk.Label(topFrame,text='Delimiter')
  delimiter.grid(row=7,column=0,columnspan=2)

  d=tk.IntVar()
  r1 = tk.Radiobutton(topFrame,text='comma',variable=d,value=1)
  r1.grid(row=7,column= 3,sticky='w')

  r2 = tk.Radiobutton(topFrame,text='semicolon',variable=d,value=2)
  r2.grid(row=7,column= 3,sticky='e')

  r3 = tk.Radiobutton(topFrame,text='pipe',variable=d,value=3)
  r3.grid(row=7,column= 4,sticky='w')

  r4 = tk.Radiobutton(topFrame,text='caret',variable=d,value=4)
  r4.grid(row=7,column= 5,sticky='w')

  selection =" "
  def sel():
    global delimitoR
    selection = int(d.get())
    delimitoR=delimitors[selection]
    print(address,delimitoR,tkvar.get(),Header.get())

  test=tk.Button(topFrame, text='TEST', command=sel)
  test.grid(row=8 ,column=3,columnspan=2)
  def start_second_interface():
    global address
    global delimitoR
    v1=address
    v2=Header.get()
    v3=tkvar.get()
    v4=delimitoR
    second_interface(v1,v2,v3,v4)

  Next= tk.Button(bottomFrame,text='NEXT',command=start_second_interface,bg='green')
  Next.pack(side='left')

  Cancel=tk.Button(bottomFrame , text ='CANCEL',command=quit)
  Cancel.pack(side='left')


def second_interface(v1,v2,v3,v4):
  global Data
  master = tk.Toplevel()
  topFrame = tk.Frame(master)
  topFrame.pack()
  
  bottomFrame = tk.Frame(master)
  bottomFrame.pack(side='bottom')

  #row=0
  Upload = tk.Label(topFrame, text="Upload CSV File")
  Col_hand = tk.Label(topFrame, text = "Column Handling",bg='blue')
  Upload.grid(row=0,column=0,columnspan=4)
  Col_hand.grid(row=0,column=4,columnspan=4)

  #row=1
  space = tk.Label(topFrame, text="")
  space.grid(row=1)

  #row=2
  import_from_csv_file = tk.Label(topFrame, text="Columns handling")
  import_from_csv_file.grid(row=2,column=0,columnspan=2)
  #row=3
  space = tk.Label(topFrame, text="")
  space.grid(row=3)

  att=[]
  with open(v1,'rt')as f:
    data = csv.DictReader(f)
    att=[]
    #at=[]
    i=v2
    for row in data:
      if(i>0):
        at=list(row.keys())
        att=" ".join(at)
        print(at)
        break
      else:
        break
    for i in at:
      Data[i]=[]
    #print(Data)
    for row in data:
      for col in row:
        Data[col].append(row[col])
    #print(Data)
    
  #row=4
  select_csv_file = tk.Label(topFrame, text="Select the fields to be displayed on the Data Table")
  select_csv_file.grid(row=4,column=0,columnspan=2)

  #row=5
  available_field=tk.Label(topFrame, text="Available Fields")
  available_field.grid(row=5,column=0,columnspan=2)

  #row=6
  valores = tk.StringVar()
  valores.set(att)
  keylist = list(map(str,valores.get().split()))
  
  lstbox = tk.Listbox(topFrame, listvariable=valores, selectmode=tk.MULTIPLE, width=20, height=10)
  lstbox.grid(column=0, row=6, columnspan=2)

  def select():
      global columns
      reslist = list()
      seleccion = lstbox.curselection()
      for i in seleccion:
          entrada = lstbox.get(i)
          reslist.append(entrada)
      columns=list(reslist)
      for val in reslist:
          print(val)
  #row=7
  note = tk.Label(topFrame,text=" Selected are in blue colour")
  note.grid(row=7,column=0,columnspan=4)
  
  #row=8
  note = tk.Label(topFrame,text=" To unselect click on blue coloured fields")
  note.grid(row=8,column=0,columnspan=4)

  #row=9
  btn = tk.Button(topFrame, text="Proceed to Selected column", command=select)
  btn.grid(column=1, row=9)

  
  def start_third_interface():
    global columns
    print(columns)
    third_interface(columns)
   
    
  def start_third_interface1():
    global columns
    columns=list(keylist)
    print(columns)
    third_interface(columns)
    
  Next= tk.Button(bottomFrame,text='NEXT',bg='green',command=start_third_interface)
  Next.pack(side='left')

  skip=tk.Button(bottomFrame,text='Skip this step',bg='red',command=start_third_interface1)
  skip.pack(side='left')
  
  Cancel=tk.Button(bottomFrame , text ='CANCEL',command=quit)
  Cancel.pack(side='left')  
  
def third_interface(columns):
  master = tk.Toplevel()
  topFrame = tk.Frame(master)
  topFrame.pack()

  #row=0
  height=1
  width=len(columns)
  for i in range(height): #Rows
    for j in range(width): #Columns
        b = tk.Label(topFrame, text=columns[j],bg='black',fg='white')
        b.grid(row=i, column=j)
  
  heights=len(Data[columns[0]])
  print(heights)
  for i in range(heights): #Rows
    for j in range(width): #Columns
        b = tk.Label(topFrame, text=Data[columns[j]][i])
        b.grid(row=i+1, column=j)
  
  bottomFrame = tk.Frame(master)
  bottomFrame.pack(side='bottom')
  
  
first_interface()





