import os
import yaml

_path = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(_path) as _f:
    _config = yaml.safe_load(_f)

SPARQL_ENDPOINTS = _config["endpoints"]
ENDPOINT_URI_PATTERNS = _config["endpoint_uri_patterns"]
DEFAULT_ENDPOINT = _config["default_endpoint"]
DEFAULT_LIMIT = _config["default_limit"]
MAX_LIMIT = _config["max_limit"]
PREFIXES = _config["prefixes"]
