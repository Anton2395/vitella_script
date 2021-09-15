from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveMy:
	def __init__(self):
		self.gauth = GoogleAuth()
		self.gauth.LocalWebserverAuth()
		self.drive = GoogleDrive(self.gauth)

	def load_new_backup(self, setting, logs):
		file = self.drive.CreateFile({'parents': [{'id': setting.folder_cloud}]})
		file.SetContentFile(setting.name_file)
		file.Upload()
		logs.append_load_backup_to_cloud(setting.name_file)

	def delete_backup_file_cloud(self, setting, logs):
		file_list = self.drive.ListFile({'q': 'trashed=false'}).GetList()
		for file in file_list:
			if file['title'] == setting.conf_last_name:
				file.Delete()
		logs.append_delete_old_backup_cloude(setting.name_file)