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

from dotenv import load_dotenv
load_dotenv()
connection_url = f'singlestoredb://{os.environ.get("USER_NAME")}:{os.environ.get("PASSWORD")}@{os.environ.get("DML_ENDPOINT")}/{os.environ.get("DATABSE_NAME")}'
os.environ["SINGLESTOREDB_URL"] = connection_url
os.environ["DATABASE_URL"] = connection_url

class Book(BaseModel):
    name: str
    isbn: str
    pageCount: int

# Create a FastAPI application
app = FastAPI()

#create db object
db = database.DB(connection_url)
 
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



async def run_on_nova():
	import singlestoredb.apps as apps
	await apps.run_function_app(app)
      
def run_on_local():

    uvicorn.run("s2_codeservice_template.__init__:app", host=os.getenv('HOST'), port=os.getenv('PORT'), reload=False)

def main():
    # Use this for nova platform
    asyncio.run(run_on_nova())
    # This is for local development
    # run_on_local()

if __name__ == "__main__":
	main()

