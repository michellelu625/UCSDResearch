# Surgeon Ergonomics Analysis Using Wearable Sensor Data

This repository contains data analysis and visualization code developed as part of a research project at **UC San Diego** investigating surgeon ergonomics and back pain using wearable sensor data collected from **Apple AirPods**.

The goal of the project was to analyze time-series motion data recorded during surgical procedures and explore correlations between movement patterns, posture, and reported musculoskeletal strain—particularly back pain.

## Research Context

Surgeons are at high risk for chronic musculoskeletal injury due to prolonged static postures and repetitive movements during operations. This project leverages wearable inertial sensor data to quantitatively analyze physical strain over time and identify patterns that may contribute to ergonomic risk.

Data was collected via a custom application that recorded motion signals from AirPods, including acceleration and rotational measurements across multiple axes.

## What This Repository Contains

- Time-series analysis of inertial sensor data  
- Visualization of motion signals across time  
- Exploratory analysis of acceleration and rotational patterns  
- Cross-axis comparisons (X, Y, Z) for both linear acceleration and rotation  
- Code written in **Python** and **MATLAB** for complementary analysis workflows  

## Analysis Performed

### Sensor Signals Analyzed
- Gravitational acceleration (X, Y, Z axes)  
- Rotational motion (X, Y, Z axes)  
- Timestamped motion signals aligned across channels  

### Methods
- Parsed and cleaned time-series data from Excel exports  
- Converted timestamps for consistent plotting and alignment  
- Visualized sensor signals over time to identify trends, peaks, and posture shifts  
- Compared rotational and acceleration components to infer movement patterns  
- Generated plots to support correlation analysis with reported discomfort and fatigue  

### Example Output
- Acceleration and rotation plotted as continuous time-series  
- Axis-specific plots highlighting posture changes and sustained load  
- Visual evidence of movement variability across surgical sessions  

## Technologies Used

- **Python**
  - `pandas` for data ingestion and preprocessing  
  - `matplotlib` for time-series visualization  
- **MATLAB**
  - Signal processing and supplementary analysis  
- Excel-based sensor data exports  

## Skills Demonstrated

- Time-series data analysis  
- Wearable sensor data processing  
- Data visualization and exploratory analysis  
- Applied biomechanics and ergonomics research  
- Translating raw sensor signals into interpretable insights  
- Cross-tool workflows (Python + MATLAB)  

## Context

This work was completed as part of a UC San Diego research project focused on applying data science and wearable technology to real-world health and ergonomics problems. It represents hands-on experience working with noisy real-world sensor data and extracting meaningful insights relevant to clinical and workplace health.

---

*More advanced or downstream analysis and applications are described in related research materials.*
