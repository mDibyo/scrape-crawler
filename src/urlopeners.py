#!/usr/bin/env python
from urllib import FancyURLopener


__author__ = "Dibyo Majumdar"
__email__ = "dibyo.majumdar@gmail.com"


URL_OPENER = FancyURLopener()


class DesktopURLOpener(FancyURLopener):
    version = 'Mozilla/5.0'
