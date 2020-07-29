# Skia ImageCat
## Simple script to show images in your terminal
Uses [skia-python](https://github.com/kyamagu/skia-python) to read images and resize to fit the screen the option **--fit_to** fits the image either to the width or to the 
height of the terminal window (only downscales larger images). 
You can also influence that size using **--scale** to up/downscale the rendered image

Module is *pip installable*, after you clone the repo you can run  ```pip install . ``` inside the repo directory to install it so it gets added to the global python scripts path.

# Examples

```
 pyimagecat path\to\image.png
```

## Show image filling the whole (current) width of the terminal window

```
 pyimagecat path\to\image.png --fit_to w
```


## Resize the image by 50% and Show it

```
 pyimagecat path\to\image.png --scale 0.5
```

## Pipe image and Show it

```
cat path\to\image.png |  pyimagecat -
```

## Windows version (cmd) (PowerShell has problematic pipe handling to use it like this)

```
type path\to\image.png |  pyimagecat -
```

