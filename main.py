import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import *
import database
import os
from PIL import Image, ImageTk





class AddStudent(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Attributes
        self.title("")
        self.geometry(f"800x500+{(window.winfo_screenwidth() - 800) // 2}+{(window.winfo_screenheight() - 500) // 2}")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # widgets
        self.student_reg_label = ctk.CTkLabel(self, text="STUDENT REGISTRATION FORM", font=("Verdana", 25, "bold"))
        self.student_reg_label.place(relx=0.21, rely=0.1)

        self.id_box = ctk.CTkEntry(self, placeholder_text="  ID", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=150, height=50)
        self.id_box.place(relx=0.08, rely=0.3)

        self.student_name_box = ctk.CTkEntry(self, placeholder_text="  Student Name", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=250, height=50)
        self.student_name_box.place(relx=0.277, rely=0.3)

        self.father_name_box = ctk.CTkEntry(self, placeholder_text="  Father Name", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=250, height=50)
        self.father_name_box.place(relx=0.6, rely=0.3)

        self.course_name_box = ctk.CTkEntry(self, placeholder_text="  Selected Course Name", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=250, height=50)
        self.course_name_box.place(relx=0.08, rely=0.45)

        self.course_fee_box = ctk.CTkEntry(self, placeholder_text="Course Fee", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=100, height=50)
        self.course_fee_box.place(relx=0.405, rely=0.45)

        self.course_duration_box = ctk.CTkEntry(self, placeholder_text="  Course Duration", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=140, height=50)
        self.course_duration_box.place(relx=0.543, rely=0.45)

        self.admission_date_box = ctk.CTkEntry(self, placeholder_text="  Admission Date", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=150, height=50)
        self.admission_date_box.place(relx=0.725, rely=0.45)

        self.contact_box = ctk.CTkEntry(self, placeholder_text="  Contact Number", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=250, height=50)
        self.contact_box.place(relx=0.08, rely=0.60)

        self.address_box = ctk.CTkEntry(self, placeholder_text="  Address", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=407, height=50)
        self.address_box.place(relx=0.405, rely=0.60)

        self.submit_button = ctk.CTkButton(self, text="SUBMIT", command=self.get_inputs_data, font=("Arial", 20, "bold"), fg_color="green", hover_color="#385734", corner_radius=20, width=300, height=50)
        self.submit_button.place(relx=0.31, rely=0.85)


    def get_inputs_data(self):
        id = self.id_box.get()
        student_name = self.student_name_box.get()
        father_name = self.father_name_box.get()
        course_name = self.course_name_box.get()
        course_fee = self.course_fee_box.get()
        course_duration = self.course_duration_box.get()
        admission_date = self.admission_date_box.get()
        contact = self.contact_box.get()
        address = self.address_box.get()

        if id=="" or student_name=="" or father_name=="" or course_name=="" or course_fee=="" or course_duration=="" or admission_date=="" or contact=="" or address=="" or not course_fee.isdigit():
            show_message = ctk.CTkLabel(self, text="All fields are required!\nContact and Course Fee should be numbers", text_color="red", font=("", 20))
            show_message.place(relx=0.27, rely=0.75)
            self.after(2000, show_message.destroy)

        elif database.id_exists(id):
            show_message = ctk.CTkLabel(self, text="ID Already Registered!", text_color="#FFF", font=("", 20))
            show_message.place(relx=0.35, rely=0.75)
            self.after(2000, show_message.destroy)
        else:
            database.add_students(id, student_name, father_name, course_name, course_fee, course_duration, admission_date, contact, address)
            show_message = ctk.CTkLabel(self, text=f"{student_name} successfully Added", text_color="green", font=("", 25))
            show_message.place(relx=0.27, rely=0.75)
            self.after(2000, show_message.destroy)

            self.submit_button.configure(state="disabled")

            self.after(4000, self.destroy)


class SearchStudent(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Attributes
        self.title("")
        self.geometry(f"600x500+{(window.winfo_screenwidth() - 600) // 2}+{(window.winfo_screenheight() - 500) // 2}")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # widgets
        self.search_by_id_label = ctk.CTkLabel(self, text="Search by ID: ", font=("Arial", 20, "bold"))
        self.search_by_id_label.place(relx=0.150, rely=0.1)

        self.id_entry_box = ctk.CTkEntry(self, text_color="#000", fg_color="#fff", width=150, height=40, font=("Arial", 20, "bold"))
        self.id_entry_box.place(relx=0.380, rely=0.090)

        self.search_button = ctk.CTkButton(self, text="Search", command=self.show_data_on_labels, hover_color="#385734", fg_color="green", corner_radius=15, font=("Arial", 20, "bold"))
        self.search_button.place(relx=0.650, rely=0.090, relwidth=0.200, relheight=0.090)

        self.name_label = ctk.CTkLabel(self, text="Name:", text_color="#fff", font=("Arial", 20))
        self.name_label.place(relx=0.150, rely=0.300)
        self.show_name = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_name.place(relx=0.150, rely=0.350)

        self.father_name_label = ctk.CTkLabel(self, text="Father Name:", text_color="#fff", font=("Arial", 20))
        self.father_name_label.place(relx=0.600, rely=0.300)
        self.show_father_name = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_father_name.place(relx=0.600, rely=0.350)

        self.course_name_label = ctk.CTkLabel(self, text="Learning Course Name:", text_color="#fff", font=("Arial", 20))
        self.course_name_label.place(relx=0.150, rely=0.450)
        self.show_course_name = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_course_name.place(relx=0.150, rely=0.500)

        self.course_fee_label = ctk.CTkLabel(self, text="Course Fee:", text_color="#fff", font=("Arial", 20))
        self.course_fee_label.place(relx=0.600, rely=0.450)
        self.show_course_fee = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_course_fee.place(relx=0.600, rely=0.500)

        self.course_duration_label = ctk.CTkLabel(self, text="Course Duration:", text_color="#fff", font=("Arial", 20))
        self.course_duration_label.place(relx=0.150, rely=0.600)
        self.show_course_duration = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_course_duration.place(relx=0.150, rely=0.650)

        self.admission_date_label = ctk.CTkLabel(self, text="Date of Admission:", text_color="#fff", font=("Arial", 20))
        self.admission_date_label.place(relx=0.600, rely=0.600)
        self.show_admission_date = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_admission_date.place(relx=0.600, rely=0.650)

        self.contact_label = ctk.CTkLabel(self, text="Contact:", text_color="#fff", font=("Arial", 20))
        self.contact_label.place(relx=0.150, rely=0.750)
        self.show_contact = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_contact.place(relx=0.150, rely=0.800)

        self.address_label = ctk.CTkLabel(self, text="Address:", text_color="#fff", font=("Arial", 20))
        self.address_label.place(relx=0.600, rely=0.750)
        self.show_address = ctk.CTkLabel(self, text="", text_color="green", font=("Arial", 20, "bold"))
        self.show_address.place(relx=0.600, rely=0.800)


    def show_data_on_labels(self):
        if database.id_exists(self.id_entry_box.get()):
            student_data = database.search_student(self.id_entry_box.get())
            self.show_name.configure(text=student_data[1])
            self.show_father_name.configure(text=student_data[2])
            self.show_course_name.configure(text=student_data[3])
            self.show_course_fee.configure(text=student_data[4])
            self.show_course_duration.configure(text=student_data[5])
            self.show_admission_date.configure(text=student_data[6])
            self.show_contact.configure(text=student_data[7])
            self.show_address.configure(text=student_data[8])
        else:
            show_info_message = ctk.CTkLabel(self, text="Not Found!\nPlease! Provide the Correct ID", text_color="red", font=("Arial", 25, "bold"))
            show_info_message.place(relx=0.200, rely=0.850)
            self.after(2000, show_info_message.destroy)


class UpdateStudent(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        # Attributes
        self.title("MTI Student Update Window")
        self.geometry(f"1000x500+{(window.winfo_screenwidth() - 1000) // 2}+{(window.winfo_screenheight() - 500) // 2}")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # widgets
        self.id_box = ctk.CTkEntry(self, placeholder_text="  ID", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=100, height=40)
        self.id_box.place(relx=0.01, rely=0.75)

        self.student_name_box = ctk.CTkEntry(self, placeholder_text="  Student Name", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=150, height=40)
        self.student_name_box.place(relx=0.120, rely=0.75)

        self.father_name_box = ctk.CTkEntry(self, placeholder_text="  Father Name", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=150, height=40)
        self.father_name_box.place(relx=0.280, rely=0.75)

        self.course_name_box = ctk.CTkEntry(self, placeholder_text="  Selected Course Name", fg_color="white",text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=200, height=40)
        self.course_name_box.place(relx=0.440, rely=0.75)

        self.course_fee_box = ctk.CTkEntry(self, placeholder_text="Course Fee", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=130, height=40)
        self.course_fee_box.place(relx=0.650, rely=0.75)

        self.course_duration_box = ctk.CTkEntry(self, placeholder_text="  Course Duration", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=200, height=40)
        self.course_duration_box.place(relx=0.790, rely=0.75)

        self.admission_date_box = ctk.CTkEntry(self, placeholder_text="  Admission Date", fg_color="white",text_color="black", font=("Arial", 15, "bold"), corner_radius=5,width=150, height=40)
        self.admission_date_box.place(relx=0.01, rely=0.85)

        self.contact_box = ctk.CTkEntry(self, placeholder_text="  Contact Number", fg_color="white", text_color="black", font=("Arial", 15, "bold"), corner_radius=5, width=150, height=40)
        self.contact_box.place(relx=0.175, rely=0.85)

        self.address_box = ctk.CTkEntry(self, placeholder_text="  Address", fg_color="white", text_color="black",font=("Arial", 15, "bold"), corner_radius=5, width=300, height=40)
        self.address_box.place(relx=0.690, rely=0.85)

        self.submit_button = ctk.CTkButton(self, text="UPDATE", command=self.update_student, font=("Arial", 20, "bold"), fg_color="orange", hover_color="#c4741d", corner_radius=20, width=250, height=40)
        self.submit_button.place(relx=0.390, rely=0.85)


        # func calls
        self.show_tree_view()

    def clear_fields(self):
        self.id_box.delete(0, END)
        self.student_name_box.delete(0, END)
        self.father_name_box.delete(0, END)
        self.course_name_box.delete(0, END)
        self.course_fee_box.delete(0, END)
        self.course_duration_box.delete(0, END)
        self.admission_date_box.delete(0, END)
        self.contact_box.delete(0, END)
        self.address_box.delete(0, END)

    def show_tree_view(self):
            style = ttk.Style(self)
            style.theme_use("clam")
            # style.layout("mystyle.Treeview", [("mystyle.Treeview.treearea", {"sticky": "nswe"})])
            style.configure("Treeview", font=("Arial", 10, "bold"), foreground="#fff", background="#555751", fieldbackground="#2b2b2a", borderwidth=0, relief="flat")
            style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#2b2b2a", foreground="#FFD700", anchor="center")
            style.map("Treeview", background=[("selected", "orange")])
            tree = ttk.Treeview(self, height=15)
            tree["columns"] = ("ID", "Student Name", "Father Name", "Course Name", "Course Fee", "Course Duration", "Admission Date", "Contact", "Address")

            tree.column("#0", width=0, stretch=tk.NO) # Hide the default first column
            tree.column("ID", width=80)
            tree.column("Student Name", width=120)
            tree.column("Father Name", width=120)
            tree.column("Course Name", width=120)
            tree.column("Course Fee", width=80)
            tree.column("Course Duration", width=120)
            tree.column("Admission Date", width=100)
            tree.column("Contact", width=100)
            tree.column("Address", width=200)

            tree.heading("ID", text="ID")
            tree.heading("Student Name", text="Student Name")
            tree.heading("Father Name", text="Father Name")
            tree.heading("Course Name", text="Course Name")
            tree.heading("Course Fee", text="Course Fee")
            tree.heading("Course Duration", text="Course Duration")
            tree.heading("Admission Date", text="Admission Date")
            tree.heading("Contact", text="Contact")
            tree.heading("Address",text="Address")

            # Create a vertical scrollbar
            scrollbar = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)

            tree.place(relx=0, rely=0, relwidth=1, relheight=0.7)
            scrollbar.place(relx=0.988, rely=0, relheight=0.7)  # Position scrollbar on the right

            # inserting data to tree
            students_rows = database.fetch_students()
            for row in students_rows:
                tree.insert("", "end", values=row)
            def focused_row(event):
                self.clear_fields()
                selceted_row = tree.focus()
                data = tree.item(selceted_row)
                row = data["values"]
                self.id_box.insert(0, row[0])
                self.student_name_box.insert(0, row[1])
                self.father_name_box.insert(0, row[2])
                self.course_name_box.insert(0, row[3])
                self.course_fee_box.insert(0, row[4])
                self.course_duration_box.insert(0, row[5])
                self.admission_date_box.insert(0, row[6])
                self.contact_box.insert(0, row[7])
                self.address_box.insert(0, row[8])

            tree.bind("<ButtonRelease-1>", focused_row)

    def update_student(self):
        id = self.id_box.get()
        student_name = self.student_name_box.get()
        father_name = self.father_name_box.get()
        course_name = self.course_name_box.get()
        course_fee = int(self.course_fee_box.get())
        course_duration = self.course_duration_box.get()
        admission_date = self.admission_date_box.get()
        contact = int(self.contact_box.get())
        address = self.address_box.get()

        if id=="":
            show_message = ctk.CTkLabel(self, text="Please, Click on the Students row", text_color="orange", font=("Arial", 15, "bold"))
            show_message.place(relx=0.400, rely=0.690)
            self.after(4000, show_message.destroy)
        else:
            try:

                database.update_students(student_name, father_name, course_name, course_fee, course_duration, admission_date, contact, address, id)
                show_message = ctk.CTkLabel(self, text=f"{student_name} Updated Successfully", text_color="green",font=("Arial", 15, "bold"))
                show_message.place(relx=0.400, rely=0.690)
                self.after(4000, show_message.destroy)
                self.show_tree_view()

            except:
                show_message = ctk.CTkLabel(self, text="Error! Occurred", text_color="red",font=("Arial", 15, "bold"))
                show_message.place(relx=0.440, rely=0.690)
                self.after(4000, show_message.destroy)


def back_up_func():
    txt_path = os.path.join(os.path.join(os.environ['USERPROFILE'])) + "\\Desktop\\Students_Backup.txt"

    students_data = database.fetch_students()
    result = "\n".join(", ".join(map(str, tup)) for tup in students_data)
    with open(txt_path, "wt") as file:
        file.write(result)


class DeleteStudent(ctk.CTkToplevel):
    def __init__(self, student_id=""):
        super().__init__()

        # Attributes
        self.student_id = student_id

        self.title("MTI Student Delete Window")
        self.geometry(f"1000x500+{(window.winfo_screenwidth() - 1000) // 2}+{(window.winfo_screenheight() - 500) // 2}")
        self.resizable(False, False)
        self.attributes("-topmost", True)


        # widgets
        self.delete_button = ctk.CTkButton(self, text="DELETE", command=self.delete_student, font=("Arial", 20, "bold"), fg_color="red", hover_color="#8c3735", corner_radius=20, width=250, height=50)
        self.delete_button.place(relx=0.380, rely=0.85)


        # func calls
        self.show_tree_view()

    def show_tree_view(self):
            style = ttk.Style(self)
            style.theme_use("clam")
            style.configure("Treeview", font=("Arial", 10, "bold"), foreground="#fff", background="#555751", fieldbackground="#2b2b2a", borderwidth=0, relief="flat")
            style.configure("Treeview.Heading", font=("Arial", 12, "bold"), background="#2b2b2a", foreground="#fff", anchor="center")
            style.map("Treeview", background=[("selected", "red")])
            tree = ttk.Treeview(self, height=15)
            tree["columns"] = ("ID", "Student Name", "Father Name", "Course Name", "Course Fee", "Course Duration", "Admission Date", "Contact", "Address")

            tree.column("#0", width=0, stretch=tk.NO) # Hide the default first column
            tree.column("ID", width=80)
            tree.column("Student Name", width=120)
            tree.column("Father Name", width=120)
            tree.column("Course Name", width=120)
            tree.column("Course Fee", width=80)
            tree.column("Course Duration", width=120)
            tree.column("Admission Date", width=100)
            tree.column("Contact", width=100)
            tree.column("Address", width=200)

            tree.heading("ID", text="ID")
            tree.heading("Student Name", text="Student Name")
            tree.heading("Father Name", text="Father Name")
            tree.heading("Course Name", text="Course Name")
            tree.heading("Course Fee", text="Course Fee")
            tree.heading("Course Duration", text="Course Duration")
            tree.heading("Admission Date", text="Admission Date")
            tree.heading("Contact", text="Contact")
            tree.heading("Address",text="Address")

            # Create a vertical scrollbar
            scrollbar = ttk.Scrollbar(self, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)

            tree.place(relx=0, rely=0, relwidth=1, relheight=0.8)
            scrollbar.place(relx=0.988, rely=0, relheight=0.8)  # Position scrollbar on the right

            # inserting data to tree
            students_rows = database.fetch_students()
            for row in students_rows:
                tree.insert("", "end", values=row)
            def focused_row(event):
                selceted_row = tree.focus()
                data = tree.item(selceted_row)
                row = data["values"]
                try:
                    self.student_id = row[0]
                except:
                    pass

            tree.bind("<ButtonRelease-1>", focused_row)

    def delete_student(self):
        if self.student_id=="" or not database.id_exists(self.student_id):
            show_message = ctk.CTkLabel(self, text="Please, Click on the Students row", text_color="#fff", font=("Arial", 15, "bold"))
            show_message.place(relx=0.390, rely=0.690)
            self.after(4000, show_message.destroy)

        else:
            try:
                database.delete_students(self.student_id)
                self.show_tree_view()
                show_message = ctk.CTkLabel(self, text="Info, Removed from Record", text_color="red", font=("Arial", 15, "bold"))
                show_message.place(relx=0.390, rely=0.690)
                self.after(4000, show_message.destroy)
            except:
                show_message = ctk.CTkLabel(self, text="Error! Something Wrong Happened", text_color="red", font=("Arial", 15, "bold"))
                show_message.place(relx=0.390, rely=0.690)
                self.after(4000, show_message.destroy)


class About(ctk.CTkToplevel):
    def __init__(self, student_id=""):
        super().__init__()

        # Attributes
        self.title("About")
        self.geometry(f"400x600+{(window.winfo_screenwidth() - 1) // 2}+{(window.winfo_screenheight() - 700) // 2}")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        # widgets
        self.ctk_img = ctk.CTkImage(light_image=Image.open("assets\\1.png"), dark_image=Image.open("assets\\1.png"), size=(400, 300))
        f_image = ctk.CTkLabel(self, text="", image=self.ctk_img, bg_color="transparent", width=10, height=10)
        f_image.place(x=0, y=0)

        self.h_ahmad = ctk.CTkLabel(self,
                                    text="Marwa Tech Institute  -  MTI",
                                    font=("Times New Roman", 22, "bold"),
                                    bg_color="transparent", width=10, height=10)
        self.h_ahmad.place(relx=0.140, rely=0.480)

        self.dev_info = """
        FEATURES:
            * Add students
            * Search studuents
            * Update existing students
            * Make backup of students
            * Delete students from database
            * About (Show this window)

        Author: Ibrahim Khan
        Github: https://github.com/Always-Root

        This project was created for learning purposes only    
        """
        self.dev_message = ctk.CTkLabel(self,
                                    text=self.dev_info,
                                    font=("Arial", 15, "bold"),
                                    justify="left", padx=10, pady=10)
        self.dev_message.pack(side="bottom", fill="x", padx=10, pady=10)



class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window
        # self.configure(fg_color="#215152")
        self.configure(fg_color="#354475")
        ctk.set_appearance_mode("dark")
        self.title("MARWA TECH INSTITUTE   |   STUDENTS MANAGEMENT SYSTEM")
        self.geometry(f"800x500+{(self.winfo_screenwidth() - 800) // 2}+{(self.winfo_screenheight() - 500) // 2}")
        self.resizable(False, False)

        # Attributes
        self.check_toplevel_window = None

        # buttons
        self.student_add_button = ctk.CTkButton(self, text="ADD STUDENT", command=self.open_add_student_window, corner_radius=20,
                                           fg_color="green", hover_color="#385734", font=("Arial", 20, "bold"))
        self.student_add_button.place(relx=0.15, rely=0.3, relwidth=0.3, relheight=0.2)

        self.student_search_button = ctk.CTkButton(self, text="SEARCH STUDENT", command=self.open_search_student_window, corner_radius=20, fg_color="green",
                                              hover_color="#385734", font=("Arial", 20, "bold"))
        self.student_search_button.place(relx=0.55, rely=0.3, relwidth=0.3, relheight=0.2)

        self.student_update_button = ctk.CTkButton(self, text="UPDATE STUDENT", command=self.open_update_student_window, corner_radius=20, fg_color="orange",
                                              hover_color="#c4741d", font=("Arial", 20, "bold"))
        self.student_update_button.place(relx=0.15, rely=0.52, relwidth=0.3, relheight=0.2)

        self.back_up_button = ctk.CTkButton(self, text="BACKUP", command=back_up_func, corner_radius=20, fg_color="#A020F0", hover_color="#301934",
                                       font=("Arial", 20, "bold"))
        self.back_up_button.place(relx=0.55, rely=0.52, relwidth=0.3, relheight=0.2)

        self.student_delete_button = ctk.CTkButton(self, text="DELETE STUDENT", command=self.open_delete_student_window, corner_radius=20, fg_color="red",
                                              hover_color="#8c3735", font=("Arial", 20, "bold"))
        self.student_delete_button.place(relx=0.15, rely=0.74, relwidth=0.3, relheight=0.2)

        self.about_button = ctk.CTkButton(self, text="ABOUT", command=self.open_about_window, corner_radius=20, font=("Arial", 20, "bold"))
        self.about_button.place(relx=0.55, rely=0.74, relwidth=0.3, relheight=0.2)

        # labels
        # self.ctk_image = ctk.CTkImage(light_image=Image.open("assets\\logo.png"),
        #                          dark_image=Image.open("assets\\logo.png"), size=(150, 150))
        # self.logo_image = ctk.CTkLabel(self, text="Marwa Tech Institute", width=10, height=10)
        # self.logo_image.place(relx=0.190, rely=0.020)

        self.student_no_label = ctk.CTkLabel(self, text="M  T  I", font=("Times New Roman", 60, "bold"), bg_color="transparent")
        self.student_no_label.place(relx=0.390, rely=0.050)

        self.reg_label = ctk.CTkLabel(self, text=f"Marwa Tech Institute", font=("Arial", 20), bg_color="transparent")
        self.reg_label.place(relx=0.390, rely=0.160)


    def open_add_student_window(self):
        if self.check_toplevel_window is None or not self.check_toplevel_window.winfo_exists():
            self.check_toplevel_window = AddStudent()  # create window if its None or destroyed

    def open_search_student_window(self):
        if self.check_toplevel_window is None or not self.check_toplevel_window.winfo_exists():
            self.check_toplevel_window = SearchStudent()  # create window if its None or destroyed

    def open_update_student_window(self):
        if self.check_toplevel_window is None or not self.check_toplevel_window.winfo_exists():
            self.check_toplevel_window = UpdateStudent()  # create window if its None or destroyed

    def open_delete_student_window(self):
        if self.check_toplevel_window is None or not self.check_toplevel_window.winfo_exists():
            self.check_toplevel_window = DeleteStudent()  # create window if its None or destroyed

    def open_about_window(self):
        if self.check_toplevel_window is None or not self.check_toplevel_window.winfo_exists():
            self.check_toplevel_window = About()  # create window if its None or destroyed

# run
window = MainWindow()
window.mainloop()