from marshmallow import Schema, fields, post_load, ValidationError, validate, pre_load, pre_dump, post_dump

COLLECTION = dict(book="Book", thesis="Thesis", magazine="Magazine" )

TYPES = dict(basic="basic", multifield="multi-field", advanced="advanced")

FIELDS = dict(all="WRD", title="WTT", author="WAT", theme="WSS", editorial="WPU", place="WPL", year="WYR", serie="WSR",
              isbn="WIS", classification="WCL", system_number="SYS", title_acc="TITG")

SPLIT = dict(yes="N", no="Y")

LANGUAGE = dict(all="", spanish="SPA", english="ENG", french="FRE", german="GER")


def validate_collection(v):
    if v not in COLLECTION:
        raise ValidationError("Collection not valid")


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


"""
    FUNCTION
    
    [FIND]
    Parameters:
    - find                      
    func=find-b
    - collection                
    local_base=[Book="l0801"]
    - type
    type=[basic"basic", multifield="multi-field", advanced="advanced"]
    - request : Texto a buscar                    
    request=[string]                        
    - field                       
    find_code=[all="WRD", title="WTT", author="WAT", theme="WSS", editorial="WPU", place="WPL", year="WYR", serie="WSR",
        isbn="WIS", classification="WCL", system_number="SYS", title_acc="TITG"]
    - split                       
    adjacent=[yes="N", no="Y"]
    - language     
    filter_code1=WLN&filter_request_1=[all="", spanish="SPA", english="ENG", french="FRE", german="GER"]
    - from_year
    filter_code_2=WYR&filter_request_2=[YYYY]    
    - to_year
    filter_code_3=WYR&filter_request_3=[YYYY]

    
    [SHORT]
    Parameters:
    - short
    func=short-sort&set_number=000033
    &sort_option=[
        yearDes_author="01---D02---A", 
        yearDes_title="01---D03---A", 
        author_yearDes="02---A01---D", 
        author-title="02---A03---A",
        title_yearAsc="03---A01---A", 
        title_author="03---A02---A"]


    [FILTER]
    Parameters:    
    -new                      
    func=short-filter-a&start_date=20170603


    [FULL_ITEM]
    Parameters:    
    -item
    func=full-set-set&set_number=000030&set_entry=000001&format=999


    [AVAILABLE]
    Parameters:
    -available
    func=item-global&doc_library=L0801&doc_number=001918315&year=&volume=&sub_library=L08


    [PAGINATION]
    Parameters:
    -start
    func=short-jump&jump=[int32]
    
    
    == DEFAULT VALUES ==
    limit=10
"""


# OBJECT MODEL 'SEARCH'
class QuerySearchSchema(Schema):
    # ID LIBRARY
    library = fields.Str(required=True)
    # NAME COLLECTION
    collection = fields.Str(required=True)
    # TYPE SEARCH
    type = fields.Str()
    # BASIC
    request = fields.Str(required=False, validate=validate_request)
    field = fields.Str()
    split = fields.Str()
    language = fields.Str()
    from_year = fields.Str(default="", validate=validate_year)
    to_year = fields.Str(default="", validate=validate_year)

    # AFTER OF FIND RESULTS
    session = fields.Str(required = False)
    start = fields.Int(required = False)

    @post_load
    def make(self, data):
        pass

    @pre_load
    def preload(self, data):
        if "library" not in data:
            raise ValidationError("Search must have a 'library' param.")

        if "request" in data:
            data["request"] = data['request'].encode('UTF-8')
        else:
            raise ValidationError("Search must have a 'request' param.")

        if "collection" not in data:
            raise ValidationError("Search must have a 'collection' param.")
        elif data["collection"] in COLLECTION:
            data["collection"] = COLLECTION[data["collection"]]
        else:
            raise ValidationError("Search must have a 'collection' param.")

        if "type" in data:
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

        if "session" in data and data["session"] == "":
            del data["session"]

        print data

    @pre_dump
    def pre_dump(self, data):
        pass

    @post_dump
    def post_dump(self, data):
        pass


class BookSearchSchema(Schema):
    id = fields.Int()
    author = fields.Str()
    title = fields.Str()
    classification = fields.Str()
    link = fields.Str()
    link_copies = fields.Str()
    copies = fields.Int()
    on_loan = fields.Int()


class ResultSearchSchema(Schema):
    session = fields.Str(required = True)
    set_number = fields.Str(required = True)
    prev = fields.Str()
    next = fields.Str()
    total = fields.Int(required = True, default = 0)
    books = fields.List(fields.Nested(BookSearchSchema), required = True)
