# Base de Données des Appareils Photo

Une base de données open source des spécifications et images d'appareils photo pour la recherche et le développement d'applications.

## Aperçu

Ce dépôt contient des spécifications détaillées de 3 586 appareils photo numériques de différents fabricants.





## Structure du Dépôt

```
CameraDatabase/
├── data/                          # Répertoire de données
│   ├── camera_data.csv    # Spécifications des appareils photo au format CSV
│   ├── camera_data.json   # Spécifications des appareils photo au format JSON
├── doc/                           # Répertoire de documentation
│   ├── README_en.md               # Documentation en anglais
│   ├── README_zh.md               # Documentation en chinois
│   ├── README_ja.md               # Documentation en japonais
│   ├── README_es.md               # Documentation en espagnol
│   ├── README_fr.md               # Documentation en français (ce fichier)
│   └── README_de.md               # Documentation en allemand
└── README.md                      # Fichier README principal
```




## Fichiers de Données

- `data/camera_data.csv` : Données de spécifications d'appareils photo au format CSV (37 colonnes)
- `data/camera_data.json` : Données de spécifications d'appareils photo au format JSON (mêmes données que CSV)

## Structure des Données

L'ensemble de données comprend les champs suivants :

| Champ en anglais | Traduction en français | Description |
|---------|----------|------|
| Brand | Marque | Fabricant de l'appareil photo |
| Model | Modèle | Nom du modèle de l'appareil photo |
| Year | Année | Année de sortie |
| image_file | Fichier image | Chemin vers l'image de l'appareil photo |
| Total megapixels | Mégapixels totaux | Nombre total de mégapixels |
| Exposure Compensation | Compensation d'exposition | Plage de compensation d'exposition disponible |
| Normal focus range | Plage de mise au point normale | Plage de distance de mise au point normale |
| Battery | Batterie | Type de batterie |
| Sensor resolution | Résolution du capteur | Résolution en pixels (largeur x hauteur) |
| Crop factor | Facteur de recadrage | Facteur de recadrage du capteur |
| Sensor type | Type de capteur | Type de capteur d'image (CCD, CMOS, etc.) |
| Dimensions | Dimensions | Dimensions physiques (mm) |
| Max aperture | Ouverture maximale | Valeur d'ouverture maximale |
| Min. shutter speed | Vitesse d'obturation minimale | Vitesse d'obturation minimale |
| White balance presets | Préréglages de balance des blancs | Nombre de préréglages de balance des blancs |
| Macro focus range | Plage de mise au point macro | Distance minimale de mise au point pour la photographie macro |
| Optical zoom | Zoom optique | Si le zoom optique est disponible |
| USB | USB | Type d'interface USB |
| Weight | Poids | Poids de l'appareil photo (g) |
| Max. aperture (35mm equiv.) | Ouverture max. (équiv. 35mm) | Ouverture maximale en équivalent 35mm |
| Focal length (35mm equiv.) | Longueur focale (équiv. 35mm) | Plage de longueur focale en équivalent 35mm |
| Also known as | Aussi connu sous le nom | Noms ou modèles alternatifs |
| Aperture priority | Priorité à l'ouverture | Si le mode priorité à l'ouverture est disponible |
| Max. image resolution | Résolution d'image maximale | Résolution d'image maximale en pixels |
| Max. shutter speed | Vitesse d'obturation maximale | Vitesse d'obturation maximale |
| Storage types | Types de stockage | Supports de stockage compatibles |
| Effective megapixels | Mégapixels effectifs | Mégapixels effectifs utilisés pour la capture d'image |
| Megapixels | Mégapixels | Nombre de mégapixels marketing |
| Max. video resolution | Résolution vidéo maximale | Résolution vidéo maximale |
| Screen size | Taille d'écran | Taille de l'écran LCD en pouces |
| Metering | Mesure | Modes de mesure disponibles |
| Digital zoom | Zoom numérique | Si le zoom numérique est disponible |
| Shutter priority | Priorité à l'obturation | Si le mode priorité à l'obturation est disponible |
| Sensor size | Taille du capteur | Dimensions physiques du capteur (mm) |
| Viewfinder | Viseur | Type de viseur |
| Screen resolution | Résolution d'écran | Résolution de l'écran LCD en points |
| ISO | ISO | Plage de sensibilité ISO disponible |

## Format des Données

Les données sont disponibles dans deux formats :

1. **CSV** : Format tabulaire simple adapté aux applications de tableur et aux outils d'analyse de données
2. **JSON** : Format structuré idéal pour les applications web et la programmation

### Exemple JSON

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

## Utilisations

Cet ensemble de données peut être utilisé pour :

- Analyse du marché des appareils photo
- Recherche en vision par ordinateur
- Formation de modèles d'apprentissage automatique
- Systèmes de recommandation d'appareils photo
- Fins éducatives

## Nettoyage des Données

Les données ont été nettoyées pour :
- Supprimer les colonnes vides
- Standardiser les noms de colonnes
- Trier par marque et année de sortie (ordre décroissant)
- Convertir toutes les valeurs manquantes en null au format JSON

## Licence

Cet ensemble de données est publié sous la licence MIT. Vous êtes libre de l'utiliser à des fins commerciales et non commerciales.

## Contributions

Les contributions pour améliorer l'ensemble de données sont les bienvenues. Veuillez soumettre une pull request ou ouvrir une issue pour discuter de vos idées.

## Remerciements

Merci à tous les fabricants d'appareils photo et aux sites d'évaluation qui ont rendu disponibles les spécifications originales. 
