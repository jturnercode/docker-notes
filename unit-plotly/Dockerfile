FROM unit:1.31.0-python3.11

# copy python requirements to image
COPY requirements.txt /config/requirements.txt

# install python requirments
RUN python3 -m pip install -r /config/requirements.txt

# To run code with bind commands comment out below lines (see readme)
COPY /webapp/* /www/
COPY /config/config.json /docker-entrypoint.d/

