import xml.etree.ElementTree as ET
import os

out_path = "label"
src_path = "Annotations"

def save_label(annotation: str, out_path: str):
    tree = ET.parse(annotation)
    root = tree.getroot()

    imgName = root.find("filename").text
    BBox = []

    for neighbor in root.iter("bndbox"):
        xmin = int(neighbor.find('xmin').text)
        ymin = int(neighbor.find('ymin').text)
        xmax = int(neighbor.find('xmax').text)
        ymax = int(neighbor.find('ymax').text)

        BBox.append([xmin, ymin, xmax, ymax])
    
    with open(os.path.join(out_path, imgName.replace("jpg", "txt")), "w") as fp:
        for ele in BBox:
            s = [str(x) for x in ele]
            fp.write("1 ")
            fp.write(" ".join(s))
            fp.write("\n")


annotations = os.listdir(src_path)
for annotation in annotations:
    save_label(os.path.join(src_path, annotation), out_path)
        
    