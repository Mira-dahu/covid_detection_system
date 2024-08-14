# COVID-19 Detection System

    An AI-powered intelligent social distance detection and mask wearing detection system. The system utilizes the state-of-the-art YOLOv5 object detection algorithm to monitor the locations and behaviors of people in video streams, automatically detecting whether people are maintaining a safe social distance and whether they are properly wearing masks. When violations are detected, the system will promptly issue alerts to remind relevant personnel to take necessary anti-epidemic measures. Unlike traditional fixed surveillance cameras, this system is mounted on a mobile patrol vehicle, allowing it to comprehensively scan public areas and break through monitoring blind spots. Through real-time data visualization, management personnel can keep track of social distance and mask wearing compliance at all times.
## Features

- Social distance detection using YOLOv5
- Mask wearing detection using Mask R-CNN

## Installation

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Download the required model weights (links provided in the Model Setup section)

## Usage

Run the main script:

## Project Structure

- `src/`: Source code
  - `main.py`: Main entry point
  - `social_distance/`: Social distancing detection module
  - `mask_detection/`: Mask detection module
  - `utils/`: Utility functions
- `tests/`: Unit tests
- `configs/`: Configuration files
- `scripts/`: Training and evaluation scripts
- `notebooks/`: Jupyter notebooks for analysis

## Docs Folder Overview  

Detailed documentation is located in the `covid_detection_system\covid_detection_system\docs` folder, intended to provide users with a comprehensive overview of the project and guidance on its usage. The documentation includes the following key sections:  

- Project Background and Motivation  

- Technical Principles Explanation 

- Usage Tutorial  

- Frequently Asked Questions (FAQ)  


## Flowchart  

The system flowchart for the project is shown below, illustrating the overall structure and key functional processes of the project:  

![System Flowchart](https://s2.loli.net/2024/08/15/ObGLzUJfq6H2ma5.png)
## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
