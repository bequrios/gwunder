import requests


def query_sparql(endpoint: str, uri: str, limit: int = 100) -> dict:
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX schema: <http://schema.org/>
    SELECT ?predicate ?object
           (GROUP_CONCAT(DISTINCT CONCAT(STR(?label), " ~~ ", COALESCE(lang(?label), "")); SEPARATOR=" || ") AS ?labels)
           (GROUP_CONCAT(DISTINCT STR(?objectType); SEPARATOR=" || ") AS ?types)
    WHERE {{
        <{uri}> ?predicate ?object .
        OPTIONAL {{
            {{ ?object rdfs:label ?label }}
            UNION
            {{ ?object schema:name ?label }}
        }}
        OPTIONAL {{
            ?object rdf:type ?objectType .
        }}
    }}
    GROUP BY ?predicate ?object
    LIMIT {limit}
    """.strip()

    headers = {
        "Accept": "application/sparql-results+json",
        "User-Agent": "Gwunder/1.0 (Triple Store Explorer)",
    }

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
