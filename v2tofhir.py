import json
import argparse
from lib import v2tojson
from lib import jsontofhir

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", type=argparse.FileType('r', encoding='UTF-8'), required=True,
                        help="Hl7v2 message to be converted.")
    parser.add_argument("-t", "--template", type=argparse.FileType('r', encoding='UTF-8'), required=True,
                        help="Mustache template to use for message conversion.")

    return parser.parse_args()

def main():
    args = get_args()

    v2json = v2tojson.convert(args.message.name)
    fhir = jsontofhir.convert(v2json, args.template.name)
    
    print(fhir)

if __name__ == "__main__":
    main()
