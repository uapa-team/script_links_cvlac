import urllib.request
import re
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "a+")
lines = inputFile.readlines()
for dni in lines:
    url = 'https://sba.colciencias.gov.co/tomcat/Buscador_HojasDeVida/busqueda?q=' + dni.replace("\n", "")
    htmlSource = str(urllib.request.urlopen(url).read())
    try:
        matchObj = re.search("https://scienti.colciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do%3Fcod_rh%3D([0-9]*)", htmlSource)
    except:
        outputFile.write(
            dni.replace("\n", "") + "," + "\n")
        continue
    outputFile.write(dni.replace("\n", "") + "," + str(matchObj.group()).replace("%3F", "?").replace("%3D", "=") + "\n")
