# VogueX
  Copyright (c) 2024 Group 83: Jayesh Gajbhar, Skanda Shastry, Swapnil Santosh Jakhi
  
  This project is licensed under the MIT License.
  
# Governance Model:
This project follows an open governance model, which includes a leadership team,
contribution guidelines, a code of conduct, and a clear decision-making process.
Contributions are welcome, and please see CONTRIBUTING.md for details.


## vogueX Fashion Recommender: Outfit Recommendation System




[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/SE-Fall-24-4GPA/VogueX/blob/master/README.md)

<a href="https://github.comSE-Fall-24-4GPA/VogueX/blob/master/LICENSE.md">
  <img src="https://img.shields.io/github/license/SE-Fall-24-4GPA/VogueX?style=flat-square" alt="License">
</a>

[![Github Repo size in bytes](https://img.shields.io/github/languages/code-size/SE-Fall-24-4GPA/VogueX)](https://github.com/SE-Fall-24-4GPA/VogueX)

![Code](https://img.shields.io/badge/codecov-89.3-blue?logo=codecov)

[![DOI](https://zenodo.org/badge/568223471.svg)](https://zenodo.org/badge/latestdoi/568223471)


[![GitHub issues](https://img.shields.io/github/issues/SE-Fall-24-4GPA/VogueX)](https://github.com/SE-Fall-24-4GPA/VogueX/issues?q=is%3Aopen)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/SE-Fall-24-4GPA/VogueX)](https://github.com/SE-Fall-24-4GPA/VogueX/issues?q=is%3Aissue+is%3Aclosed)
[![Github pull requests](https://img.shields.io/github/issues-pr/SE-Fall-24-4GPA/VogueX)](https://github.com/SE-Fall-24-4GPA/VogueX/pulls)
[![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/SE-Fall-24-4GPA/VogueX)](https://github.com/SE-Fall-24-4GPA/VogueX/pulls?q=is%3Apr+is%3Aclosed)

![Code2](https://img.shields.io/badge/flake8_lint-passing-green)
![Code3](https://img.shields.io/badge/Lint_python-passing-green)


[![Black Formatting](https://github.com/NC-State-24/VogueX/actions/workflows/format.yml/badge.svg)](https://github.com/SE-Fall-24-4GPA/VogueX/actions/workflows/format.yml)
[![Build Status](https://circleci.com/gh/NC-State-24/VogueX.svg?style=svg)](https://app.circleci.com/organization/circleci/DxsXpwKSZUv8WE3VKZ4stk)
# Fashion Recommender: A Style for Every Story 🌦👗

Have you ever picked out the perfect outfit for a big day, only to realize the weather had other plans? Or maybe you wished your wardrobe knew just when to swap out those summer florals for cozy winter knits?

**Our Fashion AI Assistant is here to revolutionize your outfit choices**—not just by helping you stay stylish, but by keeping you comfortable and prepared for whatever the day brings. This isn’t just any fashion recommender; it’s your personal style assistant that thinks ahead.


## 🔍 Advanced Features with Streamlit, ChromaDB, and Docker

1. **Streamlit UI for Enhanced User Experience**: The front-end is now powered by Streamlit, providing an interactive and user-friendly interface for real-time fashion recommendations. No need to deal with traditional HTML and CSS—simply enjoy dynamic, responsive web applications built with Python.

2. **ChromaDB for Efficient Data Handling**: We've replaced MySQL with ChromaDB, ensuring faster and more efficient data storage and retrieval using embeddings. This upgrade enhances the performance of our recommendation engine, especially when managing large datasets for machine learning models and user preferences.

3. **Dockerized for Easy Deployment**: The entire application is Dockerized for streamlined deployment. With Docker, you can run the app in any environment without the hassle of manual configurations, ensuring portability, consistency, and quick scalability.



## 🔍 Fashion Advice Powered by llama3.2 and Advanced Integrations
Our AI Fashion Assistant leverages a cutting-edge LLM model llama3.2 powered by Ollama, seamlessly integrated with enhanced tools to deliver dynamic, personalized fashion recommendations.

1. **User Preference Analytics with ChromaDB**: With ChromaDB handling data storage and retrieval using efficient embeddings, our system continually tracks your evolving style preferences. This ensures accurate, data-driven insights tailored to your unique fashion profile.
2. **Real-Time Weather Integration**: Stay fashion-forward and comfortable. Our AI assistant considers real-time weather data to offer outfit suggestions that match current conditions, whether it’s sunny, rainy, or chilly.


## 📈 Data Analytics Section

Get to know your fashion profile! Dive into our analytics to understand your most-worn colors, favorite types of clothing, and how your preferences shift over time. Our recommender grows with you, ensuring it’s always up-to-date with your style.

---

> We believe “A style for every story” is more than just a tagline—it’s a promise. Let our Fashion Recommender become your go-to style partner, no matter the weather, season, or occasion.


## Demo

[Click here to watch our demo!](https://www.youtube.com/watch?v=fjKFcISW2Hg&ab_channel=JayeshGajbhar) <br>


## 🚀 Installation Procedure

## 1. Prerequisites
Python 3.12+

Docker

Ollama

## 2. Local Setup
`git clone https://github.com/yourusername/voguex.git`

`cd voguex`

`python -m venv venv`

`#Linux/Mac: source venv/bin/activate  # Windows: venv\Scripts\activate`

`pip install -r requirements.txt`

`cp .env.copy .env  # Configure your API keys`


## 3. Docker Setup
`docker build -t voguex .`

`docker run -it -p 8501:8501 --add-host=host.docker.internal:host-gateway voguex`

Access at http://localhost:8501

Note:

Ensure Ollama is running locally before starting the application.
command = `ollama serve`

## Contributors:
- Jayesh Gajbhar (jgajbha)
- Skanda Shastry (sshastr4)
- Swapnil Santosh Jakhi (sjakhi)

> This project was completed as part of **Project 3 for the CSC510 Software Engineering** class in the NC State Graduate Program for Computer Science and was built upon the original repository by [NC-State-24/VogueX---Fashion-Recommender](https://github.com/NC-State-24/VogueX).

## More Details - Documentation
Please visit the below link for more details on our project and various use cases detailing all the release cycles.
https://voguex-docs.surge.sh/


## License
[MIT License](https://github.com/pncnmnp/SE21-project/blob/Developer/LICENSE.md)


