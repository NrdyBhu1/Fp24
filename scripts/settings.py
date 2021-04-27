import json

class SettingsHandler:
    def __init__(self, settings_file):
        self.file = settings_file

    def load_data(self):
        reading_file = open(self.file, "r")
        data = json.load(reading_file)
        reading_file.close()
        return data

    def save_data(self, data):
        writing_file = open(self.file, "w")
        json.dump(data, writing_file)
        writing_file.close()
