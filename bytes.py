"""
Learn about bytes
Bytes are similar to str type, but they are a sequence of bytes instead of Unicode code points.

Use for raw binary data, fixed-width, single-byte encoding such as ASCII

Use the byte() constructor
"""

d = b'data'
print(d,type(d))

info = b'some bytes here'
# Split the bytes using split() method for bytes
# default split character is space. Creates an array (list) split on a space
print(info.split())

# Encoding: Alt+162 = ó
# use encoding when talking to an external system expecting a specefic, perhaps different encoding
# bytes are transmitted encoded
message = "Vamos al zoológico"
print(message)
data = message.encode("utf-8")
print(data)
new_message=data.decode("utf-8")
print(new_message)
