import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from PIL import Image
import csv
from tkinter import messagebox

root = ctk.CTk()
root.iconbitmap("logo.jpg")
root.title('BudGets: A Budget Planner')
ctk.set_appearance_mode("dark")
c = '#489d22'
b = 20
file_source = "Storage/data.csv"
consumption_file = "Storage/Msc/msc_consumption.csv"
cb_file = "Storage/allowance.csv"
item_msc = "Storage/Msc/items.csv"
temp = []

with open(cb_file, 'r') as kol:  # Access the allowance
    contain = csv.reader(kol)
    for rows in contain:
        ves = rows
allowance = float(ves[0])
bil = [allowance]
allowance_text = str(allowance)

with open(cb_file, 'w', newline='') as wri:  # The allowance was already in the file
    ik = csv.writer(wri)
    ik.writerow(bil)

#  Button Image
img_1 = Image.open("img/home_w.png")
home_icon = ctk.CTkImage(light_image=img_1, size=(b, b))

img_2 = Image.open("img/elec_w.png")
bolt_icon = ctk.CTkImage(light_image=img_2, size=(b, b))

img_3 = Image.open("img/water_w.png")
water_icon = ctk.CTkImage(light_image=img_3, size=(b, b))

img_4 = Image.open("img/shop_w.png")
grocery_icon = ctk.CTkImage(light_image=img_4, size=(b, b))

img_5 = Image.open("img/leisure_w.png")
leisure_icon = ctk.CTkImage(light_image=img_5, size=(b, b))

img_6 = Image.open("img/misc_w.png")
msc_icon = ctk.CTkImage(light_image=img_6, size=(b, b))

fs_2 = ("fixedsys", 12)

def update_csv(label):
    with open(cb_file, 'r') as update:
        store = csv.reader(update)
        for i in store:
            cb = i
    label.configure(text=cb[0])  # Update Current Balance

def get_bal():
    with open(cb_file, "r") as con:
        cont = csv.reader(con)
        for row in cont:
            balance = row
        return balance[0]

current_bal = float(get_bal())

class Info(ctk.CTkFrame):

    fr_color = "transparent"
    width = 700
    height = 600
    fs_1 = ("fixedsys", 28, "bold")
    fs_2 = ("fixedsys", 15)
    fs_3 = ctk.CTkFont(family="fixedsys", size=15)
    txt_color = "#FEFEFE"

    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)
        self.pack_propagate(False)
        self.configure(width=self.width, height=self.height)
        self.pack()

        # Widgets set up
        self.l1 = ctk.CTkLabel(self, width=800, height=600)
        self.l1.pack()

        self.frame = ctk.CTkFrame(self, width=320, height=390, corner_radius=1)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.l2 = ctk.CTkLabel(self.frame, text="User Information", font=('Century Gothic', 20))
        self.l2.place(x=85, y=25)

        self.name_entry = ctk.CTkEntry(self.frame, width=220, placeholder_text="Name")
        self.name_entry.place(x=55, y=90)

        self.age_entry = ctk.CTkEntry(self.frame, width=220, placeholder_text="Age")
        self.age_entry.place(x=55, y=150)

        self.allowance_entry = ctk.CTkEntry(self.frame, width=220, placeholder_text="Allowance")
        self.allowance_entry.place(x=55, y=210)

        self.limit_entry = ctk.CTkEntry(self.frame, width=220, placeholder_text="Limit")
        self.limit_entry.place(x=55, y=270)

        self.save_btn = ctk.CTkButton(self.frame, text="Save", command=self.fill)
        self.save_btn.place(x=93, y=330)

    def fill(self):
        if self.name_entry.get() == "":
            messagebox.showerror(title="Error", message="Please provide your name")
        elif self.age_entry.get() == "":
            messagebox.showerror(title="Error", message="Please provide your age")
        elif not self.age_entry.get().isdigit() or not self.allowance_entry.get().isdigit() or not \
                self.limit_entry.get().isdigit():
            messagebox.showerror(title="Error", message="Age, Allowance, and Limit should be numeric values")
        else:
            name = self.name_entry.get()
            age = self.age_entry.get()
            allowance = self.allowance_entry.get()
            limit = self.limit_entry.get()
            row = [name, age, allowance, limit]

            mit = [limit]
            al = [allowance]

            with open(cb_file, 'w', newline='') as write:
                w = csv.writer(write)
                w.writerow(al)

            with open("Storage/limit.csv", 'w', newline='') as lim:
                l = csv.writer(lim)
                l.writerow(mit)

            # Save data to file
            with open(file_source, 'w', newline='') as details:
                con = csv.writer(details)
                con.writerow(row)
            self.pack_forget()
            MainWindow(root)


class Electric(ctk.CTkFrame):

    fr_color = "#c8d9c2"
    label_color = "#355E3B"
    txt_color = "black"
    txtlabel = "white"
    width = 700
    height = 600
    a = 180
    image1 = Image.open("img/elec_g.png")
    photo = ctk.CTkImage(dark_image=image1, size=(a, a))
    fs_1 = ("Fixedsys", 30)
    fs_2 = ("Fixedsys", 15)
    fs_3 = ctk.CTkFont(family="Fixedsys", size=20)

    def __init__(self, parent, bal):
        super().__init__(parent, corner_radius=0)
        self.pack_propagate(False)
        self.configure(width=self.width, height=self.height)
        self.pack(side=ctk.LEFT)

        # Icon Frame
        self.icon_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, height=self.height)
        self.icon_frame.place(x=10, y=10)
        # self.icon_frame.propagate(False)

        self.icon_lab = ctk.CTkLabel(self.icon_frame, text="ELECTRICITY", font=self.fs_1,
                                     text_color="white")
        self.icon_lab.pack(pady=40)

        self.icon = ctk.CTkLabel(self.icon_frame, text='', image=self.photo)
        self.icon.pack(padx=20, pady=10)

        # Widgets
        # Current Balance Frame
        self.cbal_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.cbal_frame.pack(pady=10)
        self.cbal_frame.propagate(False)

        # Current Balance
        self.lb1 = ctk.CTkLabel(self.cbal_frame, text="Current Balance:", text_color=self.txtlabel, font=self.fs_3)
        self.lb1.configure(padx=5, pady=10)
        self.lb1.grid(column=0, row=0)

        hold = float(bal)

        self.lb2 = ctk.CTkLabel(self.cbal_frame, text=str(current_bal), text_color=self.txtlabel, font=self.fs_3)
        self.lb2.configure(padx=5, pady=10)
        self.lb2.grid(column=1, row=0)

        # Consumption Frame
        self.consump_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.consump_frame.pack(pady=10)

        # Stat Info
        self.lb3 = ctk.CTkLabel(self.consump_frame, text="Consumption:", text_color=self.txtlabel, font=self.fs_3)
        self.lb3.configure(padx=10, pady=10)
        self.lb3.grid(column=0, row=0)

        with open("Storage/Elec/elec_consumption.csv", "r") as con:
            cont = csv.reader(con)
            for row in cont:
                cons = row
            temp = str(cons[0])

        self.lb4 = ctk.CTkLabel(self.consump_frame, text=temp, text_color=self.txtlabel, font=self.fs_3)
        self.lb4.configure(padx=10, pady=10)
        self.lb4.grid(column=1, row=0)

        # Bottom Frame
        self.add_frame = ctk.CTkFrame(self, height=100, fg_color="transparent")
        self.add_frame.place(x=self.height // 2 - self.add_frame._current_width + 20,
                             y=self.height - self.add_frame._current_height - 70)

        self.entry_label = ctk.CTkLabel(self.add_frame, text="ADD ITEM/S",
                                        font=self.fs_3, text_color=self.txtlabel)
        self.entry_label.grid(column=1, row=0, pady=5)

        # Bottom frame Entry
        self.app = ctk.CTkEntry(self.add_frame, placeholder_text="Appliances", font=self.fs_3, border_color="#355E3B")
        self.app.grid(column=0, row=1, padx=20, pady=10)

        self.watts = ctk.CTkEntry(self.add_frame, placeholder_text="Watts", font=self.fs_3, border_color="#355E3B")
        self.watts.grid(column=1, row=1, padx=20, pady=10)

        self.hour = ctk.CTkEntry(self.add_frame, placeholder_text="Hour Usage", font=self.fs_3, border_color="#355E3B")
        self.hour.grid(column=2, row=1, padx=20, pady=10)

        # Information Frame
        self.inf_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, width=410,
                                      height=self.height - self.add_frame._current_height - 100)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 25, y=40)
        self.inf_frame.propagate(False)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview", background="#121212", foreground="#489d22", rowheight=40, fieldbackground="#1f1b24",
                        font=self.fs_2)
        style.map("Treeview", background=[("selected", "green")])

        style.configure("Treeview.Heading", font=("Fixedsys", 15), background="#489d22")

        my_tree = ttk.Treeview(self.inf_frame)
        my_tree['columns'] = ("Appliances", "Watts", "Hour Usage", "Total")
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("Appliances", anchor=CENTER, width=150, stretch=NO)
        my_tree.column("Watts", anchor=CENTER, width=150, stretch=NO)
        my_tree.column("Hour Usage", anchor=CENTER, width=160, stretch=NO)
        my_tree.column("Total", anchor=CENTER, width=160, stretch=NO)

        # Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Appliances", text="Appliances", anchor=CENTER)
        my_tree.heading("Watts", text="Watts", anchor=CENTER)
        my_tree.heading("Hour Usage", text="Hour Usage", anchor=CENTER)
        my_tree.heading("Total", text="Total(per Month)", anchor=CENTER)
        my_tree.pack(fill="both", expand=TRUE)

        def read_and_display_data():
            count = 0

            with open('Storage/Elec/app.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if count % 2 == 0:
                        my_tree.insert(parent="", index="end", text="",
                                       values=(row[0], row[1], row[2], row[3]), tags='evenrow')
                    else:
                        my_tree.insert(parent="", index="end", text="",
                                       values=(row[0], row[1], row[2], row[3]), tags='oddrow')
                    count += 1

        # Call the function to read and display the data
        read_and_display_data()
        root.update_idletasks()

        def add_record():
            count = 0

            if self.app.get() == "" or self.watts.get() == "" or self.hour.get() == "":
                messagebox.showerror(title="Error", message="Please enter missing information")
            else:
                with open("Storage/Elec/elec_consumption.csv", 'r') as val:
                    line = csv.reader(val)
                    for i in line:
                        f = i
                cns = float(f[0])

                app_value = self.app.get()
                watts_value = self.watts.get()
                hour_value = self.hour.get()
                rate = 8.9071
                elec_total = 0

                if not watts_value.isdigit() or not hour_value.isdigit():
                    messagebox.showerror(title="Error", message="Watts and Hour must be numeric values")
                else:
                    elec_consumption = int(watts_value) / 1000 * float(hour_value) * float(rate)
                    week = elec_consumption * 7
                    month = week * 4
                    elec_total = str(round(month, 2))

                    cns += round(float(elec_total), 2)

                    my_tree.insert(parent="", index="end", text="",
                                   values=(app_value, watts_value, hour_value, elec_total))
                    count += 1

                    self.app.delete(0, END)
                    self.watts.delete(0, END)
                    self.hour.delete(0, END)

                    data = [app_value, watts_value, hour_value, elec_total]
                    with open('Storage/Elec/app.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(data)

                insert = [cns]

                with open("Storage/Elec/elec_consumption.csv", "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(insert)

                with open("Storage/Elec/elec_consumption.csv", 'r') as spend:
                    bal = csv.reader(spend)
                    for y in bal:
                        cp = y
                self.lb4.configure(text=cp[0])  # Update the Consumption

                with open(cb_file, 'r') as alr:  # Access the allowance
                    cont = csv.reader(alr)
                    for row in cont:
                        sve = row
                alcom = float(sve[0])
                new = round(alcom - float(elec_total), 2)
                k = [new]

                with open(cb_file, 'w', newline='') as w:  # Update allowance
                    i = csv.writer(w)
                    i.writerow(k)

                #  Computation
                with open(cb_file, 'r') as update:
                    store = csv.reader(update)
                    for i in store:
                        cb = i
                self.lb2.configure(text=cb[0])  # Update Current Balance


        def remove():
            item_selected = my_tree.selection()
            if not item_selected:
                return
            item = item_selected[0]

            # Get the values of the selected row
            values = my_tree.item(item, 'values')
            app_value, watts_value, hour_value, total = values

            with open('Storage/Elec/app.csv', mode='r') as file:
                reader = csv.reader(file)
                data = list(reader)

            # Find the row to remove
            new_data = [row for row in data if row != [app_value, watts_value, hour_value, total]]

            with open('Storage/Elec/app.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)

            my_tree.delete(item)

        def delete_all():
            for record in my_tree.get_children():
                my_tree.delete(record)

            # Open the CSV file in write mode, which will truncate the file
            with open('Storage/Elec/app.csv', mode='w', newline=''):
                pass  # No need to write anything, this will truncate the file

            # Delete all rows from the Treeview widget
            my_tree.delete(*my_tree.get_children())

        #  Button Add
        self.btn_remove = ctk.CTkButton(self.add_frame, text="Remove", font=self.fs_3, width=80, fg_color="green", border_color="green", border_width=0, text_color="White" ,command=remove, hover_color="#73C088")
        self.btn_remove.grid(column=0, row=2, pady=10)

        self.btn_add = ctk.CTkButton(self.add_frame, text="Add", font=self.fs_3, width=80, fg_color="green", border_color="green", border_width=0, text_color="White", command=add_record, hover_color="#73C088")
        self.btn_add.grid(column=1, row=2, pady=10)

        self.btn_deleteAll = ctk.CTkButton(self.add_frame, text="Delete All", font=self.fs_3, width=80, fg_color="green", border_color="green", border_width=0, text_color="White", command= delete_all, hover_color="#73C088")
        self.btn_deleteAll.grid(column=2 ,row= 2,pady=10)

        my_tree.pack(pady=20)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 15, y=10)


class WaterBill(ctk.CTkFrame):
    fr_color = "#c8d9c2"
    label_color = "#355E3B"
    txt_color = "black"
    txtlabel = "white"
    width = 700
    height = 600
    a = 180
    image1 = Image.open("img/water_g.png")
    photo = ctk.CTkImage(dark_image=image1, size=(a, a))
    fs_1 = ("Fixedsys", 30)
    fs_2 = ("Fixedsys", 15)
    fs_3 = ctk.CTkFont(family="Fixedsys", size=20)

    def __init__(self, parent, bal):
        super().__init__(parent)
        self.eb_frame = ctk.CTkFrame(self)
        self.pack_propagate(False)
        self.configure(width=self.width, height=self.height)
        self.pack(side=ctk.LEFT,fill=ctk.BOTH)

        # Icon Frame
        self.icon_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, height=self.height)
        self.icon_frame.place(x=10, y=10)
        # self.icon_frame.propagate(False)

        self.icon_lab = ctk.CTkLabel(self.icon_frame, text="WATER BILL", font=self.fs_1,
                                     text_color=self.txtlabel)
        self.icon_lab.pack(pady=40)
        self.icon = ctk.CTkLabel(self.icon_frame, text='', image=self.photo)
        self.icon.pack(padx=20, pady=10)


        # Widgets
        # Current Balance Frame
        self.cbal_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.cbal_frame.pack(pady=10)

        # Current Balance
        self.lb1 = ctk.CTkLabel(self.cbal_frame, text="Current Balance:", text_color=self.txtlabel, font=self.fs_3)
        self.lb1.configure(padx=10, pady=10)
        self.lb1.grid(column=0, row=0)


        hold = round(float(bal), 2)

        self.lb2 = ctk.CTkLabel(self.cbal_frame, text=str(hold), text_color=self.txtlabel, font=self.fs_3)
        self.lb2.configure(padx=10, pady=10)
        self.lb2.grid(column=1, row=0)

        # Consumption Frame
        self.consump_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.consump_frame.pack(pady=10)

        # Stat Info
        self.lb3 = ctk.CTkLabel(self.consump_frame, text="Consumption:", text_color=self.txtlabel, font=self.fs_3)
        self.lb3.configure(padx=10, pady=10)
        self.lb3.grid(column=0, row=0)

        with open("Storage/Water/water_consumption.csv", "r") as con:
            cont = csv.reader(con)
            for row in cont:
                cons = row
            temp = str(cons[0])

        self.lb4 = ctk.CTkLabel(self.consump_frame, text=temp, text_color=self.txtlabel, font=self.fs_3)
        self.lb4.configure(padx=10, pady=10)
        self.lb4.grid(column=1, row=0)

        # Bottom Frame
        self.add_frame = ctk.CTkFrame(self, height=100,fg_color="transparent")
        self.add_frame.place(x=self.height // 2 - self.add_frame._current_width + 20,
                             y=self.height - self.add_frame._current_height - 50)

        self.entry_label = ctk.CTkLabel(self.add_frame, text="ADD CONSUMPTION", font=("Fixedsys", 22))
        self.entry_label.grid(column=1, columnspan=3, row=0)

        # Bottom frame Entry
        self.month = ctk.CTkEntry(self.add_frame, placeholder_text="Month", font=self.fs_3, border_color="#355E3B")
        self.month.grid(column=0,columnspan=2,row=1, padx=10, pady=10)

        self.consum = ctk.CTkEntry(self.add_frame, placeholder_text="Consumption (m³)",font=self.fs_3,border_color="#355E3B")
        self.consum.grid(column=3,columnspan=2,row=1, padx=10, pady=10)

        # Information Frame
        self.inf_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, width=410,border_color="#355E3B",
                                      height=self.height - self.add_frame._current_height - 100)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 25, y=40)
        self.inf_frame.propagate(False)

        print(str(self.height - self.add_frame._current_height - 100))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background= "#121212",foreground="#489d22", rowheight=40,
                        fieldbackground="#1f1b24",font= self.fs_2)
        style.map("Treeview", background=[("selected", "green")])

        style.configure("Treeview.Heading", font=("Fixedsys", 15), background="#489d22")

        my_tree=ttk.Treeview(self.inf_frame)
        my_tree['columns']=("Month","Consumption(m³)","Total")
        my_tree.column("#0", width=0,stretch=NO)
        my_tree.column("Month", anchor=CENTER, width=210, stretch=NO)
        my_tree.column("Consumption(m³)", anchor=CENTER, width=210, stretch=NO)
        my_tree.column("Total", anchor=CENTER, width=210, stretch=NO)

        #  Headings
        my_tree.heading("#0",text="",anchor=W)
        my_tree.heading("Month",text="Month", anchor=CENTER)
        my_tree.heading("Consumption(m³)",text="Consumption(m³)",anchor=CENTER)
        my_tree.heading("Total", text="Total",anchor=CENTER)

        my_tree.pack(fill='both', expand=True)

        def read_and_display_data():
            global count
            count =0
            current_bal = get_bal()
            with open('Storage/Water/watbill.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if count % 2 == 0:
                        my_tree.insert(parent="", index="end", text="",
                                       values=(row[0], row[1], row[2]), tags=('evenrow'))
                    else:
                        my_tree.insert(parent="", index="end", text="",
                                       values=(row[0], row[1], row[2]), tags=('oddrow'))
                    count += 1

        #  Call the function to read and display the data
        read_and_display_data()
        root.update_idletasks()

        def add_record():
            water_consum = 0
            count = 0
            cns = 0
            if self.month.get() == "" or self.consum.get() == "":
                messagebox.showerror(title="Error", message="Please enter missing information")
            else:
                with open("Storage/Water/water_consumption.csv", 'r') as val:
                    line = csv.reader(val)
                    for i in line:
                        f = i
                cns = round(float(f[0]),2)

                month = self.month.get()
                cubic_meter = self.consum.get()
                water_rate = 16.44

                if not cubic_meter.isdigit():
                    messagebox.showerror(title="Error", message=" Cubic meter must be numeric values")
                else:
                    if int(cubic_meter) <= 10:
                        water_consum = 160
                    else:
                        water_consum = round(int(cubic_meter) * float(water_rate),2)

                    cns += water_consum

                my_tree.insert(parent="", index="end", text="",values=(month, cubic_meter, water_consum))
                count +=1

                self.month.delete(0,END)
                self.consum.delete(0,END)

                data = [month,cubic_meter,water_consum]

                with open('Storage/Water/watbill.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(data)

            insert = [cns]

            with open("Storage/Water/water_consumption.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(insert)

            with open("Storage/Water/water_consumption.csv", 'r') as spend:
                bal = csv.reader(spend)
                for y in bal:
                    cp = y
            self.lb4.configure(text=cp[0])  # Update the Consumption

            with open(cb_file, 'r') as alr:  # Access the allowance
                cont = csv.reader(alr)
                for row in cont:
                    sve = row
            alcom = float(sve[0])
            new = round(alcom - float(water_consum), 2)
            k = [new]

            with open(cb_file, 'w', newline='') as w:  # Update allowance
                i = csv.writer(w)
                i.writerow(k)

            #  Computation
            with open(cb_file, 'r') as update:
                store = csv.reader(update)
                for i in store:
                    cb = i
            self.lb2.configure(text=cb[0])  # Update Current Balance

        def remove():
                item_selected = my_tree.selection()
                if not item_selected:
                    return
                item = item_selected[0]

                # Get the values of the selected row
                values = my_tree.item(item, 'values')
                month,cubic_meter,water_consum = values

                with open("Storage/Water/watbill.csv", mode='r') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                # Find the row to remove
                new_data = [row for row in data if row != [month,cubic_meter,water_consum]]

                with open('Storage/Water/watbill.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(new_data)

                my_tree.delete(item)

        def delete_all():
            for record in my_tree.get_children():
                my_tree.delete(record)

            # Open the CSV file in write mode, which will truncate the file
            with open('Storage/Water/watbill.csv', mode='w', newline=''):
                pass  # No need to write anything, this will truncate the file

            # Delete all rows from the Treeview widget
            my_tree.delete(*my_tree.get_children())

        #  Button Add
        self.btn_remove = ctk.CTkButton(self.add_frame, text="Remove", font=self.fs_3, width=80, fg_color="green",
                                        border_color="green", border_width=0, text_color="White", hover_color="#73C088",command=remove)
        self.btn_remove.grid(column=0, row=2, padx=10, pady=10)

        self.btn_add = ctk.CTkButton(self.add_frame, text="Add", font=self.fs_3, width=80, fg_color="green",
                                     border_color="green", border_width=0, text_color="White", hover_color="#73C088",command=add_record)
        self.btn_add.grid(column=1, row=2, padx=10, pady=10, columnspan=3)

        self.btn_deleteAll = ctk.CTkButton(self.add_frame, text="Delete All", font=self.fs_3, width=80,
                                           fg_color="green", border_color="green",border_width=0, text_color="White",hover_color="#73C088",command=delete_all)
        self.btn_deleteAll.grid(column=4, row=2, padx=10, pady=10)

        my_tree.pack(pady=20)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 15, y=10)


class Grocery(ctk.CTkFrame):
    txtlabel = "white"
    label_color = "#355E3B"
    fr_color = "#fefae0"
    txt_color = "#FEFEFE"
    width = 700
    height = 600
    a = 180
    image1 = Image.open("img/shop_g.png")
    photo = ctk.CTkImage(dark_image=image1, size=(a, a))
    fs_0 = ("Fixedsys", 5)
    fs_1 = ("Fixedsys", 30)
    fs_2 = ("Fixedsys", 15)
    fs_3 = ctk.CTkFont(family="Fixedsys", size=20)

    def __init__(self, parent):
        super().__init__(parent)
        self.pack_propagate(False)
        self.configure(width=self.width, height=self.height)
        self.pack(side=ctk.LEFT)

        self.balance = 1000

        self.consumption = 0

        # Icon Frame
        self.icon_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, height=self.height)
        self.icon_frame.place(x=10, y=10)

        self.icon_lab = ctk.CTkLabel(self.icon_frame, text="Grocery", font=self.fs_1, text_color=self.txt_color)
        self.icon_lab.pack(pady=40)
        self.icon = ctk.CTkLabel(self.icon_frame, text='', image=self.photo)
        self.icon.pack(padx=10, pady=10)

        # Widgets'

        # Widgets
        # Current Balance Frame
        self.cbal_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.cbal_frame.pack(pady=10)
        self.cbal_frame.propagate(False)

        # Current Balance
        self.lb1 = ctk.CTkLabel(self.cbal_frame, text="Current Balance:", text_color=self.txtlabel, font=self.fs_3)
        self.lb1.configure(padx=5, pady=10)
        self.lb1.grid(column=0, row=0)

        with open(cb_file, "r") as bal:
            cont = csv.reader(bal)
            for row in cont:
                balance = row
        store = float(balance[0])

        self.balance_label = ctk.CTkLabel(self.cbal_frame, text=str(store), text_color=self.txt_color, font=self.fs_3)
        self.balance_label.configure(padx=10, pady=10)
        self.balance_label.grid(column=1, row=0)

        # Consumption Frame

        # Consumption Frame
        self.consump_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.consump_frame.pack(pady=10)

        # Stat Info
        self.lb3 = ctk.CTkLabel(self.consump_frame, text="Consumption:", text_color=self.txtlabel, font=self.fs_3)
        self.lb3.configure(padx=10, pady=10)
        self.lb3.grid(column=0, row=0)

        with open('Storage/Grocery/consumption.csv', "r") as con:
            store = csv.reader(con)
            for row in store:
                consum = row
        get = float(consum[0])

        self.consumption_label = ctk.CTkLabel(self.consump_frame, text=str(get), text_color=self.txt_color, font=self.fs_3)
        self.consumption_label.configure(padx=10, pady=10)
        self.consumption_label.grid(column=1, row=0)

        # Bottom Frame
        self.add_frame = ctk.CTkFrame(self, height=100, fg_color="transparent")
        self.add_frame.place(x=self.height // 2 - self.add_frame._current_width-60,
                             y=self.height - self.add_frame._current_height - 50)

        self.entry_label = ctk.CTkLabel(self.add_frame, text="Add Item/s", text_color=self.txt_color, font=self.fs_3)
        self.entry_label.grid(column=1, row=0, pady=5, columnspan=2)

        # Bottom frame Entry
        self.set = ctk.CTkEntry(self.add_frame, placeholder_text="Set", width=80, font=self.fs_3)
        self.set.grid(column=0, row=1, padx=20, pady=10)

        self.item = ctk.CTkEntry(self.add_frame, placeholder_text="Item", font=self.fs_3)
        self.item.grid(column=1, row=1, padx=20, pady=10)

        self.quantity = ctk.CTkEntry(self.add_frame, placeholder_text="Quantity", font=self.fs_3)
        self.quantity.grid(column=2, row=1, padx=20, pady=10)

        self.cost = ctk.CTkEntry(self.add_frame, placeholder_text="Cost(Php)", width=100, font=self.fs_3)
        self.cost.grid(column=3, row=1, padx=20, pady=10)


        #  Information Frame
        self.inf_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, width=410, border_color="#355E3B",
                                      height=self.height - self.add_frame._current_height - 115)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 20, y=20)
        self.inf_frame.propagate(False)

        # self.inf_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, width=440, border_color="black",
        #                               height=self.height - self.add_frame._current_height - 70)

        # self.inf_frame.place(x=self.width - self.inf_frame._current_width - 15, y=10)

        style = ttk.Style()
        style.theme_use("clam")
        style.map("Treeview")
        style.configure("Treeview.Heading", font=("Fixedsys", 15), background=c)
        style.configure("Treeview", rowheight=40, background="#121212",
                        fieldbacckground="#1f1b24", foreground=c, font=self.fs_2)

        # Table
        table = ttk.Treeview(self.inf_frame, columns=('set', 'items', 'quantity', 'cost', 'total'), show='headings',
                        height=20)

        table.heading('set', text='Set')
        table.column('set', width=60, anchor=CENTER)
        table.heading('items', text='Item/s')
        table.column('items', width=120, anchor=CENTER)
        table.heading('quantity', text='Quantity')
        table.column('quantity', width=100, anchor=CENTER)
        table.heading('cost', text='Cost')
        table.column('cost', width=100, anchor=CENTER)
        table.heading('total', text='Total')
        table.column('total', width=70, anchor=CENTER)
        table.pack(fill="both", expand=True)

        table.tag_configure("gray", background="#AFE1AF")
        table.tag_configure("normal", background="white")

        def display_on_table():
            count = 0
            with open("Storage/Grocery/remove.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 5:
                        if count % 2 == 0:
                            table.insert(parent='', index="end",text='', values=(row[0], row[1], row[2], row[3], row[4]))
                        else:
                            table.insert(parent='', index="end", text='', values=(row[0], row[1], row[2], row[3], row[4]))
                        count += 1

        display_on_table()
        root.update_idletasks()

        def add_rec():
            count = 0
            cset = 0.0

            if self.set.get() == "" or self.item.get() == "" or self.quantity.get() == "" or self.cost.get() == "":
                messagebox.showerror(title="Error", message="Please enter missing information")
            else:
                f = []
            with open("Storage/Grocery/consumption.csv", "r") as val:
                line = csv.reader(val)
                for i in line:
                    f = i
                    if len(f) >= 1:
                        cset = float(f[0])
                    else:
                        cset = 0.0

            set_val = self.set.get()
            item_val = self.item.get()
            quantity_val = self.quantity.get()
            cost_val = self.cost.get()

            if not quantity_val.isdigit() or not cost_val.isdigit():
                messagebox.showerror(title="Error", message="Quantity and Cost must be numeric values")
            else:
                total_val = float(quantity_val) * float(cost_val)
                cset += total_val  #  Consumption
                table.insert(parent="", index="end", text="", values=(set_val, item_val, quantity_val, cost_val, total_val))
                count += 1

                self.set.delete(0, END)
                self.item.delete(0, END)
                self.quantity.delete(0, END)
                self.cost.delete(0, END)

                items = [set_val, item_val, quantity_val, cost_val, total_val]

                with open('Storage/Grocery/remove.csv', 'a', newline='') as f:
                    content = csv.writer(f)
                    content.writerow(items)
                    insert = [cset]

                with open('Storage/Grocery/consumption.csv', 'w', newline="") as fl:
                    writer = csv.writer(fl)
                    writer.writerow(insert)

                with open("Storage/Grocery/consumption.csv", "r") as spend:
                    bal = csv.reader(spend)
                    for y in bal:
                        cp = y
                self.consumption_label.configure(text=cp[0]) #consump

                with open(cb_file, 'r') as alr:
                    cont = csv.reader(alr)
                    for row in cont:
                        sve = row
                currbal = float(sve[0])
                new = round(currbal - float(total_val), 2)
                k = [new]

                with open(cb_file, 'w', newline='') as w: #Current Bal
                    i = csv.writer(w)
                    i.writerow(k)

                # Comp
                with open(cb_file, 'r') as update:
                    store = csv.reader(update)
                    for i in store:
                        cb = i
                self.balance_label.configure(text=cb[0])

        # Button Add
        self.btn_add = ctk.CTkButton(self.add_frame, text="Add", width=80, fg_color="#489d22", font=(self.fs_3),
                                     text_color=self.txt_color,
                                     command=add_rec)
        self.btn_add.grid(column=0, row=2, pady=5, columnspan=2)

class Leisure(ctk.CTkFrame):
    txtlabel = "white"
    label_color = "#355E3B"
    fr_color = "transparent"
    width = 700
    height = 600
    a = 180
    image1 = Image.open("img/leisure_g.png")
    photo = ctk.CTkImage(light_image=image1, size=(a, a))
    fs_1 = ("Fixedsys", 30)
    fs_2 = ("Fixedsys", 15)
    fs_3 = ctk.CTkFont(family="Fixedsys", size=20)
    txt_color = "#FEFEFE"

    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)
        self.pack_propagate(False)
        self.configure(width=self.width, height=self.height)
        self.pack(side=ctk.LEFT)
        consumption_file_lei = "Storage/Leisure/lei_consumption.csv"
        item_lei = "Storage/Leisure/lei_items.csv"

        with open(cb_file, "r") as con:
            cont = csv.reader(con)
            for row in cont:
                balance = row

        hold = float(balance[0])

        cur_cons = ""
        with open(consumption_file_lei, 'r') as cons:
            red = csv.reader(cons)
            for o in red:
                fhil = o
                cur_cons = str(fhil[0])

        # Icon Frame
        self.icon_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, height=self.height)
        self.icon_frame.place(x=10, y=10)

        self.icon_lab = ctk.CTkLabel(self.icon_frame, text="Leisure", font=self.fs_1,
                                     text_color=self.txt_color)
        self.icon_lab.pack(pady=30)

        self.icon = ctk.CTkLabel(self.icon_frame, image=self.photo, text='')
        self.icon.pack(padx=30, pady=25)

        # Widgets
        # Current Balance Frame
        # Current Balance Frame
        self.cbal_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.cbal_frame.pack(pady=10)

        # Current Balance
        self.lb1 = ctk.CTkLabel(self.cbal_frame, text="Current Balance:", text_color=self.txtlabel, font=self.fs_3)
        self.lb1.configure(padx=10, pady=10)
        self.lb1.grid(column=0, row=0)

        self.lb2 = ctk.CTkLabel(self.cbal_frame, text=allowance_text, text_color=self.txt_color,font=self.fs_3)
        self.lb2.configure(padx=10, pady=10)
        self.lb2.grid(column=1, row=0)

        # Consumption Frame
        self.consump_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.consump_frame.pack(pady=10)

        # Stat Info
        self.lb3 = ctk.CTkLabel(self.consump_frame, text="Consumption:", text_color=self.txt_color, font=self.fs_3)
        self.lb3.configure(padx=10, pady=10)
        self.lb3.grid(column=0, row=0)

        self.lb4 = ctk.CTkLabel(self.consump_frame, text=cur_cons, text_color=self.txt_color,font=self.fs_3)
        self.lb4.configure(padx=10, pady=10)
        self.lb4.grid(column=1, row=0)

        # Bottom Frame
        self.add_frame = ctk.CTkFrame(self, height=100, fg_color=self.fr_color)
        self.add_frame.place(x=self.height // 2 - self.add_frame._current_width,
                             y=self.height - self.add_frame._current_height - 50)


        self.entry_label = ctk.CTkLabel(self.add_frame, text="Add Item/s", font=self.fs_3,
                                        text_color=self.txt_color)
        self.entry_label.grid(column=1, row=0, pady=5)

        # Bottom frame Entry
        # Bottom frame Entry


        self.item = ctk.CTkEntry(self.add_frame, placeholder_text="Item", font=self.fs_3,border_color="#355E3B")
        self.item.grid(column=0, row=1, padx=20, pady=10)

        self.quantity = ctk.CTkEntry(self.add_frame, placeholder_text="Quantity",font=self.fs_3,border_color="#355E3B")
        self.quantity.grid(column=1, row=1, padx=20, pady=10)

        self.cost = ctk.CTkEntry(self.add_frame, placeholder_text="Cost",font=self.fs_3,border_color="#355E3B")
        self.cost.grid(column=2, row=1, padx=20, pady=10)

        # Information Frame
        self.inf_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, width=410,
                                      height=self.height - self.add_frame._current_height - 100)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 25, y=40)
        self.inf_frame.propagate(False)

        # Information Content
        self.info_label = ctk.CTkLabel(self.inf_frame, text="Consumption History", text_color="black")

        # Table TableTableTableTableTableTableTableTableTableTableTableTableTable
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=40)

        style = ttk.Style()
        style.configure("Treeview", background="#121212",
                        fieldbackground="#1f1b24", foreground=c)
        style.configure("Treeview.Heading", font=("fixedsys", 14), background=c)

        my_table = ttk.Treeview(self.inf_frame, columns=('first', 'second', 'third', 'fourth'), show='headings',
                                height=self.inf_frame._current_height)
        my_table.tag_configure("headings", foreground="white")

        my_table.heading('first', text='Item/s')
        my_table.column('first', anchor=CENTER, width=200)
        my_table.heading('second', text='Quantity')
        my_table.column('second', anchor=CENTER, width=200)
        my_table.heading('third', text='Price')
        my_table.column('third', anchor=CENTER, width=100)
        my_table.heading('fourth', text='Total Cost')
        my_table.column('fourth', anchor=CENTER, width=100)
        my_table.pack(fill='both', expand=True)

        def read_and_display_data():
            count = 0
            with open(item_lei, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if count % 2 == 0:
                        my_table.insert(parent="", index="end", text="", values=(row[0], row[1], row[2], row[3]))
                    else:
                        my_table.insert(parent="", index="end", text="", values=(row[0], row[1], row[2], row[3]))
                    count += 1

        read_and_display_data()
        root.update_idletasks()

        def get_data():
            tot_data = 0
            count = 0
            with open(consumption_file_lei, 'r') as read:
                i = csv.reader(read)
                for item in i:
                    thing = item
            consumption = int(thing[0])

            if self.item.get() == "" or self.quantity.get() == "" or self.cost.get == "":
                messagebox.showerror(title="Error", message="Please enter missing information")

            else:
                item_data = self.item.get()
                quan_data = self.quantity.get()
                cost_data = self.cost.get()

                if not quan_data.isdigit() or not cost_data.isdigit():
                    messagebox.showerror(title="Error", message="Quantity and cost must be numeric values")
                else:
                    quan_data = int(quan_data)
                    cost_data = int(cost_data)

                    tot_data = quan_data * cost_data

                    my_table.insert(parent="", index="end", text="", values=(item_data, quan_data, cost_data, tot_data))
                    count += 1

                    self.item.delete(0, ctk.END)
                    self.quantity.delete(0, ctk.END)
                    self.cost.delete(0, ctk.END)

                    data = (item_data, quan_data, cost_data, tot_data)

                    with open(item_lei, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(data)

            consumption += tot_data
            insert = [consumption]

            with open(consumption_file_lei, 'w', newline='') as item:
                x = csv.writer(item)
                x.writerow(insert)

            # Msc Consumption data
            with open(consumption_file_lei, 'r') as spend:
                bal = csv.reader(spend)
                for y in bal:
                    cp = y
            self.lb4.configure(text=cp[0])  # Update the Consumption

            with open(cb_file, 'r') as alr:  # Access the allowance
                cont = csv.reader(alr)
                for row in cont:
                    sve = row
            alcom = float(sve[0])
            new = alcom - tot_data
            k = [new]

            with open(cb_file, 'w', newline='') as w:  # Update allowance
                i = csv.writer(w)
                i.writerow(k)

            #  Computation
            with open(cb_file, 'r') as update:
                store = csv.reader(update)
                for i in store:
                    cb = i
            self.lb2.configure(text=cb[0])  # Update Current Balance

            # Button Add
        self.btn_add = ctk.CTkButton(self.add_frame, text="Add", width=100, fg_color=c,font=self.fs_3,
                                     hover_color="#333333",
                                     border_width=2, border_color=c, text_color=self.txt_color, command=get_data)
        self.btn_add.grid(column=1, row=2, pady=10)


class Msc(ctk.CTkFrame):
    txtlabel = "white"
    label_color = "#355E3B"
    fr_color = "transparent"
    width = 700
    height = 600
    a = 180
    image1 = Image.open("img/misc_g.png")
    photo = ctk.CTkImage(light_image=image1, size=(a, a))
    fs_1 = ("fixedsys", 28, "bold")
    fs_2 = ("fixedsys", 15)
    fs_3 = ctk.CTkFont(family="fixedsys", size=20)
    txt_color = "#FEFEFE"

    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)
        self.pack_propagate(False)
        self.configure(width=self.width, height=self.height)
        self.pack(side=ctk.LEFT)

        cur_cons = ""
        with open(consumption_file, 'r') as cons:
            red = csv.reader(cons)
            for o in red:
                fhil = o
                cur_cons = str(fhil[0])

        # Icon Frame
        self.icon_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, height=self.height)
        self.icon_frame.place(x=10, y=10)

        self.icon_lab = ctk.CTkLabel(self.icon_frame, text="Miscellaneous", font=self.fs_1,
                                     text_color=self.txt_color)
        self.icon_lab.pack(pady=30)

        self.icon = ctk.CTkLabel(self.icon_frame, image=self.photo, text='')
        self.icon.pack(padx=30, pady=25)

        # Widgets
        # Current Balance Frame

        self.cbal_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.cbal_frame.pack(pady=10)

        # Current Balance
        self.lb1 = ctk.CTkLabel(self.cbal_frame, text="Current Balance:", text_color=self.txt_color, font=self.fs_3)
        self.lb1.configure(padx=10, pady=10)
        self.lb1.grid(column=0, row=0)

        self.lb2 = ctk.CTkLabel(self.cbal_frame, text=allowance_text, text_color=self.txt_color,font=self.fs_3)
        self.lb2.configure(padx=10, pady=10)
        self.lb2.grid(column=1, row=0)

        # Consumption Frame
        self.consump_frame = ctk.CTkFrame(self.icon_frame, fg_color=self.label_color)
        self.consump_frame.pack(pady=10)

        # Stat Info
        self.lb3 = ctk.CTkLabel(self.consump_frame, text="Consumption:", text_color=self.txt_color, font=self.fs_3)
        self.lb3.configure(padx=10, pady=10)
        self.lb3.grid(column=0, row=0)

        self.lb4 = ctk.CTkLabel(self.consump_frame, text=cur_cons, text_color=self.txt_color,font=self.fs_3)
        self.lb4.configure(padx=10, pady=10)
        self.lb4.grid(column=1, row=0)

        # Bottom Frame
        self.add_frame = ctk.CTkFrame(self, height=100, fg_color=self.fr_color)
        self.add_frame.place(x=self.height // 2 - self.add_frame._current_width,
                             y=self.height - self.add_frame._current_height - 50)

        self.entry_label = ctk.CTkLabel(self.add_frame, text="Add Item/s", font=self.fs_1,
                                        text_color=self.txt_color)
        self.entry_label.grid(column=1, row=0, pady=5)

        # Bottom frame Entry
        # Bottom frame Entry
        # Bottom frame Entry

        self.item = ctk.CTkEntry(self.add_frame, placeholder_text="Item",font= self.fs_3,border_color="#355E3b")
        self.item.grid(column=0, row=1, padx=20, pady=10)

        self.quantity = ctk.CTkEntry(self.add_frame, placeholder_text="Quantity",font=self.fs_3, border_color="#355E3b")
        self.quantity.grid(column=1, row=1, padx=20, pady=10)

        self.cost = ctk.CTkEntry(self.add_frame, placeholder_text="Cost", font=self.fs_3,border_color="#355E3b")
        self.cost.grid(column=2, row=1, padx=20, pady=10)

        # Information Frame
        self.inf_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=10, width=410,
                                      height=self.height - self.add_frame._current_height - 100)
        self.inf_frame.place(x=self.width - self.inf_frame._current_width - 25, y=40)
        self.inf_frame.propagate(False)

        # Information Content
        self.info_label = ctk.CTkLabel(self.inf_frame, text="Consumption History", text_color="black")

        # Table
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', rowheight=40)

        style = ttk.Style()
        style.configure("Treeview", background="#121212",
                        fieldbackground="#1f1b24", foreground=c, font=self.fs_2)
        style.configure("Treeview.Heading", font=("fixedsys", 14), background=c)

        my_table = ttk.Treeview(self.inf_frame, columns=('first', 'second', 'third', 'fourth'), show='headings',
                                height=self.inf_frame._current_height)
        my_table.tag_configure("headings", foreground="white")

        my_table.heading('first', text='Item/s')
        my_table.column('first', anchor=CENTER, width=200)
        my_table.heading('second', text='Quantity')
        my_table.column('second', anchor=CENTER, width=200)
        my_table.heading('third', text='Price')
        my_table.column('third', anchor=CENTER, width=100)
        my_table.heading('fourth', text='Total Cost')
        my_table.column('fourth', anchor=CENTER, width=100)
        my_table.pack(fill='both', expand=True)

        def read_and_display_data():
            count = 0
            with open(item_msc, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if count % 2 == 0:
                        my_table.insert(parent="", index="end", text="", values=(row[0], row[1], row[2], row[3]))
                    else:
                        my_table.insert(parent="", index="end", text="", values=(row[0], row[1], row[2], row[3]))
                    count += 1

        read_and_display_data()
        root.update_idletasks()

        def get_data():
            tot_data = 0
            count = 0
            with open(consumption_file, 'r') as read:
                i = csv.reader(read)
                for item in i:
                    thing = item
            consumption = float(thing[0])

            if self.item.get() == "" or self.quantity.get() == "" or self.cost.get == "":
                messagebox.showerror(title="Error", message="Please enter missing information")

            else:
                item_data = self.item.get()
                quan_data = self.quantity.get()
                cost_data = self.cost.get()

                if not quan_data.isdigit() or not cost_data.isdigit():
                    messagebox.showerror(title="Error", message="Quantity and cost must be numeric values")
                else:
                    quan_data = int(quan_data)
                    cost_data = float(cost_data)

                    tot_data = quan_data * cost_data

                    my_table.insert(parent="", index="end", text="", values=(item_data, quan_data, cost_data, tot_data))
                    count += 1

                    self.item.delete(0, ctk.END)
                    self.quantity.delete(0, ctk.END)
                    self.cost.delete(0, ctk.END)

                    data = (item_data, quan_data, cost_data, tot_data)

                    with open(item_msc, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(data)

            with open("Storage/limit.csv", 'r') as dj:
                jd = csv.reader(dj)
                for i in jd:
                    m = i
            lim = int(m[0])

            if tot_data < lim:
                consumption += tot_data  # Computation of consumption
            else:
                messagebox.showwarning("Warning", "You are almost out of balance!")
                consumption = consumption
            insert = [consumption]

            with open(consumption_file, 'w', newline='') as item:
                x = csv.writer(item)
                x.writerow(insert)

            # Msc Consumption data
            with open(consumption_file, 'r') as spend:
                bal = csv.reader(spend)
                for y in bal:
                    cp = y
            self.lb4.configure(text=cp[0])  # Update the Consumption

            with open(cb_file, 'r') as alr:  # Access the allowance
                cont = csv.reader(alr)
                for row in cont:
                    sve = row
            alcom = float(sve[0])
            new = alcom - tot_data
            k = [new]

            with open(cb_file, 'w', newline='') as w:  # Update allowance
                i = csv.writer(w)
                i.writerow(k)

            #  Computation
            with open(cb_file, 'r') as update:
                store = csv.reader(update)
                for i in store:
                    cb = i
            self.lb2.configure(text=cb[0])  # Update Current Balance

            # Button Add

        self.btn_add = ctk.CTkButton(self.add_frame, text="Add", width=100, fg_color=c, font= self.fs_3, hover_color="#333333",
                                     border_width=2, border_color=c, text_color=self.txt_color, command=get_data)
        self.btn_add.grid(column=1, row=2, pady=10)


class MainWindow:

    def __init__(self, master):
        self.frame = ctk.CTkFrame(master, fg_color=c, corner_radius=0, width=200)
        self.main_frame = ctk.CTkFrame(master)
        self.index = 0

        self.set_frames()
        self.electric_btn = ctk.CTkButton(self.frame, image=bolt_icon, text='ELECTRIC', hover_color="#333333",
                                          compound="left",
                                          corner_radius=0,
                                          anchor='w',
                                          font=fs_2, width=120, height=50, fg_color=c,
                                          command=self.elec_switch)  # Electric Button
        self.electric_btn.pack(padx=20, pady=20, fill="x")

        self.water_btn = ctk.CTkButton(self.frame, image=water_icon, text='WATER', hover_color="#333333",
                                       compound="left",
                                       corner_radius=0,
                                       anchor='w',
                                       font=fs_2, width=120, height=50,  fg_color=c,
                                       command=self.water_switch)  # Water Bill
        self.water_btn.pack(padx=20, pady=20, fill="x")

        self.grocery_btn = ctk.CTkButton(self.frame, image=grocery_icon, text='GROCERY', hover_color="#333333",
                                         compound="left",
                                         corner_radius=0,
                                         anchor='w',
                                         font=fs_2, width=120, height=50, fg_color=c,
                                         command=self.grocery_switch)  # grocery
        self.grocery_btn.pack(padx=20,pady=20, fill="x")

        self.leisure_btn = ctk.CTkButton(self.frame, image=leisure_icon, text='LEISURE', hover_color="#333333",
                                         compound="left",
                                         corner_radius=0,
                                         anchor='w',
                                         font=fs_2, width=120, height=50, fg_color=c,
                                         command=self.leisure_switch)  # leisure
        self.leisure_btn.pack(padx=20, pady=20, fill="x")

        self.msc_btn = ctk.CTkButton(self.frame, image=msc_icon, text='MISCELLANEOUS', width=120, hover_color="#333333",
                                     compound="left",
                                     corner_radius=0,
                                     anchor='w',
                                     font=fs_2, height=50, fg_color=c,
                                     command=self.msc_switch)  # Msc
        self.msc_btn.pack(padx=20, pady=20, fill="x")

        self.frame.pack(side=ctk.LEFT)
        self.frame.pack_propagate(False)
        self.frame.configure(width=160, height=600)

        self.main_frame.pack(side=ctk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=700, height=600)

    def set_frames(self):

        self.frame_list = [Electric(self.main_frame, get_bal()),
                           WaterBill(self.main_frame, get_bal()),
                           Grocery(self.main_frame),
                           Leisure(self.main_frame),
                           Msc(self.main_frame)]

    def elec_switch(self):
        update_csv(self.frame_list[0].lb2)
        self.frame_list[1].forget()
        self.frame_list[2].forget()
        self.frame_list[3].forget()
        self.frame_list[4].forget()
        self.frame_list[0].tkraise()
        self.frame_list[0].pack()

    def water_switch(self):
        update_csv(self.frame_list[1].lb2)
        self.frame_list[2].forget()
        self.frame_list[3].forget()
        self.frame_list[4].forget()
        self.frame_list[0].forget()
        self.frame_list[1].tkraise()
        self.frame_list[1].pack()

    def grocery_switch(self):
        update_csv(self.frame_list[2].balance_label)
        self.frame_list[3].forget()
        self.frame_list[4].forget()
        self.frame_list[0].forget()
        self.frame_list[1].forget()
        self.frame_list[2].tkraise()
        self.frame_list[2].pack()

    def leisure_switch(self):
        update_csv(self.frame_list[3].lb2)
        self.frame_list[4].forget()
        self.frame_list[0].forget()
        self.frame_list[1].forget()
        self.frame_list[2].forget()
        self.frame_list[3].tkraise()
        self.frame_list[3].pack()

    def msc_switch(self):
        update_csv(self.frame_list[4].lb2)
        self.frame_list[0].forget()
        self.frame_list[1].forget()
        self.frame_list[2].forget()
        self.frame_list[3].forget()
        self.frame_list[4].tkraise()
        self.frame_list[4].pack()


Info(root)
root.mainloop()
