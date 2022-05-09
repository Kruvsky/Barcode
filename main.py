from barcode import EAN13
from barcode.writer import ImageWriter

codigo_barra = EAN13('123123123123', writer=ImageWriter())
codigo_barra.save("barcode")
'codigo_barra.png'

codigos_produtos = {
    "Monitor": "234567123445",
    "Mouse": "289461758362",
    "Teclado": "172594411111",
    "Headset": "647284111111"}

for produto in codigos_produtos:
    codigo = codigos_produtos[produto]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f"codigo_barra_{produto}")
