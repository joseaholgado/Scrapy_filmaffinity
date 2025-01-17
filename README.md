## Requirements

- Python 3.12
- Scrapy
- Pandas
- NumPy
- Ipywidgets
- ydata-profiling

## Installation

1. Clone the repository:
    ```sh
    git clone <REPOSITORY_URL>
    cd proyecto-scrapy
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

## Usage

1. Run the spider to extract data:
    ```sh
    cd proyecto_scrapy
    scrapy crawl filmaffinity_spider -O ../datasets/dataset.json
    ```

2. Open the notebook [scrapy.ipynb](http://_vscodecontentref_/10) to convert the data to CSV and perform exploratory analysis:
    ```sh
    jupyter notebook notebooks/scrapy.ipynb
    ```

## Code Structure

- [filmaffinity_spider.py](http://_vscodecontentref_/11): Contains the spider that extracts data from FilmAffinity.
- [scrapy.ipynb](http://_vscodecontentref_/12): Notebook that converts the extracted data to CSV and performs exploratory analysis.



## Requisitos

- Python 3.12
- Scrapy
- Pandas
- NumPy
- Ipywidgets
- ydata-profiling

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd proyecto-scrapy
    ```

2. Instala las dependencias utilizando Poetry:
    ```sh
    poetry install
    ```

## Uso

1. Ejecuta el spider para extraer los datos:
    ```sh
    cd proyecto_scrapy
    scrapy crawl filmaffinity_spider -O ../datasets/dataset.json
    ```

2. Abre el notebook [scrapy.ipynb](http://_vscodecontentref_/10) para convertir los datos a CSV y realizar el análisis exploratorio:
    ```sh
    jupyter notebook notebooks/scrapy.ipynb
    ```

## Estructura del Código

- [filmaffinity_spider.py](http://_vscodecontentref_/11): Contiene el spider que extrae los datos de FilmAffinity.
- [scrapy.ipynb](http://_vscodecontentref_/12): Notebook que convierte los datos extraídos a CSV y realiza un análisis exploratorio.
