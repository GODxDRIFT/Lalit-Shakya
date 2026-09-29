"""Run in the site folder:  pip install pillow  &&  python optimize_images.py
Recompresses every .jpg/.jpeg/.png preview (max width 1200px) in place, same file names."""
import glob, os
from PIL import Image
for f in glob.glob('*.jpg')+glob.glob('*.jpeg'):
    b=os.path.getsize(f); im=Image.open(f).convert('RGB')
    if im.width>1200: im=im.resize((1200,round(im.height*1200/im.width)),Image.LANCZOS)
    im.save(f,'JPEG',quality=78,optimize=True,progressive=True)
    print(f, b//1024,'KB ->',os.path.getsize(f)//1024,'KB')
