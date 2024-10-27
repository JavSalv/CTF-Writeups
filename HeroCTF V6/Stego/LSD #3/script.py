from PIL import Image
import sys


def binaryToString(binary):
    return ''.join([chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8)])


try:
    filename = sys.argv[1] if len(sys.argv)==2 else "secret.png"
    img = Image.open(filename,"r")
except:
    print("File not found")
    exit(1)


    
print(f"Decoding {filename}")
    
width, height = img.size

x,y = 0,0

salida = ""

while x < width and y < height:
    pixel = list(img.getpixel((x,y)))
    salida += str(pixel[2] & 1)
    x +=1
    y+=1    
    
with open("output.txt","w") as file_out:
    file_out.write(binaryToString(salida))    
    