from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def log_in():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()
	return gauth


def load_new_backup(setting, logs):
	gauth = log_in()
	drive = GoogleDrive(gauth)
	file = drive.CreateFile({'parents': [{'id': setting.folder_cloud}]})
	file.SetContentFile(setting.name_file)
	file.Upload()
	logs.append_load_backup_to_cloud(setting.name_file)

def delete_backup_file_cloud(setting):


class GoogleDrive:
	def __init__(self):
		self.gauth = GoogleAuth()
		self.gauth.LocalWebserverAuth()
		self.drive = GoogleDrive(gauth)

	def load_new_backup(self, setting, logs):
		file = self.drive.CreateFile({'parents': [{'id': setting.folder_cloud}]})
		file.SetContentFile(setting.name_file)
		file.Upload()
		logs.append_load_backup_to_cloud(setting.name_file)

	def delete_backup_file_cloud(self, setting, logs):
		file = self.drive.CreateFile({'id': setting.conf_last_name})
		file.Delete()