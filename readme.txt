auto twit setup

1.check last update, using painter name in dynamodb imglist, upload image files to S3,
2.SSH to EC2, twipro\list_images1.py  param: [dir:images?, file:images?.txt]
3. backup dynamoDB, export imglist items to csv file
4. run list_dyn2.py, param: [images?.txt,]


retwit:
local: retwi-01.py


list file names in directory:
dir-tree-02.py   param: [rootdir: .\images, output file: flist?.txt]
