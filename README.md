<h1 align="center">
<img src="https://github.com/AitorHernandez1/RFI/blob/main/ad5494c8f35d4e3e8343b48ccb45afaa.png?raw=true" width="100">
</h1><br>

# RFI: Importancia de características para modelos de regresión

[![PyPI Latest Release](https://img.shields.io/pypi/v/outdpik.svg)](https://pypi.org/project/RFI/)
[![Package Status](https://img.shields.io/pypi/status/pandas.svg)](https://pypi.org/project/RFI/)
[![Documentation Status](https://readthedocs.org/projects/outdpik/badge/?version=latest)](https://outdpik.readthedocs.io/en/latest/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Description
RFI es un paquete de python diseñado para evaluar conjuntos de datos extrayendo sus variables más importantes con el fin de optimizar el entrenamiento del modelo.

## Por qué RFI?
Por qué utilizar la RFI en lugar de otras técnicas de selección de variables?

- Optimización
- Basado en algoritmo de Random Forest
- El resultado es un DF, una vez obtenido, solamente es necesario entrenarlo.

## Donde descargarlo
El código fuente está actualmente disponible en GitHub:
https://github.com/AitorHernandez1/RFI

El instalador de la última versión publicada está disponible en el [Python
Package Index (PyPI)](https://pypi.org/project/RFI)

```sh
# PyPI
pip install RFI
```

## Cómo usar RFI
Ejemplos de consifuración de RFIrfi:

```python
import RFI
rfi = RFI()
```

Le proporcionamos un DataFrame de pandas:

```python
importances = RFI.seleccion_modelo_regression(df)
```
Plotting advantages:

```python
outdp.plot_outliers(df = df, col = "x")
```
<h1 align="center">
<img src="https://github.com/DanielPuentee/outdpik/blob/main/branding/logo/primary/graph.png?raw=true" width=450 alt="Strip plot outliers detection">
</h1><br>

## Dependencies
- [pandas - Provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive](https://pandas.pydata.org/)
- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org)
- [SciPy - Includes modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more](https://scipy.org/)
- [matplotlib - Comprehensive library for creating static, animated, and interactive visualizations in Python](https://matplotlib.org/)
- [seaborn - Provides a high-level interface for drawing attractive statistical graphics](https://seaborn.pydata.org/)

## License
This project is licensed under the terms of the [GNU](https://github.com/DanielPuentee/outdpik/blob/main/license.txt) - see the LICENSE file for details.

## Documentation
The official documentation is hosted on: https://outdpik.readthedocs.io/en/latest/

## Development
Want to contribute? Great!
Open a discussion in Github in this repo and we will answer as soon as possible.
