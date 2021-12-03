# Netzwerk Tracker

Netzwerk Tracker is a Python library for dealing with bad internet connections.<br/>
It will try to ping every X seconds randomly most common internet sites. <br/>
All made requests get tracked into a `track.txt` with timestamp and data.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Netzwerk Tracker. <br/>

```bash
pip install --no-cache-dir -r requirements.txt
```

## Docker

You can also use the provided DOCKERFILE to run Netzwerk Tracker within a Docker Container.

### Build the Image

```bash
docker build -t netzwerk-tracker .
```

## Usage

You can run Netzwerk Tracker directly on your system or with the provided Docker image.

### System

```bash
python ./tracker.py
```
### Docker

(Don't forget to build the image beforehand!)

```bash
docker run -it --rm --name my-tracker netzwerk-tracker
```

Note: This will run a single-use (--rm) container. It will disappear after exiting.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)