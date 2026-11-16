# RPS Game

A command line game of Rock Paper Scissors, played against the computer. Includes automated tests and continuous integration with GitHub Actions.

## Prerequisites

Install Python 3.x (for example using Anaconda).

## Setup

1. Clone the repo from GitHub and put it somewhere (like your Desktop):

```sh
git clone https://github.com/lucassuarez0/RPS-Game.git
```

2. Navigate to the local repo from the command line (for example if on your desktop):

```sh
cd ~/Desktop/RPS-Game
```

3. Create a new Anaconda virtual environment called "rps-env" (first time only):

```sh
conda create -n rps-env python=3.11
```

4. Activate the virtual environment (every time you come back to the project):

```sh
conda activate rps-env
```

5. Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Run the example script:

```sh
python app/my_script.py
```

Play the game:

```sh
python app/rps.py

# alternatively:
python -m app.rps
```

## Testing

Run the automated tests:

```sh
pytest
```