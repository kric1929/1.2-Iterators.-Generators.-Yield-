import hashlib


def get_md5_each_line(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            strip_line = line.strip()
            byte_line = strip_line.encode()
            yield hashlib.md5(byte_line)


if __name__ == '__main__':
    for i in get_md5_each_line('countries-url.txt'):
        print(i.hexdigest())
