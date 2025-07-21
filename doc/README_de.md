# Kameradatenbank

Eine Open-Source-Datenbank mit Kameraspezifikationen und -bildern für Forschung und Anwendungsentwicklung.

## Überblick

Dieses Repository enthält detaillierte Spezifikationen von 3.586 Digitalkameras verschiedener Hersteller.





## Repository-Struktur

```
CameraDatabase/
├── data/                          # Datenverzeichnis
│   ├── camera_data.csv    # Kameraspezifikationen im CSV-Format
│   ├── camera_data.json   # Kameraspezifikationen im JSON-Format
├── doc/                           # Dokumentationsverzeichnis
│   ├── README_en.md               # Englische Dokumentation
│   ├── README_zh.md               # Chinesische Dokumentation
│   ├── README_ja.md               # Japanische Dokumentation
│   ├── README_es.md               # Spanische Dokumentation
│   ├── README_fr.md               # Französische Dokumentation
│   └── README_de.md               # Deutsche Dokumentation (diese Datei)
└── README.md                      # Haupt-README-Datei
```




## Datendateien

- `data/camera_data.csv`: Kameraspezifikationen im CSV-Format (37 Spalten)
- `data/camera_data.json`: Kameraspezifikationen im JSON-Format (gleiche Daten wie CSV)

## Datenstruktur

Der Datensatz enthält die folgenden Felder:

| Englisches Feld | Deutsche Übersetzung | Beschreibung |
|---------|----------|------|
| Brand | Marke | Kamerahersteller |
| Model | Modell | Modellname der Kamera |
| Year | Jahr | Erscheinungsjahr |
| image_file | Bilddatei | Pfad zum Kamerabild |
| Total megapixels | Gesamtpixelzahl | Gesamtzahl der Megapixel |
| Exposure Compensation | Belichtungskorrektur | Verfügbarer Belichtungskorrekturbereich |
| Normal focus range | Normaler Fokusbereich | Regulärer Fokusabstandsbereich |
| Battery | Akku | Akkutyp |
| Sensor resolution | Sensorauflösung | Auflösung in Pixeln (Breite x Höhe) |
| Crop factor | Formatfaktor | Cropfaktor des Sensors |
| Sensor type | Sensortyp | Art des Bildsensors (CCD, CMOS, usw.) |
| Dimensions | Abmessungen | Physische Abmessungen (mm) |
| Max aperture | Maximale Blende | Maximaler Blendenwert |
| Min. shutter speed | Min. Verschlusszeit | Minimale Verschlusszeit |
| White balance presets | Weißabgleich-Voreinstellungen | Anzahl der Weißabgleich-Voreinstellungen |
| Macro focus range | Makro-Fokusbereich | Minimaler Fokusabstand für Makrofotografie |
| Optical zoom | Optischer Zoom | Ob optischer Zoom verfügbar ist |
| USB | USB | USB-Schnittstellentyp |
| Weight | Gewicht | Gewicht der Kamera (g) |
| Max. aperture (35mm equiv.) | Max. Blende (35mm Äquiv.) | Maximale Blende im 35mm-Äquivalent |
| Focal length (35mm equiv.) | Brennweite (35mm Äquiv.) | Brennweitenbereich im 35mm-Äquivalent |
| Also known as | Auch bekannt als | Alternative Namen oder Modelle |
| Aperture priority | Blendenpriorität | Ob der Blendenpriorität-Modus verfügbar ist |
| Max. image resolution | Max. Bildauflösung | Maximale Bildauflösung in Pixeln |
| Max. shutter speed | Max. Verschlusszeit | Maximale Verschlusszeit |
| Storage types | Speichertypen | Kompatible Speichermedien |
| Effective megapixels | Effektive Megapixel | Effektive Megapixel für die Bilderfassung |
| Megapixels | Megapixel | Marketing-Megapixelzahl |
| Max. video resolution | Max. Videoauflösung | Maximale Videoauflösung |
| Screen size | Bildschirmgröße | LCD-Bildschirmgröße in Zoll |
| Metering | Belichtungsmessung | Verfügbare Belichtungsmessmodi |
| Digital zoom | Digitaler Zoom | Ob digitaler Zoom verfügbar ist |
| Shutter priority | Verschlusspriorität | Ob der Verschlusspriorität-Modus verfügbar ist |
| Sensor size | Sensorgröße | Physische Abmessungen des Sensors (mm) |
| Viewfinder | Sucher | Suchertyp |
| Screen resolution | Bildschirmauflösung | LCD-Bildschirmauflösung in Punkten |
| ISO | ISO | Verfügbarer ISO-Empfindlichkeitsbereich |

## Datenformat

Die Daten sind in zwei Formaten verfügbar:

1. **CSV**: Einfaches tabellarisches Format, geeignet für Tabellenkalkulationsprogramme und Datenanalysetools
2. **JSON**: Strukturiertes Format, ideal für Webanwendungen und Programmierung

### JSON-Beispiel

```json
{
    "Brand": "Canon",
    "Model": "EOS R5 Mark II",
    "Year": "2024",
    "image_file": "data/images/canon_eos-r5-mark-ii.jpg",
    "Total megapixels": "50.3",
    "Exposure Compensation": "\u00b13 EV (in 1/3 EV, 1/2 EV steps)",
    "Normal focus range": null,
    "Battery": "LP-E6P lithium-ion battery",
    "Sensor resolution": "8216 x 5477",
    "Crop factor": "1.0",
    "Sensor type": "CMOS",
    "Dimensions": "138.5 x 101.2 x 93.5 mm",
    "Max aperture": null,
    "Min. shutter speed": "30 sec",
    "White balance presets": "8.0",
    "Macro focus range": null,
    "Optical zoom": null,
    "USB": "USB 3.2 (10 GBit/sec)",
    "Weight": "746 g",
    "Max. aperture (35mm equiv.)": null,
    "Focal length (35mm equiv.)": null,
    "Also known as": null,
    "Aperture priority": "Yes",
    "Max. image resolution": "8192 x 5464",
    "Max. shutter speed": "1/8000 sec",
    "Storage types": "SD/SDHC/SDXC, CFexpress Type B",
    "Effective megapixels": "45.0",
    "Megapixels": null,
    "Max. video resolution": "8192x4320 (60/50/30p/\u200b25p/24p)",
    "Screen size": "3.2\"",
    "Metering": "Multi, Center-weighted, Spot, Partial",
    "Digital zoom": null,
    "Shutter priority": "Yes",
    "Sensor size": "36 x 24 mm",
    "Viewfinder": "Electronic",
    "Screen resolution": "2,100,000 dots",
    "ISO": "Auto, 100-51200 (extends to 50-102400)"
  }
```

## Verwendungszwecke

Dieser Datensatz kann verwendet werden für:

- Analyse des Kameramarkts
- Forschung im Bereich Computer Vision
- Training von Machine-Learning-Modellen
- Kamera-Empfehlungssysteme
- Bildungszwecke

## Datenbereinigung

Die Daten wurden bereinigt, um:
- Leere Spalten zu entfernen
- Spaltennamen zu standardisieren
- Nach Marke und Erscheinungsjahr (absteigend) zu sortieren
- Alle fehlenden Werte im JSON-Format in null umzuwandeln

## Lizenz

Dieser Datensatz wird unter der MIT-Lizenz veröffentlicht. Sie können ihn frei für kommerzielle und nicht-kommerzielle Zwecke verwenden.

## Beiträge

Beiträge zur Verbesserung des Datensatzes sind willkommen. Bitte reichen Sie einen Pull-Request ein oder eröffnen Sie ein Issue, um Ihre Ideen zu diskutieren.

## Danksagung

Vielen Dank an alle Kamerahersteller und Bewertungswebsites, die die ursprünglichen Spezifikationen zur Verfügung gestellt haben. 
