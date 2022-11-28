
<!-- PROJECT LOGO -->
# Olympus
_Two Part program that either helps consolidate future CodeSet orders or remove low-volume probes from inventory_.

<!-- ABOUT THE PROJECT -->
## About The Program

This program or tool was built to simply a repetitve task that the oligo team needs to perform.
On average it takes about two hours to set up either process, this allows no manuel work and 
accomplishes the same tasks in a fraction of the time.


### Built With

* [Flask](https://github.com/pallets/flask): Simple web server interface
* [Pandas](https://github.com/pandas-dev/pandas): Easy processing meme text from csv files
* [Pillow](https://github.com/python-pillow/Pillow): Image processing to add text



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

`pdftotext` binary is required and can be installed...
* On Ubuntu 20.04
  ```sh
  sudo apt install poppler-utils
  ```

### Installation

1. Clone this repo.
   ```sh
   git clone https://github.com/Jelvig/meme-generator.git (not active)
   ```
2. Setup [virtual env](virtual-env-docs) inside project folder and activate.
   ```sh
   cd ./meme-generator
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install python deps
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

#### Using the cli

```sh
$ python main.py --help
usage: main.py [-h] [-p PATH] [-b BODY] [-a AUTHOR]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to and image file.
  -b BODY, --body BODY  Body or Content written to image.
  -a AUTHOR, --author AUTHOR
                        Author name written to image.
```
Or run the default options **```python main.py```** to create a meme in ```./tmp```

#### Flask Web Development Server
Starting dev server
```sh
$ export FLASK_APP=app
$ flask run
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Once started(using the default port) go to http://127.0.0.1:5000/


_For more information on this process checkout [Flasks Development Server Documentation](flask-dev-server-docs)_.

## Modules
* pandas
* flask
* requests
* python-docx
