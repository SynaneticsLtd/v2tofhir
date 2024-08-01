FIELD_NAME = "Field-"
REPETITION_NAME = "Repetition-"
COMPONENT_NAME = "Component-"
SUBCOMPONENT_NAME = "SubComponent-"

def convert(path: str):
  message = read_message(path)
  v2json = parse_message(message)
  
  return v2json


def read_message(path: str):
  f = open(path, "r")
  
  return f.read()
  

def parse_message(message):
  segements = message.splitlines()
  
  json_dict = {}
  
  for segment_index, segement in enumerate(segements):
    segement_dict = parse_segment(segement, segment_index)
    json_dict.update(segement_dict)  
  
  return json_dict


def parse_segment(segement: str, segment_index: int):
  fields = segement.split('|')
  
  return parse_fields(fields, segment_index)
  

def parse_fields(fields: list, segment_index: int):
  segment_key = fields[0] + "-" + str(segment_index)
  
  segment_dict = {}
  segment_dict[segment_key] = {}

  for i, field in enumerate(fields[1:]):
    repetitions = field.split('~')
    repetitions_dict = {}
  
    for k, repetition in enumerate(repetitions):
      components = repetition.split('^')
      components_dict = {}
    
      for m, component in enumerate(components):
        subcomponents = component.split('&')
        subcomponents_dict = {}
      
        for n, subcomponent in enumerate(subcomponents):
          subcomponents_dict[SUBCOMPONENT_NAME + str(n)] = subcomponent
      
        components_dict[COMPONENT_NAME + str(m)] = subcomponents_dict
    
      repetitions_dict[REPETITION_NAME + str(k)] = components_dict
  
    segment_dict[segment_key][FIELD_NAME+str(i)] = repetitions_dict
  
  return segment_dict
