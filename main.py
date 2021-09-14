import pyodbc 
import datetime
import time

from Google_load import log_in
from Google_load import load_new_backup

from DB_MS_SQL import conect_to_DB
from DB_MS_SQL import delete_old_data_from_DB
from DB_MS_SQL import create_backup_file
from DB_MS_SQL import delete_backup_file_local

from settings import Settings
from LOGS import Logs






if __name__ == '__main__':
	""" Удаление данных старше двух лет (730-и дней), создание резервной копии, загрузка резервной копии в облоко"""
	setting = Settings()
	logs = Logs()
	con, cursor = conect_to_DB()
	
	start = time.time()
	delete_old_data_from_DB(cursor, setting, logs)
	end = time.time()
	print(f'data_delete --- {str(round((end-start)/60, 2))} min')
	
	start = time.time()
	create_backup_file(cursor, setting, logs)
	end = time.time()
	print(f'backup_create --- {str(round((end-start)/60, 2))} min')
	
	start = time.time()
	load_new_backup(setting, logs)
	end = time.time()
	print(f'LOAD FINISH --- {str(round((end-start)/60, 2))} min')

	delete_backup_file_local(setting, logs)
	setting.rewrite_conf()
	logs.close_file()








