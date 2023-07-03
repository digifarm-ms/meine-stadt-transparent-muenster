import os

# The settings can be overwritten by mounting a differnt file into the docker container
access_logfile = "-"
port = os.getenv('PORT', '8000')
bind = f"0.0.0.0:{port}"
capture_output = True
log_file = "-"
timeout = 60
workers = 2
