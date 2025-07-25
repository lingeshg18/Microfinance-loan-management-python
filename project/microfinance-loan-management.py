from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

host="localhost"
user="root"
password="321@hsegnil"
database="microfinance_project_db"
port="3308"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database,port=port)

#main window
window=Tk()
window.geometry("600x600")
window.config(bg="#f0f4f7")
window.title("Microfinance Loan System - Login")

user_name_var=StringVar()
password_var=StringVar()
customer_name_var=StringVar()
customer_age_var=StringVar()
customer_gender_var=StringVar()
customer_email_var=StringVar()
customer_phone_var=IntVar()
customer_address_var=StringVar()
customer_username_var=StringVar()
customer_password_var=StringVar()
manage_customer_username_var=StringVar()
new_staff_admin_name_var=StringVar()
new_staff_admin_age_var=StringVar()
new_staff_admin_email_var=StringVar()
new_staff_admin_phone_var=StringVar()
new_staff_admin_address_var=StringVar()
new_staff_admin_username_var=StringVar()
new_staff_admin_password_var=StringVar()
manage_staff_username_var=StringVar()
change_password_admin_var=StringVar()
change_password_staff_var=StringVar()
change_password_customer_var=StringVar()
add_new_customer_admin_name_var=StringVar()
add_new_customer_admin_age_var=StringVar()
add_new_customer_admin_gender_var=StringVar()
add_new_customer_admin_email_var=StringVar()
add_new_customer_admin_phone_var=IntVar()
add_new_customer_admin_address_var=StringVar()
add_new_customer_admin_username_var=StringVar()
add_new_customer_admin_password_var=StringVar()
add_new_customer_staff_name_var=StringVar()
add_new_customer_staff_age_var=StringVar()
add_new_customer_staff_gender_var=StringVar()
add_new_customer_staff_email_var=StringVar()
add_new_customer_staff_phone_var=IntVar()
add_new_customer_staff_address_var=StringVar()
add_new_customer_staff_username_var=StringVar()
add_new_customer_staff_password_var=StringVar()


def customer_register():
    customer_registration_window=Tk()
    customer_registration_window.geometry("600x600")
    customer_registration_window.config(bg="#f0f4f7")
    customer_registration_window.title("New Customer Registration")

    label=Label(customer_registration_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
    label=Label(customer_registration_window,text="New Customer Registration", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=145,y=30)
    label=Label(customer_registration_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)

    label=Label(customer_registration_window,text="NAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=80)
    entry_name=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_name_var)
    entry_name.place(x=160,y=80)

    label=Label(customer_registration_window,text="AGE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=120)
    entry_age=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_age_var)
    entry_age.place(x=160,y=120)

    label=Label(customer_registration_window,text="GENDER:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=160)
    gender_options = ["Male", "Female", "Other"]
    gender_menu = OptionMenu(customer_registration_window, customer_gender_var, *gender_options)
    gender_menu.config(font=("georgia", 12), width=18)
    gender_menu.place(x=160, y=160)

    label=Label(customer_registration_window,text="EMAIL:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=200)
    entry_email=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_email_var)
    entry_email.place(x=160,y=200)

    label=Label(customer_registration_window,text="PHONE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=240)
    entry_phone=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_phone_var)
    entry_phone.place(x=160,y=240)

    label=Label(customer_registration_window,text="ADDRESS:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=280)
    entry_address=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_address_var)
    entry_address.place(x=160,y=280)

    label=Label(customer_registration_window,text="USERNAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=320)
    entry_username=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_username_var)
    entry_username.place(x=160,y=320)

    label=Label(customer_registration_window,text="PASSWORD:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=360)
    entry_password=Entry(customer_registration_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=customer_password_var,show="*")
    entry_password.place(x=160,y=360)

    def customer_registration_submit():
        name=entry_name.get()
        age=entry_age.get()
        gender=customer_gender_var.get()
        email=entry_email.get()
        phone=entry_phone.get()
        address=entry_address.get()
        username=entry_username.get()
        password=entry_password.get()

        if name and age and gender and email and phone and address and username and password:
            try:
                cursor=conn.cursor()
                cursor.execute("SELECT * from users WHERE username=%s",(username,))
                if cursor.fetchone():
                    messagebox.showerror("Error","Username already present❗❗")

                else:
                    cursor.execute("INSERT into users (full_name,age,gender,email,phone,address,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(name,age,gender,email,phone,address,username,password))
                    conn.commit()
                    messagebox.showinfo("Success","Data saved successfully")
                    customer_registration_window.destroy()

            except Exception as e:
                messagebox.showerror("Database Error",str(e))
        else:
            messagebox.showerror("Error","Incomplete!! ❌ Please complete all fields")

        

    btn=Button(customer_registration_window,text="Submit",height=1,width=11,font=("georgia",15),bg="#2980b9",fg="white",command=customer_registration_submit).place(x=230,y=450)

    customer_registration_window.mainloop()
def login():
    login_username=user_name_var.get()
    login_password=password_var.get()

    try:
        cursor=conn.cursor()
        cursor.execute("SELECT * from users WHERE username=%s",(login_username,))
        selected_row=cursor.fetchone()
        
        if selected_row:
            db_id,db_name,db_age,db_gender,db_username,db_password,db_email,db_phone,db_address,db_role,db_status,db_createdat=selected_row
            if db_password==login_password:
                if db_role=="admin":
                    admin_dashboard_window=Tk()
                    admin_dashboard_window.geometry("600x600")
                    admin_dashboard_window.config(bg="#f0f4f7")
                    admin_dashboard_window.title("Admin Dashboard")
                    # heading
                    label=Label(admin_dashboard_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                    label=Label(admin_dashboard_window,text="Admin Dashboard - Microfinance System", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=80,y=35)
                    label=Label(admin_dashboard_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                    # welcome
                    label=Label(admin_dashboard_window,text=f"Hello Admin {db_name}, welcome back!!", bg="#f0f4f7", fg="#171a4d",font=("georgia",14)).place(x=0,y=100)
                    # buttons
                    def add_new_customer_admin():
                        new_customer_registration_admin_window=Tk()
                        new_customer_registration_admin_window.geometry("600x600")
                        new_customer_registration_admin_window.config(bg="#f0f4f7")
                        new_customer_registration_admin_window.title("New Customer Registration - Admin")

                        label=Label(new_customer_registration_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(new_customer_registration_admin_window,text="Admin Dashboard - New Customer", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=95,y=30)
                        label=Label(new_customer_registration_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)

                        label=Label(new_customer_registration_admin_window,text="NAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=80)
                        entry_new_customer_admin_name=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_name_var)
                        entry_new_customer_admin_name.place(x=160,y=80)

                        label=Label(new_customer_registration_admin_window,text="AGE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=120)
                        entry_new_customer_admin_age=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_age_var)
                        entry_new_customer_admin_age.place(x=160,y=120)

                        label=Label(new_customer_registration_admin_window,text="GENDER:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=160)
                        gender_options = ["Male", "Female", "Other"]
                        gender_menu = OptionMenu(new_customer_registration_admin_window, add_new_customer_admin_gender_var, *gender_options)
                        gender_menu.config(font=("georgia", 12), width=18)
                        gender_menu.place(x=160, y=160)

                        label=Label(new_customer_registration_admin_window,text="EMAIL:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=200)
                        entry_new_customer_admin_email=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_email_var)
                        entry_new_customer_admin_email.place(x=160,y=200)

                        label=Label(new_customer_registration_admin_window,text="PHONE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=240)
                        entry_new_customer_admin_phone=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_phone_var)
                        entry_new_customer_admin_phone.place(x=160,y=240)

                        label=Label(new_customer_registration_admin_window,text="ADDRESS:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=280)
                        entry_new_customer_admin_address=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_address_var)
                        entry_new_customer_admin_address.place(x=160,y=280)

                        label=Label(new_customer_registration_admin_window,text="USERNAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=320)
                        entry_new_customer_admin_username=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_username_var)
                        entry_new_customer_admin_username.place(x=160,y=320)

                        label=Label(new_customer_registration_admin_window,text="PASSWORD:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=360)
                        entry_new_customer_admin_password=Entry(new_customer_registration_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_admin_password_var,show="*")
                        entry_new_customer_admin_password.place(x=160,y=360)

                        def new_customer_registration_admin_submit():
                            name=entry_new_customer_admin_name.get()
                            age=entry_new_customer_admin_age.get()
                            gender=add_new_customer_admin_gender_var.get()
                            email=entry_new_customer_admin_email.get()
                            phone=entry_new_customer_admin_phone.get()
                            address=entry_new_customer_admin_address.get()
                            username=entry_new_customer_admin_username.get()
                            password=entry_new_customer_admin_password.get()

                            if name and age and gender and email and phone and address and username and password:
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("SELECT * from users WHERE username=%s",(username,))
                                    if cursor.fetchone():
                                        messagebox.showerror("Error","Username already present❗❗")

                                    else:
                                        cursor.execute("INSERT into users (full_name,age,gender,email,phone,address,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(name,age,gender,email,phone,address,username,password))
                                        conn.commit()
                                        messagebox.showinfo("Success","Data saved successfully")
                                        new_customer_registration_admin_window.destroy()

                                except Exception as e:
                                    messagebox.showerror("Database Error",str(e))
                            else:
                                messagebox.showerror("Error","Incomplete!! ❌ Please complete all fields")

                            

                        btn=Button(new_customer_registration_admin_window,text="Submit",height=1,width=11,font=("georgia",15),bg="#2980b9",fg="white",command=new_customer_registration_admin_submit).place(x=230,y=450)

                        new_customer_registration_admin_window.mainloop()
                    def manage_customer():
                        manage_customer_window=Tk()
                        manage_customer_window.geometry("600x600")
                        manage_customer_window.config(bg="#f0f4f7")
                        manage_customer_window.title("Manage Customer")
                        # heading
                        label=Label(manage_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(manage_customer_window,text="Admin Dashboard - Manage Customer ", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=95,y=35)
                        label=Label(manage_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                        # search option
                        label=Label(manage_customer_window,text="Search by username:", bg="#f0f4f7", fg="#171a4d",font=("georgia",16)).place(x=0,y=100)
                        entry_username_manage_customer=Entry(manage_customer_window,width=25,font=("georgia",15),bg="white",fg="black",textvariable=manage_customer_username_var)
                        entry_username_manage_customer.place(x=205,y=100)
                        # tree view
                        cursor.execute("SELECT * FROM users WHERE role='customer'")
                        rows = cursor.fetchall()

                        columns = ("ID", "Name","Age","Gender","Username", "Password","Email","Phone","Address","Role","Status","Created at")
                        tree = ttk.Treeview(manage_customer_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=100, anchor="center")

                        for row in rows:
                            tree.insert("", "end", values=row)

                        scrollbar = ttk.Scrollbar(manage_customer_window, orient="vertical", command=tree.yview)
                        tree.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=580, y=140, height=350)
                        scrollbar = ttk.Scrollbar(manage_customer_window, orient="horizontal", command=tree.xview)
                        tree.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=10, y=490, width=580)

                        tree.place(x=10, y=140, width=570, height=350)


                        def search_customer():
                            search_username=entry_username_manage_customer.get()
                            
                            try:
                                cursor=conn.cursor()
                                cursor.execute("SELECT * from users WHERE username=%s",(search_username,))
                                searched_row=cursor.fetchone()

                                if searched_row:
                                    db_id,db_name,db_age,db_gender,db_username,db_password,db_email,db_phone,db_address,db_role,db_status,db_createdat=searched_row
                                    selected_customer_window=Tk()
                                    selected_customer_window.geometry("600x600")
                                    selected_customer_window.config(bg="#f0f4f7")
                                    selected_customer_window.title(f"{db_name} - Profile")
                                    label=Label(selected_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                                    label=Label(selected_customer_window,text=f"Selected Customer Profile - '{db_name}'", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=0,y=35)
                                    label=Label(selected_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                                     # tree view
                                    cursor.execute("SELECT * from users WHERE username=%s",(search_username,))
                                    searched_row=cursor.fetchone()

                                    columns = ("ID", "Name","Age","Gender","Username", "Password","Email","Phone","Address","Role","Status","Created at")
                                    tree = ttk.Treeview(selected_customer_window, columns=columns, show="headings", height=8)

                                    for col in columns:
                                        tree.heading(col, text=col)
                                        tree.column(col, width=100, anchor="center")

                                    
                                    tree.insert("", "end", values=searched_row)

                                    tree.place(x=10, y=120, width=570, height=100)

                                    scrollbar = ttk.Scrollbar(selected_customer_window, orient="horizontal", command=tree.xview)
                                    tree.configure(xscrollcommand=scrollbar.set)
                                    scrollbar.place(x=10, y=225, width=580)

                                    def manage_customer_edit():
                                        manage_customer_edit_window=Tk()
                                        manage_customer_edit_window.geometry("600x600")
                                        manage_customer_edit_window.config(bg="#f0f4f7")
                                        manage_customer_edit_window.title("Manage Customer - Edit")

                                        manage_customer_edit_gender_var=StringVar()
                                        manage_customer_edit_status_var=StringVar()

                                        label=Label(manage_customer_edit_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                                        label=Label(manage_customer_edit_window,text="Manage Customer - Edit", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=135,y=35)
                                        label=Label(manage_customer_edit_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                                        Label(manage_customer_edit_window, text="Full Name:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=100)
                                        name_entry = Entry(manage_customer_edit_window, width=30,font=("georgia",12))
                                        name_entry.insert(0, db_name)
                                        name_entry.place(x=150, y=100)

                                        Label(manage_customer_edit_window, text="Age:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=140)
                                        age_entry = Entry(manage_customer_edit_window, width=30,font=("georgia",12))
                                        age_entry.insert(0, db_age)
                                        age_entry.place(x=150, y=140)

                                        manage_customer_edit_gender_var.set(db_gender) 

                                        Label(manage_customer_edit_window, text="Gender:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=180)
                                        gender_options = ["Male", "Female", "Other"]
                                        gender_menu = OptionMenu(manage_customer_edit_window, manage_customer_edit_gender_var, *gender_options)
                                        gender_menu.config(font=("georgia", 12), width=18)
                                        gender_menu.place(x=150, y=180)

                    
                                        Label(manage_customer_edit_window, text="Password:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=220)
                                        password_entry = Entry(manage_customer_edit_window, width=30,font=("georgia",12))
                                        password_entry.insert(0, db_password)
                                        password_entry.place(x=150, y=220)

                                        Label(manage_customer_edit_window, text="Email:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=260)
                                        email_entry = Entry(manage_customer_edit_window, width=30,font=("georgia",12))
                                        email_entry.insert(0, db_email)
                                        email_entry.place(x=150, y=260)

                                        Label(manage_customer_edit_window, text="Phone:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=300)
                                        phone_entry = Entry(manage_customer_edit_window, width=30,font=("georgia",12))
                                        phone_entry.insert(0, db_phone)
                                        phone_entry.place(x=150, y=300)

                                        Label(manage_customer_edit_window, text="Address:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=340)
                                        address_entry = Entry(manage_customer_edit_window, width=30,font=("georgia",12))
                                        address_entry.insert(0, db_address)
                                        address_entry.place(x=150, y=340)

                                        manage_customer_edit_status_var.set(db_status)

                                        Label(manage_customer_edit_window, text="Status:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=380)
                                        status_options = ["Active", "Inactive"]
                                        status_menu = OptionMenu(manage_customer_edit_window, manage_customer_edit_status_var, *status_options)
                                        status_menu.config(font=("georgia", 12), width=18)
                                        status_menu.place(x=150, y=380)  

                                        def update():
                                            name=name_entry.get()
                                            age=age_entry.get()
                                            gender=manage_customer_edit_gender_var.get()
                                            password=password_entry.get()
                                            email=email_entry.get()
                                            phone=phone_entry.get()
                                            address=address_entry.get()
                                            status=manage_customer_edit_status_var.get()

                                            if not all([name,age,gender,password,email,phone,address,status]):
                                                messagebox.showerror("Error", "All fields must be filled.")
                                                return
                                            try:
                                                cursor=conn.cursor()
                                                cursor.execute("UPDATE users SET full_name=%s,age=%s,gender=%s,password=%s,email=%s,phone=%s,address=%s,status=%s WHERE username=%s",(name,age,gender,password,email,phone,address,status,db_username))
                                                conn.commit()
                                                messagebox.showinfo("Success", "Customer updated successfully.")
                                                manage_customer_edit_window.destroy()

                                            except Exception as e:
                                                messagebox.showerror("Database Error", str(e))    

                                        btn=Button(manage_customer_edit_window,text="Update",height=1,width=15,font=("georgia",12),bg="#2980b9",fg="white",command=update).place(x=225,y=450)
                                        manage_customer_edit_window.mainloop()
                                    
                                    def manage_customer_delete():
                                        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete customer '{db_username}' and all related data?")
                                        if not confirm:
                                            return
                                        try:
                                            cursor = conn.cursor()
                                            cursor.execute("SELECT loan_id FROM loans WHERE username = %s", (db_username,))
                                            loan_ids = cursor.fetchall()
    
                                            for loan_id_tuple in loan_ids:
                                                loan_id = loan_id_tuple[0]
                                                cursor.execute("DELETE FROM repayments WHERE loan_id = %s", (loan_id,))
                                        
                                            cursor.execute("DELETE FROM loans WHERE username = %s", (db_username,))
                                            cursor.execute("DELETE FROM users WHERE username = %s", (db_username,))
                                            
                                            conn.commit()
                                            messagebox.showinfo("Success", f"Customer '{db_username}' and all associated loans and repayments deleted successfully.")
                                            manage_customer_window.destroy()
                                            selected_customer_window.destroy()

                                        except Exception as e:
                                            messagebox.showerror("Database Error", str(e))
                                    def manage_customer_refresh():
                                        try:
                                            for item in tree.get_children():
                                                tree.delete(item)

                                            cursor=conn.cursor()
                                            cursor.execute("SELECT * FROM users WHERE role = 'customer'")
                                            rows = cursor.fetchall()

                                            for row in rows:
                                                tree.insert("", "end", values=row)
                                            selected_customer_window.destroy()
                                        
                                        except Exception as e:
                                            messagebox.showerror("Database Error", str(e))

                                        
                                    label_link=Label(selected_customer_window,text="[Edit]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                                    label_link.place(x=100,y=300)
                                    label_link.bind("<Button-1>", lambda e: manage_customer_edit())
                                    label_link=Label(selected_customer_window,text="[Delete]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                                    label_link.place(x=215,y=300)
                                    label_link.bind("<Button-1>", lambda e: manage_customer_delete())
                                    label_link=Label(selected_customer_window,text="[Refresh]",bg="#f0f4f7",fg="Red",font=("normal",15,"underline"),cursor="hand2")
                                    label_link.place(x=355,y=300)
                                    label_link.bind("<Button-1>", lambda e: manage_customer_refresh())
                                       
                                    selected_customer_window.mainloop()
                                
                                else:
                                    messagebox.showinfo("Not Found", "No customer found with that username.")

                            except Exception as e:
                                messagebox.showerror("Database Error",str(e))      

                        label_link=Label(manage_customer_window,text="Search",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                        label_link.place(x=515,y=100)
                        label_link.bind("<Button-1>", lambda e: search_customer())
                        manage_customer_window.mainloop()
                    
                    def create_staff_admin():
                        create_staff_admin_window=Tk()
                        create_staff_admin_window.geometry("600x600")
                        create_staff_admin_window.config(bg="#f0f4f7")
                        create_staff_admin_window.title("Create Staff / Admin")

                        new_staff_admin_gender_var = StringVar()
                        new_staff_admin_gender_var.set("Select Gender")
                        new_staff_admin_role_var = StringVar()
                        new_staff_admin_role_var.set("Select Role")
                        new_staff_admin_status_var = StringVar()
                        new_staff_admin_status_var.set("Select Status")


                        label=Label(create_staff_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(create_staff_admin_window,text="Create Staff / Admin", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=165,y=30)
                        label=Label(create_staff_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)

                        label=Label(create_staff_admin_window,text="NAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=80)
                        entry_name=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_name_var)
                        entry_name.place(x=160,y=80)

                        label=Label(create_staff_admin_window,text="AGE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=120)
                        entry_age=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_age_var)
                        entry_age.place(x=160,y=120)

                        label=Label(create_staff_admin_window,text="GENDER:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=160)
                        gender_options = ["Male", "Female", "Other"]
                        gender_menu = OptionMenu(create_staff_admin_window, new_staff_admin_gender_var, *gender_options)
                        gender_menu.config(font=("georgia", 12), width=18)
                        gender_menu.place(x=160, y=160)

                        label=Label(create_staff_admin_window,text="EMAIL:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=200)
                        entry_email=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_email_var)
                        entry_email.place(x=160,y=200)

                        label=Label(create_staff_admin_window,text="PHONE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=240)
                        entry_phone=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_phone_var)
                        entry_phone.place(x=160,y=240)

                        label=Label(create_staff_admin_window,text="ADDRESS:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=280)
                        entry_address=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_address_var)
                        entry_address.place(x=160,y=280)

                        label=Label(create_staff_admin_window,text="USERNAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=320)
                        entry_username=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_username_var)
                        entry_username.place(x=160,y=320)

                        label=Label(create_staff_admin_window,text="PASSWORD:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=360)
                        entry_password=Entry(create_staff_admin_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=new_staff_admin_password_var,show="*")
                        entry_password.place(x=160,y=360)

                        label=Label(create_staff_admin_window,text="ROLE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=400)
                        role_options = ["Admin", "Staff"]
                        role_menu = OptionMenu(create_staff_admin_window, new_staff_admin_role_var, *role_options)
                        role_menu.config(font=("georgia", 12), width=18)
                        role_menu.place(x=160, y=400)

                        label=Label(create_staff_admin_window,text="STATUS:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=440)
                        status_options = ["Active", "Inactive"]
                        status_menu = OptionMenu(create_staff_admin_window, new_staff_admin_status_var, *status_options)
                        status_menu.config(font=("georgia", 12), width=18)
                        status_menu.place(x=160, y=440)

                        def staff_admin_registration_submit():
                            name=entry_name.get()
                            age=entry_age.get()
                            gender=new_staff_admin_gender_var.get()
                            email=entry_email.get()
                            phone=entry_phone.get()
                            address=entry_address.get()
                            username=entry_username.get()
                            password=entry_password.get()
                            role=new_staff_admin_role_var.get()
                            status=new_staff_admin_status_var.get()

                            if name and age and gender and email and phone and address and username and password and role and status:
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("SELECT * from users WHERE username=%s",(username,))
                                    if cursor.fetchone():
                                        messagebox.showerror("Error","Username already present❗❗")

                                    else:
                                        cursor.execute("INSERT into users (full_name,age,gender,email,phone,address,username,password,role,status) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,age,gender,email,phone,address,username,password,role,status))
                                        conn.commit()
                                        messagebox.showinfo("Success","Data saved successfully")
                                        create_staff_admin_window.destroy()

                                except Exception as e:
                                    messagebox.showerror("Database Error",str(e))
                            else:
                                messagebox.showerror("Error","Incomplete!! ❌ Please complete all fields")                            

                        btn=Button(create_staff_admin_window,text="Submit",height=1,width=11,font=("georgia",15),bg="#2980b9",fg="white",command=staff_admin_registration_submit).place(x=230,y=500)
                        
                        create_staff_admin_window.mainloop()

                    def manage_staff():
                        manage_staff_window=Tk()
                        manage_staff_window.geometry("600x600")
                        manage_staff_window.config(bg="#f0f4f7")
                        manage_staff_window.title("Manage Customer")

                        # heading
                        label=Label(manage_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(manage_staff_window,text="Admin Dashboard - Manage Staff ", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=110,y=35)
                        label=Label(manage_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                        # search option
                        label=Label(manage_staff_window,text="Search by username:", bg="#f0f4f7", fg="#171a4d",font=("georgia",16)).place(x=0,y=100)
                        entry_username_manage_staff=Entry(manage_staff_window,width=25,font=("georgia",15),bg="white",fg="black",textvariable=manage_staff_username_var)
                        entry_username_manage_staff.place(x=205,y=100)
                        # tree view
                        cursor.execute("SELECT * FROM users WHERE role='staff'")
                        rows = cursor.fetchall()

                        columns = ("ID", "Name","Age","Gender","Username", "Password","Email","Phone","Address","Role","Status","Created at")
                        tree = ttk.Treeview(manage_staff_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=100, anchor="center")

                        for row in rows:
                            tree.insert("", "end", values=row)

                        scrollbar = ttk.Scrollbar(manage_staff_window, orient="vertical", command=tree.yview)
                        tree.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=580, y=140, height=350)
                        scrollbar = ttk.Scrollbar(manage_staff_window, orient="horizontal", command=tree.xview)
                        tree.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=10, y=490, width=580)

                        tree.place(x=10, y=140, width=570, height=350)


                        def search_staff():
                            search_username=entry_username_manage_staff.get()
                            
                            try:
                                cursor=conn.cursor()
                                cursor.execute("SELECT * from users WHERE username=%s",(search_username,))
                                searched_row=cursor.fetchone()

                                if searched_row:
                                    db_id,db_name,db_age,db_gender,db_username,db_password,db_email,db_phone,db_address,db_role,db_status,db_createdat=searched_row
                                    selected_staff_window=Tk()
                                    selected_staff_window.geometry("600x600")
                                    selected_staff_window.config(bg="#f0f4f7")
                                    selected_staff_window.title(f"{db_name} - Profile")
                                    label=Label(selected_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                                    label=Label(selected_staff_window,text=f"Selected Staff Profile - '{db_name}'", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=0,y=35)
                                    label=Label(selected_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                                     # tree view
                                    cursor.execute("SELECT * from users WHERE username=%s",(search_username,))
                                    searched_staff_row=cursor.fetchone()

                                    columns = ("ID", "Name","Age","Gender","Username", "Password","Email","Phone","Address","Role","Status","Created at")
                                    tree = ttk.Treeview(selected_staff_window, columns=columns, show="headings", height=8)

                                    for col in columns:
                                        tree.heading(col, text=col)
                                        tree.column(col, width=100, anchor="center")

                                    
                                    tree.insert("", "end", values=searched_staff_row)

                                    tree.place(x=10, y=120, width=570, height=100)

                                    scrollbar = ttk.Scrollbar(selected_staff_window, orient="horizontal", command=tree.xview)
                                    tree.configure(xscrollcommand=scrollbar.set)
                                    scrollbar.place(x=10, y=225, width=580)

                                    def manage_staff_edit():
                                        manage_staff_edit_window=Tk()
                                        manage_staff_edit_window.geometry("600x600")
                                        manage_staff_edit_window.config(bg="#f0f4f7")
                                        manage_staff_edit_window.title("Manage Staff - Edit")

                                        manage_staff_edit_gender_var=StringVar()
                                        manage_staff_edit_status_var=StringVar()                                        

                                        label=Label(manage_staff_edit_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                                        label=Label(manage_staff_edit_window,text="Manage Staff - Edit", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=165,y=35)
                                        label=Label(manage_staff_edit_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                                        Label(manage_staff_edit_window, text="Full Name:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=100)
                                        name_entry = Entry(manage_staff_edit_window, width=30,font=("georgia",12))
                                        name_entry.insert(0, db_name)
                                        name_entry.place(x=150, y=100)

                                        Label(manage_staff_edit_window, text="Age:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=140)
                                        age_entry = Entry(manage_staff_edit_window, width=30,font=("georgia",12))
                                        age_entry.insert(0, db_age)
                                        age_entry.place(x=150, y=140)

                                        manage_staff_edit_gender_var.set(db_gender) 

                                        Label(manage_staff_edit_window, text="Gender:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=180)
                                        gender_options = ["Male", "Female", "Other"]
                                        gender_menu = OptionMenu(manage_staff_edit_window, manage_staff_edit_gender_var, *gender_options)
                                        gender_menu.config(font=("georgia", 12), width=18)
                                        gender_menu.place(x=150, y=180)                
                    
                                        Label(manage_staff_edit_window, text="Password:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=220)
                                        password_entry = Entry(manage_staff_edit_window, width=30,font=("georgia",12))
                                        password_entry.insert(0, db_password)
                                        password_entry.place(x=150, y=220)

                                        Label(manage_staff_edit_window, text="Email:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=260)
                                        email_entry = Entry(manage_staff_edit_window, width=30,font=("georgia",12))
                                        email_entry.insert(0, db_email)
                                        email_entry.place(x=150, y=260)

                                        Label(manage_staff_edit_window, text="Phone:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=300)
                                        phone_entry = Entry(manage_staff_edit_window, width=30,font=("georgia",12))
                                        phone_entry.insert(0, db_phone)
                                        phone_entry.place(x=150, y=300)

                                        Label(manage_staff_edit_window, text="Address:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=340)
                                        address_entry = Entry(manage_staff_edit_window, width=30,font=("georgia",12))
                                        address_entry.insert(0, db_address)
                                        address_entry.place(x=150, y=340)

                                        manage_staff_edit_status_var.set(db_status)

                                        Label(manage_staff_edit_window, text="Status:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=380)
                                        status_options = ["Active", "Inactive"]
                                        status_menu = OptionMenu(manage_staff_edit_window, manage_staff_edit_status_var, *status_options)
                                        status_menu.config(font=("georgia", 12), width=18)
                                        status_menu.place(x=150, y=380)

                                        def update_staff():
                                            name=name_entry.get()
                                            age=age_entry.get()
                                            gender=manage_staff_edit_gender_var.get()
                                            password=password_entry.get()
                                            email=email_entry.get()
                                            phone=phone_entry.get()
                                            address=address_entry.get()
                                            status=manage_staff_edit_status_var.get()

                                            if not all([name,age,gender,password,email,phone,address,status]):
                                                messagebox.showerror("Error", "All fields must be filled.")
                                                return
                                            else:
                                                try:
                                                    cursor=conn.cursor()
                                                    cursor.execute("UPDATE users SET full_name=%s,age=%s,gender=%s,password=%s,email=%s,phone=%s,address=%s,status=%s WHERE username=%s",(name,age,gender,password,email,phone,address,status,db_username))
                                                    conn.commit()
                                                    messagebox.showinfo("Success", "Customer updated successfully.")
                                                    manage_staff_edit_window.destroy()

                                                except Exception as e:
                                                    messagebox.showerror("Database Error", str(e))    

                                        btn=Button(manage_staff_edit_window,text="Update",height=1,width=15,font=("georgia",12),bg="#2980b9",fg="white",command=update_staff).place(x=225,y=450)
                                        manage_staff_edit_window.mainloop()
                                    
                                    def manage_staff_delete():
                                        try:
                                            cursor.execute("SELECT COUNT(*) FROM loans WHERE user_id = %s", (db_id,))
                                            count = cursor.fetchone()[0]

                                            if count > 0:
                                                messagebox.showwarning("Cannot Delete", "This staff is assigned to loans. Reassign or delete those first.")
                                                return
                                            # Proceed to delete the staff
                                            cursor.execute("DELETE FROM users WHERE username = %s", (db_username,))
                                            conn.commit()
                                            messagebox.showinfo("Deleted", "Staff user deleted successfully.")
                                            selected_staff_window.destroy()
                                            manage_staff_window.destroy()

                                        except Exception as e:
                                            messagebox.showerror("Database Error", str(e))
                                    def manage_staff_refresh():
                                        try:
                                            for item in tree.get_children():
                                                tree.delete(item)

                                            cursor=conn.cursor()
                                            cursor.execute("SELECT * FROM users WHERE role = 'customer'")
                                            rows = cursor.fetchall()

                                            for row in rows:
                                                tree.insert("", "end", values=row)
                                            selected_staff_window.destroy()
                                            manage_staff_window.destroy()
                                        
                                        except Exception as e:
                                            messagebox.showerror("Database Error", str(e))

                                        
                                    label_link=Label(selected_staff_window,text="[Edit]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                                    label_link.place(x=100,y=300)
                                    label_link.bind("<Button-1>", lambda e: manage_staff_edit())
                                    label_link=Label(selected_staff_window,text="[Delete]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                                    label_link.place(x=215,y=300)
                                    label_link.bind("<Button-1>", lambda e: manage_staff_delete())
                                    label_link=Label(selected_staff_window,text="[Refresh]",bg="#f0f4f7",fg="Red",font=("normal",15,"underline"),cursor="hand2")
                                    label_link.place(x=355,y=300)
                                    label_link.bind("<Button-1>", lambda e: manage_staff_refresh())
                                       
                                    selected_staff_window.mainloop()
                                
                                else:
                                    messagebox.showinfo("Not Found", "No customer found with that username.")

                            except Exception as e:
                                messagebox.showerror("Database Error",str(e))      

                        label_link=Label(manage_staff_window,text="Search",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                        label_link.place(x=515,y=100)
                        label_link.bind("<Button-1>", lambda e: search_staff())
                        manage_staff_window.mainloop()
                    def manage_loans():
                        manage_loans_admin_window=Tk()
                        manage_loans_admin_window.geometry("600x600")
                        manage_loans_admin_window.config(bg="#f0f4f7")
                        manage_loans_admin_window.title("Manage Loans - Admin")
                        
                        label=Label(manage_loans_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(manage_loans_admin_window,text="Manage Loans - Admin", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=150,y=35)
                        label=Label(manage_loans_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                         # tree view
                        cursor.execute("SELECT * FROM loans")
                        rows= cursor.fetchall()

                        columns = ("Loan ID", "Users ID","Username","Name","Amount", "Tenure","Interest Rate","Status","Application Date")
                        tree = ttk.Treeview(manage_loans_admin_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=100, anchor="center")

                        for row in rows:
                            tree.insert("", "end", values=row)

                        scrollbar = ttk.Scrollbar(manage_loans_admin_window, orient="vertical", command=tree.yview)
                        tree.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=580, y=100, height=350)
                        scrollbar = ttk.Scrollbar(manage_loans_admin_window, orient="horizontal", command=tree.xview)
                        tree.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=10, y=450, width=580)

                        tree.place(x=10, y=100, width=570, height=350)

                        def manage_loans_refresh():
                            for row in tree.get_children():
                                tree.delete(row)

                            cursor.execute("SELECT * FROM loans")
                            rows = cursor.fetchall()

                            for row in rows:
                                tree.insert("", "end", values=row)


                        def manage_loans_treeview_double_click(event):  
                            selected_item = tree.focus()
                            if not selected_item:
                                return

                            row_data = tree.item(selected_item)['values']
                            if not row_data:
                                return

                            # Create new window
                            manage_loans_doubleclick_window= Toplevel()
                            manage_loans_doubleclick_window.geometry("700x200")
                            manage_loans_doubleclick_window.config(bg="#f0f4f7")
                            manage_loans_doubleclick_window.title("Loan Details")

                            # Create Treeview with same columns
                            columns = ("Loan ID", "User ID", "Username", "Name", "Amount", "Tenure", "Interest Rate", "Status", "Application Date")
                            detail_tree = ttk.Treeview(manage_loans_doubleclick_window, columns=columns, show="headings", height=3)

                            for col in columns:
                                detail_tree.heading(col, text=col)
                                detail_tree.column(col, width=70, anchor="center")

                            scrollbar = ttk.Scrollbar(manage_loans_doubleclick_window, orient="horizontal", command=tree.xview)
                            tree.configure(xscrollcommand=scrollbar.set)
                            scrollbar.place(x=0, y=120, width=500)                                

                            detail_tree.insert("", "end", values=row_data)
                            detail_tree.place(x=0,y=20,width=500,height=100)

                            loan_id=row_data[0]

                            def approve_loans_admin():
                                try:
                                    cursor.execute("UPDATE loans SET status = 'Approved' WHERE loan_id = %s", (loan_id,))
                                    conn.commit()
                                    messagebox.showinfo("Success", f"Loan #{loan_id} status updated to Approved.")
                                    manage_loans_doubleclick_window.destroy()
                                    manage_loans_refresh()  
                                except Exception as e:
                                    messagebox.showerror("Database Error", str(e))
                            def reject_loans_admin():
                                try:
                                    cursor.execute("UPDATE loans SET status = 'Rejected' WHERE loan_id = %s", (loan_id,))
                                    conn.commit()
                                    messagebox.showinfo("Success", f"Loan #{loan_id} status updated to Rejected.")
                                    manage_loans_doubleclick_window.destroy()
                                    manage_loans_refresh()  
                                except Exception as e:
                                    messagebox.showerror("Database Error", str(e))
                            def manage_loans_doubleclick_close():
                                confirm=messagebox.showinfo("Close","Are you sure you want to close the window?")
                                if confirm:
                                    manage_loans_doubleclick_window.destroy()
                            def delete_customer_loan():
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("DELETE FROM loans WHERE loan_id=%s",(loan_id,))
                                    conn.commit()
                                    messagebox.showinfo("Success", "Customer deleted successfully.")
                                    manage_loans_doubleclick_window.destroy()
                                    manage_loans_refresh()

                                except Exception as e:
                                    messagebox.showerror("Database Error", str(e))           

                            label_link=Label(manage_loans_doubleclick_window,text="[Delete]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                            label_link.place(x=550,y=140)
                            label_link.bind("<Button-1>", lambda e: delete_customer_loan())

                            label_link=Label(manage_loans_doubleclick_window,text="[Approve]",bg="#f0f4f7",fg="green",font=("normal",15,"underline"),cursor="hand2")
                            label_link.place(x=550,y=20)
                            label_link.bind("<Button-1>", lambda e: approve_loans_admin()) 

                            label_link=Label(manage_loans_doubleclick_window,text="[Reject]",bg="#f0f4f7",fg="red",font=("normal",15,"underline"),cursor="hand2")
                            label_link.place(x=550,y=60)
                            label_link.bind("<Button-1>", lambda e: reject_loans_admin())

                            label_link=Label(manage_loans_doubleclick_window,text="[Close]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                            label_link.place(x=550,y=100)
                            label_link.bind("<Button-1>", lambda e: manage_loans_doubleclick_close())

                        tree.bind("<Double-1>", manage_loans_treeview_double_click)

                        def add_new_loans():
                            add_new_loan_window=Toplevel()
                            add_new_loan_window.geometry("600x600")
                            add_new_loan_window.config(bg="#f0f4f7")
                            add_new_loan_window.title("New Loan")

                            label=Label(add_new_loan_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                            label=Label(add_new_loan_window,text="New Loan", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=235,y=30)
                            label=Label(add_new_loan_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)

                            cursor.execute("SELECT * FROM users WHERE role='customer'")
                            rows = cursor.fetchall()

                            columns = ("ID", "Name","Age","Gender","Username", "Password","Email","Phone","Address","Role","Status","Created at")
                            tree_loan_users = ttk.Treeview(add_new_loan_window, columns=columns, show="headings", height=8)

                            for col in columns:
                                tree_loan_users.heading(col, text=col)
                                tree_loan_users.column(col, width=100, anchor="center")

                            for row in rows:
                                tree_loan_users.insert("", "end", values=row)

                            scrollbar = ttk.Scrollbar(add_new_loan_window, orient="vertical", command=tree_loan_users.yview)
                            tree_loan_users.configure(yscrollcommand=scrollbar.set)
                            scrollbar.place(x=580, y=140, height=350)
                            scrollbar = ttk.Scrollbar(add_new_loan_window, orient="horizontal", command=tree_loan_users.xview)
                            tree_loan_users.configure(xscrollcommand=scrollbar.set)
                            scrollbar.place(x=10, y=490, width=580)

                            tree_loan_users.place(x=10, y=140, width=570, height=350)
                            
                            def add_loan_for_selected_customer(event):

                                selected_item = tree_loan_users.focus()
                                if not selected_item:
                                    messagebox.showwarning("No Selection", "Please select a customer.")
                                    return

                                user_data = tree_loan_users.item(selected_item, "values")
                                user_id = user_data[0]
                                full_name = user_data[1]
                                username = user_data[4]

                                add_loan_for_selected_customer_window=Toplevel()
                                add_loan_for_selected_customer_window.geometry("600x600")
                                add_loan_for_selected_customer_window.config(bg="#f0f4f7")
                                add_loan_for_selected_customer_window.title(f"Add Loan for {full_name}")

                                label=Label(add_loan_for_selected_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                                label=Label(add_loan_for_selected_customer_window,text=f"Add loan for{full_name}", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=135,y=30)
                                label=Label(add_loan_for_selected_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)


                                label=Label(add_loan_for_selected_customer_window, text=f"Customer No.{user_id}: {full_name} ({username})", bg="#f0f4f7", fg="#171a4d", font=("georgia", 15)).place(x=30,y=100)

                                label=Label(add_loan_for_selected_customer_window, text="Amount:", bg="#f0f4f7", fg="#171a4d",font=("georgia", 15)).place(x=30,y=150)
                                amount_var_loans = StringVar()
                                entry_amount_loans=Entry(add_loan_for_selected_customer_window, textvariable=amount_var_loans,width=30,font=("georgia", 13)).place(x=200,y=150)

                                label=Label(add_loan_for_selected_customer_window, text="Tenure (months):", bg="#f0f4f7", fg="#171a4d",font=("georgia", 15)).place(x=30,y=200)
                                tenure_var_loans = StringVar()
                                enrty_tenure_loans=Entry(add_loan_for_selected_customer_window, textvariable=tenure_var_loans,width=30,font=("georgia", 13)).place(x=200,y=200)

                                label=Label(add_loan_for_selected_customer_window, text="Interest Rate (%):", bg="#f0f4f7", fg="#171a4d",font=("georgia", 15)).place(x=30,y=250)
                                interest_var_loans = StringVar()
                                entry_interest_loans=Entry(add_loan_for_selected_customer_window, textvariable=interest_var_loans,width=30,font=("georgia", 13)).place(x=200,y=250)


                                def submit_loan():
                                    try:
                                        amount = float(amount_var_loans.get())
                                        tenure = int(tenure_var_loans.get())
                                        interest = float(interest_var_loans.get())
                                        status = "Pending"
                                        from datetime import date
                                        application_date = date.today()

                                        cursor.execute("SELECT COUNT(*) FROM loans WHERE user_id = %s", (user_id,))
                                        existing_loan_count = cursor.fetchone()[0]
                                        if existing_loan_count > 0:
                                            messagebox.showwarning("Duplicate Loan", f"User ID {user_id} already has a loan.")
                                            return

                                        cursor.execute("""
                                            INSERT INTO loans (user_id, username, full_name, amount, tenure, interest_rate, status, application_date)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                        """, (user_id, username, full_name, amount, tenure, interest, status, application_date))
                                        conn.commit()

                                        messagebox.showinfo("Success", f"Loan added for {full_name}")
                                        add_loan_for_selected_customer_window.destroy()
                                        manage_loans_refresh()


                                    except Exception as e:
                                        messagebox.showerror("Database Error", str(e))

                                btn=Button(add_loan_for_selected_customer_window,text="Submit",height=1,width=15,font=("georgia",12),bg="#2980b9",fg="white",command=submit_loan).place(x=225,y=350)

                                add_loan_for_selected_customer_window.mainloop()


                            tree_loan_users.bind("<Double-1>", add_loan_for_selected_customer)

                            add_new_loan_window.mainloop()

                        def manage_loans_close():
                            confirm=messagebox.showinfo("Close","Are you sure you want to close the window?")
                            if confirm:
                                manage_loans_admin_window.destroy()

                        label_link=Label(manage_loans_admin_window,text="[Add New Loans]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                        label_link.place(x=75,y=525)
                        label_link.bind("<Button-1>", lambda e: add_new_loans())
                        
                        label_link=Label(manage_loans_admin_window,text="[Close]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                        label_link.place(x=350,y=525)
                        label_link.bind("<Button-1>", lambda e: manage_loans_close())

                        manage_loans_admin_window.mainloop()
                    def loan_reports():
                        loan_reports_window=Toplevel()
                        loan_reports_window.geometry("600x600")
                        loan_reports_window.config(bg="#f0f4f7")
                        loan_reports_window.title("Loan Reports Window")

                        label=Label(loan_reports_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(loan_reports_window,text="Admin Dashboard - Loan Reports", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=120,y=30)
                        label=Label(loan_reports_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)

                        label=Label(loan_reports_window,text="🔢 Summary Stats (Top Panel):", bg="#f0f4f7", fg="#171a4d",font=("georgia",14)).place(x=15,y=85)

                        columns = ("Metric", "Value")
                        tree_total_reports = ttk.Treeview(loan_reports_window, columns=columns, show="headings", height=5)
                        tree_total_reports.heading("Metric", text="Metric")
                        tree_total_reports.heading("Value", text="Value")
                        tree_total_reports.column("Metric", width=280, anchor="w")
                        tree_total_reports.column("Value", width=280, anchor="center")

                        tree_total_reports.place(x=15, y=115)

                        label = Label(loan_reports_window, text="📌 Filter by Status:", bg="#f0f4f7", fg="#171a4d", font=("georgia", 14))
                        label.place(x=15, y=260)
                        status_var = StringVar()
                        status_combobox = ttk.Combobox(loan_reports_window, textvariable=status_var, state="readonly", width=12, font=("georgia", 13))
                        status_combobox["values"] = ["All", "Approved", "Rejected", "Pending"]
                        status_combobox.current(0)
                        status_combobox.place(x=190, y=260)

                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM loans")
                        rows= cursor.fetchall()

                        columns = ("Loan ID", "Users ID","Username","Name","Amount", "Tenure","Interest Rate","Status","Application Date")
                        tree_loan_reports = ttk.Treeview(loan_reports_window, columns=columns, show="headings", height=6)

                        for col in columns:
                            tree_loan_reports.heading(col, text=col)
                            tree_loan_reports.column(col, width=100, anchor="center")

                        for row in rows:
                            tree_loan_reports.insert("", "end", values=row)

                        scrollbar = ttk.Scrollbar(loan_reports_window, orient="vertical", command=tree_loan_reports.yview)
                        tree_loan_reports.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=570, y=300, height=200)
                        scrollbar = ttk.Scrollbar(loan_reports_window, orient="horizontal", command=tree_loan_reports.xview)
                        tree_loan_reports.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=15, y=500, width=580)

                        tree_loan_reports.place(x=15, y=300, width=555, height=200)

                        def loan_reports_refresh():
                            for row in tree_loan_reports.get_children():
                                tree_loan_reports.delete(row)

                            selected_status = status_var.get()

                            if selected_status == 'All':
                                cursor.execute("SELECT * FROM loans")
                            else:
                                cursor.execute("SELECT * FROM loans WHERE status = %s", (selected_status,))
                            rows = cursor.fetchall()

                            for row in rows:
                                tree_loan_reports.insert("", "end", values=row)

                        label_link=Label(loan_reports_window,text="[Refresh]",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
                        label_link.place(x=350,y=260)
                        label_link.bind("<Button-1>", lambda e: loan_reports_refresh())

                        try:
                            cursor = conn.cursor()
                            cursor.execute("SELECT COUNT(*), IFNULL(SUM(amount), 0) FROM loans")
                            total_loans, total_amount = cursor.fetchone()
                            cursor.execute("SELECT COUNT(*) FROM loans WHERE status = 'Approved'")
                            approved_loans = cursor.fetchone()[0]
                            cursor.execute("SELECT COUNT(*) FROM loans WHERE status='Rejected'")
                            rejected_loans = cursor.fetchone()[0]
                            cursor.execute("SELECT COUNT(*) FROM loans WHERE status = 'Pending'")
                            pending_loans = cursor.fetchone()[0]

                            tree_total_reports.insert("", "end", values=("Total Loans", total_loans))
                            tree_total_reports.insert("", "end", values=("Total Amount Disbursed", f"₹{total_amount:.2f}"))
                            tree_total_reports.insert("", "end", values=("Approved Loans", approved_loans))
                            tree_total_reports.insert("", "end", values=("Rejected Loans", rejected_loans))
                            tree_total_reports.insert("", "end", values=("Pending Loans", pending_loans))

                        except Exception as e:
                            messagebox.showerror("Database Error", str(e))
                            return

                        loan_reports_window.mainloop()
                    def change_password_admin():
                        change_password_admin_window=Toplevel()
                        change_password_admin_window.geometry("600x600")
                        change_password_admin_window.config(bg="#f0f4f7")
                        change_password_admin_window.title(f"Change password - {db_name}")

                        label=Label(change_password_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(change_password_admin_window,text="Admin Dashboard - Change Password", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=90,y=35)
                        label=Label(change_password_admin_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        Label(change_password_admin_window, text="Change Password:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=150)
                        new_password_admin_entry = Entry(change_password_admin_window, width=30,font=("georgia",13))
                        new_password_admin_entry.insert(0, db_password)
                        new_password_admin_entry.place(x=250, y=150)

                        label=Label(change_password_admin_window,text="Repeat Password:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50,y=250)
                        repeat_new_password_admin_entry=Entry(change_password_admin_window,width=30,font=("georgia",13),bg="white",fg="black",textvariable=change_password_admin_var,show="*")
                        repeat_new_password_admin_entry.place(x=250,y=250)

                        def update_password_admin():
                            new_password_admin=new_password_admin_entry.get()
                            new_password_repeat_admin=repeat_new_password_admin_entry.get()

                            if (new_password_admin!=new_password_repeat_admin):
                                messagebox.showerror("Error", "Incorrect Password")
                                return
                            else:
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("UPDATE users SET password=%s WHERE username=%s",(new_password_admin,db_username))
                                    conn.commit()
                                    messagebox.showinfo("Success", "Password updated successfully.")
                                    change_password_admin_window.destroy()

                                except Exception as e:
                                    messagebox.showerror("Database Error", str(e))    

                        btn=Button(change_password_admin_window,text="Update",height=1,width=15,font=("georgia",12),bg="#2980b9",fg="white",command=update_password_admin).place(x=225,y=350)

                        change_password_admin_window.mainloop()
                    def logout_admin():
                        confirm=messagebox.showinfo("Logout","Are you sure you want to logout?")
                        if confirm:
                            admin_dashboard_window.destroy()

                    btn=Button(admin_dashboard_window,text=" ➕ Add New Customer │ │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=add_new_customer_admin).place(x=0,y=150)
                    btn=Button(admin_dashboard_window,text=" 📋 Manage Customer||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=manage_customer).place(x=0,y=200)
                    btn=Button(admin_dashboard_window,text=" 👤 Create Staff/Admin | Main Content Area |",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=create_staff_admin).place(x=0,y=250)
                    btn=Button(admin_dashboard_window,text=" 🧑‍💼 Manage Staff | (changes based on selection) |",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=manage_staff).place(x=0,y=300)
                    btn=Button(admin_dashboard_window,text=" 🧾 Manage Loans ||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=manage_loans).place(x=0,y=350)
                    btn=Button(admin_dashboard_window,text=" 📊 Loan Reports ||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=loan_reports).place(x=0,y=400)
                    btn=Button(admin_dashboard_window,text=" 🔐 Change Password ||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=change_password_admin).place(x=0,y=450)
                    btn=Button(admin_dashboard_window,text=" 🚪 Logout │ │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=logout_admin).place(x=0,y=500)
                    admin_dashboard_window.mainloop()
                if db_role=="staff":
                    staff_dashboard_window=Tk()
                    staff_dashboard_window.geometry("600x600")
                    staff_dashboard_window.config(bg="#f0f4f7")
                    staff_dashboard_window.title("Staff Dashboard")
                    # heading
                    label=Label(staff_dashboard_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                    label=Label(staff_dashboard_window,text="Staff Dashboard - Microfinance System", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=80,y=35)
                    label=Label(staff_dashboard_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                    # welcome
                    label=Label(staff_dashboard_window,text=f"Hello Staff {db_name}!!", bg="#f0f4f7", fg="#171a4d",font=("georgia",14)).place(x=0,y=100)

                    def add_new_customer_staff():
                        new_customer_registration_staff_window=Tk()
                        new_customer_registration_staff_window.geometry("600x600")
                        new_customer_registration_staff_window.config(bg="#f0f4f7")
                        new_customer_registration_staff_window.title("New Customer Registration - Staff")

                        label=Label(new_customer_registration_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(new_customer_registration_staff_window,text="Staff Dashboard - New Customer", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=105,y=30)
                        label=Label(new_customer_registration_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)

                        label=Label(new_customer_registration_staff_window,text="NAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=80)
                        entry_new_customer_staff_name=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_name_var)
                        entry_new_customer_staff_name.place(x=160,y=80)

                        label=Label(new_customer_registration_staff_window,text="AGE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=120)
                        entry_new_customer_staff_age=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_age_var)
                        entry_new_customer_staff_age.place(x=160,y=120)

                        label=Label(new_customer_registration_staff_window,text="GENDER:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=160)
                        gender_options = ["Male", "Female", "Other"]
                        gender_menu = OptionMenu(new_customer_registration_staff_window, add_new_customer_staff_gender_var, *gender_options)
                        gender_menu.config(font=("georgia", 12), width=18)
                        gender_menu.place(x=160, y=160)

                        label=Label(new_customer_registration_staff_window,text="EMAIL:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=200)
                        entry_new_customer_staff_email=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_email_var)
                        entry_new_customer_staff_email.place(x=160,y=200)

                        label=Label(new_customer_registration_staff_window,text="PHONE:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=240)
                        entry_new_customer_staff_phone=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_phone_var)
                        entry_new_customer_staff_phone.place(x=160,y=240)

                        label=Label(new_customer_registration_staff_window,text="ADDRESS:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=280)
                        entry_new_customer_staff_address=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_address_var)
                        entry_new_customer_staff_address.place(x=160,y=280)

                        label=Label(new_customer_registration_staff_window,text="USERNAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=320)
                        entry_new_customer_staff_username=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_username_var)
                        entry_new_customer_staff_username.place(x=160,y=320)

                        label=Label(new_customer_registration_staff_window,text="PASSWORD:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=30,y=360)
                        entry_new_customer_staff_password=Entry(new_customer_registration_staff_window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=add_new_customer_staff_password_var,show="*")
                        entry_new_customer_staff_password.place(x=160,y=360)

                        def new_customer_registration_staff_submit():
                            name=entry_new_customer_staff_name.get()
                            age=entry_new_customer_staff_age.get()
                            gender=add_new_customer_staff_gender_var.get()
                            email=entry_new_customer_staff_email.get()
                            phone=entry_new_customer_staff_phone.get()
                            address=entry_new_customer_staff_address.get()
                            username=entry_new_customer_staff_username.get()
                            password=entry_new_customer_staff_password.get()

                            if name and age and gender and email and phone and address and username and password:
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("SELECT * from users WHERE username=%s",(username,))
                                    if cursor.fetchone():
                                        messagebox.showerror("Error","Username already present❗❗")

                                    else:
                                        cursor.execute("INSERT into users (full_name,age,gender,email,phone,address,username,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(name,age,gender,email,phone,address,username,password))
                                        conn.commit()
                                        messagebox.showinfo("Success","Data saved successfully")
                                        new_customer_registration_staff_window.destroy()


                                except Exception as e:
                                    messagebox.showerror("Database Error",str(e))
                            else:
                                messagebox.showerror("Error","Incomplete!! ❌ Please complete all fields")

                        btn=Button(new_customer_registration_staff_window,text="Submit",height=1,width=11,font=("georgia",15),bg="#2980b9",fg="white",command=new_customer_registration_staff_submit).place(x=230,y=450)

                        new_customer_registration_staff_window.mainloop()
                    def view_all_customer():
                        view_all_customer_window=Tk()
                        view_all_customer_window.geometry("600x600")
                        view_all_customer_window.config(bg="#f0f4f7")
                        view_all_customer_window.title("View All Customer")
                        # heading
                        label=Label(view_all_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(view_all_customer_window,text="Staff Dashboard - View all Customer ", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=90,y=35)
                        label=Label(view_all_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                    
                        # tree view
                        cursor.execute("SELECT * FROM users WHERE role='customer'")
                        rows = cursor.fetchall()

                        columns = ("ID", "Name","Age","Gender","Username", "Password","Email","Phone","Address","Role","Status","Created at")
                        tree = ttk.Treeview(view_all_customer_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=100, anchor="center")

                        for row in rows:
                            tree.insert("", "end", values=row)

                        scrollbar = ttk.Scrollbar(view_all_customer_window, orient="vertical", command=tree.yview)
                        tree.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=580, y=140, height=350)
                        scrollbar = ttk.Scrollbar(view_all_customer_window, orient="horizontal", command=tree.xview)
                        tree.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=10, y=490, width=580)

                        tree.place(x=10, y=140, width=570, height=350)

                        def close_view_customer():
                            view_all_customer_window.destroy()

                        label_link=Label(view_all_customer_window,text="[Close]",bg="#f0f4f7",fg="red",font=("normal",15,"underline"),cursor="hand2")
                        label_link.place(x=280,y=525)
                        label_link.bind("<Button-1>", lambda e: close_view_customer())

                        view_all_customer_window.mainloop()

                    def process_loan_apps():
                        process_loan_apps_window=Tk()
                        process_loan_apps_window.geometry("600x600")
                        process_loan_apps_window.config(bg="#f0f4f7")
                        process_loan_apps_window.title("Staff Dashboard - Process Loan Apps")

                        label=Label(process_loan_apps_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(process_loan_apps_window,text="Staff Dashboard - Process Loan Apps", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=75,y=35)
                        label=Label(process_loan_apps_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        columns = ("Loan ID", "User ID", "Customer Name", "Amount", "Tenure", "Interest Rate", "Status", "Applied On")
                        tree = ttk.Treeview(process_loan_apps_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=110, anchor="center")

                        tree.place(x=15, y=120, width=570, height=300)

                        # Scrollbar
                        scrollbar = Scrollbar(process_loan_apps_window, orient=VERTICAL, command=tree.yview)
                        tree.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=585, y=120, height=300)
                        scrollbar = Scrollbar(process_loan_apps_window, orient=HORIZONTAL, command=tree.xview)
                        tree.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=15, y=420, width=570)

                        # Load loans function
                        def load_pending_loans():
                            tree.delete(*tree.get_children())
                            cursor.execute("""
                                SELECT l.loan_id, l.user_id, u.full_name, l.amount, l.tenure, l.interest_rate,
                                    l.status, DATE(l.created_at)
                                FROM loans l
                                JOIN users u ON u.id = l.user_id
                                WHERE l.status = 'Pending'
                            """)
                            rows = cursor.fetchall()
                            for row in rows:
                                tree.insert("", "end", values=row)

                        # Approve/Reject logic
                        def process_application(new_status):
                            selected = tree.focus()
                            if not selected:
                                messagebox.showwarning("Selection Required", "Please select a loan to process.")
                                return

                            loan_values = tree.item(selected, "values")
                            loan_id = loan_values[0]

                            try:
                                cursor.execute("UPDATE loans SET status = %s WHERE loan_id = %s", (new_status, loan_id))
                                conn.commit()
                                messagebox.showinfo("Success", f"Loan {loan_id} marked as {new_status}.")
                                load_pending_loans()
                            except Exception as e:
                                messagebox.showerror("Database Error", str(e))

                        # Buttons
                        Button(process_loan_apps_window, text="✅ Approve", font=("Georgia", 14),
                            bg="green", fg="white", command=lambda: process_application("Approved")).place(x=100, y=480)
                        Button(process_loan_apps_window, text="❌ Reject", font=("Georgia", 14),
                            bg="red", fg="white", command=lambda: process_application("Rejected")).place(x=300, y=480)
                        load_pending_loans()

                        process_loan_apps_window.mainloop()
                    def track_repayments():
                        track_repayments_staff_window=Tk()
                        track_repayments_staff_window.geometry("600x600")
                        track_repayments_staff_window.config(bg="#f0f4f7")
                        track_repayments_staff_window.title("Staff Dashboard - Track Repayments")

                        label=Label(track_repayments_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(track_repayments_staff_window,text="Staff Dashboard - Track Repayments", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=90,y=35)
                        label=Label(track_repayments_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        status_track_repayments_var = StringVar()
                        status_options = ["All", "Pending", "Ongoing", "Completed"]
                        status_track_repayments_var.set("All")
                        Label(track_repayments_staff_window, text="📌 Filter by Status:", bg="#f0f4f7",fg="#171a4d", font=("georgia", 14)).place(x=15, y=100)
                        status_filter = ttk.Combobox(track_repayments_staff_window, textvariable=status_track_repayments_var, values=status_options, state="readonly",width=12, font=("georgia", 13))
                        status_filter.place(x=200, y=100)

                        # Treeview Configuration
                        cursor.execute("SELECT l.loan_id, l.user_id, u.full_name, l.amount, IFNULL(SUM(r.amount_paid), 0) AS paid,l.amount - IFNULL(SUM(r.amount_paid), 0) AS remaining FROM loans l LEFT JOIN repayments r ON l.loan_id = r.loan_id JOIN users u ON u.id = l.user_id GROUP BY l.loan_id, l.user_id, u.full_name, l.amount;")
                        rows = cursor.fetchall()
                        columns = ("Loan ID", "Customer ID", "Customer Name", "Amount", "Amount Paid", "Remaining", "Status")
                        tree_track_repayments = ttk.Treeview(track_repayments_staff_window, columns=columns, show="headings", height=20)

                        for col in columns:
                            tree_track_repayments.heading(col, text=col)
                            tree_track_repayments.column(col, anchor="center", width=120)
                        for row in rows:
                            loan_id, user_id, full_name, amount, paid, remaining = row
                            if paid == 0:
                                status = "Pending"
                            elif paid < amount:
                                status = "Ongoing"
                            else:
                                status = "Completed"
                            tree_track_repayments.insert("", "end", values=(loan_id, user_id, full_name, f"₹{amount:.2f}", f"₹{paid:.2f}", f"₹{remaining:.2f}", status))

                        tree_track_repayments.place(x=15, y=150, width=580, height=350)

                        def track_repayments_refresh():
                            try:
                                tree_track_repayments.delete(*tree_track_repayments.get_children())
                                selected_status = status_filter.get().strip()

                                base_query = """
                                    SELECT l.loan_id, l.user_id, u.full_name, l.amount,
                                        IFNULL(SUM(r.amount_paid), 0) AS paid,
                                        l.amount - IFNULL(SUM(r.amount_paid), 0) AS remaining
                                    FROM loans l
                                    LEFT JOIN repayments r ON l.loan_id = r.loan_id
                                    JOIN users u ON u.id = l.user_id
                                    GROUP BY l.loan_id, l.user_id, u.full_name, l.amount
                                """

                                if selected_status == "Pending":
                                    query = base_query + " HAVING IFNULL(SUM(r.amount_paid), 0) = 0"
                                elif selected_status == "Ongoing":
                                    query = base_query + " HAVING IFNULL(SUM(r.amount_paid), 0) > 0 AND IFNULL(SUM(r.amount_paid), 0) < l.amount"
                                elif selected_status == "Completed":
                                    query = base_query + " HAVING IFNULL(SUM(r.amount_paid), 0) >= l.amount"
                                else:
                                    query = base_query

                                cursor.execute(query)
                                rows = cursor.fetchall()

                                for row in rows:
                                    loan_id, user_id, full_name, amount, paid, remaining = row
                                    if paid == 0:
                                        status = "Pending"
                                    elif paid < amount:
                                        status = "Ongoing"
                                    else:
                                        status = "Completed"
                                    tree_track_repayments.insert("", "end", values=(
                                        loan_id, user_id, full_name, f"₹{amount:.2f}", f"₹{paid:.2f}", f"₹{remaining:.2f}", status
                                    ))

                            except Exception as e:
                                messagebox.showerror("Database Error", str(e))

                        scrollbar_y = ttk.Scrollbar(track_repayments_staff_window, orient="vertical", command=tree_track_repayments.yview)
                        tree_track_repayments.configure(yscrollcommand=scrollbar_y.set)
                        scrollbar_y.place(x=875, y=150, height=350)

                        scrollbar_x = ttk.Scrollbar(track_repayments_staff_window, orient="horizontal", command=tree_track_repayments.xview)
                        tree_track_repayments.configure(xscrollcommand=scrollbar_x.set)
                        scrollbar_x.place(x=15, y=500, width=580)

                        label_link = Label(track_repayments_staff_window, text="[Refresh]", bg="#f0f4f7", fg="red",font=("normal", 15, "underline"), cursor="hand2")
                        label_link.place(x=400, y=100)
                        label_link.bind("<Button-1>", lambda e: track_repayments_refresh())

                    
                        track_repayments_staff_window.mainloop()
                    def change_password_staff():
                        change_password_staff_window=Tk()
                        change_password_staff_window.geometry("600x600")
                        change_password_staff_window.config(bg="#f0f4f7")
                        change_password_staff_window.title(f"Change password - {db_name}")

                        label=Label(change_password_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(change_password_staff_window,text="Staff Dashboard - Change Password", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=90,y=35)
                        label=Label(change_password_staff_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        Label(change_password_staff_window, text="Change Password:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=150)
                        new_password_staff_entry = Entry(change_password_staff_window, width=30,font=("georgia",13))
                        new_password_staff_entry.insert(0, db_password)
                        new_password_staff_entry.place(x=250, y=150)

                        label=Label(change_password_staff_window,text="Repeat Password:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50,y=250)
                        repeat_new_password_staff_entry=Entry(change_password_staff_window,width=30,font=("georgia",13),bg="white",fg="black",textvariable=change_password_staff_var,show="*")
                        repeat_new_password_staff_entry.place(x=250,y=250)

                        def update_password_staff():
                            new_password_staff=new_password_staff_entry.get()
                            new_password_repeat_staff=repeat_new_password_staff_entry.get()

                            if (new_password_staff!=new_password_repeat_staff):
                                messagebox.showerror("Error", "Incorrect Password")
                                return
                            else:
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("UPDATE users SET password=%s WHERE username=%s",(new_password_staff,db_username))
                                    conn.commit()
                                    messagebox.showinfo("Success", "Password updated successfully.")
                                    change_password_staff_window.destroy()

                                except Exception as e:
                                    messagebox.showerror("Database Error", str(e))    

                        btn=Button(change_password_staff_window,text="Update",height=1,width=15,font=("georgia",12),bg="#2980b9",fg="white",command=update_password_staff).place(x=225,y=350)

                        change_password_staff_window.mainloop()

                    def logout_staff():
                        confirm=messagebox.showinfo("Logout","Are you sure you want to logout?")
                        if confirm:
                            staff_dashboard_window.destroy()
                    # buttons
                    btn=Button(staff_dashboard_window,text=" ➕ Add New Customer │ │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=add_new_customer_staff).place(x=0,y=150)
                    btn=Button(staff_dashboard_window,text=" 📋 View All Customer │ Main Content Area │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=view_all_customer).place(x=0,y=200)
                    btn=Button(staff_dashboard_window,text=" 🧾 Process Loan Apps │ (content loads dynamically) │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=process_loan_apps).place(x=0,y=250)
                    btn=Button(staff_dashboard_window,text=" 💳 Track Repayments │ │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=track_repayments).place(x=0,y=300)
                    btn=Button(staff_dashboard_window,text=" 🔐 Change Password ||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=change_password_staff).place(x=0,y=350)
                    btn=Button(staff_dashboard_window,text=" 🚪 Logout │ │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=logout_staff).place(x=0,y=400)
                    staff_dashboard_window.mainloop()
                if db_role=="customer":
                    customer_dashboard_window=Tk()
                    customer_dashboard_window.geometry("600x600")
                    customer_dashboard_window.config(bg="#f0f4f7")
                    customer_dashboard_window.title("Customer Dashboard")
                    label=Label(customer_dashboard_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                    label=Label(customer_dashboard_window,text="Customer Dashboard - Microfinance System", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=60,y=35)
                    label=Label(customer_dashboard_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                    # welcome
                    label=Label(customer_dashboard_window,text=f"Welcome {db_name}!!", bg="#f0f4f7", fg="#171a4d",font=("georgia",14)).place(x=0,y=100)

                    def view_my_loan():
                        customer_view_my_loan_window=Tk()
                        customer_view_my_loan_window.geometry("600x600")
                        customer_view_my_loan_window.config(bg="#f0f4f7")
                        customer_view_my_loan_window.title(f"{db_name} - Loan Window")

                        label=Label(customer_view_my_loan_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(customer_view_my_loan_window,text="Customer Dashboard - View My Loan", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=90,y=35)
                        label=Label(customer_view_my_loan_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)
                        try:
                            cursor.execute("""
                                SELECT l.loan_id, l.user_id, u.username, u.full_name, l.amount, l.tenure, l.interest_rate,
                                    CASE
                                        WHEN IFNULL(SUM(r.amount_paid), 0) = 0 THEN 'Pending'
                                        WHEN IFNULL(SUM(r.amount_paid), 0) >= l.amount THEN 'Completed'
                                        ELSE 'Ongoing'
                                    END AS status,
                                    DATE(l.created_at) AS application_date,
                                    IFNULL(SUM(r.amount_paid), 0) AS paid,
                                    (l.amount - IFNULL(SUM(r.amount_paid), 0)) AS balance
                                FROM loans l
                                JOIN users u ON u.id = l.user_id
                                LEFT JOIN repayments r ON r.loan_id = l.loan_id
                                WHERE l.user_id = %s
                                GROUP BY l.loan_id, l.user_id, u.username, u.full_name, l.amount, l.tenure, l.interest_rate, l.created_at
                            """, (db_id,))


                            rows= cursor.fetchall()

                        except Exception as e:
                            messagebox.showerror("Database Error", str(e))

                        columns = ("Loan ID", "User ID", "Username", "Name", "Amount", "Tenure", "Interest Rate","Status", "Application Date", "Amount Paid", "Remaining Balance")
                        tree_customer = ttk.Treeview(customer_view_my_loan_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree_customer.heading(col, text=col)
                            tree_customer.column(col, width=100, anchor="center")

                        for row in rows:
                            tree_customer.insert("", "end", values=row)

                        scrollbar = ttk.Scrollbar(customer_view_my_loan_window, orient="horizontal", command=tree_customer.xview)
                        tree_customer.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=10, y=200, width=580)

                        tree_customer.place(x=10, y=100, width=570, height=100)

                        customer_view_my_loan_window.mainloop()
                    def make_emi_payment():
                        make_emi_payment_window=Tk()
                        make_emi_payment_window.geometry("600x600")
                        make_emi_payment_window.config(bg="#f0f4f7")
                        make_emi_payment_window.title(f"{db_name} - Make Payment")

                        label=Label(make_emi_payment_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(make_emi_payment_window,text=f"Customer Dashboard - Make Payment", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=80,y=35)
                        label=Label(make_emi_payment_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        label=Label(make_emi_payment_window,text=f"Welcome, {db_name}👋 │ 💳 Make EMI Payment │", bg="#f0f4f7", fg="#171a4d",font=("georgia",14)).place(x=0,y=100)
                        cursor = conn.cursor()
                        cursor.execute("""
                            SELECT l.loan_id, l.amount, IFNULL(SUM(r.amount_paid), 0) AS paid
                            FROM loans l
                            LEFT JOIN repayments r ON l.loan_id = r.loan_id
                            WHERE l.user_id = %s
                            GROUP BY l.loan_id, l.amount
                        """, (db_id,))
                        loan_data = cursor.fetchone()

                        if loan_data:
                            loan_id, total_amount, amount_paid = loan_data
                            balance = total_amount - amount_paid

                            if amount_paid == 0:
                                status = "Pending"
                            elif amount_paid < total_amount:
                                status = "Ongoing"
                            else:
                                status = "Completed"

                        else:
                            messagebox.showinfo("No Loan", "No active loan found for this customer.")
                            make_emi_payment_window.destroy()
                            return
                        Label(make_emi_payment_window, text=f"Loan ID: {loan_id}", bg="#f0f4f7", font=("georgia", 14)).place(x=50, y=150)
                        Label(make_emi_payment_window, text=f"Total Amount: ₹{total_amount:.2f}", bg="#f0f4f7", font=("georgia", 14)).place(x=50, y=190)
                        Label(make_emi_payment_window, text=f"Amount Paid: ₹{amount_paid:.2f}", bg="#f0f4f7", font=("georgia", 14)).place(x=50, y=230)
                        Label(make_emi_payment_window, text=f"Remaining Balance: ₹{balance:.2f}", bg="#f0f4f7", font=("georgia", 14)).place(x=50, y=270)
                        Label(make_emi_payment_window, text="Enter EMI Amount (₹):", bg="#f0f4f7", font=("georgia", 14)).place(x=50, y=320)
                        emi_entry = Entry(make_emi_payment_window, font=("georgia", 14))
                        emi_entry.place(x=270, y=320)
                        Label(make_emi_payment_window, text=f"Payment Status: {status}", bg="#f0f4f7", font=("georgia", 14)).place(x=50, y=450)

                        def record_payment():
                            try:
                                amount = float(emi_entry.get())
                                if amount <= 0:
                                    raise ValueError("Enter a valid amount.")
                                if amount > balance:
                                    raise ValueError("EMI exceeds balance amount.")
                                confirm=messagebox.showinfo("Success", f"₹{amount:.2f} payment recorded successfully.")
                                if confirm:
                                    cursor.execute("INSERT INTO repayments (loan_id, amount_paid, payment_date) VALUES (%s, %s, NOW())", (loan_id, amount))
                                    cursor.execute(
                                                "UPDATE loans SET total_paid = total_paid + %s WHERE loan_id = %s",
                                                (amount, loan_id)
                                            )                                    
                                    conn.commit()
                                    make_emi_payment_window.destroy()       
                            except ValueError as ve:
                                messagebox.showerror("Invalid Input", str(ve))
                            except Exception as e:
                                messagebox.showerror("Database Error", str(e))

                        Button(make_emi_payment_window, text="Record Payment", font=("georgia", 14), bg="#2980b9", fg="white", command=record_payment).place(x=50, y=370)
                        Button(make_emi_payment_window, text="Cancel", font=("georgia", 14), bg="gray", fg="white", command=make_emi_payment_window.destroy).place(x=300, y=370)

                        make_emi_payment_window.mainloop()
                    def payment_history():
                        payment_history_window=Tk()
                        payment_history_window.geometry("600x600")
                        payment_history_window.config(bg="#f0f4f7")
                        payment_history_window.title(f"{db_name} - Payment History")

                        label=Label(payment_history_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(payment_history_window,text=f"{db_name} Dashboard - Payment History", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=80,y=35)
                        label=Label(payment_history_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        label=Label(payment_history_window,text=f"Welcome, {db_name}👋", bg="#f0f4f7", fg="#171a4d",font=("georgia",14)).place(x=0,y=100)
                        try:
                            cursor.execute("""
                                SELECT 
                                    r.repayment_id,
                                    r.loan_id,
                                    r.amount_paid,
                                    DATE(r.paid_on),
                                    l.amount AS loan_amount,
                                    (
                                        l.amount - (
                                            SELECT SUM(r2.amount_paid) 
                                            FROM repayments r2 
                                            WHERE r2.loan_id = r.loan_id AND r2.paid_on <= r.paid_on
                                        )
                                    ) AS remaining_balance
                                FROM repayments r
                                JOIN loans l ON r.loan_id = l.loan_id
                                WHERE l.user_id = %s
                                ORDER BY r.paid_on DESC
                            """, (db_id,))
                            repayments = cursor.fetchall()
                        except Exception as e:
                            messagebox.showerror("Database Error", str(e)) 

                        columns = ("Repayment ID", "Loan ID", "Amount Paid", "Payment Date", "Remaining Balance")
                        tree = ttk.Treeview(payment_history_window, columns=columns, show="headings", height=8)

                        for col in columns:
                            tree.heading(col, text=col)
                            tree.column(col, width=130, anchor="center")

                        for repayment in repayments:
                            repayment_id, loan_id, amount_paid, paid_date, loan_amount, remaining = repayment
                            tree.insert("", "end", values=(
                                repayment_id,
                                loan_id,
                                f"₹{amount_paid:.2f}",
                                paid_date,
                                f"₹{remaining:.2f}"
                            ))
                        tree.place(x=15, y=150, width=570, height=300)
                        scrollbar = ttk.Scrollbar(payment_history_window, orient="vertical", command=tree.yview)
                        tree.configure(yscrollcommand=scrollbar.set)
                        scrollbar.place(x=585, y=150, height=300)
                        scrollbar = ttk.Scrollbar(payment_history_window, orient="horizontal", command=tree.xview)
                        tree.configure(xscrollcommand=scrollbar.set)
                        scrollbar.place(x=15, y=450, width=585)
                            
                        payment_history_window.mainloop()
                    def change_password_customer():
                        change_password_customer_window=Tk()
                        change_password_customer_window.geometry("600x600")
                        change_password_customer_window.config(bg="#f0f4f7")
                        change_password_customer_window.title(f"Change password - {db_name}")

                        label=Label(change_password_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
                        label=Label(change_password_customer_window,text="Customer Dashboard - Change Password", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=70,y=35)
                        label=Label(change_password_customer_window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=70)

                        Label(change_password_customer_window, text="Change Password:", bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50, y=150)
                        new_password_customer_entry = Entry(change_password_customer_window, width=30,font=("georgia",13))
                        new_password_customer_entry.insert(0, db_password)
                        new_password_customer_entry.place(x=250, y=150)

                        label=Label(change_password_customer_window,text="Repeat Password:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50,y=250)
                        repeat_new_password_customer_entry=Entry(change_password_customer_window,width=30,font=("georgia",13),bg="white",fg="black",textvariable=change_password_customer_var,show="*")
                        repeat_new_password_customer_entry.place(x=250,y=250)

                        def update_password_customer():
                            new_password_customer=new_password_customer_entry.get()
                            new_password_repeat_customer=repeat_new_password_customer_entry.get()

                            if (new_password_customer!=new_password_repeat_customer):
                                messagebox.showerror("Error", "Incorrect Password")
                                return
                            else:
                                try:
                                    cursor=conn.cursor()
                                    cursor.execute("UPDATE users SET password=%s WHERE username=%s",(new_password_customer,db_username))
                                    conn.commit()
                                    messagebox.showinfo("Success", "Password updated successfully.")
                                    change_password_customer_window.destroy()

                                except Exception as e:
                                    messagebox.showerror("Database Error", str(e))    

                        btn=Button(change_password_customer_window,text="Update",height=1,width=15,font=("georgia",12),bg="#2980b9",fg="white",command=update_password_customer).place(x=225,y=350)

                        change_password_customer_window.mainloop()
                    def logout_customer():
                        confirm=messagebox.showinfo("Logout","Are you sure you want to logout?")
                        if confirm:
                            customer_dashboard_window.destroy()
                    # buttons
                    btn=Button(customer_dashboard_window,text=" 🧾  View My Loan ||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=view_my_loan).place(x=0,y=150)
                    btn=Button(customer_dashboard_window,text=" 💳 Make EMI Payment │ Main Content Area │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=make_emi_payment).place(x=0,y=200)
                    btn=Button(customer_dashboard_window,text=" 📜 Payment History │ (updates based on selection) │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=payment_history).place(x=0,y=250)
                    btn=Button(customer_dashboard_window,text=" 🔐 Change Password ||",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=change_password_customer).place(x=0,y=300)
                    btn=Button(customer_dashboard_window,text=" 🚪 Logout │ │",height=1,width=40,font=("georgia",12),bg="#2980b9",fg="white",command=logout_customer).place(x=0,y=350)
                    customer_dashboard_window.mainloop()
            else:
                messagebox.showerror("Error","Incorrect password")
        else:
            messagebox.showerror("Error","Incorrect username")     
    except Exception as e:
        messagebox.showerror("Database Error",str(e))   

label=Label(window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=0)
label=Label(window,text="MICROFINACE LOAN MANAGEMENT SYSTEM", bg="#f0f4f7", fg="#171a4d",font=("georgia",18)).place(x=35,y=30)
label=Label(window,text="------------------------------------------------------------------------------------------------------", bg="#f0f4f7", fg="black",font=("georgia",14)).place(x=0,y=60)
label=Label(window,text="- Lingesh Kumar G", bg="#f0f4f7", fg="BLACK",font=("georgia",14)).place(x=400,y=100)
label=Label(window,text="USERNAME:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50,y=150)
entry_name=Entry(window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=user_name_var)
entry_name.place(x=180,y=150)
label=Label(window,text="PASSWORD:",bg="#f0f4f7",fg="#171a4d",font=("georgia",15)).place(x=50,y=200)
entry_name=Entry(window,width=30,font=("georgia",15),bg="white",fg="black",textvariable=password_var,show="*")
entry_name.place(x=180,y=200)
btn=Button(window,text="Login",height=1,width=11,font=("georgia",15),bg="#2980b9",fg="white",command=login).place(x=230,y=300)
label_link=Label(window,text="Register as customer",bg="#f0f4f7",fg="black",font=("normal",15,"underline"),cursor="hand2")
label_link.place(x=205,y=400)
label_link.bind("<Button-1>", lambda e: customer_register())

window.mainloop()