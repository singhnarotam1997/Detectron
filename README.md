# Detectron

Detectron is Facebook AI Research's software system that implements state-of-the-art object detection algorithms, including [Mask R-CNN](https://arxiv.org/abs/1703.06870). It is written in Python and powered by the [Caffe2](https://github.com/caffe2/caffe2) deep learning framework.

The detectron that comes with DensePose is suitable for python2 so this is for the users who want to run DensePose built on python3.
Also, the original detectron repo at "https://github.com/facebookresearch/Detectron.git" does not help a DensePose model to create IUV image. Using this detectron, you can perform inference on a model with BODY_UV parameter as ON like in DensePose_ResNet50_FPN_s1x-e2e or DensePose_ResNet101_FPN_s1x-e2e. These pretrained weights can be found on "https://dl.fbaipublicfiles.com/densepose/" server.

To build the detectron just do "python setup.py build_ext install" 

If you are having issues in builing Caffe2 with detectron support, check Gianni Rosa's website. Particularly, http://gianni.rosagallina.com/en/posts/2018/10/04/caffe2-gpu-windows-1.html and http://gianni.rosagallina.com/en/posts/2018/10/09/caffe2-gpu-windows-2.html should be helpful. 
