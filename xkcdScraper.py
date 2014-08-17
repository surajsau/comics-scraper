from bs4 import BeautifulSoup
import os
import urllib2

dirname = "/home/surajsau/pstuff/imgs"
def saveimg(url, filename):
    try:
        pic = urllib2.urlopen(url).read()
        filepath = os.path.join(dirname,filename)
        print('Saving file: ' + filepath)
        out = open( filepath, "wb")
        out.write(pic)
        out.close()
    except:
        print("Could not save file: " + filename)

imageNo = 1
end = False
notFoundCount = 0
while not end:
    url = "http://xkcd.com/" + str(imageNo)
    try:
        print url,
        data = urllib2.urlopen(url).read()
        soup = BeautifulSoup(data)
        image_tags = soup.find_all('img')
    except:
        print "unknown url"  
        break 

    try:
        image_tag = filter(lambda x: x['src'].find('comics')>=0, image_tags)
        image_tag = image_tag[0]
        comic_image_url = image_tag['src']
        filename = "XKCD-" + str(imageNo) + ".jpeg"
        saveimg(comic_image_url, filename)
        imageNo +=1
    except:
        print "my mistake" 
        break   
