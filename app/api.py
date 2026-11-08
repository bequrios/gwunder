import os
import yaml
from flask import Blueprint, request, jsonify

from app.config import SPARQL_ENDPOINTS, DEFAULT_ENDPOINT, DEFAULT_LIMIT, MAX_LIMIT
from app.services.sparql import query_sparql

api_bp = Blueprint("api", __name__)


def load_prefixes():
    path = os.path.join(os.path.dirname(__file__), "prefixes.yaml")
    with open(path) as f:
        return yaml.safe_load(f)


@api_bp.route("/api/endpoints", methods=["GET"])
def get_endpoints():
    return jsonify(
        {
            "endpoints": SPARQL_ENDPOINTS,
            "default": DEFAULT_ENDPOINT,
            "max_limit": MAX_LIMIT,
            "prefixes": load_prefixes(),
        }
    )


@api_bp.route("/api/query", methods=["GET"])
def run_query():
    uri = request.args.get("uri", "").strip()
    endpoint_name = request.args.get("endpoint", DEFAULT_ENDPOINT)
    limit = min(int(request.args.get("limit", DEFAULT_LIMIT)), MAX_LIMIT)

    if not uri:
        return jsonify({"status": "error", "error": "Missing 'uri' parameter"}), 400

    if not uri.startswith(("http://", "https://")):
        uri = f"http://{uri}"

    endpoint_url = SPARQL_ENDPOINTS.get(endpoint_name)
    if not endpoint_url:
        return jsonify({"status": "error", "error": f"Unknown endpoint: {endpoint_name}"}), 400

    result = query_sparql(endpoint_url, uri, limit)
    result["uri"] = uri
    result["endpoint"] = endpoint_url
    result["limit"] = limit

    if result["status"] == "error":
        return jsonify(result), 502

    return jsonify(result)
