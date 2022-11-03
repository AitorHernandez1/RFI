<h1 align="center">
<img src="https://github.com/AitorHernandez1/RFI/blob/main/ad5494c8f35d4e3e8343b48ccb45afaa.png?raw=true" width="100">
</h1><br>

# RFI: Importancia de características para modelos de regresión
![PyPI](https://img.shields.io/pypi/v/RFI)
[![Package Status](https://img.shields.io/pypi/status/pandas.svg)](https://pypi.org/project/RFI/)

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
La librería devolverá el dataframe conteniendo las variables más importantes.

## Dependencies
- [pandas - Proporciona estructuras de datos rápidas, flexibles y expresivas, diseñadas para que trabajar con datos "relacionales" o "etiquetados" sea fácil e intuitivo.](https://pandas.pydata.org/)
- [NumPy - Añade soporte para matrices multidimensionales de gran tamaño, matrices y funciones matemáticas de alto nivel para operar con estas matrices](https://www.numpy.org)
- [Scikit-learn - Herramientas sencillas y eficaces para el análisis predictivo de datos.](https://scikit-learn.org/stable/)
## Licencia
This project is licensed under the terms of the [MIT](https://github.com/AitorHernandez1/RFI/blob/main/LICENSE.txt) - see the LICENSE file for details.
