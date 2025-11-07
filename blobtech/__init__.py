# Source - https://stackoverflow.com/a
# Posted by Shawn Duong
# Retrieved 2025-11-06, License - CC BY-SA 4.0

import os

__all__ = []
dirname = os.path.dirname(os.path.abspath(__file__))

for f in os.listdir(dirname):
    if f != "__init__.py" and os.path.isfile("%s/%s" % (dirname, f)) and f[-3:] == ".py":
        __all__.append(f[:-3])
