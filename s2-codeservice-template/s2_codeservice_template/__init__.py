'''
Poetry Script for local development: 
	poetry run local-dev
	
HOST and PORT variables can be defined using the ../.env file.

'''


import os
from fastapi import FastAPI
from s2_codeservice_template import database
import asyncio
import uvicorn
from pydantic import BaseModel
import singlestoredb.apps as apps
from dotenv import load_dotenv
load_dotenv(".env")

# if you do not want to use different db for different env, just set env = "",
# OR do not set variable ENV in .env file
env = os.environ.get("ENV")
print(env)
if env != 'SINGLESTOREDB_APP' and env!=None:

    connection_url = database.getConnectionString(env)

    # only one DB connection string can exist in OS at one time. TODO: change it such that we can use multiple, thus being able to run multiple projects together on local
    os.environ["SINGLESTOREDB_URL"] = connection_url
    os.environ["DATABASE_URL"] = connection_url
print(os.environ["SINGLESTOREDB_URL"])
class Book(BaseModel):
    name: str
    isbn: str
    pageCount: int

# Create a FastAPI application
app = FastAPI()

#create db object
db = database.DB(os.environ["SINGLESTOREDB_URL"])
 
# Define a route at the root web address ("/")
@app.get("/")
async def root():
    return await db.createTable()

@app.get("/books")
async def books():
    return await db.getValues()

@app.post("/insert")
async def insert(book: Book):
    print(book,book.dict())
    return await db.insertValues(book.dict())



async def run_codeservice():
    await apps.run_function_app(app,wait_for_exit=True)
      
def main():
    asyncio.run(run_codeservice())

if __name__ == "__main__":
    main()

