# Prerequisites
## Install Dependencies
* python >= 3.8
* pytorch
* if error just install it xd
## YoloV5 & dataset
first git clone the yoloV5(https://github.com/ultralytics/yolov5) and download the dataset.
```console
$ git clone https://github.com/ultralytics/yolov5.git
```
dataset doown load: https://github.com/qhgz2013/anime-face-detector

# Data preprocessing and Training
## Data fromat
the dataset contain the foldaer "Annotations" and "JPEGImages". Using the script:
```console
$ python data_processing/resize_make_label.py
```
to make the dataset fit the yoloV5 format. In order to execute it, you need to change the path in the script:
```python
Ann_path = # path to Annotations
Ani_path = # path to JPEGImages
img_path = # path to resized images, output path
lb_path = # path to labels, output path
imageSize = 480     # image size
```
## Train yoloV5
In order to train yoloV5, you can see the tutorials: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data

I make the .yml file for this project, just change the path to folder.
```console
$ mv dataset.yml yolov5
```
train yolov5 with pretrain model.
```console
$ cd yolov5
$ python train.py --img 480 --batch 32 --epochs 50 --data dataset.yaml --weights yolov5x.pt --workers 12
```
I provide the weight of 50 epochs in the folder "weight_50eps", the link to download: coming soon.

# Run example
## Run image and video
you can run the images in a folder.
Mode 0 is for detect images, you need to provide the image folder path and output path.
Mode 1 is for detect video, you need to provide the video path.
```console
$ python main.py --mode 0 --in_path testcases --outpath result_example --weight weight_50eps/best.pt

$ python main.py --mode 1 --v_path video.mp4 --weight weight_50eps/best.pt
```
## Web crawler: Images
it will download the images for two page in the web: https://safebooru.org/
```console
$ python collectData.py
```
