import os
import xml.etree.ElementTree as ET

tree = ET.parse('(6) - Copy.xml')

tree.find('./folder').text = 'cobaaja'

tree.write('(6) - Copy.xml')


def ubah_xml(path, namafolder):
    tree = ET.parse(path)
    tree.find('./folder').text = namafolder
    # tree.find('./').text =
    tree.write(path)

path1 =
namafolder1 =
namapath1 = os.path.join(namafolder1, namafile1)