# v2tofhir
Convert Hl7v2 to FHIR using Mustache templates

## Setup

Tested using Python 3.11

With venv:

```sh
python3 -m venv venv

source ./venv/bin/activate

pip install -r ./requirements.txt
```

## Usage

Help:

```sh
python v2tofhir -h
```

```sh
usage: v2tofhir.py [-h] -m MESSAGE -t TEMPLATE

options:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        Hl7v2 message to be converted.
  -t TEMPLATE, --template TEMPLATE
                        Mustache template to use for message conversion.
```

## Examples

```sh
python v2tofhir.py -m ./v2/dch-ref12.v2 -t ./templates/patient_dch-ref12.mustache
```

## Pipeline validation

See https://github.com/SynaneticsLtd/v2tofhir/actions/runs/10248115912 for example of validation output in Artifacts section.

Note: Pipeline continues even if error in validation, so validation output is stored as part of the pipeline run
