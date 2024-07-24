# Image Compression using K-Means Clustering

This project implements an image compression algorithm using K-Means clustering. It can significantly reduce the memory footprint of images, saving up to 99% of memory in some cases.

## Description

This Python script uses the K-Means clustering algorithm to compress images by reducing the number of colors used. It works by clustering similar colors together and representing each cluster with its centroid color.

## Features

- Reads image files (JPG, JPEG supported)
- Compresses images using K-Means clustering
- Visualizes original and compressed images side by side
- Calculates and displays memory savings

## Requirements

- Python 3.12
- NumPy
- scikit-learn
- Matplotlib

## Usage

1. Place your image file in the `data/` directory.
2. Run the script:
```bash
python main.py
```
3. When prompted, enter the name of your image file.
4. The script will display the original and compressed images, along with memory usage statistics.

## How it works

1. The script reads the image file and reshapes it into a 2D array of pixels.
2. It applies K-Means clustering (with 100 clusters by default) to group similar colors.
3. Each pixel in the image is then replaced with its closest cluster centroid color.
4. The compressed image is reconstructed and displayed alongside the original.

## Memory Savings

This compression method can save a significant amount of memory, up to 99% in some cases. The exact savings depend on the complexity and color diversity of the original image.

