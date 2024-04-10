import struct

fp = open("arquivo.bin", 'wb+')

fp.write(struct.pack('i', 10))
fp.write(bytes('Carregador'.ljust(10), 'latin-1'))
fp.write(struct.pack('f', 9.5))
fp.seek(0)
mat = struct.unpack('i', fp.read(4))[0]
print(mat)
b = fp.read(10)
s = b.decode('latin-1')
print(s)
print(struct.unpack('f', fp.read(4))[0])
fp.seek(6)
print(fp.read(8).decode('latin-1'))
