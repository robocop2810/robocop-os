import sys 
import os
import time
from tqdm import tqdm
from tkinter import *
from tkinter import filedialog

dirName = 'robocop-os_files'

def robocopossetup():
    #robocop-os setup
    print("ROBOCOP-OS_INFO: First time setup !")
    print("Directory " , dirName ,  " Created ") 


def robotext():
    #robotext_code
    os.system('python robotext.py')



print(r"""\

               __                                        
   _________  / /_  ____  _________  ____     ____  _____
  / ___/ __ \/ __ \/ __ \/ ___/ __ \/ __ \   / __ \/ ___/
 / /  / /_/ / /_/ / /_/ / /__/ /_/ / /_/ /  / /_/ (__  ) 
/_/   \____/_.___/\____/\___/\____/ .___/   \____/____/  
                                 /_/                     
""")
time.sleep(1)
#check if system has been used before(setup)
try:
    os.mkdir(dirName)
    robocopossetup()
except FileExistsError:
    pass

for i in tqdm(range(100)):
    time.sleep(0.1)
#system started
print('#ROBOCOP-OS_INFO: services started !')

print('For help type "help"')
while True:
    command = input('console :')
    if command == 'help' :
        print(r"""\
            __         __    
           / /_  ___  / /___ 
          / __ \/ _ \/ / __ \
         / / / /  __/ / /_/ /
        /_/ /_/\___/_/ .___/ 
                    /_/      
        """)
        print(r"""list of commands: 
              robotext
              roboimg""")

    if command == 'robotext':
        print(r"""\       
                       __          __            __ 
           _________  / /_  ____  / /____  _  __/ /_
          / ___/ __ \/ __ \/ __ \/ __/ _ \| |/_/ __/
         / /  / /_/ / /_/ / /_/ / /_/  __/>  </ /_  
        /_/   \____/_.___/\____/\__/\___/_/|_|\__/                     
        
        """)
        for i in tqdm(range(1000)):
            time.sleep(0.0001)
        robotext()
    if command == 'roboimg':
        print(r"""
                   __               _                       
       _________  / /_  ____ _   __(_)__ _      _____  _____
      / ___/ __ \/ __ \/ __ \ | / / / _ \ | /| / / _ \/ ___/
     / /  / /_/ / /_/ / /_/ / |/ / /  __/ |/ |/ /  __/ /    
    /_/   \____/_.___/\____/|___/_/\___/|__/|__/\___/_/     
        """)