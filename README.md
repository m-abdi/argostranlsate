# Argostranslate
A versatile translation service offering multiple interfaces for easy integration into various workflows.

## Features
- Support for multiple interfaces including gRPC and CLI.
- Easy to set up and use with Docker support.

## Requirements
- Python 3.12.2 (or higher)
- Compatible with major operating systems.





## Installation

1. Clone the repository:
```
git clone https://github.com/m-abdi/argostranlsate.git
```

2. Install the requirements:
```
pip install -r requirements.txt
```
3. Set the required environment variables in the `.env` file (see `.env.example` for a template).


## Usage

### Source code:

#### gRPC Interface
- Ideal for applications requiring remote procedure calls.
- To start the gRPC server:
 ```
python src/interfaces/grpc/argostranslate.py
 ```
> Note: The default port for the server is 50051.

#### CLI Interface
 ```
python -m src.interfaces.cli.cli 'سلام' --from-lang fa --to-lang en
 ```


### Docker:

#### CLI 
```
docker run -e ARGOS_PACKAGES_DIR="/app/models" -e ARGOS_DEVICE_TYPE="cpu" mordad/argostranslate:cli python -m src.interfaces.cli.cli 'سلام' --from-lang fa --to-lang en
```

#### gRPC
```
docker run -e ARGOS_PACKAGES_DIR="/app/models" -e ARGOS_DEVICE_TYPE="cpu" mordad/argostranslate:grpc
```