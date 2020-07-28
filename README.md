# Skia ImageCat
## Simple script to render image in terminal
Uses [skia-python](https://github.com/kyamagu/skia-python) to read images and resize to fit the screen the option **--fit_to** fits the image either to the width or to the 
height of the terminal window. You can also influence that size using 
**--scale** to up/downscale the rendered image


# Examples

```python -m pyimagecat <path_to_image>```

## Show image filling the whole (current) width of the terminal window

```python -m pyimagecat <path_to_image> --fit_to w```


## Resize the image by 50% and Show it

```python -m pyimagecat <path_to_image> --scale 0.5```

## Pipe image and Show it

```cat <path_to_image> | python -m pyimagecat -```

## Windows version (cmd) (PowerShell has problematic pipe handling to use it like this)

```type <path_to_image> | python -m pyimagecat -```


# TODO
[] Make it into an installable module( add a setup.py)