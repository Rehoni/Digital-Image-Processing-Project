import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

print(c.echo('haha'))
path = 'lena.jpg'
# c.open('lena.jpg')  # open jpg

print(c.shape(path))
print(c.size(path))
print(c.mean(path))
# print(c.gray(path))

# print(c.sobel(path))
