import zerorpc
import sys
from scikitfunc.imagefunc import Show


class HelloRPC(object):

    def hello(self, name):
        print("Hello, %s" % name)

    def echo(self, text):
        """echo any text"""
        return text

    def mean(self, file_path):
        show = Show()
        show.open_image(file_path)
        return show.image_mean()

    def size(self, file_path):
        show = Show()
        show.open_image(file_path)
        return show.image_size()

    def shape(self, file_path):
        show = Show()
        show.open_image(file_path)
        return show.image_shape()


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
