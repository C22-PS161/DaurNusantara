import xml.etree.ElementTree as ET
import pandas as pd
import glob

def convert_to_xml(path):
    list_xml = []
    for file in glob.glob (path + '/*.xml'): #mengecek setiap file .xml
        tree = ET.parse(file)
        root = tree.getroot()
        for object_tag in root.findall('object'): #dikarenakan tiap gambar bisa ada lebih dari 1 objek
            values = (
                root.find('filename').text, #filename
                int(root.find('size').find('width').text), #size width
                int(root.find('size').find('height').text), #size height
                object_tag[0].text, #nama objek
                int(object_tag.find('bndbox').find('xmin').text), #bndbox xmin
                int(object_tag.find('bndbox').find('ymin').text), #bndbox ymin
                int(object_tag.find('bndbox').find('xmax').text), #bndbox xmax
                int(object_tag.find('bndbox').find('ymax').text) #bndbox ymax
            )
            list_xml.append(values)
    headercsv = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    pd_xml = pd.DataFrame(list_xml, columns=headercsv)
    return pd_xml

############################

def main():
    path = './dataset/annotate'
    data_xml = convert_to_xml(path)
    data_xml.to_csv('./csv/labels.csv', index=None) #konversi ke CSV
    print("Berhasil mengkonversikan xml ke CSV")

main()    