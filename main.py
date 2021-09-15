import pyodbc 
import datetime
import time


from Google_load import GoogleDriveMy

from DB_MS_SQL import conect_to_DB
from DB_MS_SQL import delete_old_data_from_DB
from DB_MS_SQL import create_backup_file
from DB_MS_SQL import delete_backup_file_local

from settings import Settings
from LOGS import Logs


if __name__ == '__main__':
	""" Удаление данных старше двух лет (730-и дней), создание резервной копии, загрузка резервной копии в облоко"""
	
	#создание сущностей настроек, событий, работы с облачным хранилищем, базы данных.
	setting = Settings()
	logs = Logs()
	g_drive = GoogleDriveMy()
	con, cursor = conect_to_DB()
	
	#удаление данных старше двух лет (730-и дней)
	start = time.time()
	delete_old_data_from_DB(cursor, setting, logs)
	end = time.time()
	print(f'data_delete --- {str(round((end-start)/60, 2))} min')
	
	#создание резервной копии базы данных
	start = time.time()
	create_backup_file(cursor, setting, logs)
	end = time.time()
	print(f'backup_create --- {str(round((end-start)/60, 2))} min')
	
	#удаление старой резервной копии из облачного хранилища
	start = time.time()
	g_drive.delete_backup_file_cloud(setting, logs)
	end = time.time()
	print(f'delete_old_backup_cloud --- {str(round((end-start)/60, 2))} min')

	#загрузка новой резервной копии в облочное хранилища
	start = time.time()
	g_drive.load_new_backup(setting, logs)
	end = time.time()
	print(f'LOAD_new_backup_cloud --- {str(round((end-start)/60, 2))} min')

	#удаление локальной резервной копии
	start = time.time()
	delete_backup_file_local(setting, logs)
	end = time.time()
	print(f'delete_backup_local --- {str(round((end-start)/60, 2))} min')

	#настройка скрипта для следующего использования
	setting.rewrite_conf()

	#закрытие файла логов
	logs.close_file()