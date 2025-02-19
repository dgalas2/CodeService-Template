import singlestoredb as s2
import os
from dotenv import load_dotenv
from s2_codeservice_template import singleton
load_dotenv(".env")

def getEnvName(env):
	if env=="" or env==None:
		return ""
	else:
		return env + "_"

def getConnectionString(env):
	connection_url = f'singlestoredb://{os.environ.get(getEnvName(env)+"DB_USER_NAME")}:{os.environ.get(getEnvName(env)+"DB_PASSWORD")}@{os.environ.get(getEnvName(env)+"DML_HOST")}:{os.environ.get(getEnvName(env)+"DML_PORT")}/{os.environ.get(getEnvName(env)+"DATABSE_NAME")}'
	return connection_url

class DB(metaclass=singleton.Singleton):
	def __init__(self,conn_url):
		self.conn = s2.connect(conn_url)
		self.cursor = self.conn.cursor()
	
	async def createTable(self):
		
		return self.cursor.execute(r'''
			CREATE TABLE IF NOT EXISTS book (
				id int AUTO_INCREMENT,
				name text,
				isbn text,
				pageCount int,
				PRIMARY KEY (id)
			)
		''')

	async def insertValues(self,values):
		print(values["name"])
		return self.cursor.execute(f'''INSERT INTO book (name, isbn, pageCount) VALUES  ("{values['name']}","{values['isbn']}",{values['pageCount']})''')

	async def getValues(self):
		self.cursor.execute('SELECT * FROM book')
		return self.cursor.fetchall()
