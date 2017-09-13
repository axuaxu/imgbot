import magic

blob = open('g.txt').read()
m = magic.Magic(mime_encoding=True)
encoding = m.from_buffer(blob)