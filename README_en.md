# Camera Database

An open-source database of camera specifications and images for research and application development.

## Overview

This repository contains detailed specifications for 3,586 digital cameras from various manufacturers, along with a sample of camera images. The full dataset includes 3,585 camera images.

> **Note**: Due to GitHub file size limitations, only a small subset of camera images is included in this repository. The complete image dataset can be provided upon request.

## Data Files

- `camera_data_cleaned.csv`: CSV format camera specifications (37 columns)
- `camera_data_cleaned.json`: JSON format camera specifications (same data as CSV)
- `images/`: Directory containing sample camera images in PNG format

## Data Structure

The dataset includes the following fields:

| Field | Description |
|-------|-------------|
| Brand | Camera manufacturer |
| Model | Camera model name |
| Year | Release year |
| image_file | Path to the camera image |
| Total megapixels | Total number of megapixels |
| Exposure Compensation | Available exposure compensation range |
| Normal focus range | Regular focusing distance range |
| Battery | Battery type |
| Sensor resolution | Resolution in pixels (width x height) |
| Crop factor | Sensor crop factor |
| Sensor type | Type of image sensor (CCD, CMOS, etc.) |
| Dimensions | Physical dimensions (mm) |
| Max aperture | Maximum aperture value |
| Min. shutter speed | Minimum shutter speed |
| White balance presets | Number of white balance presets |
| Macro focus range | Minimum focusing distance for macro photography |
| Optical zoom | Whether optical zoom is available |
| USB | USB interface type |
| Weight | Camera weight (g) |
| Max. aperture (35mm equiv.) | Maximum aperture in 35mm equivalent |
| Focal length (35mm equiv.) | Focal length range in 35mm equivalent |
| Also known as | Alternative names or models |
| Aperture priority | Whether aperture priority mode is available |
| Max. image resolution | Maximum image resolution in pixels |
| Max. shutter speed | Maximum shutter speed |
| Storage types | Compatible storage media |
| Effective megapixels | Effective megapixels used for image capture |
| Megapixels | Marketing megapixel count |
| Max. video resolution | Maximum video resolution |
| Screen size | LCD screen size in inches |
| Metering | Available metering modes |
| Digital zoom | Whether digital zoom is available |
| Shutter priority | Whether shutter priority mode is available |
| Sensor size | Physical sensor dimensions (mm) |
| Viewfinder | Viewfinder type |
| Screen resolution | LCD screen resolution in dots |
| ISO | Available ISO sensitivity range |

## Data Format

The data is available in two formats:

1. **CSV**: Simple tabular format suitable for spreadsheet applications and data analysis tools
2. **JSON**: Structured format ideal for web applications and programming

### JSON Example

```json
{
    "Brand": "Canon",
    "Model": "EOS R5",
    "Year": 2020,
    "image_file": "images/canon_eos-r5.jpg",
    "Sensor type": "CMOS",
    ...
}
```

## Usage

This dataset can be used for:

- Camera market analysis
- Computer vision research
- Machine learning model training
- Camera recommendation systems
- Educational purposes

## Data Cleaning

The data has been cleaned to:
- Remove empty columns
- Standardize column names
- Sort by brand and release year (descending)
- Convert all missing values to null in JSON format

## License

This dataset is released under the MIT License. Feel free to use it for commercial and non-commercial purposes.

## Contributing

Contributions to improve the dataset are welcome. Please submit a pull request or open an issue to discuss your ideas.

## Acknowledgments

Thanks to all the camera manufacturers and review websites that made the original specifications available. 