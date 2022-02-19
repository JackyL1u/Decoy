import pathlib

file_path = str(pathlib.Path().resolve()) + "./Decoy.py"

myBat = open(r'./Google Chrome.bat','w+')
myBat.write('python ' + file_path)
myBat.close()