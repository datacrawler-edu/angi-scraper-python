# Angi integration workflows

## Compare contractors by service and ZIP
Use pros with query:Plumbing and a five-digit ZIP. Start with a small maxItems. Compare names, phones, ratings and services when available.

## Collect across multiple ZIP codes
Run `python examples/python/batch_zip_codes.py 78701 90210 --service Plumbing`. The script validates all ZIPs before starting, deduplicates repeated ZIPs and runs sequentially. One paid run per distinct ZIP, each capped at $0.05. Overlapping areas can return the same professional: each run is billed independently even when combined output keeps one recordId.

## Read public reviews
Use reviews with proIds from previous professional results, maxItems:2 and maxReviews:2. Clear query. For attached reviews, use profiles with includeReviews:true. Attached reviews share the professional row.

## Research service costs
Use costGuides with query:Plumbing and a ZIP, or one taskId from search instead of query. Guide text and regional/national estimates depend on service and geography.

## Export existing data
Run `python examples/python/export_csv.py DATASET_ID --output data/exported-angi.csv`. It reads an existing Dataset and makes no start request or new Actor result events. Retrieval/storage costs can still apply.
