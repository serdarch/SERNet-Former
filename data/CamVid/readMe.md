# CamVid Dataset

The Cambridge-driving Labelled Video Database (CamVid) is one of the first scene understanding databases, 
and it is based on the motion-based video collections of driving scenes recorded for semantic segmentation of object classes. 

This database contains 701 frames with sizes of 720 by 960 pixels that were captured in five video sequences, 
shot via the fixed-position CCTV-style cameras mounted on a car. The densely annotated images were manually 
generated through 32 classes and merged into 11 classes later. 

The original dataset is divided into 367 training, 101 validation, and 233 test images, as most literature practiced. 

## Model metrics

<table><tbody>
<!-- START TABLE -->
<!-- TABLE HEADER -->
<th valign="bottom">Model</th>
<th valign="bottom">Metrics File</th>
<!-- TABLE BODY -->
<!-- ROW: 1 -->
<tr><td align="left">SERNet-Former [checkpoint]</td>
<td align="center"><a href="https://huggingface.co/spaces/serdarerisen/SERNet-Former/blob/main/CamVid_NetworkMetrics_Checkpoint.mat">download</a></td>
</tr>
<!-- ROW: 2 -->
<tr><td align="left">SERNet-Former [final]</td>
<td align="center"><a href="https://huggingface.co/spaces/serdarerisen/SERNet-Former/blob/main/CamVid_NetworkMetrics_Final.mat">download</a></td>
</tr>
</tbody></table>


## Please cite

```bibtex
@article{Brostow2019,
  title={Semantic object classes in video: A high-definition ground truth database},
  author={G. J. Brostow and J. Fauqueur and R. Cipolla},
  journal={Pattern Recognition Letters},
  volume=90
  pages=119-133
  year={2019}
}

@article{Erisen2024SERNetFormer,
  title={SERNet-Former: Semantic Segmentation by Efficient Residual Network with Attention-Boosting Gates and Attention-Fusion Networks},
  author={Erişen, Serdar},
  journal={arXiv preprint arXiv:2401.15741},
  year={2024}
}
```
