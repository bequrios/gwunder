# Requirements Gwunder: Triple-Store Explorer

## Overview
A web-based tool to dereference URIs from Triple-Stores and display their associated information.

## Core Features (Phase 1)
- **SPARQL Integration**: Query triple stores via SPARQL endpoints.
- **Triple Listing**: Display all `s, p, o` triples where a given URI is the subject.
- **Full URI Display**: Show the full URI for all values (not just the slug). Use prefix shortening from a configurable `prefixes.yaml` file (e.g., `schema:hasPart` instead of `http://schema.org/hasPart`).
- **Language Tag**: If an object value is a literal with an `xml:lang`, display the language code in grey after the value (e.g., "Zürich `de`").
- **Column Filters**: Each column in the results table has a filter input. Typing dynamically hides rows that do not match the filter text (case-insensitive).
- **Internal Navigation**: If a predicate or object URI matches the URI pattern of the currently selected endpoint (defined per endpoint in config), clicking it navigates within Gwunder (same endpoint/limit settings) instead of opening the external URI. This must work independently of the real URL of Gwunder (e.g., if Gwunder is hosted at `https://example.com/gwunder`, clicking a matching URI should navigate to `https://example.com/gwunder?uri=...&endpoint=...&limit=...`).
- **Stateful URLs (Deep Linking)**: The URL must reflect the current search state (e.g., `?uri=...&endpoint=...&limit=...`) to ensure shareable and reproducible links.

## User Interface
- **Search Input**: An input field for entering a URI, paired with a "Go" button to initiate the lookup.
- **Configuration Section**: A persistent section at the top of each page allowing the user to:
  - Select from a list of pre-configured SPARQL endpoints
  - Set a `LIMIT` for the SPARQL query
  - Configure future options (extensible)
- **Prominent URI Display**: The currently dereferenced URI must be displayed prominently on the page.

## Future Features (Phase 2)
- **Visualizations**: Graphical representation of the data for specific classes.

## Non-Functional Requirements
- **Backend/Frontend Separation**: The backend and frontend must be clearly separated. They communicate exclusively via a JSON API (REST). The backend exposes endpoints for SPARQL queries; the frontend renders the results and handles user interaction.

## Technology Stack
- **Backend**: Python / Flask
- **Query Language**: SPARQL
