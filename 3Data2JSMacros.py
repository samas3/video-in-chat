def processhex(hexstr):
    s = []
    for i in range(0, len(hexstr), 2):
        s.append(int(hexstr[i:i + 2], base = 16))
    return s
def write_js(fn, lines, mode = 'gray'):
    name = '.'.join(fn.split('.')[:-1])
    with open(fn, 'r', encoding = 'utf-8') as f:
        s = f.readlines()
    s = [i.replace('\n', '') for i in s]
    with open(name + '.js', 'w', encoding = 'utf-8') as f:
        f.write('Chat.open("bilibili samas3 求三连 https://space.bilibili.com/620760367");\n')
        for i in range(0, len(s), lines):
            pixels = s[i:i + lines]
            text_ = ''
            for j in pixels:
                text = processhex(j)
                for k in text:
                    if mode == 'gray':
                        if k < 50:
                            text_ += '§0■'
                        elif k < 120:
                            text_ += '§8■'
                        elif k < 190:
                            text_ += '§7■'
                        else:
                            text_ += '§f■'
                    elif mode == 'black':
                        if k < 110:
                            text_ += '■'
                        else:
                            text_ += '□''''
                    elif mode == 'char':
                        chars = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"
                        text_ += chars[int(k / 255 * (len(chars) - 1))]'''
                text_ += '\\n'
            f.write('Chat.log("{}");\n'.format(text_))
            f.write('Time.sleep(41);\n')
        f.write('Chat.open("感谢观看！");\n')
if __name__ == '__main__':
    write_js(input(), 20, input())
