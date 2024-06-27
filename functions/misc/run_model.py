import torch
import torchvision
from torchvision import transforms

import os
import numpy as np
import cv2
from PIL import Image


model = torchvision.models.segmentation.deeplabv3_resnet101(weights = "DEFAULT")

model.eval()

transform = transforms.Compose([transforms.ToTensor() , transforms.Normalize(mean = [0.485 , 0.456 , 0.406] , std = [0.229 , 0.224 , 0.225])])

img = Image.open('_Your_image_.jpg')


pred = model(transform(img)[None , ...])

output = pred["out"].squeeze().argmax(0)
