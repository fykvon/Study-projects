import shutil
import os
import datetime as datetime

class Regulation:

    def __init__(self, name):
        self.path = name

    def make_folders(self):
        path = os.listdir(self.path)
        for ifile in path:
            next_path = os.path.join(self.path, ifile)
            all_files = os.listdir(next_path)
            for items in all_files:
                full_path = os.path.join(next_path, items)
                get_time = os.path.getmtime(full_path)  # Берём время изменения.
                normalize_time = datetime.datetime.fromtimestamp(get_time)
                normalize_time_Year_month = normalize_time.strftime('%Y/%m')
                os.makedirs(normalize_time_Year_month, exist_ok=True)
                shutil.copy2(full_path, normalize_time_Year_month)

    def act(self):
        self.make_folders()


a = Regulation(name='icons')
a.act()