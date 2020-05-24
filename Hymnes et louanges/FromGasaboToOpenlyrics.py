import json
import codecs

def CreateOpenlyricSong(songNumber, config, song, songBook):
    data = "<?xml version='1.0' encoding='UTF-8'?>"
    data += "<song xmlns='http://openlyrics.info/namespace/2009/song' version='0.8' createdIn='OpenLP 2.4.6' modifiedIn='OpenLP 2.4.6' modifiedDate='2020-05-23T19:55:36'>"
    data += "   <properties>"
    data += "       <titles>"
    data += "           <title>HL 128. Comme une terre altérée</title>"
    data += "       </titles>"
    data += "       <authors>"
    data += "           <author type='music'>Inconnu</author>"
    data += "           <author type='words'>Inconnu</author>"
    data += "       </authors>"
    data += "       <songbooks>"
    data += "           <songbook name=\'" + songBook + "\'/>"
    data += "       </songbooks>"
    data += "       <themes>"
    data += "           <theme>Le Saint-Esprit</theme>"
    data += "       </themes>"
    data += "   </properties>"
    data += "   <lyrics>"

    choruses =  [c for c in song['lyrics'] if(c['label'] == 'Choeur')]
    finales  =  [f for f in song['lyrics'] if(f['label'] == 'Final')]
    verses   =  [v for v in song['lyrics'] if( (c['label'] != 'Choeur') and (v['label'] != 'Final'))]
    
    """
    for v in verses:

    data += "   </lyrics>"
    data += "</song>



    data += "       <verse name="v1">
      <lines>Comme une terre altérée<br/>Soupire après l'eau du ciel,<br/>Nous appelons la rosée<br/>De ta grâce, Emmanuel!</lines>
    </verse>
    <verse name="c1">
      <lines>Fraîches rosées,<br/>Descendez sur nous tous!<br/>Ô divines ondées,<br/>Venez, arrosez-nous !</lines>
    </verse>
    <verse name="v2">
      <lines>Descends, ô pluie abondante,<br/>Coule à flots dans notre coeur,<br/>Donne à l'âme languissante<br/>Une nouvelle fraîcheur!</lines>
    </verse>
    <verse name="c2">
      <lines>Fraîches rosées,<br/>Descendez sur nous tous!<br/>Ô divines ondées,<br/>Venez, arrosez-nous !</lines>
    </verse>
    <verse name="v3">
      <lines>Ne laisse en nous rien d'aride<br/>Qui ne soit fertilisé;<br/>Que le coeur le plus avide<br/>Soit pleinement arrosé!</lines>
    </verse>
    <verse name="c3">
      <lines>Fraîches rosées,<br/>Descendez sur nous tous!<br/>Ô divines ondées,<br/>Venez, arrosez-nous !</lines>
    </verse>
    <verse name="v4">
      <lines>Oui, que les déserts fleurissent<br/>Sous tes bienfaisantes eaux;<br/>Que les lieux secs reverdissent<br/>Et portent des fruits nouveaux!</lines>
    </verse>
    <verse name="c4">
      <lines>Fraîches rosées,<br/>Descendez sur nous tous!<br/>Ô divines ondées,<br/>Venez, arrosez-nous !</lines>
    </verse>
    <verse name="v5">
      <lines>Viens, ô salutaire pluie,<br/>Esprit de grâce et de paix!<br/>Répands en nous une vie<br/>Qui ne tarisse jamais!</lines>
    </verse>
    <verse name="c5">
      <lines>Fraîches rosées,<br/>Descendez sur nous tous!<br/>Ô divines ondées,<br/>Venez, arrosez-nous !</lines>
    </verse>
    data = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n"
    data = data + "<bible>\n"
    for b in books:
        print(b['name'])
        data = data + "\t<b n=\"" + b['name'] + "\">\n"
        fChapters = [c for c in chapters if(b['bid'] == c['bid'])]
        for c in fChapters:
            data = data + "\t\t<c n=\"" +  str(c['chapter']) + "\">\n"
            fVerses = [v for v in verses if(c['cid'] == v['cid'])]
            for v in fVerses:
                data = data + "\t\t\t<v n=\"" + v['verse'] + "\">" + v['text'] + "</v>\n"
            data = data + "\t\t</c>\n"
        data = data + "\t</b>\n"
    data = data + "</bible>\n"

    outputFile = codecs.open("BYSB.xmm", "w", "utf-8")
    outputFile.write(data)
    outputFile.close()
    """

config = {}
print("Starting ...................")
with open('./Gasabo/config.json', encoding='utf-8') as configFile:
    config  = json.load(configFile)

i = 1
 
while i <= 654:
    songFilename = "./Gasabo/pages/" + str(i).zfill(3) + ".json"
    song = {}
    with open(i, songFilename, encoding='utf-8') as songFile:
        song  = json.load(songFile)
        CreateOpenlyricSong(config, song, "Hymnes et louanges"):
    i += 1


