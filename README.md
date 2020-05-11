Works by cutting image into 1 pixel wide strips and discarding half. Repeats the cutting process both vertically and horizontally, reducing memory used by %50 each iteration.

### Image start:
Before being cut to strips
![To be compressed](https://github.com/KoyaS/Interlacing-Compression/blob/master/images/nasaImg.jpg)

### Compressed image:
By adding the cut strips we keep the origional resolution of the image. Only after image compression we take a single copy of this compressed image and save it in its lower resolution. 
![Compressing image](https://raw.githubusercontent.com/KoyaS/Interlacing-Compression/master/compressedImage.png)
