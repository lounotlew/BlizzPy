# BlizzPy - An Open-Source Blizzard API Wrapper Library for Python
> Written by Lewis Kim

### Description

_*This project is in no way affiliated with Blizzard Entertainment._

BlizzPy is a Blizzard API wrapper for Python. It fetches the raw json data from the Blizzard API in Python dictionaries, lists, or ``pandas`` dataframes, with many built-in functions that clean, process, and filter the data from the API for the user. This means that the users will always have the option to retrieve the raw API data as-is through BlizzPy, or can choose to retrieve them in more organized, specific data structures (e.g. choosing to retrieve a dictionary whose keys are guild member names and values are guild ranks, instead of processing the raw data themselves, or retrieving a player's winrate for a specific SC2 season).

BlizzPy currently supports the WoW Community API, SC2 Community API, and D3 Community API (for US, EU, and KR), with the Game Data API and WoW Game Data API being added very soon.

Click [here](https://github.com/lounotlew/BlizzPy/tree/master/docs) to view documentations for BlizzPy.

Current version: ``v1.0.2``

### Installation

BlizzPy was written in Python 3.6, and will not work with Python 2.

You can easily install BlizzPy through ``pip``:

``pip install blizzpy``

or, if you have both Python 2 and Python 3 installed:

``pip3 install blizzpy``

PyPI Link: https://pypi.org/project/BlizzPy/#description

### References

References to the libraries and packages used in BlizzPy:

1) ``pandas`` (https://pandas.pydata.org/)
2) ``urllib`` (https://docs.python.org/3/library/urllib.html)
3) ``json`` (https://docs.python.org/3/library/json.html)
4) ``requests`` (https://www.pythonforbeginners.com/requests/using-requests-in-python)

