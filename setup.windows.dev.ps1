# install venv
python3 -m venv .venv

# install requirements
.venv\Scripts\pip install -r requirements.txt

# activate venv
.venv\Scripts\activate

# set Variable FLASK_APP
Set-Variable FLASK_APP=src.program