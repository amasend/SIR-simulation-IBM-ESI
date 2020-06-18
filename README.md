# SIR-simulation-IBM-ESI
Repository for IBM ESI project. Epidemic SIR mathematical model, simulation and visualization.

# HOW TO RUN

## Docker
First need to install a `docker` from https://docs.docker.com/get-docker/  

After installation run 
```bash
docker run -p 8050:8050 zavioer/sirsimulation:1.1 
```
and go to `127.0.0.1:8050` in your browser.

## PyPi
Second option is install package directly from PyPi. Type
```bash
pip install -i https://test.pypi.org/simple/ sir-simulation==1.0.0
```

Then you must download requirements 
```bash
pip install -r requirements.txt
```

Finally to run simulation with dashboard type 
```bash
python /simulation/app.py
```

## Documentation

Documentation are available in folder `docs`. To
generate it after download change to `docs` and run `make html` in console.
Documentation will be generate do `_build` folder. To see generated docs
run `_build/html/index.html`.

# Licence 
MIT Licence