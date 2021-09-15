from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveMy:
	"""Класс работы с облочным хранилищем"""
	def __init__(self):
		"""Инициализация данных в котором """
		#авторизация в сервисе google
		self.gauth = GoogleAuth()
		self.gauth.LocalWebserverAuth()
		#получение сущности хранилища
		self.drive = GoogleDrive(self.gauth)

	def load_new_backup(self, setting, logs):
		#метод загрузки резервной копии в облочное хранилище
		file = self.drive.CreateFile({'parents': [{'id': setting.folder_cloud}]})
		file.SetContentFile(setting.name_file)
		file.Upload()
		logs.append_load_backup_to_cloud(setting.name_file)

	def delete_backup_file_cloud(self, setting, logs):
		#метод удаление из облочного хранилища старой резервной копии
		file_list = self.drive.ListFile({'q': 'trashed=false'}).GetList()
		for file in file_list:
			if file['title'] == setting.conf_last_name:
				file.Delete()
		logs.append_delete_old_backup_cloude(setting.name_file)