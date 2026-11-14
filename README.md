# Angi scraper Python: contractors, reviews and cost-guide exports

Call the hosted Angi Actor from Python, JavaScript or cURL, or run it without code on Apify. This guide focuses on choosing inputs, multi-ZIP workflows and repeatable Dataset exports.

[Open Angi Scraper on Apify](https://apify.com/datascraperes/angi-scraper?fpr=edudata)

## What this repository helps you do

- Find US home-service contractors by service name and ZIP.
- Request public reviews separately or attached to professional profiles.
- Read service cost guides and estimates.
- Export existing data to CSV without starting another collection.

## Example result

Preview of a professional record. The complete representative object is in [sample-output.json](data/sample-output.json), with a [CSV sample](data/sample-output.csv).

```json
{
  "recordId": "pro:158861273",
  "recordType": "pro",
  "data": {
    "proId": 158861273,
    "name": "Cold is on the Right Plumbing",
    "phone": "5127628243",
    "rating": "0.0"
  }
}
```

## Run without code

Open the [Actor](https://apify.com/datascraperes/angi-scraper?fpr=edudata), choose Find professionals, enter Plumbing and ZIP 78701, and select a small maximum result count. Start the run, inspect Dataset and check SUMMARY before treating it as complete. The [no-code guide](docs/no-code-guide.md) explains optional sections and professional IDs.

## Try it with Apify's free plan

The [Apify Free plan](https://apify.com/pricing?fpr=edudata) includes $5 in monthly prepaid credit without a credit card. Available credit can cover a small test; this is not unlimited free collection. Unused credit expires each billing cycle and does not roll over. Check current terms before a larger batch.

## Quick start for developers

Use Python 3.11+ and install the pinned API client:

```bash
pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/angi_contractors.py
```

PowerShell uses `$env:APIFY_API_TOKEN = "your-token"`. Keep tokens outside Git. Examples start one run with a 180-second timeout and $0.05 maximum charge, print its run ID, verify SUMMARY and read all Dataset pages. A lost start response is never retried automatically. Inspect the existing run before repeating.

## Input example

```json
{
  "mode": "pros",
  "query": "Plumbing",
  "zipCode": "78701",
  "maxItems": 2,
  "proIds": [],
  "includeReviews": false,
  "maxReviews": 2
}
```

The [input reference](docs/input-reference.md) covers all nine fields. maxItems limits rows; proIds are required only for profiles/reviews. Clear query when supplying IDs. Page URLs are unsupported. Search resolves category/task IDs.

## Request examples

- [Python single run](examples/python/angi_contractors.py)
- [Batch ZIP codes](examples/python/batch_zip_codes.py)
- [Export an existing Dataset](examples/python/export_csv.py)
- [JavaScript](examples/javascript/request.mjs), using Node 18+
- [cURL start and existing-run inspection](examples/curl-request.md)

## Output fields

| Field | Meaning |
|---|---|
| recordId | Stable identity used to detect duplicates. |
| recordType | pro, review, costGuide, searchResult or category. |
| retrievedAt | Retrieval timestamp. |
| data | Mode-specific details, such as name, phone, reviews or guide article. |

See the [output reference](docs/output-reference.md). Attached reviews share the professional row; standalone reviews are separate rows. Optional fields can be null.

## Common use cases

Compare contractors, inspect public feedback, research service costs or resolve service IDs. The [workflow guide](docs/use-cases.md) provides concrete inputs and export commands.

## Find Angi contractors across US ZIP codes with Python

```bash
python examples/python/batch_zip_codes.py 78701 90210 --service Plumbing
```

The script validates and deduplicates ZIPs before starting one run per ZIP. Runs are billed independently; overlapping areas can return the same professional. Combined output keeps one recordId.

## Export Angi results to CSV without another run

```bash
python examples/python/export_csv.py DATASET_ID --output data/exported-angi.csv
```

The export script starts no Actor. It verifies pagination and unique identities before replacing the destination. Platform retrieval/storage costs can still apply. Keep the Dataset ID from an earlier successful run.

## FAQ

See [frequent questions](docs/faq.md), including correcting inputs, choosing IDs, review charges, estimates and uncertain start requests.

## Limits and pricing

One angi-record event is one unique Dataset row delivered and verified. Attached reviews share the professional record. There is no start fee or attached-review surcharge. Availability and safeguards can leave collection incomplete; the 500-row safety cap is not a promise of maximum availability. Consumer identity fields and logged-in data are excluded; review text is preserved as published.

| Apify tier | USD per record | Equivalent per 1,000 records USD |
|---|---:|---:|
| FREE | 0.0025 | 2.50 |
| BRONZE | 0.00225 | 2.25 |
| SILVER | 0.002 | 2.00 |
| GOLD | 0.001875 | 1.875 |
| PLATINUM | 0.001875 | 1.875 |
| DIAMOND | 0.001875 | 1.875 |

Platform usage during collection is included. Reading/exporting stored data follows platform pricing. Check the live [Actor Pricing tab](https://apify.com/datascraperes/angi-scraper?fpr=edudata) for current configuration.

## Hosted version

[Run Angi Scraper on Apify](https://apify.com/datascraperes/angi-scraper?fpr=edudata) for the Input form, API, stored outputs and run logs. This repository documents that hosted product.

## Responsible use

Respect source terms, laws and privacy obligations. Review feedback before sharing. Estimates are not binding quotes. Keep tokens private.

## Support

For example problems, [open a GitHub issue](https://github.com/datacrawler-edu/angi-scraper-python/issues) with sanitized input and command. For collection problems, use the [Actor Issues tab](https://apify.com/datascraperes/angi-scraper?fpr=edudata) and include the run ID. Never share your token.

## License

These examples and documentation use the [MIT License](LICENSE).
