*Game 15 !*
=================

Application's exe-file is into 'dist' catalog.

## Collecting of images:
*src/resources/res.py* - output file
*src/resources/res.qrc* - file with img paths
Command for collecting images:
`pyrcc5 -o src/resources/res.py src/resources/res.qrc`

## Convert from .py to .exe:
`pyinstaller -wF "src/main.py"  --icon="static/img/15.ico"`

