import conection as ct
from pydantic import BaseModel


function = ct.conection.cursor()

class USer(BaseModel):
    username:str
    Name:str
    email:str
    password:str



def search(username: str):
    
    try:
        function.execute("select * from users where username = %s",(username,))
        user_info = function.fetchall()
        
        if not user_info:
            return False
        
        for m in user_info:
            user_info = m
        
       
        usuario = {
            
            "username": user_info[0],
            "Name": user_info[1],
            "email": user_info[2],
            "password": user_info[3]
                  }
        return(USer(**usuario))

    
    
    except:
        print("A ocurrido un error ")
        
        

