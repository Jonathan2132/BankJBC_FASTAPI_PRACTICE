import datos as dt



from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


OAuth = OAuth2PasswordBearer(tokenUrl = "login")
app = FastAPI()


@app.get("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    return dt.search(form.username)