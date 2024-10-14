from simple import simplemessenger

message = simplemessenger()

message.login() # This will attempt to generate a qrcode image in the root directory.

cata = [32, 'absolute', 'brackish', 'conundrum']

number = 21972530681
content = f"Hola. {cata[1]}. {cata[0]} {cata[-1]}."

message.send(content, number)
