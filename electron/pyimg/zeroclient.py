import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

print(c.echo('haha'))
print(c.size('lena.jpg'))
print(c.mean('lena.jpg'))
print(c.shape('lena.jpg'))