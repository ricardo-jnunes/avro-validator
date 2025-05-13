import fastavro
import io
import json

schema_json = {
  "namespace": "com.example.domain",
  "type": "record",
  "name": "Customer",
  "fields": [
    { "name": "document_type", "type": "string" },
    { "name": "document number", "type": "long" },
    { "name": "name", "type": "string" },
    { "name": "title", "type": ["null", "string"], "default": None },
    { "name": "email", "type": "string" },
    {
      "name": "address",
      "type": [
        "null",
        {
          "type": "record",
          "name": "Address",
          "fields": [
            { "name": "address_type", "type": ["null", "string"], "default": None },
            { "name": "street", "type": "string" },
            { "name": "number", "type": "string" }
          ]
        }
      ],
      "default": None
    },
    { "name": "origin", "type": "string" },
    { "name": "updated_date", "type": "string" }
  ]
}

try:
    fastavro.parse_schema(schema_json)
    validation_result = "Valid Schema."
except Exception as e:
    validation_result = f"Error on validating: {str(e)}"

print(validation_result)
