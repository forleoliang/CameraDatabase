# Base de Données des Appareils Photo

Une base de données open source des spécifications et images d'appareils photo pour la recherche et le développement d'applications.

## Aperçu

Ce dépôt contient des spécifications détaillées de 3 586 appareils photo numériques de différents fabricants, ainsi qu'un échantillon d'images d'appareils photo. L'ensemble de données complet comprend 3 585 images d'appareils photo.

> **Remarque** : En raison des limitations de taille de fichier de GitHub, seul un petit sous-ensemble d'images d'appareils photo est inclus dans ce dépôt. L'ensemble complet d'images peut être fourni sur demande.

## Structure du Dépôt

```
CameraDatabase/
├── data/                          # Répertoire de données
│   ├── camera_data_cleaned.csv    # Spécifications des appareils photo au format CSV
│   ├── camera_data_cleaned.json   # Spécifications des appareils photo au format JSON
│   └── images/                    # Échantillons d'images d'appareils photo
├── README.md                      # Fichier README principal
├── README_en.md                   # Documentation en anglais
├── README_zh.md                   # Documentation en chinois
├── README_ja.md                   # Documentation en japonais
├── README_es.md                   # Documentation en espagnol
└── README_fr.md                   # Documentation en français (ce fichier)
```

## Fichiers de Données

- `data/camera_data_cleaned.csv` : Données de spécifications d'appareils photo au format CSV (37 colonnes)
- `data/camera_data_cleaned.json` : Données de spécifications d'appareils photo au format JSON (mêmes données que CSV)
- `data/images/` : Répertoire contenant des échantillons d'images d'appareils photo au format PNG

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
    "Model": "EOS R5",
    "Year": 2020,
    "image_file": "data/images/canon_eos-r5.jpg",
    "Sensor type": "CMOS",
    ...
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