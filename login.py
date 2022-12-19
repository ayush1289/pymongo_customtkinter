import customtkinter
import signup
from pymongo_test_insert import collection_name
from pymongo_test_query import items_df

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("1080x720")
        self.title("Login")
        self._set_appearance_mode("light")

        self.elabel = customtkinter.CTkLabel(master=self, text="Email Id")
        self.elabel.pack(pady=20, padx=60)

        self.email = customtkinter.CTkTextbox(master=self)
        self.email.pack(after=self.elabel, pady=20, padx=60,fill="both")


        self.plabel = customtkinter.CTkLabel(master=self, text="Password")
        self.plabel.pack(after=self.email ,pady=20, padx=60)

        self.password = customtkinter.CTkTextbox(master=self)
        self.password.pack(after=self.plabel, pady=20, padx=60,fill="both")

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Login")
        self.button.pack(after=self.password, pady=12, padx=10)

        self.signup = customtkinter.CTkButton(master=self, command=self.button_signup, text="New User")
        self.signup.pack(after=self.password, pady=12, padx=10)
    
    def button_signup(self):
        signup.App()

    def button_callback(self):
        item = {
            
            "email" : str(self.email.get("1.0",'end-1c')),
            "password" : str(self.password.get("1.0",'end-1c'))
        } 
        mydoc = collection_name.find(item)
        result = list(mydoc)
        if len(result) == 1:
            print("login successful")  
        if len(result) == 0:
            print("wrong id or pass")
            
        
        
        
        
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
