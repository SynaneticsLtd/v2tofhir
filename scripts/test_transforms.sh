#!/bin/bash

V2_MESSAGES=../v2
TEMPLATES=../templates
EXPECTED_FHIR=../fhir
TMP_FHIR=/tmp/fhir

mkdir -p $TMP_FHIR

for v2msg in $V2_MESSAGES/*.v2; do
  BASE_V2_NAME=$(basename $v2msg | cut -f 1 -d '.');

  for template in $TEMPLATES/*$BASE_V2_NAME*.mustache; do

    BASE_TEMPLATE_NAME=$(basename $template | cut -f 1 -d '.');
    python ../v2tofhir.py -m $v2msg -t $template > $TMP_FHIR/$BASE_TEMPLATE_NAME.json;
  
  done

done

diff -bur $EXPECTED_FHIR $TMP_FHIR
if [ $? -ne 0 ]; then
    echo "Transform differs from expected output in FHIR directory.";
    exit 1;
fi
