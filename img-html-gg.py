incsv = "img-01.csv"
fin = open(incsv,'r')
outhtml = "img-html-gg-01.html"
fout = open(outhtml,'w')
for line in fin:
	#print line
	narr = line.split('\\')
	#print len(narr)
	if  len(narr)>2:
         painter = narr[2]
         name = painter.split('-')
         lastname = name[-1]
         fullname = painter.replace('-','')
         pic = narr[3]
         pic=  pic.split('.')[0]
         painter = painter.replace('-',' ')
         pic = pic.replace('-',' ')
         #print (painter)
         #print (pic)
         status =  painter+'\n'+pic
         status = status.title()
        #hashstr = '\n#art '+'#painting '+'#'+fullname+' '+'#'+lastname
         status = status
         desc = painter+' '+pic
         desc = desc.title()
         imgsrc = narr[2]+'/'+narr[3]
         imgsrc = "images/"+imgsrc.replace('\n','')
         
         #items = [<li><div data-alt="img03" 
         #       data-description="<h3>Sky high</h3>" 
         #       data-max-width="1800" 
         #       data-max-height="1350">
         #       <div data-src="images/xxxlarge/3.jpg" data-min-width="1300"></div>
         #       <div data-src="images/xxlarge/3.jpg" data-min-width="1000"></div>
         #       <div data-src="images/xlarge/3.jpg" data-min-width="700"></div>
         #       <div data-src="images/large/3.jpg" data-min-width="300"></div>
         #       <div data-src="images/medium/3.jpg" data-min-width="200"></div>
         #       <div data-src="images/small/3.jpg" data-min-width="140">
         #       </div><div data-src="images/xsmall/3.jpg"></div>
         #       <noscript><img src="images/xsmall/3.jpg" alt="img03"/></noscript>
         #       </div></li>

         #print imgsrc
         imgstr = '<li><div  data-alt="img03" data-description="<h3>'+desc \
                + '</h3>" data-max-width="1800" data-max-height="1350"><div data-src="' \
                +imgsrc+'" data-min-width="1300"></div><div data-src="' \
                +imgsrc+'" data-min-width="1000"></div><div data-src="' \
                +imgsrc+'" data-min-width="700"></div><div data-src="'  \
                +imgsrc+'" data-min-width="300"></div><div data-src="'  \
                +imgsrc+'" data-min-width="200"></div><div data-src="'  \
                +imgsrc+'" data-min-width="140"></div><div data-src="'  \
                +imgsrc+'"></div><div data-src="'+imgsrc+'"></div><noscript><img src="' \
                +imgsrc+'" alt="img03"/></noscript></div></li>'
               
         print imgstr
         #<img alt="Image 2 Title" 
	     #     src="thumbs/greece.jpg"
		 #     data-image="images/greece.jpg"
	     #     data-description="Image 2 Description">
	     #print status