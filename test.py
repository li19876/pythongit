import barcode

from barcode.writer import ImageWriter

print(barcode.PROVIDED_BARCODES)#查看python-barcode支持的条形码格式

CODE128 = barcode.get_barcode_class('code128') #创建ean13格式的条形码格式对象

ean = CODE128('WXUPAH5A29F4',writer=ImageWriter())#创建条形码对象，内容为5901234123457

fullname = ean.save('./barcode/WXUPAH5A29F4',options={'module_height':10.0,"write_text":False}) #保存条形码图片，并返回保存路径。图片格式为png

print(fullname)