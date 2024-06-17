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
