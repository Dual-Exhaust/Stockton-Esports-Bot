# !bin/sh
source env/bin/activate;
set -a; source ./.env; set +a;
python3.7 main.py;
