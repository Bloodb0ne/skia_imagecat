from setuptools import setup, find_packages, find_namespace_packages

setup(
	name="pyimagecat",
	version="0.0.1",
	url="https://github.com/Bloodb0ne/skia_imagecat/",
	author="bloodb0ne",
	author_email="emilian.branzelov@gmail.com",
	description=("CLI tool for showing images in the terminal."),
	py_modules=['pyimagecat'],
	entry_points={
		'console_scripts': [
			'pyimagecat = pyimagecat:print_image'
		]
	},
	install_requires=[
		"skia-python >= 85.0",
		"numpy"
	]
)
