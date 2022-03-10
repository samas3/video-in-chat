import os, time
from PIL import Image


def list_file(filepath, choose=True):
    # 列出全部文件
    fl = list(os.walk(filepath))[0][2]

    filelist = []
    # 跳帧挑选
    if choose:
        for i in range(0, len(fl), 2):
            filelist.append(fl[i])
    else:
        filelist = fl

    return filelist


def process_picture(path_, filelist, savepath):

    # 删除文件以重新开始
    if os.path.exists(savepath):
        os.remove(savepath)

    start = time.time()
    f = open(savepath, "a+", encoding = 'utf-8')
    # 按路径处理图片
    for file in filelist:
        text_ = ''
        img = Image.open(path_ + "/" + file)
        img = img.convert('L')
        pixels = img.load()
        for h in range(img.height):
            for w in range(img.width):
                text_ += '%02x' % pixels[w, h]
            text_ += '\n'
        print(text_, file=f, end='')
    f.close()
    end = time.time()
    print("处理完成，处理了{0}张图片，用时{1}秒".format(len(filelist), round(end - start, 3)))

    return


if __name__ == "__main__":
    path = "./pic"
    '''
    list_file(path):隔一帧跳一帧
    list_file(path, False):处理全部图片
    '''
    process_picture(path, list_file(path, False), input())
