import json

# Define the json object as a string
json_string = """{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}"""

# Read the Json data into Python
json_data = json.loads(json_string)

'''
Json is the same format as dictionary in that it consist of key, value pairs of various types

If you have a Json in a file, you read the data using load function
'''

with open('data.json') as f:
  data = json.load(f)