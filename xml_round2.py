import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

#print(tree)
#print(ET.tostring(root, encoding = 'UTF8').decode('utf8'))
#print(root.tag)
#print(root.attrib)
#print([elem.tag for elem in root.iter()])

for rating in root.iter('rating'):
    #print(rating.text)
    pass

for rating in root.findall("./genre/decade/movie[rating = 'PG']"):
    #print(rating.attrib)
    pass

kkid = root.find("./genre/decade/movie[@title = 'THE KARATE KID']")
kkid.attrib["title"] = kkid.attrib["title"].title()
#print(kkid.attrib)

anime_genre = ET.SubElement(root, 'genre')
#print(ET.tostring(root, encoding = 'UTF8').decode('utf8'))
anime_genre.attrib['category'] = 'Anime'


decade = ET.SubElement(anime_genre, 'decade')
decade.attrib['years'] = "2020s"
#decade.text = 'One Piece'

bman = root.find("./genre[@category = 'Comedy']/decade/movie[@title = 'Batman: The Movie']")
dec2020 =  root.find("./genre[@category = 'Anime']/decade[@years = '2020s']")
dec2020.append(bman)

dec1960 = root.find("./genre[@category = 'Comedy']/decade[@years = '1960s']")
dec1960.remove(bman)

print(ET.tostring(root, encoding = 'UTF8').decode('utf8'))

tree.write('movies.xml')
tree = ET.parse('movies.xml')
root = tree.getroot()
for movie in root.iter('movie'):
    print(movie.attrib)

