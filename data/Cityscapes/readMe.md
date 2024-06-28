# Cityscapes dataset

Cityscapes is one of the most challenging datasets for the semantic segmentation of urban street scenes. 

It contains high-quality pixel-level annotations for 5000 images, as well as coarsely annotated 20000 images. 

The dataset contains diverse stereo video sequences with the sizes of 1024 by 2048 pixels, 
recorded during the daytime of 50 European cities visited in several months (spring, summer, and fall) 
with good or average weather conditions. 

The dataset of 5000 fine annotations is divided into three sets: 2975 for training, 500 for validation, and 1525 for testing. 

The dataset includes semantic, instance-wise, and dense pixel annotations of 30 classes grouped into eight categories. 

However, most literature uses annotations with 20 classes, 19 of which are semantic labels containing objects and stuff, 
in addition to one additional void class for do-not-care regions.
# Models
<table><tbody>
<!-- START TABLE -->
<!-- TABLE HEADER -->
<th valign="bottom">Model / Method</th>
<th valign="bottom">Baseline</th>
<th valign="bottom">mIoU</th>
<!-- TABLE BODY -->
<!-- ROW: 1 -->
<tr><td align="left">HR-Net</td>
<td align="left">HR-Net W48 + OCR</td>
<td align="center"><a href="https://github.com/hsfzxjy/models.storage/releases/download/HRNet-OCR/hrnet_ocr_cs_trainval_8227_torch11.pth">82.27</a></td>
</tr>
<!-- ROW: 2 -->
<tr><td align="left">SERNet-Former</td>
<td align="left">ResNet-50</td>
<td align="center">73.31</td>
</tr>
<!-- ROW: 3 -->
<tr><td align="left">SERNet-Former</td>
<td align="left">Efficient-ResNet_R101</td>
<td align="center">77.04</td>
<!-- ROW: 4 -->
<tr><td align="left">SERNet-Former</td>
<td align="left">Efficient-ResNet [final]</td>
<td align="center">84.83</td>
</tr>
 <!-- ROW: 5 -->
<tr><td align="left">UperNet + InternImage</td>
<td align="left">InternImage-L</td>
  <td align="center"><a href="https://huggingface.co/OpenGVLab/InternImage/resolve/main/upernet_internimage_l_512x1024_160k_cityscapes.pth">84.41</a></td>
</tr>  
 <!-- ROW: 6 -->
<tr><td align="left">UperNet + InternImage (with additional data)</td>
<td align="left">InternImage-XL</td>
  <td align="center"><a href="https://huggingface.co/OpenGVLab/InternImage/resolve/main/upernet_internimage_xl_512x1024_160k_mapillary2cityscapes.pth">86.42</a></td>
</tr>   
</tbody></table>

## Please cite

```bibtex
@inproceedings{Cordts2016CVPR,
  title={The cityscapes dataset for semantic urban scene understanding},
  author={M. Cordts and M. Omran and S. Ramos and T. Rehfeld and M. Enzweiler and R. Benenson and U. Franke and S. Roth, and B. Schiele},
  booktitle={CVPR},
  year={2016},
}

@article{Erisen2024SERNetFormer,
  title={SERNet-Former: Semantic Segmentation by Efficient Residual Network with Attention-Boosting Gates and Attention-Fusion Networks},
  author={Erişen, Serdar},
  journal={arXiv preprint arXiv:2401.15741},
  year={2024}
}
```
