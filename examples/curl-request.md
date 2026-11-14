# Angi API with cURL

Set APIFY_API_TOKEN in your shell. This starts one hosted run with a 180-second timeout and $0.05 maximum charge. Keep the returned run ID: a lost response may still mean it was created. Inspect existing runs before repeating. Do not add automatic retries to the start request.

```bash
curl --silent --show-error --fail --retry 0 --request POST \
  'https://api.apify.com/v2/acts/datascraperes~angi-scraper/runs?timeout=180&maxTotalChargeUsd=0.05' \
  --header "Authorization: Bearer ${APIFY_API_TOKEN}" \
  --header 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

Read the existing run, setting RUN_ID to the returned id:

```bash
curl --silent --show-error --fail --retry 0 \
  --header "Authorization: Bearer ${APIFY_API_TOKEN}" \
  "https://api.apify.com/v2/actor-runs/${RUN_ID}"
```

Wait for status SUCCEEDED, then read SUMMARY using the returned defaultKeyValueStoreId as STORE_ID. A successful process can still have invalid_input: require SUMMARY.complete:true before treating collection as complete.

```bash
curl --silent --show-error --fail --retry 0 \
  --header "Authorization: Bearer ${APIFY_API_TOKEN}" \
  "https://api.apify.com/v2/key-value-stores/${STORE_ID}/records/SUMMARY"
```

Use the returned defaultDatasetId as DATASET_ID. This request fetches one page only; the Python export script paginates for complete exports.

```bash
curl --silent --show-error --fail --retry 0 \
  --header "Authorization: Bearer ${APIFY_API_TOKEN}" \
  "https://api.apify.com/v2/datasets/${DATASET_ID}/items?format=json&clean=false&limit=100&offset=0"
```
