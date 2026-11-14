# Output reference

Each Dataset row has recordId(stable identity), recordType, retrievedAt(UTC timestamp) and data.

| Row type | Useful data |
|---|---|
| pro | proId, name, description, phone, address, rating, reviewCount, services, coordinates and available profileUrl. |
| review | id, proId, rating, text, date, task, cost and available coarse city/state. |
| costGuide | taskId, zipCode, costGuideId, name, range, costData, article and relatedTasks. |
| searchResult | id, name, optionType and available srPathUrl. |
| category | categoryOid, name, urlName and available imagePath. |

Attached reviews share the pro row. reviewsTotal and reviewsTruncated distinguish a subset from all available reviews. Optional fields may be null. Service coverage can differ from the office location. Costs are estimates, not binding quotes.

SUMMARY is in the default key-value store, outside the billable Dataset. complete:true/status:COMPLETED indicates a verified bounded collection. Correctable input yields complete:false/outcome:invalid_input and no diagnostic row. Interruptions can preserve saved rows while remaining incomplete.

CSV export keeps business columns plus the full data object as JSON. It starts no Actor, checks unique identities and paginates to the end, including an empty final page for exact page multiples. Failed exports do not replace an existing destination file.
