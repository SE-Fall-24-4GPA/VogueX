
## vogueX Fashion Recommender: Outfit Recommendation System

[![Build Status](https://circleci.com/gh/mukunda-p/vogueX---Fashion-Recommender/tree/dev.svg?style=svg)](https://circleci.com/gh/mukunda-p/vogueX---Fashion-Recommender/tree/dev)

[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/blob/dev/README.md)

<a href =https://github.com/mukunda-p/vogueX---Fashion-Recommender/blob/dev/LICENCE.md><img src=https://img.shields.io/github/license/mukunda-p/vogueX---Fashion-Recommender></a>

[![Github Repo size in bytes](https://img.shields.io/github/languages/code-size/mukunda-p/vogueX---Fashion-Recommender)](https://github.com/mukunda-p/vogueX---Fashion-Recommender)

[![codecov](https://codecov.io/gh/mukunda-p/vogueX---Fashion-Recommender/branch/dev/graph/badge.svg?token=O08MSPU0WT)](https://codecov.io/gh/mukunda-p/vogueX---Fashion-Recommender)

[![DOI](https://zenodo.org/badge/568223471.svg)](https://zenodo.org/badge/latestdoi/568223471)


[![GitHub issues](https://img.shields.io/github/issues/mukunda-p/vogueX---Fashion-Recommender)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/issues?q=is%3Aopen)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/mukunda-p/vogueX---Fashion-Recommender)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/issues?q=is%3Aissue+is%3Aclosed)
[![Github pull requests](https://img.shields.io/github/issues-pr/mukunda-p/vogueX---Fashion-Recommender)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/pulls)
[![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/mukunda-p/vogueX---Fashion-Recommender)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/pulls?q=is%3Apr+is%3Aclosed)

[![github workflow](https://github.com/mukunda-p/vogueX---Fashion-Recommender/actions/workflows/style_checker.yml/badge.svg)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/actions/workflows/style_checker.yml)
[![github workflow](https://github.com/mukunda-p/vogueX---Fashion-Recommender/actions/workflows/main.yml/badge.svg)](https://github.com/mukunda-p/vogueX---Fashion-Recommender/actions/workflows/main.yml)

## 💎Description</br>
Has it ever happened that you were all set with the perfect dress for your big day but you forgot to take a rain check? 

Well, don’t worry. Our fashion recommender is here to save your day. This ain’t any regular fashion recommender but a recommender that will look out for you not only in terms of style but in terms of comfort. Now you may think how would one do that? We do this by providing you choices based on:

  - Weather of the day, to let you know if you should avoid certain apparel or carry some extra accessories
  - Season to illustrate different patterns
  - Occasion to keep you in check with the highest rated choices 

There is feature of favourites where you can add your favourite attires to the favourites collection and can remove attires from the favourites.
We suggest Shopping links from e-commerce websites for the selected attires by distinguishing prices.

And if this doesn’t seem enough, one can extend this in a thousand different ways, some of which are:

Create history tabulation of preferences
Store cache for previous 5 prefernces to improve efficiency and reduce load.
Integrating the calendar app to take care of the important days and send a recommendation accordingly.

We have “A style for every story” so let it be known to the world :)

## Demo

[Click here to watch our demo!](https://drive.google.com/file/d/1q5wm0qu7Mw8gSYmC17TGPrOo3cX7KVop/view?usp=sharing) <br>


## 🚀 Installation Procedure

## 1. Prerequisites 

Guides on how to install:
  * [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  * Install python virtual environment if needed, if you do not want to hurt the python libraries on your system. 
  for Linux:
  
  `sudo apt-get install python3-virtualenv`
  
  create virtualenv:
  
  `virtualenv venv`

  Have mysql installed : https://www.mysql.com/downloads/
    note down its port(default 3306)
    

## 2. Deploying

First, clone the repository:


$ git clone git@github.com:mukunda-p/vogueX---Fashion-Recommender.git


Change working directory to the repository:


$ cd vogueX---Fashion-Recommender


For integration of mysql:

  update __init__.py with credentials for mysql

  and run the SQL schema


We have made a python script to run the application.
Just run 

$ python3 main.py


### 3. Follow the provided address and enjoy!


http://localhost:5000/


## Contributors:
- Haricharan Bharathi
- Gokul Prakash Ramesh
- Raghunandan Ganesh Mante


## License
[MIT License](https://github.com/pncnmnp/SE21-project/blob/Developer/LICENSE.md)


