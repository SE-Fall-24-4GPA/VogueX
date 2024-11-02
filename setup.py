# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from setuptools import find_packages, setup

setup(
    name="website",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask", "pytest", "flask_testing", "flask_login", "pymysql"],
)
