import cv2, sys, time, os, shutil


def start_split(filename, siz):
    if os.path.exists('pic'):
        shutil.rmtree('pic', True)
    if not os.path.exists('pic'):
        os.mkdir('pic')
    start = time.time()
    video = cv2.VideoCapture(filename)
    if not video:
        print("无法读取视频文件")
        sys.exit(1)

    count = 0
    while video.isOpened():
        #print("\r正在处理第{0}帧图像".format(count), end="")
        ret, frame = video.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resize2 = cv2.resize(gray, siz)
        cv2.imwrite("pic\\" + str(count).zfill(6) + ".jpg", resize2)
        count += 1

    video.release()

    end = time.time()
    print("\n处理完成,处理了{0}帧图像,用时{1}秒".format(count, round(end - start, 3)))
    return


if __name__ == "__main__":
    start_split(input(), (53, 20))
