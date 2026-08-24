# PDF Page Sorter

Beim Scannen von Dokumenten mit Rückseite per Dokumenteinzug kommt es oft dazu, dass die gescannte PDFs die Seiten in folgender Reihenfolge vorliegen hat:

```
1 3 5 7 ... n; n-1 n-3 ... 8 6 4 2
```

Dieses Python-Skript sortiert die Seiten einer solchen PDF-Datei richtig ein.

Es nimmt abwechselnd Seiten vom **Anfang** und **Ende** der Datei und speichert das Ergebnis als neue PDF.  

Es lohnt sich daher erst alle Vorderseiten zu scannen, dann den Stapel als Ganzes umzudrehen und dann die Rückseiten in die selbe PDF anhängen.
Dann hat man eine PDF die zur ersten Hälfte aus den Aufsteigenden ungeraden Seiten und zur zweiten Hälfte aus absteigenden ungeraden Seiten besteht (wie oben beschrieben).
Die richtige verzahnte Sortierung dieser PDF erledigt dann `duplex-scanner` . 

---

##  Funktionsweise
1. Der Benutzer gibt den vollständigen **Pfad zur PDF-Datei** ein.
2. Das Skript überprüft, ob die Datei existiert.
3. Die PDF wird geöffnet und die Seiten gezählt.
4. Die Sortierung erfolgt nach folgendem Muster:
Beispiel für eine PDF mit 6 Seiten:
```
Input-Reihenfolge: 1 3 5 6 4 2 
Output-Reihenfolge: 1 2 3 4 5 6
```
   
Beispiel für eine PDF mit 7 Seiten:
```
Input-Reihenfolge: 1 3 5 7 6 4 2
Output-Reihenfolge: 1 2 3 4 5 6 7
```

6. Das Ergebnis wird in eine neue Datei `sorted_<originalname>.pdf` gespeichert.




## Nutzung
Klone dieses Repository:
```
git clone https://github.com/Stefeberl/duplex-scanner.git
cd duplex-scanner
```
Führe das Skript aus:
```
python duplex_scan.py
```
Gib den Pfad zur gewünschten PDF-Datei ein, z. B.:

```
Bitte gib den vollständigen Pfad zu einer Datei ein: </Users/username/Documents/test.pdf>

```
Das resultiert in:
```
Datei gefunden: /Users/username/Documents/test.pdf
Wurde ergolgreich nach /Users/username/Documents/sorted_test.pdf geschrieben.
```

