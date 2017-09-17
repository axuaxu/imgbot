auto twit setup

1.check last update, using painter name in dynamodb imglist, upload image files to S3,
2.SSH to EC2, twipro\list_images1.py  param: [dir:images?, file:images?.txt]
3. backup dynamoDB, export imglist items to csv file
4. run list_dyn2.py, param: [images?.txt,]
5. twit: local
    lambda: lamb_img.py

retwit:
local: retwi-01.py

axu twit:
img_down_gre.py download from twit acc
img_mongo_gre.py  inser
lt to mongo DB
img_list_axu.py  twit
lamb_img_list_axu.py  lambda twit


list file names in directory:
dir-tree-02.py   param: [rootdir: .\images, output file: flist?.txt]


download images from twit:
pic_list.py  get image url   param:[input twit accs: xxx_list.txt, output: xxx_url.txt]
pic_down.py  download image  param:[input: xxx_url.txt,  download dir: \pics, \videos]


build web site:
img-tree-02.py   list image files    param: [dir, output file: img-?.csv]
img-html.py      write unitegallery html files     param:[input file: img-?.csv, output file: template:0-01.html]



