# Color Replacement Script for XML Files

A Python script that automates the process of finding and replacing specific colors in XML files, particularly in `colors.xml` files found within a specified input directory and its subdirectories. This script generates corresponding target colors based on the original color's hue and handles invalid color values while preserving the original XML file structure.

## Features

- Automates the color replacement process in XML files
- Generates corresponding target colors based on the original color's hue
- Handles invalid color values
- Preserves the original XML file structure

## Requirements

- Python 3
- The `os`, `re`, and `colorsys` libraries are utilized and included in the standard Python installation

## Usage

1. Update the `input_directory` and `output_directory` variables in the script to match your local environment.
2. Customize the target colors and hues based on user requirements
3. Ensure the script has permission to access and modify files in both the input and output directories.
4. Run the script using your Python environment or by executing `python script_name.py` in your command line or terminal.

## Contributing

Feel free to contribute to this project by reporting issues, suggesting improvements, or submitting pull requests.
