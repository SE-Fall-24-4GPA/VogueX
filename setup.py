from setuptools import find_packages, setup

setup(
    name="website",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask", "pytest", "flask_testing", "flask_login", "pymysql"],
)
