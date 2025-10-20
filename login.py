import customtkinter as ctk
from tkinter import END
import sys, os
from PIL import Image



# for verifying username and password
def verify_user_and_pass():
    username = username_entry.get()
    password = password_entry.get()

    if username == "123" and password == "123":
        # replace the current process (login.py) with main.py
        os.execv(sys.executable, [sys.executable, "main.py"])
        # login_window.destroy()
        
    else:
        password_entry.delete(0, END)
        message = ctk.CTkLabel(login_window, text="Invalid! Username or Password", text_color="red", font=("Arial", 15, "bold"), bg_color="transparent")
        message.place(relx=0.20, rely=0.75)
        login_window.after(2000, message.destroy)



#window
login_window = ctk.CTk()
ctk.set_appearance_mode("light")
login_window.title("Please, Login to SSA")
login_window.geometry(f"350x500+{(login_window.winfo_screenwidth() - 350) // 2}+{(login_window.winfo_screenheight() - 500) // 2}")
login_window.resizable(False, False)

# widgets
ctk_image = ctk.CTkImage(light_image=Image.open("assets\\logo.png"),
                                dark_image=Image.open("assets\\logo.png"), size=(200, 200))
logo_image = ctk.CTkLabel(login_window, text="", image=ctk_image, bg_color="transparent", width=10, height=10)
logo_image.place(relx=0.210, rely=0.050)

username_entry = ctk.CTkEntry(login_window, placeholder_text="Enter Username", font=("", 20), border_color="green", corner_radius=20, width=300, height=50)
username_entry.place(relx=0.07, rely=0.50)

password_entry = ctk.CTkEntry(login_window, placeholder_text="Enter Password", font=("", 20), border_color="green", corner_radius=20, width=300, height=50, show="*")
password_entry.place(relx=0.07, rely=0.65)

login_button = ctk.CTkButton(login_window, text="LOGIN", command=verify_user_and_pass, fg_color="green", hover_color="#385734", corner_radius=20, width=200, height=50)
login_button.place(relx=0.22, rely=0.85)

# run
login_window.mainloop()
