import imageio
import os
import numpy


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
    # read
    # src = os.path.join(CURRENT_DIR, "img", "src", "3_test.gif")
    # dst = os.path.join(CURRENT_DIR, "img", "dst")
    # GifOperater().read_to_png(src, dst)

    # write
    src = os.path.join(CURRENT_DIR, "img", "dst")
    dst = os.path.join(CURRENT_DIR, "img", "src", "3_test.gif")
    GifOperater().write_to_gif(src, dst)
