# VogueX
  Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
  
  This project is licensed under the MIT License.
  
# Governance Model:
This project follows an open governance model, which includes a leadership team,
contribution guidelines, a code of conduct, and a clear decision-making process.
Contributions are welcome, and please see CONTRIBUTING.md for details.


## vogueX Fashion Recommender: Outfit Recommendation System




[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/NC-State-24/VogueX/blob/master/README.md)

<a href="https://github.com/NC-State-24/VogueX/blob/master/LICENSE.md">
  <img src="https://img.shields.io/github/license/NC-State-24/VogueX?style=flat-square" alt="License">
</a>

[![Github Repo size in bytes](https://img.shields.io/github/languages/code-size/NC-State-24/VogueX)](https://github.com/NC-State-24/VogueX)

![Code](https://img.shields.io/badge/codecov-89.3-blue?logo=codecov)

[![DOI](https://zenodo.org/badge/568223471.svg)](https://zenodo.org/badge/latestdoi/568223471)


[![GitHub issues](https://img.shields.io/github/issues/NC-State-24/VogueX)](https://github.com/NC-State-24/VogueX/issues?q=is%3Aopen)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/NC-State-24/VogueX)](https://github.com/NC-State-24/VogueX/issues?q=is%3Aissue+is%3Aclosed)
[![Github pull requests](https://img.shields.io/github/issues-pr/NC-State-24/VogueX)](https://github.com/NC-State-24/VogueX/pulls)
[![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/NC-State-24/VogueX)](https://github.com/NC-State-24/VogueX/pulls?q=is%3Apr+is%3Aclosed)

![Code2](https://img.shields.io/badge/flake8_lint-passing-green)
![Code3](https://img.shields.io/badge/Lint_python-passing-green)


[![Black Formatting](https://github.com/NC-State-24/VogueX/actions/workflows/format.yml/badge.svg)](https://github.com/NC-State-24/VogueX/actions/workflows/format.yml)
[![Build Status](https://circleci.com/gh/NC-State-24/VogueX.svg?style=svg)](https://app.circleci.com/organization/circleci/DxsXpwKSZUv8WE3VKZ4stk)
# Fashion Recommender: A Style for Every Story 🌦👗

Have you ever picked out the perfect outfit for a big day, only to realize the weather had other plans? Or maybe you wished your wardrobe knew just when to swap out those summer florals for cozy winter knits?

**Our Fashion Recommender is here to revolutionize your outfit choices**—not just by helping you stay stylish, but by keeping you comfortable and prepared for whatever the day brings. This isn’t just any fashion recommender; it’s your personal style assistant that thinks ahead.

## 🌟 Key Features

1. **Weather-Based Recommendations**: Never get caught off guard again. Our recommender factors in the day’s weather, suggesting whether to avoid certain apparel or carry extra accessories.
2. **Seasonal Styling**: From spring patterns to fall favorites, get outfits tailored to the season for that on-point, all-year style.
3. **Occasion-Based Selections**: Whether it's a formal dinner or a laid-back brunch, we’ve got your style covered with top-rated options for every event.
4. **Favourites Collection**: Keep track of your top picks by adding items to your favourites, and easily manage your collection by adding or removing items as your style evolves.

## 🔍 Advanced Personalization with MLops

Our Fashion Recommender goes beyond the usual with a robust MLops-powered recommendation pipeline, designed to capture and adapt to your evolving preferences.

- **User Preference Analytics**: Gain insights into your style and make informed fashion decisions. Our data analytics feature tracks current choices and preferences, ensuring a more personalized experience each time.
- **User Ratings for Peer Reviews**: Fashion is better with a second opinion! Now, you can review styles and see ratings from others, making sure you’re always putting your best foot forward.
- **Weather Integration**: Stay comfortable with real-time weather-based outfit suggestions. Rain or shine, our recommender’s got you covered.

## 💡 Endless Possibilities for Extension

Our platform is designed to be expanded in countless ways, making it a versatile tool that adapts to your life:

- **Health & Wellness Integration**: Imagine linking with your health app to predict your menstrual cycle and recommend outfits for maximum comfort.
- **Feedback Mechanism**: Our recommender continuously improves based on your feedback, learning your unique style to offer even better suggestions.
- **Calendar Sync**: Connect your calendar to stay prepared for special events with tailored outfit suggestions for every occasion.

## 📈 Data Analytics Section

Get to know your fashion profile! Dive into our analytics to understand your most-worn colors, favorite types of clothing, and how your preferences shift over time. Our recommender grows with you, ensuring it’s always up-to-date with your style.

---

> We believe “A style for every story” is more than just a tagline—it’s a promise. Let our Fashion Recommender become your go-to style partner, no matter the weather, season, or occasion.


## Demo

[Click here to watch our demo!](https://drive.google.com/file/d/1q5wm0qu7Mw8gSYmC17TGPrOo3cX7KVop/view?usp=sharing) <br>


## 🚀 Installation Procedure

## 1. Prerequisites
Python 3.12+

Docker

Ollama

## 2. Local Setup
`git clone https://github.com/yourusername/voguex.git`

`cd voguex`

`python -m venv venv`

`source venv/bin/activate  # Windows: venv\Scripts\activate`

`pip install -r requirements.txt`

`cp .env.copy .env  # Configure your API keys`


## 3. Docker Setup
`docker build -t voguex .`

`docker run -it -p 8501:8501 --add-host=host.docker.internal:host-gateway voguex`

Access at http://localhost:8501

Note:

Ensure Ollama is running locally before starting the application.


## Contributors:
- Haricharan Bharathi (hbharat2)
- Gokul Prakash Ramesh (gramesh4)
- Raghunandan Mante (rmante)

> This project was completed as part of **Project 2 for the CSC510 Software Engineering** class in the NC State Graduate Program for Computer Science and was built upon the original repository by [mukunda-p/vogueX---Fashion-Recommender](https://github.com/mukunda-p/vogueX---Fashion-Recommender.git).

## More Details - Documentation
Please visit the below link for more details on our project and various use cases detailing all the release cycles.
https://voguex-docs.surge.sh/


## License
[MIT License](https://github.com/pncnmnp/SE21-project/blob/Developer/LICENSE.md)


