# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

# Installation Guide for Fashion Recommender

This document provides a comprehensive guide to installing and running the Fashion Recommender application.

## 1. Prerequisites

Before getting started, ensure you have the following software installed:

### Git
You need to have Git installed on your system to clone the repository. Follow the guide below to install Git:

* **[Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)**

### Python
Make sure you have Python 3.x installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### Virtual Environment
To avoid conflicts with existing Python libraries on your system, it is recommended to use a virtual environment. Follow the steps below to set it up:

#### For Linux:

1. **Install the Python Virtual Environment Package**:
   Open a terminal and run the following command:

   ```bash
   sudo apt-get install python3-virtualenv
    ```
2. **Create a Virtual Environment: Navigate to the directory where you want to create your virtual environment and run**:
    `python3 -m venv venv`
3. **Activate the Virtual Environment: To start using the virtual environment, activate it with**:
    `source venv/bin/activate`
### Cloning the Repository

1. **To get the application code, clone the repository using Git. Run the following command in your terminal**:
    `git clone https://github.com/NC-State-24/VogueX.git`

2. **Navigate to the cloned repository**:
    `cd VogueX`

### Install Dependencies

Before running the application, you need to install the required Python packages. Make sure your virtual environment is activated, then run:

`pip install -r requirements.txt`

### Running the Application

Now you are ready to run the application! Execute the following command in your terminal:

`python3 main.py`

After running the application, you can access it in your web browser at:

http://localhost:5000/

Enjoy!
Now you can enjoy using the Fashion Recommender to find the perfect outfit based on your preferences and the current weather!