'''
we are going to use a python library like qrcode and convert url to qr 
'''
import qrcode
url = input("Enter your url: ")
filename = input("Enter filename to save: ")
if not(filename.endswith(".png") ): 
    filename = input("filename you want to save it as : ")
filename= filename + ".png"
img = qrcode.make (url)
img.save(filename )