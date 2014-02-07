#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Last modified: Wang Tai (cn.wang.tai@gmail.com)

"""
generate gif thumb
"""

__revision__ = '0.1'

import PIL
from PIL import Image


def create_thumb(origin_path, thumb_path):
    pilIm = PIL.Image.open(origin_path)
    pilIm.seek(0)

    frame = pilIm.convert('RGBA')
    white_bg = Image.new('RGB', frame.size, (255, 255, 255))
    white_bg.paste(frame, mask=frame.split()[-1])
    white_bg.thumbnail((100, 100), PIL.Image.ANTIALIAS)
    white_bg.save(thumb_path, 'JPEG', quality=80)
