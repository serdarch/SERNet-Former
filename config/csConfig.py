# @package training
# Those arguments defines the training hyper-parameters
epochs: 80
num_workers: 1
batch_size: 1
shuffle: True
cuda: 0
precompute_multi_scale: False # Compute multiscate features on cpu for faster training / inference
optim:
	base_lr: 0.0005
	optimizer:
	class: SGD
	params:
	lr: ${training.optim.base_lr}
	lr_scheduler: ${lr_scheduler}
	bn_scheduler:
	bn_policy: "step_decay"
	params: 
	bn_momentum: 0.9
	bn_decay: 0.95
	decay_step: 10
	bn_clip: 1
weight_name: "latest" # can be named/changed according to the shared model weights
enable_cudnn: False
checkpoint_dir: "..."
