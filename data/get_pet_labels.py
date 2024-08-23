#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Ali Hussain Abu Ali
# DATE CREATED: 23/08/2024                                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based on the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    The labels should be in all lower case letters, with leading and trailing 
    whitespace characters stripped, and with words separated by spaces.
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
                 
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in the directory
    in_files = listdir(image_dir)
    
    # Creates an empty dictionary to hold the results (pet labels, etc.)
    results_dic = dict()
   
    # Process each file in the directory to extract the pet label
    for idx in range(0, len(in_files), 1):
       
        # Skips file if it starts with . (like .DS_Store of Mac OSX) because it 
        # isn't a pet image file
        if in_files[idx][0] != ".":
           
            # Step 1: Convert the filename to lowercase
            filename = in_files[idx].lower()

            # Step 2: Split the filename into parts using underscores
            word_list_pet_image = filename.split('_')

            # Step 3: Filter out non-alphabetic parts and build the pet label
            pet_name = ""
            for word in word_list_pet_image:
                if word.isalpha():  # Keep only alphabetic words
                    pet_name += word + " "
            
            # Step 4: Strip any leading or trailing whitespace from the pet label
            pet_name = pet_name.strip()

            # Step 5: Add the filename and pet label to the dictionary
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_name]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])
 
    # Return the results dictionary
    return results_dic
