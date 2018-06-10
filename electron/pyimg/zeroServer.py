import zerorpc
import sys
from scikitfunc.imagefunc import Show
from scikitfunc.filter import EdgeShow


class HelloRPC(object):

    def hello(self, name):
        print("Hello, %s" % name)

    def echo(self, text):
        """echo any text"""
        return text

    def __init__(self):
        self.show = Show()
        self.edge = EdgeShow()

    def open(self, file_path):
        self.show.open_image(file_path)

    def mean(self, file_path):
        return self.show.image_mean(file_path)

    def size(self, file_path):
        return self.show.image_size(file_path)

    def shape(self, file_path):
        return self.show.image_shape(file_path)

    def gray(self, file_path):
        return self.show.image_gray(file_path)

    def sobel(self):
        self.show = EdgeShow()
        return self.show.sobel()


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)


def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(HelloRPC())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()


if __name__ == '__main__':
    main()
