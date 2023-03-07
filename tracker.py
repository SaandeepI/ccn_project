
# Cloning the mmaction2 repository and Installing the necessary dependencies:Python 3, PyTorch, OpenCV, and MMACTION2.
!git clone https://github.com/open-mmlab/mmaction2.git
!pip install mmcv-full==1.3.14 -f https://download.openmmlab.com/mmcv/dist/cu102/torch1.9.0/index.html
!pip install mmdet==2.17.0
!pip install mmaction2

# import the modules
import torch
from mmcv import Config
from mmaction.apis import inference_recognizer, init_recognizer
import cv2

# Download the pre-trained TSN model config file from the MMACTION2 repository. 
!wget https://raw.githubusercontent.com/open-mmlab/mmaction2/master/configs/recognition/tsn/tsn_r50_1x1x8_50e_hmdb51_kinetics400_rgb.py
# Get the checkpoint file
!wget https://download.openmmlab.com/mmaction/recognition/tsn/tsn_r50_256p_1x1x8_100e_kinetics400_rgb/tsn_r50_256p_1x1x8_100e_kinetics400_rgb_20200817-883baf16.pth

config_file = '/content/mmaction2/configs/recognition/tsn/tsn_r50_1x1x8_50e_hmdb51_kinetics400_rgb.py'
checkpoint_file = 'tsn_r50_256p_1x1x8_100e_kinetics400_rgb_20200817-883baf16.pth'
cfg = Config.fromfile(config_file)
cfg.model.backbone.pretrained = None
cfg = Config.fromfile(config_file)
cfg.model.backbone.pretrained = None
cfg.data.videos_per_gpu = 1
cfg.data.workers_per_gpu = 1

#load the model using PyTorch and specify the device on which you want to run the model (CPU or GPU).
model = init_recognizer(cfg, checkpoint=checkpoint_file, device='cuda:0')





