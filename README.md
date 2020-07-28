# Skia ImageCat
## Simple script to render image in terminal
Uses [skia-python](https://github.com/kyamagu/skia-python) to read images and resize to fit the screen the option **--fit_to** fits the image either to the width or to the 
height of the terminal window. You can also influence that size using 
**--scale** to up/downscale the rendered image


# Examples

```
python -m pyimagecat path\to\image.png
```

## Show image filling the whole (current) width of the terminal window

```
python -m pyimagecat path\to\image.png --fit_to w
```


## Resize the image by 50% and Show it

```
python -m pyimagecat path\to\image.png --scale 0.5
```

## Pipe image and Show it

```
cat path\to\image.png | python -m pyimagecat -
```

## Windows version (cmd) (PowerShell has problematic pipe handling to use it like this)

```
type path\to\image.png | python -m pyimagecat -
```


# TODO

- [ ] Make it into an installable module( add a setup.py)
