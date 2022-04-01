import os
from os import environ
import shutil

temp_folder =  f'C:\\Users\\{environ.get("USERNAME")}\\AppData\\Local\\Temp\\'
temp_path =  os.listdir(temp_folder)


def clean_temp():

    for file in temp_path:
        
        try:

            if os.path.exists(os.path.join(temp_folder,file)):

                os.remove(os.path.join(temp_folder,file))
        
        except Exception as e:

            try:
                shutil.rmtree(os.path.join(temp_folder,file))
            
            except Exception as e:

                pass


clean_temp()
