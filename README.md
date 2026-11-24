# Business Analytics & Financial Market Visualization

> A multi-dimensional data visualization project built with **Python,
> NumPy, and Matplotlib**. The project explores relationships between
> stock price, trading volume, market sentiment, marketing spend, and
> daily returns through four complementary visualizations.

------------------------------------------------------------------------

## Project Overview

This project presents a compact business analytics dashboard using a
simulated 10-day dataset. It combines four chart types in a single
dark-themed figure to inspect patterns across financial and business
indicators.

The dashboard contains:

1.  **3D scatter plot** --- compares stock price, trading volume, and
    market sentiment.
2.  **Marketing vs. stock price scatter plot** --- explores the
    relationship between marketing budget and stock price, with
    observations labelled by day.
3.  **Horizontal histogram** --- shows the distribution of daily
    returns.
4.  **Business metrics heatmap** --- compares price, volume, sentiment,
    and marketing metrics over time.

> **Data note:** The values in the current script are illustrative
> sample data. They should not be interpreted as real market
> observations or evidence of causation.

## Technical Specifications

  Specification           Details
  ----------------------- --------------------------------------------------
  Project type            Exploratory data analysis and data visualization
  Programming language    Python
  Numerical computing     NumPy
  Visualization library   Matplotlib
  Dataset size            10 observations
  Input data              Manually defined NumPy arrays
  Figure dimensions       16 × 10 inches
  Figure layout           2 × 2 subplot grid
  Visualization count     4
  Theme                   Matplotlib `dark_background`
  3D visualization        Matplotlib 3D scatter plot
  Colour maps             `viridis` and `hot`
  Output                  Interactive Matplotlib figure window
  Data source             Synthetic / illustrative data

## Visualization Specifications

### 1. Stock Price, Volume & Sentiment --- 3D Scatter

-   **X-axis:** Stock price
-   **Y-axis:** Trading volume
-   **Z-axis:** Market sentiment
-   **Colour encoding:** Sentiment score
-   **Colour map:** `viridis`
-   **Marker size:** 200

**Objective:** Inspect the relationship between stock price, trading
volume, and sentiment across the ten observations.

### 2. Marketing Spend vs. Stock Price --- Scatter Plot

-   **X-axis:** Marketing budget
-   **Y-axis:** Stock price
-   **Marker colour:** Cyan
-   **Marker size:** 150
-   **Annotations:** Each observation is labelled from Day 1 to Day 10.

**Objective:** Visually inspect whether higher marketing spend coincides
with higher stock prices in the sample. This chart does not establish
causation.

### 3. Distribution of Daily Returns --- Horizontal Histogram

-   **Input variable:** Daily returns
-   **Number of bins:** 5
-   **Orientation:** Horizontal
-   **Bar colour:** Orange
-   **Edge colour:** White

**Objective:** Examine the frequency distribution and spread of the
daily return observations.

### 4. Business Metrics --- Heatmap

-   **Rows:** Stock price, trading volume, sentiment, and marketing
    budget
-   **Columns:** Ten observation days
-   **Volume transformation:** Divided by 10,000 for display
-   **Colour map:** `hot`
-   **Aspect ratio:** Automatic
-   **Colour scale:** Displayed using a colour bar

**Objective:** Compare how the four business metrics vary across the
observation period.

**Interpretation note:** The metrics have different units and scales.
The current heatmap uses raw values, with volume rescaled. For rigorous
cross-metric comparison, standardize each row (for example, using
z-scores) before plotting.

## Dataset Specifications

The project uses six NumPy arrays:

  Variable          Number of values Description
  --------------- ------------------ -----------------------------------------------------
  `days`                          10 Observation numbers, from Day 1 to Day 10
  `stock_price`                   10 Illustrative stock price values
  `volume`                        10 Illustrative trading volume
  `sentiment`                     10 Illustrative market sentiment scores
  `marketing`                     10 Illustrative marketing budget values
  `returns`                       10 Daily return observations, expressed as percentages

### Data characteristics

-   Observation period: 10 days
-   Stock price range: 420--560
-   Trading volume range: 100,000--350,000
-   Sentiment score range: 50--95
-   Marketing budget range: 20--60
-   Daily returns: positive and negative values

All values are sample data embedded directly in the Python script.

## Technologies Used

-   **Python** --- core programming language
-   **NumPy** --- numerical arrays and data handling
-   **Matplotlib** --- chart creation and figure layout
-   **Matplotlib 3D toolkit** --- three-dimensional scatter
    visualization

## Requirements

-   Python 3.9 or later
-   NumPy
-   Matplotlib

## Installation

``` bash
pip install numpy matplotlib
```

## Execution

Save the Python script as `main.py`, then run:

``` bash
python main.py
```

The dashboard will open in a Matplotlib figure window.

## Project Structure

``` text
business-analytics-visualization/
│
├── main.py
├── README.md
└── requirements.txt
```

### Example `requirements.txt`

``` text
numpy
matplotlib
```

## Key Learning Outcomes

-   Creating and manipulating numerical arrays with NumPy
-   Building scatter plots, histograms, heatmaps, and 3D visualizations
-   Customizing Matplotlib figures with themes, labels, annotations, and
    colour maps
-   Combining multiple visualizations into a single dashboard
-   Understanding how to communicate patterns and limitations in visual
    analysis

## Limitations

-   The dataset is synthetic and contains only ten observations.
-   The charts are exploratory and do not perform statistical inference.
-   Correlation or visual association should not be interpreted as
    causation.
-   The heatmap uses variables with different units and scales.
-   No external data source, live market feed, or predictive model is
    connected.

## Future Improvements

-   Replace sample values with a documented real-world dataset.
-   Add CSV data loading or API integration.
-   Standardize metrics before comparing them in the heatmap.
-   Add correlation analysis and trend lines where statistically
    appropriate.
-   Include axis units, legends, and more detailed chart formatting.
-   Export the dashboard and individual charts as high-resolution image
    files.
-   Build an interactive version using Plotly or Streamlit.

## Author

**Sufiyan Rajput**

-   GitHub: [GitHub Profile](https://github.com/Sufiyan098)
-   LinkedIn: [LinkedIn
    Profile](https://www.linkedin.com/in/sufiyan-rajput-877426305/)

------------------------------------------------------------------------

```{=html}
<p align="center">
```
`<strong>`{=html}Built with Python · NumPy ·
Matplotlib`</strong>`{=html}`<br>`{=html} `<sub>`{=html}Learning through
data, one visualization at a time.`</sub>`{=html}
```{=html}
</p>
```
