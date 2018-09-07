import imageio
import os
import numpy
import cv2
from PIL import Image
import shutil

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class GifOperater(object):
    def read_to_png(self, src, dst):
        if not os.path.exists(src):
            raise Exception("src not exist")
        if not os.path.exists(dst):
            os.makedirs(dst)
        reader = imageio.get_reader(src)
        print len(reader)
        for i, im in enumerate(reader):
            if len(reader) > 20:
                if i % 2 ==0:
                    imageio.imwrite(os.path.join(dst, str(i) + ".png"), im)
            else:
                imageio.imwrite(os.path.join(dst, str(i) + ".png"), im)

    def read_first_png(self, src, dst):
        if not os.path.exists(src):
            raise Exception("src not exist")
        else:
            gif_name = os.path.basename(src)
            gif_name_prefix = gif_name.split(".")[0]
        if not os.path.exists(dst):
            os.makedirs(dst)
        im = Image.open(src)
        current = im.tell()
        im.save(os.path.join(dst, gif_name_prefix + "-" + str(current) +".png"))
        os.rename(os.path.join(os.path.join(dst, gif_name_prefix + "-" + str(current) +".png")),
                                     os.path.join(dst, gif_name_prefix + ".png"))


    def opencv_get_all_gif_png(self):
        if not os.path.exists(src):
            raise Exception("src not exist")
        else:
            gif_name = os.path.basename(src)
            gif_name_prefix = gif_name.split(".")[0]
        if not os.path.exists(dst):
            os.makedirs(dst)
        im = Image.open(src)
        try:
            while True:
                current = im.tell()
                im.save(os.path.join(dst, gif_name_prefix + "-" + str(current) +".png"))
                im.seek(current+1)
        except EOFError:
            pass

    def write_to_gif(self, src, dst):
        if not os.path.exists(src):
            raise Exception("src not exist")
        if not os.path.exists(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))
        file_list = os.listdir(src)
        # print file_list
        # if len(file_list) > 20 :
        #     file_list = [lambda x: x%4 ==0, file_list]
        # print file_list
        file_list = [os.path.join(src, x) for x in file_list]
        if file_list:
            frames = list()
            for i in file_list:
                im = imageio.imread(i)
                frames.append(im)
            imageio.mimsave(dst, frames, duration=0.1)
        else:
            raise Exception("Src blank")


if __name__ == "__main__":
    # read gif
    # src = os.path.join(CURRENT_DIR, "img", "src", "1_test.gif")
    # dst = os.path.join(CURRENT_DIR, "img", "dst")
    # GifOperater().read_to_png(src, dst)

    # write gif
    # src = os.path.join(CURRENT_DIR, "img", "dst")
    # dst = os.path.join(CURRENT_DIR, "img", "src", "3_test.gif")
    # GifOperater().write_to_gif(src, dst)

    # read first pic
    src = os.path.join(CURRENT_DIR, "img", "src", "2.gif")
    dst = os.path.join(CURRENT_DIR, "img", "dst")
    GifOperater().read_first_png(src, dst)
