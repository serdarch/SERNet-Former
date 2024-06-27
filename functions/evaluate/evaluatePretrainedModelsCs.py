import torch
import torchvision
from torchvision import transforms

import os
import numpy as np
import cv2
from PIL import Image

def run(image_name):
    os.environ["TORCH_HOME"] = "...Select the path that your model is downloaded..."

    model = torchvision.models.segmentation.deeplabv3_resnet101(weights = "DEFAULT")

    model.eval()

    transform = transforms.Compose([
        transforms.ToTensor() ,
        transforms.Normalize(mean = [0.485 , 0.456 , 0.406] , std = [0.229 , 0.224 , 0.225])
    ])

    img = Image.open('_Your_image_.jpg')

    with torch.no_grad():
        pred = model(transform(img)[None , ...])
    output = pred["out"].squeeze().argmax(0)
    names = ["road" , "sidewalk" , "building" , "wall" , "fence" , "pole" , "traffic_light" , "traffic_sign" , "vegetation" ,
             "terrain" , "sky" , "person" , "rider" , "car" , "truck" , "bus" , "train" , "motocycle" , "bicycle"]

    all_objects = []
    all_segments = []

    for i in range(output.unique().shape[0] - 1):
        num = output.unique()[i + 1]
        all_objects.append(names[num - 1])

        temp = torch.zeros_like(output)
        temp[output == num] = 255

        mask = temp.numpy().astype("uint8")
        real = cv2.imread(image_name)

        real[mask != 255] = (255 , 255 , 255)
        all_segments.append(real.copy())

    return all_objects , all_segments







