# virtual environment
python3 -m venv panda-agent
source panda-agent/bin/activate
# poetry install
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
poetry --version

poetry new <project-name>
poetry init
poetry init --no-interaction

