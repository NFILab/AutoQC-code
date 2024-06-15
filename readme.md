# Quantification of cardiac capillarization in basement-membrane-immunostained myocardial slices using Segment Anything Model (SAM)

![test](https://github.com/XiwenChen-Clemson/AutoQC/blob/main/fIGS/fig3.png)


## Code description
- 1. Prepare a training dataset with bounding box annotations. Converting annotations to COCO format was handled by ```label_to_coco.ipynb```.

- 2. Roboflow was used to prepare the augmented data. In this work, we chose random clock rotation and mosic. Random rotation was utilized in three directions: 90-degree clockwise, 90-degree counter-clockwise, and 90-degree upside-down. Mosaic augmentation combined four images into a single image, by placing each image into a quadrant of the new image. 

- 3. The training of the object detector (YOLOv8-based) in the prompt-learning block was handled by ```train_det.ipynb```. AutoQC (enhanced prompts), BB-SAM (prompted by bounding boxes), P-SAM (prompted by binary-labeled key points), and SAM-Only (without prompt engineering) shared this trained object detecor.

- 4. ```prediction.ipynb``` reads an image from a user-defined path, predicts bounding boxes within the image, generats prompts, and then prompts SAM to output masks with categories.

- 5. In this work, YOLOv8-Seg was used as an end-to-end instance segmentation model for comparison with AutoQC and SAM-Only. YOLOv8-Seg's training and prediction tasks were handled by ```train_seg.ipynb```.

- 6. The perfomance evaluation of instance segmentation was handled by ```final_eval.ipynb```.


## YOLO
Details about how to train a YOLO model can be found at: [https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/]
We are using ```yolov8x.pt```.


## Segment Anything Model (SAM)
Details about how to setup SAM can be found in FacebookResearch's repository:
[https://github.com/facebookresearch/segment-anything]

## Demo Results
![test](https://github.com/XiwenChen-Clemson/AutoQC/blob/main/fIGS/fig1.png)
![test](https://github.com/XiwenChen-Clemson/AutoQC/blob/main/fIGS/fig2.png)
