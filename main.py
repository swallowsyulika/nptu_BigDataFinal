import torch
import cv2
import numpy as np
import os
import argparse


def run_image(image: str):
    # load model
    model = torch.hub.load("ultralytics/yolov5", "yolov5x")
    res = model(image)
    res.print()
    res.show()


# def resize2save(image: np, bbox: np, oriSize: np, imgSize: int, res_path: str):
#     img = cv2.resize(image, (oriSize[1], oriSize[0]))
#     w_ratio = oriSize[0] / imgSize
#     h_ratio = oriSize[1] / imgSize
#     ratioList = [h_ratio, w_ratio, h_ratio, w_ratio]

#     boxes = []
#     for ele in bbox:
#         box = [int(a * b) for a, b in zip(ele, ratioList)]
#         boxes.append(box)
    
#     for ele in boxes:
#         cv2.rectangle(img, (ele[0], ele[1]), (ele[2], ele[3]), (0, 0, 255), 3)
#     cv2.imwrite(res_path, img)
    

def eval_model_images(model, in_path: str, out_path: str):
    img = cv2.imread(in_path)
    print(in_path)
    #oriSize = img.shape
    #rimg = cv2.resize(img, dsize=(imgSize, imgSize), interpolation=cv2.INTER_CUBIC)
    res = model(img)
    res.print()
    #res.show()
    #pos = res.xyxy[0]
    #pos = [x.cpu().detach().numpy() for x in pos]
    #resize2save(rimg, pos, oriSize, imgSize, res_path)
    cv2.imwrite(out_path, np.squeeze(res.render()))


def eval_model_video(model, video_path: str):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()

        res = model(frame)

        cv2.imshow("video", np.squeeze(res.render()))

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=int, default=1, help="0: image folder, 1: video path")
    parser.add_argument('--in_path', default ='data/Anime/test')
    parser.add_argument('--out_path', default="data/Anime/res")
    parser.add_argument('--v_path', default="data/Anime/video5.mp4")
    parser.add_argument('--weight', default="yolov5/runs/train/exp/weights/best.pt")
    args = parser.parse_args()

    model = torch.hub.load("ultralytics/yolov5", "custom", path=args.weight, force_reload=True)

    if args.mode:
        eval_model_video(model, args.v_path)
    else:
        for ele in os.listdir(args.in_path):
            if ele.endswith(".txt"):
                continue
            eval_model_images(model, os.path.join(args.in_path, ele), os.path.join(args.out_path, ele))
