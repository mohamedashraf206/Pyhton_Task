import uuid
class user:
    users=[]
    signed_in = ""
    def __init__(self,fName,lName,email,password,mobile,id=(str(uuid.uuid4()))):
        self.fName=fName
        self.lName=lName
        self.password=password
        self.email=email
        self.mobile=mobile
        #generate a unique id for each user
        self.id = id
            
    def call (self):
        return "user"


 
