import json
import line_snapper
import argparse

#definovani argumentu
parser = argparse.ArgumentParser(description="zkrátí linie")
parser.add_argument("-f", "--file", type=str, required=True, help="zadejte název vstupního souboru")
parser.add_argument("-o", "--out_file", type=str, required=True, help="zadejte název souboru, do kterého budou uloženy nové sourřadnice linií")
parser.add_argument("-l", "--lenght", type=int, required=True, help="zadejte maximalní požadovanou délku segmentů linií")
args = parser.parse_args()

in_file = args.file
out_file = args.out_file
max_length = args.lenght

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
except PermissionError:
    print("Program nemá přístup ke vstupnímu souboru")

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
    new_line = line.divide_long_segments(max_length)
    #zapsani novych bod
    new_points = new_line.points()
    lines["geometry"]["coordinates"] = new_line.points()

#vytvoreni noveho geojsonu
try:
    with open (out_file, "w", encoding="UTF-8") as new_file:
        try:
            json.dump(data, new_file, indent=4)
        except TypeError:
            print("Nový soubor se nepovedlo zapsat")
            quit()
except PermissionError:
    print("Nový soubor se nepovedlo zapsat.")
    quit()