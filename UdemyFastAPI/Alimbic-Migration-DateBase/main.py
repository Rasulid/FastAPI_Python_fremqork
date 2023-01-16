from fastapi import FastAPI , Depends
import models
from DataBase import engine
from router import auth, todos, address
from company import companyapis, depenensies, users

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(companyapis.router,
                   prefix="/companyapis",
                   tags=["CompanyAPIs"],
                   dependencies=[Depends(depenensies.get_token_header)],
                   responses={418: {"descriptions": "Internal USE only"}})

app.include_router(users.router)
app.include_router(address.router)


