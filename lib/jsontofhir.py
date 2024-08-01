import json
import pystache


def convert(v2json: json, template: str):
  template = open(template, "r").read()
  
  return pystache.render(template, v2json)