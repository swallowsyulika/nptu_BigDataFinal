import cv2

img = "Images/000002.jpg"
label = "labels/000002.txt"

with open(label) as fp:
    p = fp.readlines()

    img = cv2.imread(img)
    for ele in p:
        pos = [int(x) for x in ele.split()][1:]
        cv2.rectangle(img, (pos[0], pos[1]), (pos[2], pos[3]), (0, 0, 255), 2)
        
    cv2.imshow("AnimeFaceBBox", img)
    cv2.waitKey(0)

