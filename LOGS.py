import datetime


class Logs:
	"""класс создания и редактирование лог файла"""
	def __init__(self):
		#открытие или создание файла логов
		self.logs_file = open("logs.txt", "a")

	def append_data_delete(self):
		#запись в лого о успешном удалении старых данных
		self.logs_file.write(f'{datetime.datetime.now()} --- extra data delete\n')

	def append_create_backup(self, name_file):
		#запись в лого о успешном создании локальной резервной копии
		self.logs_file.write(f'{datetime.datetime.now()} --- create local BACKUP --- name file:${name_file}\n')

	def append_delete_backup_local(self, name_file):
		#запись в лого о успешном удалении локальной резервной копии
		self.logs_file.write(f'{datetime.datetime.now()} --- local BACKUP deleted --- name file:${name_file}\n')

	def append_load_backup_to_cloud(self, name_file):
		#запись в лого о успешной загрузки резервной копии в облако
		self.logs_file.write(f'{datetime.datetime.now()} --- local BACKUP load to cloud --- name file:${name_file}\n')
		
	def append_delete_old_backup_cloude(self, name_file):
		#запись в лого о успешном удалении старой версии резервной копии в облаке
		self.logs_file.write(f'{datetime.datetime.now()} --- old BACKUP from cloud delited --- name file:${name_file}\n')

	def close_file(self):
		self.logs_file.close()