# Base de Datos de Cámaras

Una base de datos de código abierto de especificaciones y imágenes de cámaras para investigación y desarrollo de aplicaciones.

## Descripción General

Este repositorio contiene especificaciones detalladas de 3,586 cámaras digitales de varios fabricantes.




## Estructura del Repositorio

```
CameraDatabase/
├── data/                          # Directorio de datos
│   ├── camera_data.csv    # Especificaciones de cámaras en formato CSV
│   ├── camera_data.json   # Especificaciones de cámaras en formato JSON
├── doc/                           # Directorio de documentación
│   ├── README_en.md               # Documentación en inglés
│   ├── README_zh.md               # Documentación en chino
│   ├── README_ja.md               # Documentación en japonés
│   ├── README_es.md               # Documentación en español (este archivo)
│   ├── README_fr.md               # Documentación en francés
│   └── README_de.md               # Documentación en alemán
└── README.md                      # README principal
```




## Archivos de Datos

- `data/camera_data.csv`: Especificaciones de cámaras en formato CSV (37 columnas)
- `data/camera_data.json`: Especificaciones de cámaras en formato JSON (mismos datos que CSV)

## Estructura de Datos

El conjunto de datos incluye los siguientes campos:

| Campo en inglés | Traducción al español | Descripción |
|---------|----------|------|
| Brand | Marca | Fabricante de la cámara |
| Model | Modelo | Nombre del modelo de la cámara |
| Year | Año | Año de lanzamiento |
| image_file | Archivo de imagen | Ruta a la imagen de la cámara |
| Total megapixels | Megapíxeles totales | Número total de megapíxeles |
| Exposure Compensation | Compensación de exposición | Rango de compensación de exposición disponible |
| Normal focus range | Rango de enfoque normal | Rango de distancia de enfoque regular |
| Battery | Batería | Tipo de batería |
| Sensor resolution | Resolución del sensor | Resolución en píxeles (ancho x alto) |
| Crop factor | Factor de recorte | Factor de recorte del sensor |
| Sensor type | Tipo de sensor | Tipo de sensor de imagen (CCD, CMOS, etc.) |
| Dimensions | Dimensiones | Dimensiones físicas (mm) |
| Max aperture | Apertura máxima | Valor de apertura máxima |
| Min. shutter speed | Velocidad mínima del obturador | Velocidad mínima del obturador |
| White balance presets | Preajustes de balance de blancos | Número de preajustes de balance de blancos |
| Macro focus range | Rango de enfoque macro | Distancia mínima de enfoque para fotografía macro |
| Optical zoom | Zoom óptico | Si el zoom óptico está disponible |
| USB | USB | Tipo de interfaz USB |
| Weight | Peso | Peso de la cámara (g) |
| Max. aperture (35mm equiv.) | Apertura máxima (equiv. 35mm) | Apertura máxima en equivalente de 35mm |
| Focal length (35mm equiv.) | Longitud focal (equiv. 35mm) | Rango de longitud focal en equivalente de 35mm |
| Also known as | También conocido como | Nombres o modelos alternativos |
| Aperture priority | Prioridad de apertura | Si el modo de prioridad de apertura está disponible |
| Max. image resolution | Resolución máxima de imagen | Resolución máxima de imagen en píxeles |
| Max. shutter speed | Velocidad máxima del obturador | Velocidad máxima del obturador |
| Storage types | Tipos de almacenamiento | Medios de almacenamiento compatibles |
| Effective megapixels | Megapíxeles efectivos | Megapíxeles efectivos usados para captura de imagen |
| Megapixels | Megapíxeles | Recuento de megapíxeles de marketing |
| Max. video resolution | Resolución máxima de video | Resolución máxima de video |
| Screen size | Tamaño de pantalla | Tamaño de pantalla LCD en pulgadas |
| Metering | Medición | Modos de medición disponibles |
| Digital zoom | Zoom digital | Si el zoom digital está disponible |
| Shutter priority | Prioridad de obturador | Si el modo de prioridad de obturador está disponible |
| Sensor size | Tamaño del sensor | Dimensiones físicas del sensor (mm) |
| Viewfinder | Visor | Tipo de visor |
| Screen resolution | Resolución de pantalla | Resolución de pantalla LCD en puntos |
| ISO | ISO | Rango de sensibilidad ISO disponible |

## Formato de Datos

Los datos están disponibles en dos formatos:

1. **CSV**: Formato tabular simple adecuado para aplicaciones de hojas de cálculo y herramientas de análisis de datos
2. **JSON**: Formato estructurado ideal para aplicaciones web y programación

### Ejemplo JSON

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

## Usos

Este conjunto de datos puede usarse para:

- Análisis del mercado de cámaras
- Investigación en visión por computadora
- Entrenamiento de modelos de aprendizaje automático
- Sistemas de recomendación de cámaras
- Propósitos educativos

## Limpieza de Datos

Los datos han sido limpiados para:
- Eliminar columnas vacías
- Estandarizar nombres de columnas
- Ordenar por marca y año de lanzamiento (descendente)
- Convertir todos los valores faltantes a null en formato JSON

## Licencia

Este conjunto de datos se publica bajo la Licencia MIT. Siéntase libre de usarlo para propósitos comerciales y no comerciales.

## Contribuciones

Las contribuciones para mejorar el conjunto de datos son bienvenidas. Por favor, envíe una solicitud de extracción o abra un problema para discutir sus ideas.

## Agradecimientos

Gracias a todos los fabricantes de cámaras y sitios web de reseñas que hicieron disponibles las especificaciones originales. 
