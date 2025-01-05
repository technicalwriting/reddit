if not test -d venv; python3 -m venv venv; end
. venv/bin/activate.fish
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
deactivate
