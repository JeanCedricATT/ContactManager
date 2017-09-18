class MyContact:
    def __int__(self,Name,Phone,Email,Website,Bday,linkedIN):
        self.Name=Name
        self.Phone=Phone
        self.Email=Email
        self.Website=Website
        self.Bday=Bday
        self.linkedIN=linkedIN

people=MyContact()
people.Name=input("Your Name: ")
people.Phone=input("Your Phone: ")
people.Email=input("Your Mail: ")
people.Website=input("Website: ")
people.Bday=input("Birthday: ")
people.linkedIN=input("Your linkedIN: ")
print(people.Name,"\n",people.Phone,"\n",people.Email,"\n",people.Website,"\n",people.Bday,"\n",people.linkedIN)
