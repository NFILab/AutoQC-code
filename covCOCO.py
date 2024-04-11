import json
import glob
import cv2 as cv
import os
import numpy as np
# import torch
import matplotlib.pyplot as plt
import cv2
import os
import matplotlib
 
class tococo(object):
    def __init__(self, json_paths, save_path, only_box= True):
        self.images = []
        self.categories = []
        self.annotations = []
    
        self.json_paths = json_paths
        self.save_path = save_path
#         self.label_path = label_path
        # 
        self.class_ids = {'cell': 0, 'capillary':1}
#         self.class_id = 1
        self.coco = {}
         
        self.box_flag = only_box
        
    def npz_to_coco(self):
        annid = 0
        for num, jpg_path in enumerate(self.json_paths):
            label_json =jpg_path
            with open(label_json, 'r') as f:
                    data = json.load(f)
            imgname = data['info']['name'].split('.')[0] #jpg_path.split('\\')[-1].split('.')[0]
#             img = cv.imread(jpg_path)
#             jsonf = open(self.label_path + imgname + '.json').read()  # 
#             labels = json.loads(jsonf)
            h, w = data['info']['width'],data['info']['height']
            self.images.append(self.get_images(imgname, h, w, num))
            labels = data['objects']
            for label in labels:
                # self.categories.append(self.get_categories(label['class'], self.class_id))
#                 px,py,pw,ph=label['bbox']
                x1, y1, x2, y2=label['bbox']
                box=[x1,y1,x2-x1,y2-y1]
#                 print(box)
                poly = np.array(label['segmentation']).reshape(-1)
                self.annotations.append(self.get_annotations(box, num, annid, label['category'],poly))
                annid = annid + 1
 
        self.coco["images"] = self.images
        
        self.categories.append(self.get_categories('cell', 0))
        self.categories.append(self.get_categories('capillary',1))
        self.coco["categories"] = self.categories
        self.coco["annotations"] = self.annotations
        # print(self.coco)
 
    def get_images(self, filename, height, width, image_id):
        image = {}
        image["height"] = height
        image['width'] = width
        image["id"] = image_id
        # 
        image["file_name"] = filename+'.jpg'
        # print(image)
        return image
 
    def get_categories(self, name, class_id):
        category = {}
        if name =='cell':
            category["supercategory"] = 'cell'
        else:
            category["supercategory"] = 'capillary'
        # id=0
        category['id'] = class_id
        # name=1
        category['name'] = name
        # print(category)
        return category
 
    def get_annotations(self, box, image_id, ann_id, calss_name, poly):
        annotation = {}
        w, h = box[2], box[3]
        area = w * h
        # print(list(poly))
        annotation['id'] = ann_id
        annotation['image_id'] = image_id
        annotation['category_id'] = self.class_ids[calss_name]
        if self.box_flag== False:
            annotation['segmentation'] =[[ i.astype(float) for i in poly  ]] #[[ ]] (for  det) #  [[ i.astype(float) for i in poly  ]]
        else:
            annotation['segmentation'] = [ [] ]
        annotation['iscrowd'] = 0
        # 
        annotation['area'] = float(area)
        annotation['bbox'] = box
        
        # category_id=0
        
        # 
        
        # print(annotation)
        return annotation
 
    def save_json(self):
        self.npz_to_coco()
        label_dic = self.coco
        # print(label_dic)
        instances_train2017 = json.dumps(label_dic)
        if self.box_flag== False:
            f = open(os.path.join(self.save_path+'ground.json'), 'w')
        else:
            f = open(os.path.join(self.save_path+'ground_box.json'), 'w')
        f.write(instances_train2017)
        f.close()



        
import json
import glob
import cv2 as cv
import os
 
 
class tococo_test(object):
    def __init__(self, json_paths, save_path):
        self.images = []
        self.categories = []
        self.annotations = []
        
        self.json_paths = json_paths
        self.save_path = save_path
#         self.label_path = label_path
        
        self.class_ids = {'cell': 0, 'capillary':1}
#         self.class_id = 1
        self.coco = {}
 
    def npz_to_coco(self):
        annid = 0
        self.categories.append(self.get_categories('cell', 0))
        self.categories.append(self.get_categories('capillary',1))
        self.coco["categories"] = self.categories
        for num, jpg_path in enumerate(self.json_paths):
            label_json =jpg_path
            with open(label_json, 'r') as f:
                    data = json.load(f)
            imgname = data['info']['name'].split('.')[0] #jpg_path.split('\\')[-1].split('.')[0]
#             img = cv.imread(jpg_path)
#             jsonf = open(self.label_path + imgname + '.json').read()  # 
#             labels = json.loads(jsonf)
            h, w = data['info']['width'],data['info']['height']
            self.images.append(self.get_images(imgname, h, w, num))
            labels = data['objects']
            for label in labels:
                label_dict = {}
                # self.categories.append(self.get_categories(label['class'], self.class_id))
#                 px,py,pw,ph=label['bbox']
                x1, y1, x2, y2=label['bbox']
                box=[x1,y1,x2-x1,y2-y1]
#                 print(box)
                poly = np.array(label['segmentation']).reshape(-1)
                score = label['score']
                label_dict = self.get_annotations(box, num, annid, label['category'],poly,score)
                
                # label_dict["categories"] = [self.get_categories(label['category'], None)]
            
                self.annotations.append(label_dict)
                annid = annid + 1
 
        self.coco["images"] = self.images
        
        
        self.coco["annotations"] = self.annotations
        # print(self.coco)
 
    def get_images(self, filename, height, width, image_id):
        image = {}
        image["height"] = height
        image['width'] = width
        image["id"] = image_id
        # 
        image["file_name"] = filename+'.jpg'
        # print(image)
        return image
 
    def get_categories(self, name, class_id):
        category = {}
        if name =='cell':
            category["supercategory"] = 'cell'
            category['id'] = 0
        else:
            category["supercategory"] = 'capillary'
            category['id'] = 1
        # id=0
        # category['id'] = class_id 
        # name=1
        category['name'] = name
        # print(category)
        return category
 
    def get_annotations(self, box, image_id, ann_id, calss_name, poly,score):
        annotation = {}
        w, h = box[2], box[3]
        area = w * h
        # print(list(poly))
        
        annotation['id'] = ann_id
        annotation['image_id'] = image_id
        annotation['category_id'] = self.class_ids[calss_name]
        annotation['segmentation'] =[[ i.astype(float) for i in poly  ]] #[[ ]] #  [[ i.astype(float) for i in poly  ]]
        annotation['iscrowd'] = 0
        #
        annotation['area'] = float(area)
        annotation['bbox'] = box
        annotation['score'] = score
        
        # annotation['segmentation'] =[[ i.astype(float) for i in poly  ]] #[[ ]] #  [[ i.astype(float) for i in poly  ]]
        annotation['iscrowd'] = 0
        # 
      
       
        # category_id=0
     
        # print(annotation)
        return annotation
 
    def save_json(self):
        self.npz_to_coco()
        label_dic = self.coco["annotations"] #self.coco
        # print(label_dic)
        instances_train2017 = json.dumps(label_dic)
        # nstances_train2017.json
        f = open(os.path.join(self.save_path+'pred.json'), 'w')
        f.write(instances_train2017)
        f.close()
 