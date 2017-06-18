from marshmallow import Schema, fields, ValidationError


TYPES = dict(basic="basic", multifield="multi-field", advanced="advanced")

FIELDS = dict(all="WRD", title="WTT", author="WAT", theme="WSS", editorial="WPU", place="WPL", year="WYR", serie="WSR",
              isbn="WIS", calssification="WCL", system_number="SYS", title_acc="TITG")

SPLIT = dict(yes="N", no="Y")

LANGUAGE = dict(all="", spanish="SPA", english="ENG", french="FRE", german="GER")


def validate_type(v):
    if v not in TYPES:
        raise ValidationError("Type of search not valid")


def validate_request(v):
    if len(v) >= 64:
        raise ValidationError("Request not valid")


def validate_field(v):
    if v not in FIELDS:
        raise ValidationError("Field not valid")


def validate_split(v):
    if v not in SPLIT:
        raise ValidationError("Split not valid")


def validate_language(v):
    if v not in LANGUAGE:
        raise ValidationError("Language not valid")


def validate_year(v):
    if len(v) == 4:
        try:
            return int(v)
        except:
            raise ValidationError("Year not valid")
    else:
        raise ValidationError("Year not valid")


# OBJECT MODEL 'SEARCH'
class SearchSchema(Schema):
    # ID LIBRARY
    library = fields.Str(required=True)
    # NAME COLLECTION
    collection = fields.Str(required=True)
    ## TYPE SEARCH
    type = fields.Str(validate=validate_type)
    # BASIC
    request = fields.Str(required=True, validate=validate_request)
    field = fields.Str(default="all", validate=validate_field)
    split = fields.Str(default="yes", validate=validate_split)
    language = fields.Str(default="all", validate=validate_language)
    from_year = fields.Str(default="", validate=validate_year)
    to_year = fields.Str(default="", validate=validate_year)

    def replace_values(self, data):
        data["request"] = data['request'].encode('UTF-8')

        if "field" in data:
            data["type"] = TYPES[data["type"]]
        else:
            data["type"] = "basic"

        if "field" in data:
            data["field"] = FIELDS[data["field"]]
        else:
            data["field"] = "WRD"

        if "split" in data:
            data["split"] = SPLIT[data["split"]]
        else:
            data["split"] = "N"

        if "language" in data:
            data["language"] = LANGUAGE[data["language"]]
        else:
            data["language"] = ""