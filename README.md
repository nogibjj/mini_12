[![CI](https://github.com/nogibjj/tinayiluo_mini_12/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/tinayiluo_mini_12/actions/workflows/cicd.yml)

### Project Overview: Airline Safety Prediction Using MLflow

**Objective:**
The project's main aim is to develop a machine learning model capable of predicting the seating capacity of airplanes based on their historical accident and fatality records from 1985 to 2014. A significant aspect of this project is the integration of MLflow, a tool designed to streamline the process of tracking experiments, managing models, and maintaining a systematic workflow in machine learning projects.

**Dataset Overview:**
We utilize the `airline-safety.csv` dataset, sourced from the Aviation Safety Network. This comprehensive dataset covers safety metrics for 56 airlines, presented in a CSV format. It includes weekly data on available seat kilometers and detailed records of incidents, fatal accidents, and fatalities. These records are divided into two distinct periods: 1985–1999 and 2000–2014. The dataset offers a thorough basis for analyzing trends and predicting airline safety standards.

#### [Resource Link](https://github.com/fivethirtyeight/data/tree/master/airline-safety) 

### Project Execution Steps:

1. **Data Loading and Preprocessing**:
    - Initially, the dataset is imported into a Pandas DataFrame for handling and manipulation.
    - The next step involves extracting key features that are relevant to the prediction model.

2. **Model Training**:
    - The dataset is divided into two subsets: training and testing sets, to facilitate a robust model training and evaluation process.
    - The primary focus here is to train the machine learning model using the training set.

3. **MLflow Integration**:
    - MLflow is employed for its robust capabilities in logging various parameters, metrics, and the final trained model.
    - Specific details such as the type of model used and the path of the dataset are meticulously logged.
    - Key performance metrics, including model accuracy, are recorded to evaluate the effectiveness of the model.

### Preparation for Use:
1. Clone the project repository using Git.
2. Install necessary dependencies by executing `make install`.
3. Launch the main application script with `python main.py`.
4. Access the MLflow user interface by running `mlflow ui`. This interface allows for an interactive exploration of the model’s performance and other recorded metrics.
5. Investigate the saved model and related artifacts located in the `mlruns/0` directory for detailed insights.

### Code Quality Assurance:
1. Utilize `make format` to ensure the code is well-formatted and adheres to standard conventions.
2. Apply `make lint` to perform code linting, identifying potential errors or problematic patterns in the code.
3. Conduct comprehensive testing of the codebase using `make test` to confirm functionality and reliability. 

This approach ensures a rigorous, structured, and well-documented procedure for developing a predictive model in the field of airline safety, augmented by MLflow's capabilities in managing and tracking machine learning experiments.