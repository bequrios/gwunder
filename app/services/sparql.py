import requests


def query_sparql(endpoint: str, uri: str, limit: int = 100) -> dict:
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999-02-22-rdf-syntax-ns#>
    SELECT ?predicate ?object ?objectLabel ?objectType
    WHERE {{
        <{uri}> ?predicate ?object .
        OPTIONAL {{
            ?object rdfs:label ?objectLabel .
            FILTER(lang(?objectLabel) = "en")
        }}
        OPTIONAL {{
            ?object rdf:type ?objectType .
        }}
    }}
    LIMIT {limit}
    """.strip()

    headers = {"Accept": "application/sparql-results+json"}

    try:
        response = requests.post(
            endpoint,
            data={"query": query},
            headers=headers,
            timeout=30,
        )
        response.raise_for_status()
        results = response.json()
        return {"status": "success", "results": results.get("results", {}).get("bindings", [])}
    except requests.RequestException as e:
        return {"status": "error", "error": str(e)}
