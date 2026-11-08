SPARQL_ENDPOINTS = {
    "dbpedia": "https://dbpedia.org/sparql",
    "wikidata": "https://query.wikidata.org/sparql",
    "lod": "https://linkeddata.dbpedia.org/sparql",
    "lindas-int": "https://int.ld.admin.ch/query",
    "lindas-prod": "https://ld.admin.ch/query",
}

ENDPOINT_URI_PATTERNS = {
    "dbpedia": "dbpedia.org",
    "wikidata": "wikidata.org",
    "lod": "dbpedia.org",
    "lindas-int": "ld.admin.ch",
    "lindas-prod": "ld.admin.ch",
}

DEFAULT_ENDPOINT = "dbpedia"
DEFAULT_LIMIT = 100
MAX_LIMIT = 1000
