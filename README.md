<H3>ÚKOL 4</H3>
<p>Program slouží ke zkrácení linií tak, aby jejich jednotlivé segmenty nepřesahovaly zadanou délku.Toho dosáhne tak že napřed načte datový soubor obsahují geometrické údaje o liniích. Z třechto údajů vytvoří liniové objekty třidy Polyline ze souboru line_snapper.py a na nich rozděluje jednotlivé segmenty dokud nejsou kratší než požadovaná maximální délka. Nové geometrické údaje těchto bodů aktualizují údaje původní. Tento proces proběhne na všech liniích v datovém souboru a následně je vytvořen nový soubor obsahující aktualizované linie.</p>
<p>Program je spouštěn z přikazové řádky zapsáním příkazu:</p>
	<p><i>python3 ukol_4.py -f vstupní soubor -o výstupní soubor -l požadovaná maximální délka segmentu v metrech</i></p>
<p>Konkrétně tedy např. takto:</p>
        <p><i>python3 ukol_4.py -f vstup.geojson -o vystup.geojson -l 30</i></p>
<p><b>Při spuštení je zapotřebí definovat tři argumety:</b></p>
        <p><b>-f vstupní soubor.</b></p>
               <p>Uživatel zadá název datového souboru, který chce zpracovávat (i s příponou). Je zapotřebí aby šlo o JSON obasující FeatureCollection s jednotlivými Features které musí mit geometrii typu LineString. Zároveň musí být tyto linie v         metrickém     souřadnicovém systému (Křovákovo zobrazení).</p>
       <p><b>-o výstupní soubor</b></p>
                <p>Uživatel zadá název souboru, který bude obsahovat aktulizované geometrické údaje. Artibuty všech linií budou zachovány.</p>
        <p><b>-l maximální délka segmentu v metrech</b></p>
               <p>Uživatel zadá počet metrů, který uvádí maximální dovolenou velikost segmentů upravených linií.</p>
