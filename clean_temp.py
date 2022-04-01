import os
from os import environ
import shutil

temp_folder =  f'C:\\Users\\{environ.get("USERNAME")}\\AppData\\Local\\Temp\\'
temp_path =  os.listdir(temp_folder)


def clean_temp():

    for file in temp_path:

        file_path = os.path.join(temp_folder,file) 
        os.chmod(file_path, 0o777)
        
        try:

            if os.path.exists(file_path):

                os.remove(file_path)
        
        except:

            try:

                shutil.rmtree(file_path)
            
            except:

                pass


clean_temp()
