L'effet de sourdine revisité: les motifs définis par Spitzer
============================================================

##  A La "désindividualisation" (209) / Entindividualisierung (136)

### A1 l'article indéfini (209)

Beispiele (Spitzer)

* "À de moindres faveurs des malheureux prétendent, / Seigneur ; c'est un exil que mes pleurs vous demandent" (Andromaque)

Queries

* A1 ([word="de"][word="les"]|[word="un.?"])[pos="noun"]
* A1x [word="de"][word="les"][pos="noun"]

Anmerkungen

* Nicht gut modelliert, weil das natürlich nur in ganz bestimmten Kontexten dem entspricht, was Spitzer hier meint. 


### A2 le pluriel au lieu du singulier / "des + substantif (pluriel) + proposition relative" (212) // "des + pluralisches Substantiv + Relativsatz (142)

Beispiele (Spitzer)

* "Je révoque des lois dont j'ai plaint la rigueur"
* "Modérez des bontés dont l'excès m'embarrasse"

Queries

* A2 [pos="det.*" & form="de"][pos="det.*"][pos="noun.*"][tag="PR.*"]

Anmerkungen

* Recht gut modelliert


### A3 "expressions impersonnelles" avec "on" (213) / unpersönliche Ausdrücke mit on

Beispiele (Spitzer)

* (viele)

Queries

* A3: [lemma="on"] (approximation)

Anmerkungen

* Nicht mehr bei Racine, sondern sogar deutlich weniger. Aber das sind natürlich nur die rohen "on"-counts. 


##  B Affaiblissement de l'expression directe du sentiment (214)

### B1 "le démonstratif de distance" (au lieu du possessif) (214) / "distanzierender Gebrauch des Demonstrativs" (144)

Beispiele (Spitzer)

* "ce fils"
* "ce fruit de sa vieillesse"
* "cette reine"

Queries

* B1 [pos="det" & lemma="ce"] [pos="noun"]

Anmerkungen

* Racine 7.7, Proches 6.5, rrf 1.17 zugunsten Racine (leicht überrepräsentiert); aber mit p-value von 0.07 nicht signifikant.


### B2 [S05] "les périphrases" locatives / lokative Periphrasen

Beispiele (Spitzer)

* B2A "(en) ces lieux" / "sur ces bords" (pour "ici")
* B2B "ce jour" (pour aujourd'hui)

Queries

* B2A ([word="en"][word="ces"][word="lieux"]|[word="sur"][word="ces"][word="bords"])
* B2B [word="ce"][word="jour"]
* zum Vergleich [word="ici"]
* (fw) [word="en"][word="ces"][word="lieux"] 
* (fw) [word="sur"][word="ces"][word="bords"] 
* (fw) [word="ce"][word="jour"] 

Anmerkungen

* Racine verwendet "en ces lieux" und "sur ces bords" deutlich häufiger als die anderen (rrf 1,36!), das ist aber nicht statistisch signifikant. Auch bei den Proches ist eine breite Verteilung da.
* Außerdem fällt auf, dass Racine auch "ici" deutlich mehr verwendet, also gerade nicht seltener, wie von Spitzer angedeutet
* Spitzer schreibt, "ici" sei bei Racine selten; also umgekehrte Erwartung!

 
## C Affaiblissement (paradoxal) de l'expression (219)


### C1 "le SI d'affirmation forte": "substantif + si + adjectif" / "si + adjectif + substantif" (219) / das beteuernde si und tant

Exemples (Spitzer)

* "des transports si charmants"
* "une si douce erreur"
* "une mort si juste"
* "des dépouilles si chères"

Queries

* C1 ([pos="noun" & type="common"][word="si" & pos="adverb"][pos="adj.*"]|[word="si" & pos="adverb"][pos="adj.*"][pos="noun" & type="common"])
* [frpos="Nc.*"][word="si"][frpos="Ag|Ga"]: Racine 1.13, Proches 1.00, Autres 0.70
* [word="transports"][word="si"] [word="charmants"]

Anmerkungen

* Lässt sich gut modellieren.
* Hier ist nun wirklich nicht klar, inwiefern das was mit "Dämpfung" zu tun hat...


#### C2 "tant + de + substantif" (220) / das beteuernde tant

Beispiele (Spitzer)

* "entre tant de beautés" 

Queries:

* C2 [word="tant_de"][pos="noun" & type="common"] 
* [word="tant_de"] [word="beauté.?"] 
* [frpos="Nc.*"][word="tant"][frpos="Ag"]
* [word="tant_de"][pos="noun.*"] 

Anmerkungen

* Lässt sich gut modellieren.


## D "Refrèner le chant lyrique du Moi" (221)

### D1 il/elle objectivant (221) - alternance de moi et non-moi

####     D1a utiliser le nom au lieu d'un pronom

Beispiele (Spitzer)

* Joas: Joas ne cessera jamais de vous aimer.

Anmerkungen

* Man könnte theoretisch einfach einmal schauen, ob Racine insgesamt mehr Eigennamen verwendet als die anderen. Aber das ist erstens kein sehr präziser Query, und zweitens ist die Freeling-Annotation für NP (proper nouns) unglaublich schlecht, mit vielen Funktionswörtern am Versanfang, die als NP erkannt wurden (Et, Je, etc.). Das müsste man erst optimieren, bevor das sinnvoll ist. Außerdem sind in meiner aktuellen Fassung die Sprechernamen mit drin, die zwar meist in Kapitälchen sind, aber das wäre besser, sie gleich rauszunehmen. 


### D2 montrer / présenter

Anmerkungen

* Das ist sehr schwierig zu identifizieren! 


##  E Dépersonnalisation du discours / De l'individuel à l'universel

### E1 pluriel de majesté (225) 

Beispiele (Spitzer)

* "Tu veux que je le fuie? Eh bien! rien ne m'arrête: / Allons, n'envions plus son indigne conquête... / Fuyons..." (Andromaque)

Queries

* [pos="verb.*" & form=".*ons"] 
* [tag="VMM01P0"]

Anmerkungen

* Die beiden Queries sind nicht identisch. Und es werden natürlich alle Formen gefunden, nicht nur diejenigen, die tatsächlich ein "pluralis majestatis" enthalten. 

### E2 pays de majesté

Beispiele (Spitzer)

* "L'ÉPIRE sauvera ce que Troie a sauvé" (Andromaque)

Anmerkungen

* Mit der aktuellen Annotation nicht sinnvoll zu machen. 


## F La personnification des abstraits (227)

### F1 substantif abstrait + verbe subjectif ou d'action

Beispiele (Spitzer)

* "ce reste de fierté qui craint d'être importune"
* "dédaigner l'inconstance", "fléchir sa rigueur"
* "des soupirs qui craignaient"
* "désordre éternel règne"
* "chagrin inquiet l'arrache"

* Substantive: fierté, inconstance, rigueur, soupirs, désordre, chagrin, douleur, puissance, voeux, désirs, inimité, 
* Verben: craindre, dédaigner, fléchir, regner, arracher, ordonner, pousser, accorder, vouloir, 

Queries

* [wnlex="noun.attribute|noun.cognition|noun.feeling|noun.communication"][word!=",|!|:|\."]{0,2}[wnlex="verb.motion"]
* [lemma="fierté|inconstance|rigueur|soupirs|désordre|chagrin|douleur|puissance|voeux|désirs|inimité"][]{0,4}[lemma="craindre|dédaigner|fléchir|regner|arracher|ordonner|pousser|accorder|vouloir"]  
* Verben: craindre, dédaigner, fléchir, regner, arracher, ordonner, pousser, accorder, vouloir, 
* (fw) [lxn="[noun.attribute|noun.cognition]"][]{0,2}[lxn="verb.motion"] 
* (fw) [pos="noun*"][]{0,2}[form="qui"][]{0,2}[pos="verb"] 


### F2 Lieu comme auteur d'une action (230): lieu + verbe (230)

Beispiele (Spitzer)

* "Qui l'eût dit, qu'un rivage à mes yeux si funeste / Présenterait d'abord Pylade aux yeux d'Oreste?" (Andromaque)

Queries

*  [lemma="terre|monde|mer|abîme|rivage|astre|forêt|gouffre|rocher|île|fleuve|précipice|ruisseau|pente|ferme|butte|bois|rivière|seine|vallée|col|champ|étang|marais|massif|roche|endroit|lieu"][]{0,5}[wnlex="verb.motion"]

Anmerkungen

* Spitzer nennt nur ein Beispiel!
* WordNet kennt relevante Kategorien: "wnlex=noun.object" beinhaltet ein Reihe von Ortsbezeichnungen, aber auch vieles andere.
* F2x ist viel zu unpräzise, weil keine syntaktische Abhängigkeit modelliert wird 

    
### F3: Jour auteur d'une action: jour + verbe (230)

Beispiele (Spitzer)

* "Le jour qui de leurs rois vit éteindre la race / Eteignit tout le feu de leur antique audace." (Athalie)

Queries

* F3x [lemma="jour"]
* F3y [lemma="jour"], Auswahl nach Kontext

Anmerkungen

* F3x: Das bleibt natürlich sehr vage, die meisten Treffer sind "false positives".
* F3y:
* Es mangelt hier klar an einem syntaktischen Parsing und einer besseren semantischen Annotation, wie so oft. Dann könnte man "jour" in Subjektposition suchen, das passende Verb unabhängig von der Nähe dazu identifizieren und prüfen, ob es ein Handlungsverb ist.


## G Estomper les contours, abolir les limites (230/233)

### G1 "pluriels qui estompent les contours" (230) / konturverwischende Plurale

Beispiele (Spitzer)

* amours, fureurs, flammes, soupirs, désirs, alarmes, refus, soins

Queries

* G1 [word="amours|fureurs|flammes|soupirs|désirs|alarmes|refus|soins|mépris|retardements|attraits|vengeances|charmes|alarmes|amours|caprices|contentements|craintes|dégoûts|ennuis|haines|ingratitudes|remerciements|respects|ressentiments|souhaits|sympathies|timidités|volontés"%c]
* [word="amours|fureurs|flammes|soupirs|désirs|alarmes|refus|soins|mépris|retardements|vengeances|charmes|attraits"]
* [wnlex="noun.feeling" & num="plural"]
 
Anmerkungen 

* Die Unterschiede zwischen den beiden Queries und ihren Ergebnissen sind interessant. Obwohl der zweite Query eigentlich weniger bestimmt ist als der erste, gibt es für den ersten wesentlich mehr Treffer. Das liegt daran, dass die WordNet-Annotation mal wieder wenig Abdeckung hat und unter den "noun.feeling" zwar mehr Begriffe fallen (16 statt nur 8), aber eben einige der von Spitzer erwähnten Begriffe fehlen (fureurs, flammes, soupirs, désirs, refus, soins). 
* G1 bildet die gemeinsame Liste der beiden anderen Queries ab. 

### G2 "les mots qui estompent les contours" (233) / konturverwischende Begriffe

Pas seulement expression plus noble, mais plus floue.

Beispiele (Spitzer)

* sein (pour ventre), flanc (pour ventre), lit (pour mariage), hymen (pour mariage), courroux (pour colère)

Queries

* G2 [word="sein|flanc|lit|lien|hymen|courroux"%c] # alle von Spitzer erwähnten Wörter
* [word="sein|flanc|hymen|courroux"] # nur die eindeutigen Wörter
* [word="lit|lien"] # nur die beiden nicht eindeutigen Wörter, und wörtliche Verwendungen händisch gelöscht; da ergibt sich ein massiver Unterschied zugunsten Racines.
   
Anmerkungen

* Das hier ist ein interessanter Fall, weil es ein Musterbeispiel für die Abweichungsstilistik ist. Jedes der Worte wird erst dadurch zum "Treffer", dass es an dieser Stelle für ein anderes stehen könnte bzw. dass eben auch das andere dort stehen könnte. Das ist schwer abzufragen. Hier gehe ich einfach davon aus, dass diese Wörter immer Treffer sind und nehme in Kauf, auch ein paar wörtliche Treffer mitzunehmen. 
   

### G3 "le neutre ce que" (233) / das neutrale ce que

Beispiele (Spitzer)

* "L'Épire sauvera ce que Troie a sauvé." (Andromaque)
* "Épouser ce qu'il hait et perdre ce qu'il aime." (Andromaque)

Queries

* G3 [word="ce_que"%c]
* [][][pos="verb"][]{0,3}[word="ce_que"][]{0,3}[pos="verb"][][]

Anmerkungen

* G3x: Der Type ist bei den Proches wesentlich häufiger als bei Racine! Und für ein Mal ist das auch signifikant. 
* G3y: Beschränkung auf einen Verb-Kontext vorher und nachher. Außerdem Auswahl der Beispiele von Hand. 
* G3z = Gz: Beschränkung auf einen Verb-Kontext vorher und nachher ohne Auswahl der Beispiele.
* Spitzer sagt weder genau, warum hier ein "effet de sourdine" zu verzeichnen ist, noch sagt er, wie die vielen Instanzen von "ce que" dahingehend beschrieben werden können, ob so ein Effekt erkennbar ist oder nicht. Das macht die Entscheidung schwierig, ob und wie unter den Treffern noch ausgewählt werden sollte. Eine Strategie ist, jeweils ein Verb vorher und nachher zu verlangen, weil das in allen Spitzer-beispielen so ist. 


### G4 "le relatif "où" placé après des abstraits" (234) / das Relativpronomen où nach Abstrakta

Beispiele (Spitzer)

* "avec des yeux où règnait la douceur"
* "pour avancer cette mort où je cours"
* l'hymen où je me suis rangée"
* la honte où je suis descendue."

Queries

* G4 [wnlex="noun.feeling"|lemma="coeur|honte|pudeur|mélancolie|déplaisir|penchant|chagrin|oeil|mort|hymen"][word=","]{0,1}[word="où"%c] 
* [wnlex="noun.feeling"][word=","]{0,1}[word="où"%c]
* [wnlex="noun.feeling"|wnlex="noun.attribute"|wnlex="noun.cognition"|wnlex="noun.communication"|lemma="coeur|honte|pudeur|mélancolie|honte|pudeur|déplaisir|penchant|chagrin|oeil|mort|hymen"][word=","]{0,1}[word="où"%c]

* G4 (neu) [wnlex="noun.feeling"|lemma="coeur|honte|pudeur|mélancolie|déplaisir|penchant|chagrin|oeil|mort|hymentrouble|mal|désespoir|malheurs|joie|bonheur|malheur|ennui|horreur|douleur|erreur|noeud|peine|rage|sacrifice|transport|colère|courroux|crainte|hyménée"][word=","]{0,1}[word="où"%c] 

Anmerkungen

* En réalité, Spitzer renvoie ici presque exclusivement à des émotions et quelques noms assez concrets. Liste complète de Spitzer: "coeur|honte|pudeur|mélancolie|honte|pudeur|déplaisir|penchant|chagrin|yeux|mort|hymen"


G5 les verbes phraséologiques (236): daigner, vouloir, oser, savoir / phraseologische Verben

Beispiele (Spitzer)

Queries

* G5: [lemma="daigner|oser|prétendre"][]{0,4}[pos="verb"] 

Anmerkungen

* Gut zu modellieren.


## G6 périphrase avec voir: PronomPers. + (AUX) + VOIR (241) / Periphrasen mit voir

Exemples / variantes (Spitzer)

* a "tu vis + VER"
* b "j'ai vu + VER"
* c "il m'a vu + VER (faire qqch)"
* d "tu m'as vu + VER"

Queries: 

* G6 [tag="PP.*"]{1,2}[tag="VA.*"]{0,1}[lemma="voir"][tag="VMN.*"]
* [frpos="Pp.*"][frpos="Vu.*"][frlemma="VOIR"][frpos="V.*"]
* [frpos="Pp.*"][frpos="Pp.*"]{0,1}[frpos="Vu.*"][frlemma="VOIR"][frpos="V.*"]
* [tag="PP.*"]{1,2}[tag="VA.*"]{0,1}[lemma="voir"][tag="VM.*"]

Anmerkungen

* tt1: "j'ai vu couler" uvm.; Racine: 0.16, Proches 0.07, Autres 0.08 => plus fréquent chez Racine!
* tt2: "je vous ai vu préférer..." etc. Racine: 0.06, Proches 0.02, Autres 0.03 => plus fréquent chez Racine!
* G5x: Recht gute Abbildung des Phänomens; häufiger bei Racine, aber nicht massiv und nicht signifikant.
* G6: Etwas bessere Abbildung des Phänomens, weil nur infinitive; häufiger bei Racine, aber nicht massiv und nicht signifikant.


### G7 expression périphrastique du verbe / umschreibender Ausdruck des Verbs

Beispiele (Spitzer)

* "porter ses pas" / "guider ses pas" (244), aber er bringt kein Racine-Beispiel!!! 

Queries

* [lemma="porter|guider"][][lemma="pas"]
* [tag="VM.*"][tag="DP.*"][lemma="pas" & pos="noun"]
* G6  [tag="VM.*" & lemma!="accompagner|suivre"][tag="DP.*"][lemma="pas" & pos="noun"]

Anmerkungen

* Beispiel: tc0649 "Au trône de Cyrus lui fit porter ses pas"
* weitere Beispiele: détourne ses pas, précipitez ses pas, retenu ses pas, suivre ses pas
* Es gibt mit porter/guider tatsächlich nur ein Beispiel bei Racine! Kein Wunder, dass Spitzer nichts zitiert.
* Mit anderen Verben noch einige relevante Treffer: 27 Treffer bei Racine
* Und: bei den Proches kaum treffer, und häufig 0 in einem Stück; Median 0! 
* Klar überrepräsentiert bei Racine, sogar deutlich signifikant.


## H Effet refroidissant, atténuant (245)

###  H1 adjectifs d'appréciation + NOM / wertenden Adjektiva und Adverbien (ger:178)

Beispiele (Spitzer)

* "votre juste crainte"
* "une juste terreur"

Queries

* (tt) [frlemma="JUSTE"][frpos="Nc.*"] 
* (tt) [frlemma="JUSTE"][frlemma="CRAINTE|COLÈRE|COURROUX|FUREUR|VENGEANCE|DOULEUR|CHÂTIMENT|ALARMES|EFFROI|DÉSESPOIR|HORREUR|SUPPLICE|DÉSIR|REMORDS|TERREUR|HAINE|AGRESSEUR|AMBITION|AMOUR|AUTORITÉ|AVERSION|DÉPIT|DEVOIR|ERREUR|EXCÈS|FERMETÉ|FIERTÉ|FRAYEUR|HAINE|HOMICIDE|IGNOMINIE|IMPATIENCE|INDIGNATION|JALOUSIE|MENACE|MÉPRIS|ORGUEIL|PEINE|PLAINTE|PUISSANCE|PUNITION|RAGE|RIGUEUR|SACRIFICE|ARRÊTS|FLAMMES|RIGUEUR"]
* Ergebnis: Racine 0.24, Proches 0.19, Autres 0.15 => häufiger bei Racine!
* H1x [lemma="juste"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & form!="ciel|cris|effets"]
* H1y [lemma="juste|oisif|utile|heureux|indigne|extrême|importun|triste|sombre|infortuné|noble|zélé|redoutable|détestable|funeste"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & form!="ciel|cris|effets"] 
* H1z [pos="adj.*"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & form!="ciel|cris|effets"] 
* H1 [pos="adj.*" & lemma!="même|autre|seul|3|capable|commun|nouveau|propre|grand|long|mutuel|moindre|jeune|premier|vieux|entier"][wnlex="noun.attribute|noun.state|noun.feeling|noun.time|noun.cognition" & lemma!="ciel|cri|effet|vie|jour|heure|de|amant|fait|voix|moment|paix|vue|couleur|moment|lien|secret|clarté|avantage|avis|climat|instant|journée|avantage|qualité|obstacle|apparence|vieillesse|caractère|choix|exploit|sujet|gloire"] 

Anmerkungen

* Problem ist, dass von LS nur diejenigen Konstruktionen gemeint sind (oder sein können), in denen das Substantiv als semantische Komponente einen Exzess oder zumindest eine große Intensität impliziert, was formal nicht so leicht zu definieren ist; allenfalls mit einer Liste.
* Auch beim Adjektiv gibt es ein Modellierungsproblem, weil Spitzer eine lange Liste an Adjektiven nennt, die alle in irgendeiner Form evaluierend / axiologisch sind. Das wiederum ist aber von Wordnet nicht erfasst, das nur "adj.all kennt oder keine Annotation. Einfach alle Adjektive zu nehmen, ist aber wiederum auch nicht zielführend.
* H11y: Nur die Adjektive, die Spitzer für Racine nennt; und nur die Wordnet-relevanten Nouns. Dann ist aber ein pro-Racine bias schon eingebaut.
* H1: Alle Adjektive und alle Wordnet-relevanten Nouns, aber mit einer Ausschlussliste. So fasst man den Query breit, ohne allzu viele false Positives mitzubekommen, aber auch ohne Racine-Bias. 

### H2 Adverbien

### H3 trop + ADJ (250) / trop + Adjektiv

Beispiele (Spitzer)

* "mon bras trop prompt à..."

Queries

* H3 [word="trop"][pos="adj.*"]

Anmerkungen

* Das ist schlicht, scheint aber recht gut zu funktionieren. Fast alle Adjektive, die in dieser Kombination vorkommen, drücken tatsächlich etwas Extremes aus. Hier sollte also kein Racine-Bias zu finden sein. Und die Konstruktion ist tatsächlich auch bei den Proches stark und signifikant überrepräsentiert.

### H3 Oxymoron (253)

Beispiele (Spitzer) 

* heureuse cruauté, innocent stratagème, fureur si belle, détestable fruit, honnête faussaire, pouvoir inutile, beau désespoir, dangereux adieux, funeste soin, tranquille fureur, orgeuilleuse faiblesse, heureuse rigueur, funeste plaisir, heureux larcin, fatal honneur, saintement homicides

Queries

* (mit Racine-Bias): (zwei Listen)
* (alle adj+noun, dann auswählen): [pos="adj.*"][pos="noun.*"]

### H4 Anithèse (257)

### H5 Chiasme (260)

### H6 Antithèse avec "perspective insoupconnée" (262)

### H7 Stichotomies (rares chez Racine!) (264)

### H8 Autocorrections / Selbstkorrektur (204)

### H9 Juxtapositions asyndétiques (269)

### H10 Structure binaire / Zweigliedrigkeit (ger:206) 

Beispiele (Spitzer)

* A: "et la lettre et le seing"
* B: "et transir et brûler"
* C: "ni le frein ni la voix"
* D: (mit ou, keine Beispiele)
* E: (Auflockerung): "D'où te bannit ton sexe et ton impiété"

Queries

* H10A (Substantive, nur et): [word="et"%c][]?[pos="noun" & type="common"][word=","]?[word="et"%c][]?[pos="noun" & * H10B (Verben, alle Varianten): [word="et|ou|ni"%c][]?[pos="verb"][word=","]?[word="et|ou|ni"%c][]?[pos="verb"]
type="common"]
* H10C (mit ni): [word="ni"%c][]?[pos="noun" & type="common"][word=","]?[word="ni"%c][]?[pos="noun" & type="common"]
* H10D (mit ou): [word="ou"%c][]?[pos="noun" & type="common"][word=","]?[word="ou"%c][]?[pos="noun" & type="common"]

Anmerkungen

* Die strengeren Fassung lassen sich gut identifizieren, aber die Auflockerungen bringen dann einfach zu viele false positives.

### H11 répétition de mots ou de radicaux (273) / Stamm(wort)wiederholung (ger:209)

Beispiele (Spitzer)

* "Mener en conquérant sa nouvelle conquête" 


### H12 Atténuation par le remplissage d'hémistisches: oppositions d'adjectifs ou de participes présents (275)

Beispiele (Spitzer)

* "soumis ou furieux"
* "invisible et présente"

Queries:

* (tt2) [frpos="ADJ.*|VER:pper"] [frpos="PUN"]{0,1} [frlemma="ou"] [frpos="ADJ.*"]
* H12 [pos="adj.*" | tag="VMP.*"][tag="F.*"]{0,1}[lemma="ou"|lemma="et"][pos="adj.*" | tag="VMP.*"] + händische Bearbeitung

Anmerkungen

* Gesamtkorpus: 70x; Racine: 15x, Andere: 55 (=12)
* Beispiele genauer anschauen, einige sind nicht korrekt.
* Hier wird einerseits ein Problem der quantitativen Stilistik klar: die abstrakte Struktur ADJ+(,)+ou+ADJ ist für den Computer einfach zu finden, aber ob die Adjektive semantisch in Opposition stehen, wäre nur mit weiteren Annotationen eventuell automatisch zu klären (Sentiment Analysis).
* Zugleich wird ein Problem der hermeneutischen Stilistik Spitzers deutlich: die Frage, ob hier wirklich eine "atténuation" vorliegt, ist kaum mit harten Argumenten zu entscheiden; da ist sein Blick schon sehr stark davon geprägt, was er sucht (top-down Wahrnehmung).
* Das gilt auch für die beiden folgenden Phänomene

### H13 Atténuation par le remplissage d'hémistisches: atténuation par les adjectifs appréciatifs

Beispiele (Spitzer) 
* "un zèle imprudent"
* "victime obéissante"
* "indigne artifice"

Query
* (fw) [pos="noun"][pos="adj.*"|tag="VMP.*"]

### H14 Atténuation par le remplissage d'hémistisches: appositions

Beispiele (Spitzer)

* "honteuse à ma mémoire"
* "promptes à me venger"


## K

### K1 Ordre de mots poétique de type latin (inversion); (278)

### K2 Ordre de mots enveloppée, synthétique (279)

## L Stilisierte Aufregung (ger:216)

### L1 Répétition solennelle (fre:280) / feierliche Wiederholung

Definition

* "da ist die feierliche Wiederholung von drohenden Prophezeiungen, mahnenden Imperativen, angsvollen Fragen, beteuernden Behauptungen" (ger:216) 

Beispiele (Spitzer)

* "Il peut, Seigneur, il peut, dans ce désordre extrême..."
* "Qui sait même, qui sait si le roi votre père..."  

Queries (RegEx)

* L1 ".* (\w{5,8}) .{0,25} \\1.*"
* ".* (\w{5,8}) .{0,15} \\1.*"
* ".* (\w{5,8}) .{0,50} \\1.*"

Anmerkungen

* Sowohl mit der engen Auslegung einer Wiederholung (L1x, wiederholte Wörter müssen nahe beieinander stehen) als auch mit einer erweiterten Auslegung (L1y) ergibt sich kein deutlicher, definitiv kein signifikanter Unterschied zwischen Racine und den Proches. Allerdings ist hier die reine Wiederholung modelliert, ohne inhaltliche Einschränkung auf die "mahnenden Imperative" etc. 


### L2 Asyndète de gradation / "das steigernde Asyndeton" (ger:217)

Beispiele (Spitzer)

* "Infortuné, proscrit, incertain de régner..."
* "Charmant, jeune, traînant tous les coeurs après soi..."
* "Muet, chargé de soins, et les larmes aux yeux..." 
* Le fer, le bandeau, la flamme est toute prête..." 
Queries

* L2A (Verben): [pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|dire" & word!="faut|suis|dit"][]{0,1}[word=","][pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|aller|dire" & word!="faut|suis|dit"][]{0,1}[word=","][pos="verb" & lemma!="falloir|chercher|pouvoir|faire|être|avoir|devoir|dire" & word!="faut|suis|dit"] 
* L2B (Substantive): ([]{0,2}[pos="noun" & type="common"][word=","][]{0,1}){3}

Anmerkungen

* Hier beziehen sich die Beispiele immer auf die dreifache Wiederholung mehrerer unterschiedlicher Veben oder Substantive. Das lässt sich nocht recht gut mit CQP modellieren, allerdings ist natürlich die inhaltliche Steigerung nicht abbildbar.
* Spannend allerdings das Ergebnis: Die asyndetische Folge von Verben ist untypisch für Racine, während die asyndetische Folge von Substantiven tatsächlich bei Racine einen höheren Median hat, allerdings beides nicht signifikant. 



### L3 Asyndète avec condensation de différentes composantes (283) / "Ballung verschiedener Akzidentien oder Ingredientien zu einem einheitlichen Ganzen durch ein verschiedene Nomina (Infinitive, usw.) zusammenfassendes *tout*" (ger:219) 

Beispiele (Spitzer)

* (lange Passagen)

Queries

* L3x: [word="tout"%c][word="cela"%c]

Anmerkungen

* L3x: Nur die Fälle mit "tout cela"
* 



### L4 Alignement de constructions nominales (284) / Aneinanderreihung von Nominalkonstruktionen

Beispiele (Spitzer) 

* Un seul exemple: "Soliman jouissait d'une pleine puissance : L'Égypte ramenée a son obéissance, Rhodes, des Ottomans ce redoutable écueil De tous ses défenseurs devenu le cercueil, Du_Danube asservi les rives désolées, De_l'_Empire_Persan les bornes reculées, Dans leurs climats brûlants les Africains domptés, Faisaient taire les lois devant ses volontés." (Bajazet)

Queries 

* L4 ([pos="noun"][tag="VMP.*"][]{0,8}){2,4} (also eine Sequenz von "Substantiv + Partizip + einige Worte, mehrfach)

Anmerkungen

* Treffer: "L'impie Achab détruit, et de son sang trempé Le champ que par le meurtre il avait usurpé ; Près_de ce champ fatal Jézabel immolée, Sous les pieds de les chevaux cette reine foulée ; Dans son sang inhumain les chiens désaltérés, Et de son corps hideux les membres déchirés ; Des prophètes menteurs la troupe confondue, Et la flamme de le ciel sur l'autel descendue ; Élie à les éléments parlant en souverain, Les cieux par lui fermés et devenus d'airain, Et la terre trois ans sans pluie et sans rosée ; Les morts se ranimant à la voix d'Élisée ;" (Athalie)

Notizen

* In der Tat erscheinen diese Sequenzen bei Racine sehr verbreitet zu sein. Im Vergleich der Mittelwerte zeigt sich das deutlich, mit 0.1/1000 Wörtern bei Racine, aber nur 0.05/1000 Wörtern bei den Anderen.

## M Übrige Phänomene

### M1 Aposiopèse (287) / "die Aposiopese, die Selbstunterbrechung der Rede" (ger:225)

Anmerkungen

* Schlicht markiert durch die drei Punkte "...",.

### M2 "ganz einfache Verse oder Halbverse, die auf eine hochrhetorische Versreihe folgen" (ger:228)

Anmerkungen

* Das lässt sich nicht gut formal modellieren.

### M3 Nebensatzfolge (ger:232)

### M4 Abgeschwächte Interjektionen / Ausrufe (ger: 232)

#### M4A Interjektionen

Beispiele (Spitzer)

* "Hélas ! un fils n'a rien qui ne soit à son père."
* "Ah, je l'ai trop aimé pour ne le point hair."

Queries

* M4A: [pos="interj"][word="!"]  
* M4Ax: [word="ah|hélas"%c] 
* M4Ay: [word="ah|hélas"%c][word="!"] 

Anmerkungen

* Spitzer sagt, Racine verwende sehr viele Interjektionen (und schwäche diese aber im Kontext ab). Die Ergebnisse zeigen, dass Racine gleich viele oder weniger Interjektionen als die Proches verwendet, allerdings bleibt unmodelliert, ob sie durch den Kontext jeweils abgeschwächt werden oder nicht. Das lässt sich nicht fassen. 

#### M4B Ausrufe

Beispiele (Spitzer)

* "Bajazet interdit ! Atalide étonnée !"
* "O soins tardifs et superflus !" 

Queries

* M4B: [pos!="interj"][word="!"]

Anmerkungen

* Ganz einfacher Query, der nicht das Phänomen modelliert, sondern einen Indikator für das Phänomen. Die Ausrufezeichen nach Interjektionen sind ausgeschlossen, weil sie schon in M4A enthalten sind.


### M5 Apostrophen an höhere Mächte

### M6 "perseverierende Wortwiederholung" (ger:239)

Anmerkungen

* siehe hierzu weiter oben.


### M7 Rundzahlen

Beispiele (Spitzer)

* mille, cent

Queries

* M7 [word="mille|cent"%c]

Anmerkungen

* Interessant, dass diese Rundzahlen tatsächlich nur leicht überrepräsentiert sind bei Racine, allerdings sagt das wenig über ihre jeweilige Funktionalisierung und Kontextualisierung aus. 


### M8 Der Wechsel von "vous" und "toi"



