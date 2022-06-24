# 91869 & 91867 Assement
# Julie's Party Hire

#from tkinter import *
#from tkinter import ttk

#root = Tk()
#def callback():
   # val1=entry.get()
    #val2= entry2.get()
    #val3= entry3.get()
    #print("Customers Full Name:" +val1)
    #print("Customers Receipt Number:" + val2)
    #print("Row Number#:" + val3)
   # if chvar.get() ==1:
       # print("Ballons ")


## Create the title / label for the program

#lbltitle = ttk.Label(root, text= "Julie's Party Hire", font=(("Arial"),32 ))
#lbltitle.grid(row=0,column=3,columnspan=2)


# Customer Name Code 

# Create an entry box for the customer name 
#entry = ttk.Entry(root, width = 30)
#entry.insert(0,"")
#entry.grid(row=1, column=1)

#create a label for customer name
#lblname= ttk.Label(text="Your Full Name:")
#lblname.grid(row=1, column=0, sticky=W)


### Print Details Button ####

#button=ttk.Button(text= " Print Details ")
#button.grid(row = 1 , column =5 , stick= E)
#button.config(command = callback )


##### Receipt Number Code #####

#Create an entry box for the recipt code
#entry2= ttk.Entry(root, width = 30)
#entry2.insert(0, "        ")
#entry2.grid(row=2, column = 1)

#Create a label for receipt number
#lblname2 = ttk.Label(text="Receipt Number:")
#lblname2.grid(row=2, column=0,sticky = W)


# Quit Button 

#button2=ttk.Button(text="Quit")
#button2.config(command= quit)
#button2.grid(row=2, column =5 , sticky = E )

# Row#  

#Create an Entry Box for Row 

#entry3= ttk.Entry(root, width = 30)
#entry3.insert(0, "        ")
#entry3.grid(row=4, column = 1)

#Create a Label for Row

#lblname3=ttk.Label(text="Row#")
#lblname3.grid(row=4,column=0,sticky= W )


# Item Hired 

# Create a label for items hired
#lblname3=ttk.Label(text="Item Hired:")
#lblname3.grid(row=3, column=0,sticky = W)

#Create a Checkcombobox 

#Items = StringVar()
#ComboBox= ttk.Combobox(root,textvariable=Items,values=("Ballons", "Lights",
                                                    #   "Party Hats"," Streamers ",  "Sound System", "Dance Floors", "Invitation Cards" )
                    #   ,state ="readonly").grid(row=3,column=1)

# Number of Items Hired

#Create a label for number of items hired
#lblname4=ttk.Label(text="Number of Items Hired:")
#lblname4.grid(row=4,column=0,sticky=W)

# Print details of all the customers
#def print_customer_details():
    #global total_entries,name_count

    #create the colum headings
    #name_count=0
   # Label(main_window, font=("Arial 10 bold"), text="Row").grid(column=0, row=10)
    #Label(main_window, font=("Arial 10 bold"), text="Customers Full Name").grid(column=1, row=10)
   # Label(main_window, font=("Arial 10 bold"), text="Receipt Number").grid(column=2, row=10)
   # Label(main_window, font=("Arial 10 bold"), text="Items Hired ").grid(column=3, row=10)
   # Label(main_window, font=("Arial 10 bold"), text="Number of Items").grid(column=4, row=10)

 #add each item in the list onto its own row
  #  while name_count < total_entries :
      #  Label(main_window, text=name_count).grid(column=0,row=name_count+11)
      #  Label(main_window, text=(customer_details[name_count][0])).grid(column=1,row=name_count+11)
       # Label(main_window, text=(customer_details[name_count][1])).grid(column=2,row=name_count+11)
       # Label(main_window, text=(customer_details[name_count][2])).grid(column=3,row=name_count+11)
      #  Label(main_window, text=(customer_details[name_count][3])).grid(column=4,row=name_count+11)
      #  main_window.geometry("")
       # name_count += 1
   
#def append_details ():
  #  global customer_details, entry_name, entry_name_first, entry_name_blank, entry_receipt, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_item, entry_item_blank, entry_quantity, entry_quantity_blank, entry_quantity_limit, entry_quantity_letter, total_entries


# Append Button

#Button(main_window, text="Append Details", command=append_details)
#Button.grid(column= 5, row=3, sticky = E)

# Size of the window
#main_window.geometry("1000x500")

#start the program running
#def main():

    #global main_window
   # global customer_details,

#main_window=Tk()
#main_winodow.mainloop()


####### NOTE!!!!
   #I am restarting my coding process from the start as I have made it
   # to complicated to continure with the code I started with. I have turned all the
   # codes above into comments so you can see my progress from before and that I
   # can use it as my discussion and evideince of work.

   ## New Code

from tkinter import *
from tkinter import ttk
import random
import re

main_window= Tk()

#       quit command for the whole program
#def quit ():
   # main_window.destory()

#    append detials for the whole program
customer_details = []

#      print customer details
def print_details():
    global total_entries, entry_name, entry_receipt, entry_items, entry_number
    name_count = 0
#    Create the column headings
# Row Heading
    Label(main_window, font=("Arial 12 bold"),text="Row").grid(column = 0 , row =10)
# Customer Name heading
    Label(main_window, font=("Arial 12 bold"),text="Full Customer Name").grid(column = 1 , row =10)
# Receipt Number heading
    Label(main_window, font=("Arial 12 bold"),text="Receipt Number").grid(column = 2 , row= 10)
# Items Hired heading
    Label(main_window, font=("Arial 12 bold"),text="Items Hired").grid(column = 3 , row =10)
# Number of items hired heading
    Label(main_window, font=("Arial 12 bold"),text="Number of items").grid(column = 4, row =10)

#total_entries = 0

# add each value to its respective row
    while name_count <  total_entries:
            Label(main_window, text = name_count).grid(column=0,row=name_count+11)
            Label(main_window,text = (customer_details[name_count][0])).grid(column=1,row=name_count+11)
            Label(main_window,text = (customer_details[name_count][1])).grid(column=2,row=name_count+11)
            Label(main_window,text = (customer_details[name_count][2])).grid(column=3,row=name_count+11)
            Label(main_window,text = (customer_details[name_count][3])).grid(column=4,row=name_count+11)
            name_count +=1
           
            
    

def append_details():
    #global customer_details
    global customer_details, total_entries, entry_name, entry_receipt, entry_items, entry_number
    customer_details.append([entry_name.get(), entry_receipt.get(), entry_items.get(), entry_number.get()])
    #clear the boxes
    entry_name.delete(0, "end")
    entry_receipt.delete(0, "end")
    entry_items.delete(0, "end")
    entry_number.delete(0, "end")
    total_entries +=1

    
    #          delete a row from a list command
customer_details = []
def delete_row():
        global customer_details, delete_item, total_entries, name_count
        del customer_details[int(delete_item.get())]
        total_entries = total_entries- 1
        name_count= 0
        delete_item.delete(0, "end")
        Label(main_window, text="                    " ).grid(column=0, row=name_count+11)
        Label(main_window, text="                    " ).grid(column=1, row=name_count+11)
        Label(main_window, text="                    " ).grid(column=2, row=name_count+11)
        Label(main_window, text="                    " ).grid(column=3, row=name_count+11)
        Label(main_window, text="                    " ).grid(column=4, row=name_count+11)
        print_details()
        
customer_details = []
total_entries = 0

#       All the buttons for the program

# Quit Command
Quit = Button(main_window, fg="red",text="Quit", command = quit, width = 12)
Quit.grid(column = 5 ,row = 1,sticky=E)

# Append Command
Append = Button(main_window, fg= "green", text= " Append Details" , command= append_details, width =12)
Append.grid(column = 5 , row = 3 , sticky=E)

#Print Command
Print =Button(main_window , fg="blue", text="Print Details", command = print_details ,width =12)
Print.grid(column = 5 , row = 0 , sticky=E)

# Delete Row Command
Delete_row=Button(main_window, fg= "red", text= " Delete Row#", command = delete_row, width = 12)
Delete_row.grid(column = 3, row = 5, sticky =W)



#       All the Labels for the program

#Customer Full Name
Customer = Label(main_window,text="Customers Full Name:")
Customer.grid(column = 1 , row = 1 , sticky=W)

# Title for the program
Title = Label(main_window,text=" Julie's Party Hire", font=(("Arial"),30 ))
Title.grid(column = 3, row = 0 )

# Receipt Number
Receipt = Label(main_window, text="Receipt Number:")
Receipt.grid(column = 1 , row = 2 , sticky=W)

# Items Hired
Items = Label(main_window,text="Items Hired: ")
Items.grid(column = 1 , row =3, sticky=W)

# Number of Items Hired
Numbers =Label(main_window,text="Number of Items Hired: ")
Numbers.grid(column = 1 , row =4, sticky=W)

# Delete Row
Delete= Label(main_window,text=" Delete Row#")
Delete.grid(column = 1 , row =5, sticky=W)

# Row#
#Label(main_window, text="Row#")
#Label.grid(column = 1 , row = 5 , sticky=W)

#      All the entry boxes for the program

# Customer Entry
entry_name= Entry(main_window)
entry_name.grid(column =2 , row =1 )

#Receipt Number Entry
entry_receipt = Entry(main_window)
entry_receipt.grid(column =2 , row =2)

# Items Hired - I WILL CHANGE THIS TO A COMBOBOX LATER ( JUST FOR NOW I WILL USE AN ENTRY)
entry_items= Entry(main_window)
entry_items.grid(column =2 , row =3)

# Number of items
entry_number= Entry(main_window)
entry_number.grid(column =2 , row =4)

# Row#
delete_item= Entry(main_window)
delete_item.grid(column =2 , row =5)

    

#     must check for vaild inputs ( int , strings , non blank functions, etc )


#   check if customers full name has been entered in its entry box, set error message
if  len(entry_name.get()) == 0:
        Label(main_window, fg = "red" , text = "This cannot be left blank, please enter a vaild entry of a customers full name.").grid(row = 1 , column = 3 )
        input_check = 1 

#    check if receipt number has been entered, set error message
if len(entry_receipt.get()) == 0: Label(main_window, fg= "red" , text="This cannot be left blank, please enter a vaild entry of the customers receipt number.").grid(row = 2, column= 3 )
input_check = 1
        
        
#      check if the receipt has a string in the entry causing it to be an invaild entry, set error message
if len(entry_receipt.get()) != 0:  
        if entry_receipt.get().strip().isdecimal() == False:
            Label(main_window, fg= "red ", text= " No letters can be entered as the reciept number. Please enter a vaild receipt number.").grid(row=3, column =3)
           
#     check for other charchters or spaces inbetween the numbers of the reciept number

if len (entry_receipt.get()) != 0:
    if entry_receipt.get().strip().isdecimal() == False:
        Label(main_window, text=" A space or charcther other than a number has been entered, this is invaild. Please enter the receipt number again.", fg="red ").grid(row= 3 , column = 3 )
            
   # if entry_receipt.get().strip().isdecimal() ==True:
        

 #check that item is not blank, set error message
if len( entry_items.get()) == 0: Label(main_window, fg="red", text= "This cannot be left blank, please enter the items you wish to hire.").grid(row=3, column =3)

####if len( entry_items.get()) > 0:


# check the number of items is not blank and it must be 1 and 500, set error message
if len( entry_number.get()) == 0 : Label(main_window, fg = "red" , text=" This cannot be left blank, please enter the number of items you wish to hire.").grid(row=4, column = 3)
     

#      vaule check

#try:
      #  inter = int(entry_number.get())
     #  if 500< int(entry_number.get()) or int(entry_numbers.get()) < 0:
      #      entry_number_blank.destory()
      #      entry_number_letter.destory()
      #      entry_number_limit.destory()
      #      entry_number_limit(main_window, fg ="red", text="Invaild values. Please enter a vaild number between 1 and 500.").grid(row=6, column = 5)

      #  if 501 > int(entry_number.get())>0:
         #entry_number_blank.destory()
          #  entry_number_letter.destory()
          #  entry_number_limit.destory()

#  if vaule cannot be checked , set error (custom ) message
    #except ValueError: entry_number_letter = Label(main_window, fg ="red" , text =" Inavild vaule. Please only enter the number .").grid(row=7, column =5)
    
        
 # append all if everything is checked and meets the requirements of the program
#if len(re.findall(r'\w+', entry_name.get())) >1:
   # if entry_receipt.get().strip().isdecimal() == True:
    #    if len(re.findall(r'\w+', entry_itmes.get())) >0:
       #          if entry_number.get().strip().isdecimal()== True:
       #              if 501 > int(entry_numbers.get()) >0:
             #            customer_details.append([entry_name.get().tite(), entry_receipt.get(),entry_items.get(),entry_number.get()])
                    #     entry_name.delete(0 , "end")
                      #   entry_receipt.delete(0, "end")
                    #     entry_items.delete(0, "end")
                    #     entry_number.delete(0, "end")
                    #     total_entries += 1
                         
        

    #       all global entries

#def GUI():
    #global customer_details, entry_name, entry_name_first, entry_name_blank, entry_receipt, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_items, entry_items_blank, entry_number, entry_number_blank, entry_number_limit, entry_number_letter, total_entries, delete_item
    

#def placeholder():
  #  global main_window
  #  global entry_name_blank, entry_receipt, entry_receipt_string, entry_receipt_blank, entry_receipt_special, entry_items, entry_items_blank, entry_number, entry_number_blank, entry_number_limit, entry_number_letter
   # global customer_details, entry_name, entry_name_first
   # entry_name_blank = Label(main_window, text = " ")
   # entry_receipt_blank = Label(main_window, text = " ")
   # entry_receipt_string = Label(main_window, text = " ")
   # entry_receipt_special = Label(main_window, text="")
   # entry_items_blank = Label(main_window, text="")
   # entry_number_blank = Label(main_window, text="")
   # entry_number_letter = Label(main_window, text="")
   # entry_number_limit = Label(main_window, text="")
    

def main():
    global main_window
    global customer_details, entry_name, entry_receipt, enter_items,entry_number, total_entries

    


# the GUI
#GUI()
#placeholder()

main_window.title("Program")


main_window.mainloop()

main()

   
