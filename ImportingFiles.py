#importing files from directory on drive
import shutil
import os
#directory names variables
original_dir='/home/kochel/Pobrane/train' 
base_dir='/home/kochel/Pobrane/small'
train_dir = os.path.join(base_dir, 'train')
validation_dir=os.path.join(base_dir, 'validation')
test_dir=os.path.join(base_dir, 'test')

train_cats_dir=os.path.join(train_dir,'cats')
train_dogs_dir=os.path.join(train_dir,'dogs')
validation_cats_dir=os.path.join(validation_dir,'cats')
validation_dogs_dir=os.path.join(validation_dir,'dogs')
test_cats_dir=os.path.join(test_dir,'cats')
test_dogs_dir=os.path.join(test_dir,'dogs')

os.mkdir(base_dir)


os.mkdir(train_dir)


os.mkdir(validation_dir)


os.mkdir(test_dir)


os.mkdir(train_cats_dir)
os.mkdir(train_dogs_dir)
os.mkdir(validation_cats_dir)
os.mkdir(validation_dogs_dir)
os.mkdir(test_cats_dir)
os.mkdir(test_dogs_dir)

fnames = ['cat.{}.jpg'.format(i) for i in range(7500)]
for fname in fnames:
    src = os.path.join(original_dir, fname)
    dsc = os.path.join(train_cats_dir, fname)
    shutil.copyfile(src,dsc)
fnames = ['dog.{}.jpg'.format(i) for i in range(7500)]
for fname in fnames:
    src = os.path.join(original_dir, fname)
    dsc = os.path.join(train_dogs_dir, fname)
    shutil.copyfile(src,dsc)



fnames = ['cat.{}.jpg'.format(i) for i in range(7500,10000)]
for fname in fnames:
    src = os.path.join(original_dir, fname)
    dsc = os.path.join(validation_cats_dir, fname)
    shutil.copyfile(src,dsc)
fnames = ['dog.{}.jpg'.format(i) for i in range(7500,10000)]
for fname in fnames:
    src = os.path.join(original_dir, fname)
    dsc = os.path.join(validation_dogs_dir, fname)
    shutil.copyfile(src,dsc)


fnames = ['cat.{}.jpg'.format(i) for i in range(10000,12500)]
for fname in fnames:
    src = os.path.join(original_dir, fname)
    dsc = os.path.join(test_cats_dir, fname)
    shutil.copyfile(src,dsc)
fnames = ['dog.{}.jpg'.format(i) for i in range(10000,12500)]
for fname in fnames:
    src = os.path.join(original_dir, fname)
    dsc = os.path.join(test_dogs_dir, fname)
    shutil.copyfile(src,dsc)





