from PIL import Image
import string
import os
print (os.getcwd())
letters = list(string.ascii_lowercase)
os.chdir('data_256/')
idx=1
for l in letters:
    os.chdir(l+'/')
    dir_list = os.listdir()
    for fol in dir_list:
        os.chdir(fol + '/')
        images=os.listdir()
        for i in images:
            stri=str(i)
            f=stri.find('jpg')
            if (f==-1):
                continue
            ori=Image.open(str(i))
            a=ori.convert('L')
            a=a.resize((224,224),Image.NEAREST)
            a.save('../../../test-grey/'+str(idx)+'.jpg')
            ori.save('../../../test-colored/'+str(idx)+'.jpg')
            idx=idx+1
        os.chdir('../')
    os.chdir('../')
