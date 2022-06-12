# 91869 & 91867 Assement
# Julie's Party Hire

from tkinter import *
from tkinter import ttk

root = Tk()
def callback():
    val1=entry.get()
    val2= entry2.get()
    val3= entry3.get()
    print("Customers Full Name:" +val1)
    print("Customers Receipt Number:" + val2)
    print("Row Number#:" + val3)
    if chvar.get() ==1:
        print("Ballons ")


## Create the title / label for the program

lbltitle = ttk.Label(root, text= "Julie's Party Hire", font=(("Arial"),32 ))
lbltitle.grid(row=0,column=3,columnspan=2)


# Customer Name Code 

# Create an entry box for the customer name 
entry = ttk.Entry(root, width = 30)
entry.insert(0,"")
entry.grid(row=1, column=1)

#create a label for customer name
lblname= ttk.Label(text="Your Full Name:")
lblname.grid(row=1, column=0, sticky=W)


### Print Details Button ####

button=ttk.Button(text= " Print Details ")
button.grid(row = 1 , column =5 , stick= E)
button.config(command = callback )


##### Receipt Number Code #####

#Create an entry box for the recipt code
entry2= ttk.Entry(root, width = 30)
entry2.insert(0, "        ")
entry2.grid(row=2, column = 1)

#Create a label for receipt number
lblname2 = ttk.Label(text="Receipt Number:")
lblname2.grid(row=2, column=0,sticky = W)


# Quit Button 

button2=ttk.Button(text="Quit")
button2.config(command= quit)
button2.grid(row=2, column =5 , sticky = E )

# Row#  

#Create an Entry Box for Row 

entry3= ttk.Entry(root, width = 30)
entry3.insert(0, "        ")
entry3.grid(row=4, column = 1)

#Create a Label for Row

lblname3=ttk.Label(text="Row#")
lblname3.grid(row=4,column=0,sticky= W )


# Item Hired 

# Create a label for items hired
lblname3=ttk.Label(text="Item Hired:")
lblname3.grid(row=3, column=0,sticky = W)


Items = StringVar()
ComboBox= ttk.Combobox(root,textvariable=Items,values=("Ballons", "Lights",
                                                       "Party Hats"," Streamers ",  "Sound System", "Dance Floors", "Invitation Cards" )
                       ,state ="readonly").grid(row=3,column=1)

# Number of Items Hired

#Create a label for number of items hired
lblname4=ttk.Label(text="Number of Items Hired:")
lblname4.grid(row=4,column=0,sticky=W)

# Print details of all the customers
def print_customer_details():
    global total_entries,name_count

    #create the colum headings
    name_count=0
    Label(main_window, font=("Arial 10 bold"), text="Row").grid(column=0, row=10)
    Label(main_window, font=("Arial 10 bold"), text="Customers Full Name").grid(column=1, row=10)
    Label(main_window, font=("Arial 10 bold"), text="Receipt Number").grid(column=2, row=10)
    Label(main_window, font=("Arial 10 bold"), text="Items Hired ").grid(column=3, row=10)
    Label(main_window, font=("Arial 10 bold"), text="Number of Items").grid(column=4, row=10)

 #add each item in the list onto its own row
    while name_count < total_entries :
        Label(main_window, text=name_count).grid(column=0,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=1,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=2,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=3,row=name_count+11)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=4,row=name_count+11)
        main_window.geometry("")
        name_count += 1
   
def append_details ():
    global customer_details, entry_name, entry_name_first, entry_name_blank, entry_receipt, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_item, entry_item_blank, entry_quantity, entry_quantity_blank, entry_quantity_limit, entry_quantity_letter, total_entries


# Append Button
root.geometry("1000x500") # Size of the window
root.mainloop()
