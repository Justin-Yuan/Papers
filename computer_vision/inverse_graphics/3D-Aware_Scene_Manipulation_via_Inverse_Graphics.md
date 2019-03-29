# 3D-Aware Scene Manipulation via Inverse Graphics
[link](http://papers.nips.cc/paper/7459-3d-aware-scene-manipulation-via-inverse-graphics.pdf)

**very similar idea**

## Intro 

- interpreable expressive, disentangled (semantics, geometry, appearance) scene representation, contaisn comprehensive structural and textural information for each object
- scene encoder for inverse graphics, decoder = differentiable shape renderer + neural texture generator
- 3D scene de-rendering networks (3D-SDN)

## Modeling 

- semantic branch -> Dilated Residual Networks (DRN) for semantic segmentation 
- geometric branch -> Mask-RCNN for object proposal generation, 8 object meshes as car CAD models from ShapeNet 
- textural branch 
- VGG network as feature extractor 

## Evaluation 

- evaluated on Virtual KITTI and Cityscapes 
- built **Virtual KITTI Image Editing Benchmark**
- learned representations can be useful for image reasoning, captining, analogy-making 

## Future Work 

- handle uncommon object appearance and pose 
- deal with deformable shapes, e.g. human bodies 