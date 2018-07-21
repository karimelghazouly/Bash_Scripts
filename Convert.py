from PIL import Image
import string
import os
os.chdir('../data_256/')
dics = ['a/alley/', 'a/aqueduct/', 'b/badlands/', 'b/butte/', 'b/beach/', 'c/canal/natural/', 'c/coast/', 'c/canyon/',
      'c/corn_field/', 'c/cliff/', 'c/creek/', 'd/desert/vegetation/', 'f/farm/', 'f/field/wild/', 'f/field/cultivated/',
      'f/forest/broadleaf/', 'f/forest_path/', 'f/formal_garden/'
      ]
idx=1
for dir in dics:
    os.chdir(dir)
    images = os.listdir()
    cnt = dir.count('/')
    cnt = cnt+1
    back = '../'*cnt
    for i in images:
        ori = Image.open(str(i))
        a = ori.convert('L')
        a = a.resize((224,224),Image.NEAREST)
        ori = ori.resize((224,224),Image.NEAREST)
        a.save(back+'test-grey/'++str(idx)+'.jpg')
        ori.save(back+'test-colored/'+str(idx)+'.jpg')
        idx = idx+1
    os.chdir(back)
    os.chdir('data_256/')
