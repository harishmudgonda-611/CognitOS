# CognitOS research ingestion boundary

CognitOS has a Python project layout with `src/`, `config/`, `scripts/` and `tests/`. This integration is scoped to research ingestion and must not alter its existing agent/runtime contracts.

## Adapter responsibilities
- **MarkItDown**: optional conversion of user-provided documents into text with source-file provenance.
- **Crawl4AI**: optional extraction from permitted public pages, producing Markdown plus original URL and retrieval timestamp.
- **Scrapy**: optional domain-scoped crawling for sites whose terms and robots policy permit it.
- **Scrapling / AutoScraper**: fixture-driven extraction helpers, not anti-bot bypass mechanisms.

## Normalized research record
Each item should include `source_url`, `retrieved_at` (UTC), `title`, `content_type`, `text`, `extractor`, `content_sha256` and any crawl-policy decision. Keep source text separate from generated summaries and agent conclusions.

## Safety and defaults
No crawler runs automatically. No credentials, cookies, browser profiles or tokens are collected. Do not bypass authentication, CAPTCHAs, paywalls, robots directives, rate limits or access controls. Respect site terms and copyright. Add explicit per-domain allowlists, request budgets, timeouts and deduplication before enabling network collection.

## Dependencies and validation
This branch introduces no dependency or runtime behavior. Select one adapter at a time, pin versions, keep optional extras separate, and add fixture tests plus blocked-domain and failure-path tests before integrating into the agent loop.