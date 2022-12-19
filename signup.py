import customtkinter
from pymongo_test_insert import collection_name
import sys
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1080x720")
        self.title("Sign Up")
        self._set_appearance_mode("light")

        self.elabel = customtkinter.CTkLabel(master=self, text="Email Id")
        self.elabel.pack(pady=20, padx=60)

        self.email = customtkinter.CTkTextbox(master=self)
        self.email.pack(after=self.elabel, pady=20, padx=60,fill="both")


        self.plabel = customtkinter.CTkLabel(master=self, text="Password")
        self.plabel.pack(after=self.email ,pady=20, padx=60)

        self.password = customtkinter.CTkTextbox(master=self)
        self.password.pack(after=self.plabel, pady=20, padx=60,fill="both")

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Signup")
        self.button.pack(after=self.password, pady=12, padx=10)
        

    def button_callback(self):
        
        item = {
            
            "email" : str(self.email.get("1.0",'end-1c')),
            "password" : str(self.password.get("1.0",'end-1c'))
        }
        print(item)
        self.email.delete("0.0","end")
        self.password.delete("0.0","end")
        collection_name.insert_one(item)
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
