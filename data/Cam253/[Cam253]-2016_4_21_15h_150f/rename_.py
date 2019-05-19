import os 

image_dir = 'data/Cam253/[Cam253]-2016_4_21_15h_150f'
image_list = os.listdir(image_dir)
for image in image_list:
    if(image.endswith('.jpg')):
        src = image_dir +'/' +  image
        dest = src.replace("/000","/0")
        print(image)
        os.rename(src,dest)


