![Wine Quality](https://github.com/ruturaj0626/Exploring-Wine-Quality-EDA-ML/blob/main/stuff/Wine_Quality2.png)

# Exploring Wine Quality: EDA and Machine Learning

This repository contains code and data for exploring wine quality through exploratory data analysis (EDA) and machine learning (ML) techniques.

## Overview

This project aims to analyze and predict wine quality based on various chemical properties using machine learning models. The main steps involved include data preprocessing, model training, evaluation using regression metrics, and visualization of results.

## Project Structure

The project is structured as follows:

```
project/
│
├── data/
│   └── winequality-red.csv               # Dataset file (not part of this project)
│
├── data_processing.py             # Module for data preprocessing
├── hyperparameters.py             # Module defining hyperparameters for models
├── modeling.py                    # Module for training machine learning models
├── metrics.py                     # Module containing evaluation metrics
├── visualization.py               # Module for visualizing results
└── main_script.py                 # Main script to run the entire pipeline
```

## Modules

- **data_processing.py**: Contains functions for preprocessing the dataset, including scaling numerical features.
  
- **hyperparameters.py**: Defines hyperparameters used in machine learning models, such as Random Forest regressor parameters.

- **modeling.py**: Implements functions for training machine learning models, specifically a Random Forest regressor in this project.

- **metrics.py**: Provides functions for evaluating the performance of machine learning models using regression metrics like Mean Squared Error (MSE) and R-squared (R2) score.

- **visualization.py**: Includes functions for visualizing feature importances and predicted vs actual values using matplotlib and seaborn.

- **main_script.py**: Orchestrates the entire pipeline, from loading the dataset to model evaluation and visualization.

## Setup

To run this project, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/your_username/exploring-wine-quality.git
   cd exploring-wine-quality
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Run the main script**:
   ```
   python main_script.py
   ```

## Requirements

- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
