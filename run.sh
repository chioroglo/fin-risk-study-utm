if [ ! -d "venv" ]; then
    # If not, create a virtual environment
    python -m .venv venv
fi
source .venv/scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd app
clear
flask run --debug --reload --port 5000
cd ../