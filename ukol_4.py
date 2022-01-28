import json
import line_snapper
import argparse

#definovani argumentu
parser = argparse.ArgumentParser(description="zkrátí linie")
parser.add_argument("-f", "--file", type=str, help="zadejte název vstupního souboru")
parser.add_argument("-o", "--out_file", type=str, help="zadejte název souboru, do kterého budou uloženy nové sourřadnice linií")
parser.add_argument("-l", "--lenght", type=int, help="zadejte maximalní požadovanou délku segmentů linií")
args = parser.parse_args()

in_file = args.file
out_file = args.out_file
max_lenght = args.lenght

#in_file = "kdfslg.geojson"
#in_file = "data_none_valid.geojson"
#in_file = "data.geojson"
#out_file = "new_data.geojson"
#max_lenght = 30

#nacteni dat
#pokud nebude soubor nalezen bude vyvolana chyba a program se ukonci 
try:
    with open (in_file, encoding="UTF-8") as file:
        #pokud nebude soubor validni JSON bude vyvolana chyba a program se ukonci
        try:
            data = json.load(file)
        except ValueError:
            print("Vstupní soubor není validní JSON")
            quit()
except FileNotFoundError:
    print("Vstupní soubor nebyl nalezen")
    quit()

#aktualizace bodu, tvorici linie  
for lines in data["features"]:
    #nacteni souradnic bodu tvorici linii
    coordinates = lines["geometry"]["coordinates"]
    #definovani bodu ze souradnic
    points = []
    for point in coordinates:
        points.append(line_snapper.Point(*point))
    #vytvoreni segmentu z bodu
    segments = []
    for i in range(len(points)-1):
        segment = line_snapper.Segment(points[i], points[i+1])
        segments.append(segment)
    #vytvoreni linie ze segmentu
    line = line_snapper.Polyline(*segments)
    #vytvoreni nove linie se zkracenymi segmenty
    new_line = line.divide_long_segments(max_lenght)
    #zapsani novych bod
    lines["geometry"]["coordinates"] = new_line.points()

#vytvoreni noveho geojsonu
with open (out_file, "w", encoding="UTF-8") as new_file:
    json.dump(data, new_file, indent=4)