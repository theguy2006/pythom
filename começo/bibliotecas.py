import time, random, qrcode
# print('Aguarde...')
# time.sleep(4)
# print('pronto!')
# while True:
#     numero_aleatorio = random.randint(1, 50)
#     print(numero_aleatorio)
#     time.sleep(1)
#     if numero_aleatorio % 2 == 0:
#         break

img = qrcode.make('https://www.youtube.com/@conanrock')
img.save('qr_canal.png')