from PIL import Image

"""This file will first break a photo into horizontal stripes and take out half. Then it will concatinate the 
    peices and break the resulting image into vertical stripes before removing half and concatinating them as
    well. This will be one iteration of compression and you may repeat this up to d//2 times where d is the 
    smaller number of height and width"""

compression_iterations = 5

im = Image.open('images/nasaImg.jpg')
print('Origional Dimensions:', im.size)

def halfRedux(im):
    width, height = im.size

    # Cuts and places image Vertically
    vert_im = Image.new('RGB', (width//2, height)) # Creates new blank image
    verticalIndicies = [(x,0,x+1,height) for x in range(0,width,2)] # Creates vertical slices
    verticallySliced = [im.crop(imgIndex) for imgIndex in verticalIndicies] # Cuts indecies from image
    for sliceNo in range(0, len(verticallySliced)):
        vert_im.paste(verticallySliced[sliceNo],(sliceNo,0)) # For loop places image slices over previous blank image

    # Cuts and places image Horizontally
    width, height = vert_im.size
    horiz_im = Image.new('RGB', (width, height//2)) # Creates new blank image
    horizontalIndicies = [(0,y,width,y+1) for y in range(0,height,2)] # Creates horizontal slices
    horizontallySliced = [vert_im.crop(imgIndex) for imgIndex in horizontalIndicies] # Cuts indecies from image
    for sliceNo in range(0, len(horizontallySliced)):
        horiz_im.paste(horizontallySliced[sliceNo],(0,sliceNo)) # For loop places image slices over previous blank image

    return(horiz_im)

newImg = halfRedux(im)
for i in range(compression_iterations):
    newImg = halfRedux(newImg)

newImg.save('interlaced', format='JPEG')
print('New Dimensions:', newImg.size)

# imagePortion = (0,0,1,200)
# cropped_im = im.crop(imagePortion)
# cropped_im.save('interlaced',format='JPEG')