# Genesis Documentation (English Version)

## Create a clean env

using python >= 3.9, install Sphinx and other dependencies

```bash
pip install -r requirements.txt 
```

## Build the documentation

```bash

# build the html
rm -rf build/; make gettext; make html-all; 
# watch the change lively
sphinx-autobuild ./source ./build/html



```
