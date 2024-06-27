import torchvision.models as models
	resnet50 = models.resnet50(pretrained=True)
	resnet101 = models.resnet101(pretrained=True)
	resnext101 = models.resnext101_64X4D1(pretrained=True)
	efficientnet_b6 = models.efficientnet_b6(pretrained=True)
	regnet_y_128gg = models.regnet_Y_128GF_SWAG_E2E_V1(pretrained=True)
	vit_b_16 = models.vit_b_16_SWAG_E2E_V16(pretrained=True)
	vit_b_32 = models.vit_b_32(pretrained=True)
	vit_l_16 = models.vit_l_16(pretrained=True)
