# Gwunder

"Gwunder" is a Swiss-German (Bernese) word meaning "it interests me" or "curiosity."

This project is a web-based tool designed to dereference URIs from Triple-Stores and display their associated information. It allows users to explore linked data by querying SPARQL endpoints and visualizing the relationships between entities.

## Features
- **SPARQL Integration**: Connect to various Triple-Stores via SPARQL endpoints.
- **Triple Exploration**: View all `s, p, o` triples associated with a specific subject URI.
- **Search Input**: Enter a URI and hit "Go" to initiate the lookup.
- **Configuration Panel**: Select endpoint, set query limit, and manage future options from a persistent section on each page.
- **Prominent URI Display**: The currently dereferenced URI is displayed prominently on the page.
- **Deep Linking**: Every query result is uniquely representable via a shareable URL.
- **Visualizations**: (Planned) Graphical representations for specific data classes.

## Technology Stack
- **Backend**: Python / Flask (API server)
- **Frontend**: (TBD) – consumes the JSON API
- **Communication**: REST / JSON API
- **Query Language**: SPARQL

## Status
- [x] Requirements Definition
- [x] Project Initialization
- [ ] Environment Setup
- [ ] Core Backend Development
- [ ] Frontend Implementation
