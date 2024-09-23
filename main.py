import datos as dt



from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from datetime import datetime ,timedelta
from jose import jwt
from passlib.context import CryptContext

verficar = CryptContext(schemes=["bcrypt"])

OAuth = OAuth2PasswordBearer(tokenUrl = "login")
app = FastAPI()

exps = 20
secretword = "hola"
am = "HS256"


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    username = dt.search(form.username)
    
    if not username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=(f"El usuario {form.username} no existe o no es valido"))
    
    vf =  verficar.verify(str(form.password),str(username.password))
    if not vf:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST ,detail=(f"El contrasena {form.password} no es valido"))
        
    
    exp = datetime.utcnow() + timedelta(minutes=1)
    
    access_token ={
        "sub":form.username,
        "exp":exp
    }
    
    return {"access_token": jwt.encode(access_token,secretword,algorithm=am) ,"toeken_type":"bearer"}
    
    
    
    
    