# v2tofhir
Convert Hl7v2 to FHIR using Mustache templates

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
python v2tofhir.py -m ./v2/dch-ref12.v2 -t ./templates/patient_dch-ref12.mustache > fhir/patient_dch-ref12.json
```