# option 1: virtual environment
python3 -m venv venv
source venv/bin/activate

# poetry install, don't need to create venv separately
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry --version

poetry new <project-name>
poetry init
poetry init --no-interaction

poetry install
poetry run python -c "from fastapi import FastAPI; print('FastAPI OK')"
