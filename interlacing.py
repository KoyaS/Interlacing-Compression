from PIL import Image

"""This program runs a compression algorithm on given input image. This is lossy compression.
    The programwill first break a photo into horizontal stripes and take out half. Then it will concatinate the 
    peices and break the resulting image into vertical stripes before removing half and concatinating them as well.

    NOTE: this is only true if keep_origional_dimensions is True. Otherwise the image's dimensions will be halved
    for each iteration in compression_iterations"""

compression_iterations = 10
keep_origional_dimensions = True
img_source = 'images/nasaImg.jpg'

def halfRedux(im):
    width, height = im.size
    oWidth, oHeight = width, height # Keeps the origional resolution in memory
    orig_dimens = vert_im = Image.new('RGB', (oWidth, oHeight)) # Will be used to keep origional resolution of image intact

    # Cuts and places image Vertically (||)
    vert_im = Image.new('RGB', (width//2, height)) # Creates new blank image
    verticalIndicies = [(x,0,x+1,height) for x in range(0,width,2)] # Creates vertical slices
    verticallySliced = [im.crop(imgIndex) for imgIndex in verticalIndicies] # Cuts indecies from image
    for sliceNo in range(0, len(verticallySliced)):
        vert_im.paste(verticallySliced[sliceNo],(sliceNo,0)) # For loop places image slices over previous blank image

    # Cuts and places image Horizontally (=)
    width, height = vert_im.size
    horiz_im = Image.new('RGB', (width, height//2)) # Creates new blank image
    horizontalIndicies = [(0,y,width,y+1) for y in range(0,height,2)] # Creates horizontal slices
    horizontallySliced = [vert_im.crop(imgIndex) for imgIndex in horizontalIndicies] # Cuts indecies from image
    for sliceNo in range(0, len(horizontallySliced)):
        horiz_im.paste(horizontallySliced[sliceNo],(0,sliceNo)) # For loop places image slices over previous blank image
    
    orig_dimens.paste(horiz_im,(0,0)),          orig_dimens.paste(horiz_im,(oWidth//2,0))             # Pastes images
    orig_dimens.paste(horiz_im,(0,oHeight//2)), orig_dimens.paste(horiz_im,(oWidth//2,oHeight//2))    # in a 2x2 grid

    return(horiz_im, orig_dimens)

# Start Compression
im = Image.open(img_source)
print('Origional Dimensions:', im.size)

newImg, orig_dimens = halfRedux(im)
for i in range(1,compression_iterations):
    if keep_origional_dimensions:
        newImg, orig_dimens = halfRedux(orig_dimens)
    else:
        newImg, orig_dimens = halfRedux(newImg)

if keep_origional_dimensions:
    orig_dimens.save('interlaced', format='JPEG')
else:
    newImg.save('interlaced', format='JPEG')
    print('New Dimensions:', newImg.size)