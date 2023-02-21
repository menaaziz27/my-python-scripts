import os
import shutil

current = os.path.dirname(__file__)

for file in os.listdir(current):
    if "elody" in file:
        os.rename(os.path.join(current,file), os.path.join(current,"0" + file))
