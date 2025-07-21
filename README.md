# Interactive Climate Change Visualizations

This project is a data visualization coursework submission that explores historical climate change trends using interactive charts and maps. Built entirely with D3.js, it presents a series of web-based visualizations to analyze global and zonal temperature anomalies from 1880 to the present.

**Live Demo:** 

---

## Research Questions

This project aims to answer the following research questions through interactive data visualization:

* **Q1:** Analyse the development of global average temperature across historical records. Are there detectable changes in the warming trend when comparing the early industrial era (1880 - 1949) with the modern era (1950 – 2024)?
* **Q2:** How do temperature anomalies in the Arctic and Antarctic (polar regions) compare to the global average over the last 70 years?
* **Q3:** Is there visual evidence of accelerated polar amplification in recent decades?

---

## Visualizations

This project includes three distinct, interactive visualizations designed to address the research questions:

### 1. Temperature Anomaly Graph (`graph.html`)

This visualization presents a multi-line chart comparing the temperature anomalies of the **Global** average, the **Arctic**, and the **Antarctic** over time. It directly addresses **Q2** and **Q3** by showing the divergence in warming rates.
* **Interactive Tooltip:** Hover anywhere on the chart to see the precise data for the closest year.
* **Filterable Legend:** Click on a region in the legend to toggle the visibility of its corresponding line, allowing for focused comparisons.

### 2. Zonal Anomaly Map (`main.html`)

This is the main visualization, featuring a choropleth map that displays temperature anomalies across different latitudinal zones for any given year. This provides a clear geographical context for the data.
* **Year Slider:** Drag the slider to seamlessly transition between years.
* **Play/Pause Animation:** Click the play button to start an animated slideshow of climate change from the selected year to the present.
* **Dynamic Title:** The title updates in real-time to show the selected year's global average and its change from the previous year.

### 3. Comparison Dashboard (`map_compare.html`)

This view allows for a direct, side-by-side comparison of two distinct years, combining a visual map with a detailed data table. This visualization is designed to directly address **Q1** by allowing users to compare an early industrial year with a modern one.
* **Year Inputs:** Enter any two years to generate their respective zonal maps.
* **Dynamic Summary:** A summary panel displays the global average for both years and calculates the total change between them.
* **Data Table:** A detailed table provides the precise numerical anomalies for all zones and the calculated difference.

---

## Data Sources & Processing

* **Primary Data Source:** [NASA GISS Surface Temperature Analysis (GISTEMP v4)](https://data.giss.nasa.gov/gistemp/).
* **Geographic Data:** [TopoJSON world atlas](https://github.com/topojson/world-atlas).

A Python script (`csv_make.py`) using the pandas library was developed to process the raw CSV files from NASA. This script cleans, merges, and transforms the data into a single, structured `climate_data.json` file, which serves as the unified data source for all D3.js visualizations.

---

## Technologies Used

* **Visualization:** D3.js (v7)
* **Data Processing:** Python 3 with the pandas library
* **Web:** HTML5, CSS3, JavaScript (ES6)
* **Geographic Data:** TopoJSON
