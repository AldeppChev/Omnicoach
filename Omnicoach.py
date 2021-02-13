## LIBRARIES ##

from PIL import Image
import pytesseract
import csv
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Sacha\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

## CODE ##

#PLEASE CHANGE THE PATH OF THE PICTURE TO THE ONE DESIRED !#
image = Image.open('ScreenOW6.jpg')

#cropped_image = image.crop((0,880,900,1080))
kills = image.crop((0,880,300,950))
obj_kills = image.crop((300,880,550,950))
obj_time = image.crop((580,880,900,950))
hero_dmg = image.crop((130,950,230,995))
heal = image.crop((300,950,550,1020))
deaths = image.crop((580,930,810,1000))

kills.save('kills.jpg')
obj_kills.save('obj_kills.jpg')
obj_time.save('obj_time.jpg')
hero_dmg.save('hero_dmg.jpg')
heal.save('heal.jpg')
deaths.save('deaths.jpg')

#cropped_image.save('testcrop.jpg')
ik = Image.open('kills.jpg')
iok = Image.open('obj_kills.jpg')
iot = Image.open('obj_time.jpg')
ihd = Image.open('hero_dmg.jpg')
ih = Image.open('heal.jpg')
id = Image.open('deaths.jpg')

print(ik.size)
print(pytesseract.image_to_string(id))
List = [ik,iok,iot,ihd,ih,id]

## image2.show()

def is_digit_or_comma_or_semicolon(char) :
    if ord(char) >= ord('0') and ord(char) <= ord('9') or ord(char) == ord(',') or ord(char) == ord(':') :
        return True
    return False

""" def raw_to_list(raw) :
    L = []
    Fin = False
    for i in range(len(raw)) :
        if is_digit_or_comma_or_semicolon(raw[i]) :
            nbr = ""
            if not Fin :
                while is_digit_or_comma_or_semicolon(raw[i]) :
                    nbr = nbr + raw[i]
                    i+=1
                if not is_digit_or_comma_or_semicolon(raw[i+1]) :
                    Fin = True
                L.append(nbr)
        else :
            Fin = False
    return  L """

def raw_to_string(raw) :
    str = ""
    for i in range(len(raw)) :
        if is_digit_or_comma_or_semicolon(raw[i]) :
            while (is_digit_or_comma_or_semicolon(raw[i]) or is_digit_or_comma_or_semicolon(raw[i+1])) :
                str += raw[i]
                i+=1
            return str
    return str

data_list = []
for i in range(len(List)) :
    raw = pytesseract.image_to_string(List[i])
    data_list.append(raw_to_string(raw))
print(data_list)

with open('omnicoach.csv','w',newline='') as file :
    writer = csv.writer(file)
    writer.writerow(["ELIMINATIONS",data_list[0]])
    writer.writerow(["OBJECTIVE KILLS", data_list[1]])
    writer.writerow(["OBJECTIVE TIME", data_list[2]])
    writer.writerow(["HERO DAMAGE DONE", data_list[3]])
    writer.writerow(["HEALING DONE", data_list[4]])
    writer.writerow(["DEATHS", data_list[5]])