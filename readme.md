# Quantification of cardiac capillarization in single-immunostained myocardial slices using weakly supervised instance segmentation




## How to run
- Step 1. convert the annotation format to COCO format by ``` label_to_coco.ipynb```.

- Step 2. Use roboflow to prepare the augmented data to YOLOv8. We choose random clock rotation and mosic.


- Step 3. Train detection model by ```train_det.ipynb```.

- Step 4. use ```prediction.ipynb``` to perform the segmentation for autoQC, only-BBOX, only-points, and only-SAM.

- Step 5. For comparison of end-to-end model, use ```train_seg.ipynb``` for training and prediction of end-to-end model (yolov8).


- Step 6. use ```final_eval.ipynb``` for evaluation.



For better understand how to train YOLO model, please refer to: [https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/]
We are using ```yolov8x.pt```.

'/home/{user_id}/.config/Ultralytics/settings.yaml'
