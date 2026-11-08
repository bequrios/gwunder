# Requirements: Triple-Store Explorer

## Overview
A web-based tool to dereference URIs from Triple-Stores and display their associated information.

## Core Features (Phase 1)
- **SPARQL Integration**: Query triple stores via SPARQL endpoints.
- **Triple Listing**: Display all `s, p, o` triples where a given URI is the subject.
- **Stateful URLs (Deep Linking)**: The URL must reflect the current search state (e.g., `?uri=...&endpoint=...`) to ensure shareable and reproducible links.

## Future Features (Phase 2)
- **Visualizations**: Graphical representation of the data for specific classes.

## Technology Stack
- **Backend**: Python / Flask
- **Query Language**: SPARQL
