#coding=utf-8
import sys
import os

content = '#coding=utf-8\n'


def process(dirname):
    l = os.listdir(dirname)
    for ll in l:
        print ll
        if ll.startswith('.') == False:
            if os.path.isdir(os.path.join(dirname, ll)):
                process(os.path.join(dirname, ll))
            else:
                if ll.endswith('.py'):
                    text = ''
                    with open(os.path.join(dirname, ll), 'r') as f:
                         text = f.read()

                    with open(os.path.join(dirname, ll), 'w') as f:
                        f.write(content)
                        f.write(text)


def write_file(filename, contents, charset='utf-8'):
    with open(filename, 'w') as f:
        f.write(contents.encode(charset))


if __name__ == '__main__':
    dir = sys.argv
    if len(dir) != 2:
        print "error params"
        exit()

    path = dir[1]
    if dir[0] == '.':
        path = os.path.abspath('.')

    process(path)
