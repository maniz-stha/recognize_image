# Recognize Images #
## Introduction ##
Have you ever been to some office picnics or some family functions or some events and later get a ton of images from the function? Images of all the people you know and don't know or don't care about. When all you wanted were some few good images of your own or your loved ones. But then you have to manually go over all the images to find your images.

So to remove this pain, I created this script to automatically select the images of the selected person and copy them to one location, using face recognition library.

All you got to do is copy all the images to the **unknown_images** folder, add a good image of your own or person whose image you want to copy to the **known_images** folder and run the script. The matched images are then copied to the **matched_images** folder.

From the terminal, just run the command

```python
python copy_image.py
```

### Library Used ###
https://github.com/ageitgey/face_recognition