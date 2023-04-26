import barcode
from barcode.writer import ImageWriter

# create a Code39 barcode
code = barcode.get('code39', 'Hello1234', writer=ImageWriter())

# save the barcode image as a PNG file
filename = code.save('mybarcode')
