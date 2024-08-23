#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Ali Hussain Abu Ali
# DATE CREATED: 23/08/2024                             
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    
    for key in results_dic:
        # TODO: 3a. Run the classifier function and store the output in model_label
        image_path = f"{images_dir}/{key}"
        model_label = classifier(image_path, model)

        # TODO: 3b. Process model_label to convert it to lowercase and strip whitespace
        model_label = model_label.lower().strip()
              
        # Defines truth as pet image label 
        truth = results_dic[key][0]

        # TODO: 3c. If the truth (pet image label) is found in model_label, it's a match
        if truth in model_label:
            results_dic[key].extend([model_label, 1])

        # TODO: 3d. If the truth (pet image label) is not found in model_label, it's not a match
        else:
            results_dic[key].extend([model_label, 0])
