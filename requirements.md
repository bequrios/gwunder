# Requirements: Triple-Store Explorer

## Overview
A web-based tool to dereference URIs from Triple-Stores and display their associated information.

## Core Features (Phase 1)
- **SPARQL Integration**: Query triple stores via SPARQL endpoints.
- **Triple Listing**: Display all `s, p, o` triples where a given URI is the subject.
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

## Technology Stack
- **Backend**: Python / Flask
- **Query Language**: SPARQL
