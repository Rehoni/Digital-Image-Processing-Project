import zerorpc


class HelloRPC(object):

    def hello(self, name):
        print("Hello, %s" % name)


a = HelloRPC()
a.hello("rpc")

s = zerorpc.Server(HelloRPC())
s.bind("tcp://127.0.0.1:4242")
s.run()
