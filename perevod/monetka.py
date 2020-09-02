
exec import os
import warnings
import io

from PIL import Image
def convert(img, renderIRC=False, cutoff=150, size=1.3, invert=False, alphaColor=(0,0,0)):
 i = Image.open(img)
 WIDTH = int(90*size)
 HIGHT = int(40*size)
 s = i.size
 if s[0]==0 or s[1]==0 or (float(s[0])/float(WIDTH))==0 or (float(s[1])/float(HIGHT))==0:
  return []
 ns = (WIDTH,int(s[1]/(float(s[0])/float(WIDTH))))
 if ns[1]>HIGHT:
  ns = (int(s[0]/(float(s[1])/float(HIGHT))),HIGHT)
 i2 = i.resize(ns)
 bimg = []
 for r in range(0,i2.size[1],4):
  line = u''
  lastCol = -1
  for c in range(0,i2.size[0],2):
   val = 0
   i = 0
   cavg = [0,0,0]
   pc = 0
   for ci in range(0,4):
    for ri in range(0,3 if ci<2 else 1):
     if ci>=2:
      ci-=2
      ri=3
     if c+ci<i2.size[0] and r+ri<i2.size[1]:
      p = i2.getpixel((c+ci,r+ri))
      alpha = p[3] if len(p)>3 else 1
      if invert and alpha>0:
       p = map(lambda x: 255-x, p)
      elif alpha==0:
       p = alphaColor
     else:
      p = (0,0,0)
     luma = (0.2126*float(p[0]) + 0.7152*float(p[1]) + 0.0722*float(p[2]))
     pv = sum(p[:3])
     if luma > cutoff:
      val+=1<<i
      cavg = map(sum,zip(cavg,p))
      pc+=1
     i += 1
   line += chr(0x2800+val)
  bimg.append(line)
 return bimg
 
im = io.BytesIO(await client.download_file(reply, bytes))
await message.edit("{}".format("\n".join(convert(im))))
