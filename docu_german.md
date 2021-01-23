# Pygiator

Mit dem Pygiator kann man zwei Python-Skripte vergleichen und dabei feststellen ob es sich um ein Plagiat handelt. Dieses Programm wurde im Zuge der Lehrveranstaltung **Skriptsprachen** entwickelt. Die Anforderungen dabei waren:

+ zwei Eingangsparameter - die beiden Pythonskripte
+ ein Ausgangsparameter - die Ähnlichkeit

## Installation und Anforderungen

Um den Pygiator lokal laufen zu lassen ist es erforderlich, dass [Python 3.8 oder höher](https://www.python.org/)  installiert ist. Es müssen auch weitere Module installiert werden, dafür liegt die **requirements.txt** Datei bereit. Die Installation dieser erfolgt durch die Eingabe von folgendem Kommando:

```bash
pip install -r requirements.txt
```

Außerdem kann das Programm auch auf [Streamlit](https://share.streamlit.io/qtr1ck/plagiat_scanner/main) abgerufen werden. Dafür sind lediglich eine aufrechte Internetverbindung und ein Browser erforderlich.

## Verwendung

In der Seitenleiste sind zwei Felder, durch einen Klick darauf öffnet sich ein neues Fenster, wo die Python-Dateien ausgewählt werden können. Sobald zwei Skripte ausgewählt sind, erfolgt die Berechnung und das Resultat wird Prozent und zusätzlich als eine Heatmap angezeigt.

Wenn ein Resultat vorliegt, kann die Heatmap mit einem Slider in der Seitenleiste noch angepasst werden. Dabei kann ein Grenzwert ausgewählt werden und all jene Zeilen welche eine größere Ähnlichkeit vorweisen, werden rot eingefärbt.

Desweiteren können die beiden Dateien vertauscht werden, links über der Heatmap befindet sich eine Checkbox, durch aus- bzw. abwählen werden sie dabei vertauscht.

## Implementierung

### Lösungsidee

Da der Quellcode an sich schwer zu analysieren ist, muss dieser aufbereitetet werden, in diesem Fall bietet es sich gut an den Code in Tokens umzuwandeln. Dabei wird die Bedeutung der einzelnen Blöcke des Quellcodes bestimmt und in einer Zeichenkette von Tokens gespeichert. Es gibt folgende Kategorien für die Tokens:

```bash
categories = {
    'Call':         ['A', 'rgb(80, 138, 44)'],
    'Builtin':      ['B', 'rgb(212, 212, 102)'],
    'Comparison':   ['C', 'rgb(176, 176, 176)'],
    'FunctionDef':  ['D', 'rgb(4, 163, 199)'],
    'Function':     ['F', 'rgb(199, 199, 72)'],
    'Indent':       ['I', 'rgb(237, 237, 237)'],
    'Keyword':      ['K', 'rgb(161, 53, 219)'],
    'Linefeed':     ['L', 'rgb(255, 255, 255)'],
    'Namespace':    ['M', 'rgb(232, 232, 209)'],
    'Number':       ['N', 'rgb(192, 237, 145)'],
    'Operator':     ['O', 'rgb(212, 212, 212)'],
    'Punctuation':  ['P', 'rgb(214, 216, 216)'],
    'Pseudo':       ['Q', 'rgb(14, 3, 163)'],
    'String':       ['S', 'rgb(194, 126, 0)'],
    'Variable':     ['V', 'rgb(184, 184, 176)'],
    'WordOp':       ['W', 'rgb(8, 170, 207)'],
    'NamespaceKw':  ['X', 'rgb(161, 53, 219)']
}
```

Nachdem die Tokenstrings für die beiden Skripte vorliegen, efolgt der Vergleich dieser. Dabei wird zeilenweise die Gleichheit überprüft und es wird immer eine Zeile des ersten Skripts mit jenen des zweiten überprüft, letztendlich zählt nur die größte Ähnlichkeit einer Zeile und die Anderen werden verworfen. Für den Vergleich wird der ***SequenceMatcher*** aus dem Modul ***difflib*** verwendet, welcher einen Wert zwischen 0 und 1 zurückgibt, abhängig von der Ähnlichkeit der beiden Sequenzen.

### Backend

TODO: noch schreiben

### Frontend

Das Frontend wurde mit [**Streamlit**](https://www.streamlit.io/) umgesetzt. Streamlit ist eine Python Bibliothek, mit welcher Web Applikationen auf Basis von Python sehr einfach erstellt werden können. Um es verwenden zu können muss nur das entsprechende Modul
installiert sein. Diese Bibliothek bietet bereits die entsprechenden Funktionalitäten um Texte, Diagramme oder auch Widgets abzubilden.

Der Pygiator ist dabei in drei Bereiche unterteilt:

+ Seitenleiste
+ Startseite
+ Ergebnisseite

Sobald zwei Dateien ausgewählt sind, wird die Ergebnisseite angezeigt. Dort befindet sich ganz oben ein Dropdown Menü für den **Winnowing** Algorithmus, in ausgeklappten Zustand kann man dort die Parameter dafür anpassen und sieht auch das Ergebnis davon.
Darunter folgen die Checkbox für das vertauschen der Dateien und das eigentliche Ergebnis mit der Heatmap.
