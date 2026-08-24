# PDF Page Sorter

Dieses Python-Skript sortiert die Seiten einer PDF-Datei neu.  
Es nimmt abwechselnd Seiten vom **Anfang** und **Ende** der Datei und speichert das Ergebnis als neue PDF.  

---

##  Funktionsweise
1. Der Benutzer gibt den vollständigen **Pfad zur PDF-Datei** ein.
2. Das Skript überprüft, ob die Datei existiert.
3. Die PDF wird geöffnet und die Seiten gezählt.
4. Die Sortierung erfolgt nach folgendem Muster:
   - 1. Seite (Anfang)
   - letzte Seite (Ende)
   - 2. Seite (Anfang)
   - vorletzte Seite (Ende)
   - usw.
5. Das Ergebnis wird in eine neue Datei `sorted_<originalname>.pdf` gespeichert.

Beispiel für eine PDF mit 6 Seiten:
Original: 1 2 3 4 5 6
Sortiert: 1 6 2 5 3 4


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

