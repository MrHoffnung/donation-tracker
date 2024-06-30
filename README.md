# DonationTracker
DonationTracker was written to motivate me to spend more time in my editor. Every day I don't program for at least 90 minutes, I have to donate 1 euro to Plant-for-the-Planet. This simple program tracks that.

## Installation
To use DonationTracker by yourself you have to download Poetry from [here](https://python-poetry.org/docs/#installing-with-the-official-installer). If you have  downloaded Poetry, you can continue with this guide.

### Clone the repository on your machine 
```shell
dsaads
```

### Navigate to the clone
```shell
cd /path/to/the/clone
```

### Run Poetry
```shell
poetry shell
```

### Install the dependencies
```shell
poetry install
```

### Run DonationTracker
```python
python donationtracker
```

If you have completed those steps one time, you just have to navigate to the clone (step 2), enable Poetry (step 3) and run the program (step 5).

## Configuration
To configure the program, you must create a <i>.env</i> file in the root directory of the program. You can use this file to configure the program.

### Changing Currency
To configurate the currency format, you can change the <i>CURRENCY</i> variable. Just replace <i><YOUR_CURRENCY></i> with your currency (default is €).
```
CURRENCY=<YOUR_CURRENCY>
```