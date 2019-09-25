# Dragonbones Tweaks

# Instalation
* Install `pipenv` in your machine if doesn't have it
```shell
$ pip install pipenv
```
* Type inside project folder:
```
$ pipenv shell
```

# Commands
There is only 3 parameters to run the script, try `--help` to check then:
```
$ python dragon_tweaks.py --help
```

# Image Exporter Sorting
- Easily order exported assets to help import on other softwares
- Order both `png` and `json` files from exportation
- Creates a copy to keep original data untouched

```
$ python dragon_tweaks.py --anim-export-folder=[PATH_TO_FOLDER_WITH_JSON_AND_PNG]
```
This will create a folder called `output` in the project root containing a copy to the animation folder, now with sorted files and properly named with the animation tag.

# Create Gif
- To create a Gif from sorted files, just insert `--gif` argument and adjust `--gif-fps` which is 30 by default.

```
$ python dragon_tweaks.py --anim-export-folder=[PATH_TO_FOLDER_WITH_JSON_AND_PNG] --gif --gif-fps=30
```

The generated gif will be located at output folder with properly animation folder name.

## Thanks,

Leave a start if usefull and feel free to fork it.
And also, open an issue for any suggestion or problem.
