BASE_URL = "https://www.ddxfitness.ru"

# ── Navigation paths ──────────────────────────────────────────────────────────
NAV_PATHS = {
    "home":    "/",
    "clubs":   "/clubs/",
    "tariffs": "/tarrifs/",
    "promo":   "/promo/",
    "faq":     "/faq/",
    "freeze":  "/freeze/",
    "career":  "/career/",
}

# Pages that must return HTTP 200
PUBLIC_PAGES = list(NAV_PATHS.values())

# ── Tariffs ───────────────────────────────────────────────────────────────────
EXPECTED_TARIFF_NAMES = ["Infinity", "Smart", "Light"]

# ── Lead-form test data ───────────────────────────────────────────────────────
FORM_DATA = {
    "valid_name":    "Тест Тестов",
    "valid_phone":   "+71234567890",
    "invalid_phone": "abcdef",
}

# ── Third-party API endpoints used by the site ────────────────────────────────
DADATA_URL   = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/iplocate/address"
LEADPLAN_URL = "https://app.leadplan.ru/api/pageview/add"
