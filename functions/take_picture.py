import cv2
import pathlib


def take_picture():
    path = str(pathlib.Path(__file__).parent.resolve())
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:
        cv2.imwrite(path + "/../temp_files/picture.jpg", img)
        cv2.destroyAllWindows()
    cam.release()
