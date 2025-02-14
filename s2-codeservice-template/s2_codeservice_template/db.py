import singlestoredb as s2
import os
from dotenv import load_dotenv
load_dotenv()
connection_url = f'https://{os.environ.get("USER_NAME")}:{os.environ.get("PASSWORD")}@{os.environ.get("DML_ENDPOINT")}/{os.environ.get("DATABSE_NAME")}'
os.environ["SINGLESTOREDB_URL"] = connection_url
os.environ["DATABASE_URL"] = connection_url
print(connection_url)
s2_conn = s2.connect(f'https://{os.environ.get("DML_ENDPOINT")}/{os.environ.get("DATABASE_NAME")}',user=os.environ.get("USER_NAME"),password=os.environ.get("PASSWORD"))
s2_cur = s2_conn.cursor()

async def createTable():
	
	return s2_cur.execute(r'''
		CREATE TABLE IF NOT EXISTS book (
			id int AUTO_INCREMENT,
			name text,
			isbn text,
			pageCount int,
			PRIMARY KEY (id)
		)
	''')

async def insertValues(values):
	print(values["name"])
	return s2_cur.execute(f'''INSERT INTO book (name, isbn, pageCount) VALUES  ("{values['name']}","{values['isbn']}",{values['pageCount']})''')

async def getValues():
	s2_cur.execute('SELECT * FROM book')
	return s2_cur.fetchall()
