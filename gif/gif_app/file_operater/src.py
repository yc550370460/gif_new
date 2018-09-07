import shutil
import os

IMG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")

shutil.copyfile(os.path.join(IMG_PATH, "1-0.png"), os.path.join(IMG_PATH, "1-0-copy.png"))