import os
from fastapi import FastAPI
from s2 import get_message
import singlestoredb.apps as apps
import asyncio

from dotenv import load_dotenv
load_dotenv()

# Create a FastAPI application
app = FastAPI()
 
# Define a route at the root web address ("/")
@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/s2")
async def singlestore():
    return await get_message()


async def run_on_nova():
	await apps.run_function_app(app)

def main():
    asyncio.run(run_on_nova())

if __name__ == "__main__":
    # Use this for nova platform
	main()
      
#for local development use: (replace s2_codeservice_template with parent folder name of this file)
#uvicorn.run("s2_codeservice_template.__init__:app", host="127.0.0.1", port=5678, reload=False)

