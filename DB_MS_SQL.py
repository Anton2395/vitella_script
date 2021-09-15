import pyodbc
import datetime
import os

def conect_to_DB():
	"""Подключение к базе данных"""
	con = pyodbc.connect(
		'DRIVER={SQL Server};'
		'SERVER=AST\SQLEXPRESS;'
		'DATABASE=ReportData;'
		'Trusted_Connection=yes;')
	cursor = con.cursor()
	con.autocommit = True
	return con, cursor

def delete_old_data_from_DB(cursor, setting, logs):
	"""Удаление данных старше <day_delete> дней"""
	cursor.execute(f"DELETE FROM dbo.Data where  DATEDIFF(day, TIMESTAMP, getdate())>{str(setting.day_delete)} ")
	logs.append_data_delete()

def create_backup_file(cursor, setting, logs):
	"""Создание резервной копии БД"""
	cursor.execute(f"""BACKUP DATABASE ReportData
		TO DISK = '{setting.folder}\\{setting.name_file}'""")
	while (cursor.nextset()):
		pass
	logs.append_create_backup(setting.name_file)

def delete_backup_file_local(setting, logs):
	"""Удаление файла локальной резервной копии БД"""
	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), setting.name_file)
	os.remove(path)
	logs.append_delete_backup_local(setting.name_file)