import datetime
import json


class Settings:
	"""Класс хронящий настройки скрипта"""
	def __init__(self):
		"""инициализация настроек"""
		self.name_file = f'BACKUP_ReportData_{str(datetime.datetime.now().date())}.BAK'
		self.folder = 'C:\\Users\\ACTclearWin\\Desktop\\script_vit'
		self.day_delete = 552
		self.folder_cloud = '1GtrxAgAXlzVH_xEeo4bVbG-iks8GaBAE'
		with open("conf", "r") as file:
			self.conf_last_name = json.loads(file.read())["last_name"]

	def rewrite_conf(self):
		#метод перезаписи conf файла
		conf = {"last_name": self.name_file}
		with open("conf", "w") as file:
			file.write(json.dumps(conf))