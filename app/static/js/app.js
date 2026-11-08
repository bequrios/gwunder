(function () {
    const endpointSelect = document.getElementById("endpoint");
    const limitInput = document.getElementById("limit");
    const searchForm = document.getElementById("search-form");
    const uriInput = document.getElementById("uri-input");
    const resultsSection = document.getElementById("results-section");
    const displayedUri = document.getElementById("displayed-uri");
    const resultsCount = document.getElementById("results-count");
    const resultsBody = document.getElementById("results-body");
    const errorMessage = document.getElementById("error-message");
    const loading = document.getElementById("loading");

    let prefixes = {};

    function formatUri(uri) {
        if (!uri || !uri.startsWith("http")) return uri;
        for (const [prefix, ns] of Object.entries(prefixes)) {
            if (uri.startsWith(ns)) {
                return `${prefix}:${uri.slice(ns.length)}`;
            }
        }
        return uri;
    }

    function updateUrlParams(uri, endpoint, limit) {
        const params = new URLSearchParams();
        if (uri) params.set("uri", uri);
        if (endpoint) params.set("endpoint", endpoint);
        if (limit) params.set("limit", limit);
        const qs = params.toString();
        history.pushState(null, "", qs ? `?${qs}` : window.location.pathname);
    }

    function readUrlParams() {
        const params = new URLSearchParams(window.location.search);
        return {
            uri: params.get("uri") || "",
            endpoint: params.get("endpoint") || "",
            limit: params.get("limit") || "",
        };
    }

    async function loadEndpoints() {
        const res = await fetch("/api/endpoints");
        const data = await res.json();
        endpointSelect.innerHTML = "";
        for (const [name, url] of Object.entries(data.endpoints)) {
            const opt = document.createElement("option");
            opt.value = name;
            opt.textContent = `${name} (${url})`;
            endpointSelect.appendChild(opt);
        }
        endpointSelect.value = data.default;
        limitInput.max = data.max_limit;
        prefixes = data.prefixes || {};
    }

    async function performQuery(uri, endpoint, limit) {
        loading.hidden = false;
        resultsSection.hidden = true;
        errorMessage.hidden = true;

        const params = new URLSearchParams({ uri, endpoint, limit });
        const res = await fetch(`/api/query?${params}`);
        const data = await res.json();

        loading.hidden = true;

        if (data.status === "error") {
            resultsSection.hidden = false;
            errorMessage.textContent = data.error;
            errorMessage.hidden = false;
            displayedUri.textContent = data.uri || uri;
            return;
        }

        displayedUri.textContent = data.uri;
        const results = data.results;
        resultsCount.textContent = `${results.length} triple(s) found`;

        resultsBody.innerHTML = "";
        results.forEach((row) => {
            const tr = document.createElement("tr");

            const pred = document.createElement("td");
            const predUrl = row.predicate?.value || "";
            pred.innerHTML = `<a href="${predUrl}" target="_blank" title="${predUrl}">${formatUri(predUrl)}</a>`;

            const obj = document.createElement("td");
            const objVal = row.object?.value || "";
            const objType = row.object?.type || "uri";
            const objLang = row.object?.["xml:lang"];
            if (objType === "uri") {
                obj.innerHTML = `<a href="${objVal}" target="_blank" title="${objVal}">${formatUri(objVal)}</a>`;
            } else {
                obj.textContent = objVal;
                if (objLang) {
                    const langSpan = document.createElement("span");
                    langSpan.className = "lang-code";
                    langSpan.textContent = ` ${objLang}`;
                    obj.appendChild(langSpan);
                }
            }

            const label = document.createElement("td");
            label.textContent = row.objectLabel?.value || "";

            const type = document.createElement("td");
            const typeVal = row.objectType?.value || "";
            if (typeVal) {
                type.innerHTML = `<a href="${typeVal}" target="_blank" title="${typeVal}">${formatUri(typeVal)}</a>`;
            }

            tr.appendChild(pred);
            tr.appendChild(obj);
            tr.appendChild(label);
            tr.appendChild(type);
            resultsBody.appendChild(tr);
        });

        resultsSection.hidden = false;
    }

    searchForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const uri = uriInput.value.trim();
        if (!uri) return;
        const endpoint = endpointSelect.value;
        const limit = limitInput.value;
        updateUrlParams(uri, endpoint, limit);
        performQuery(uri, endpoint, limit);
    });

    window.addEventListener("popstate", () => {
        const { uri, endpoint, limit } = readUrlParams();
        if (uri) {
            uriInput.value = uri;
            if (endpoint) endpointSelect.value = endpoint;
            if (limit) limitInput.value = limit;
            performQuery(uri, endpoint || endpointSelect.value, limit || limitInput.value);
        }
    });

    async function init() {
        await loadEndpoints();
        const { uri, endpoint, limit } = readUrlParams();
        if (uri) {
            uriInput.value = uri;
            if (endpoint) endpointSelect.value = endpoint;
            if (limit) limitInput.value = limit;
            performQuery(uri, endpoint || endpointSelect.value, limit || limitInput.value);
        }
    }

    init();
})();
