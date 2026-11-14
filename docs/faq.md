# FAQ

## Is a local scraper included?
These examples call the [hosted Actor](https://apify.com/datascraperes/angi-scraper?fpr=edudata) and handle inputs, run status and exports.

## Do I need code?
No. Use the hosted Input form and Dataset export.

## Can I paste a page URL?
Arbitrary URLs are unsupported. Enter a service and ZIP, or data.proId from previous output.

## Are all settings mandatory?
No. Normal searches use mode, Service name, ZIP and a result limit. Advanced selectors and review options are optional; modes determine which target is needed.

## What if a service is ambiguous?
Use search to obtain category/task IDs, then choose one instead of query.

## Why can an office address be in another city?
The professional can serve your ZIP while having an office elsewhere.

## Are attached reviews another charge?
They share the professional row. Standalone review rows are billable individually.

## Does SUCCEEDED always mean complete?
Check SUMMARY.complete. Correctable input can exit normally with invalid_input/complete:false.

## What if the start request times out?
Inspect existing runs before repeating: a lost response may occur after creation. Examples never automatically create a replacement run.

## Can I export without collecting again?
Yes. Use the existing Dataset ID. Platform retrieval/storage costs can still apply.

## Is collection unlimited or free?
No. The 500-row safety cap and collection safeguards apply. Available Free-plan credit can cover small tests, not unlimited usage.

## Are costs guaranteed quotes?
No. They are source estimates varying by service and geography.

## What data is excluded?
Consumer names, consumer ZIP codes, contact emails and logged-in data are excluded as fields. Public review text can itself contain personal information: review before sharing.
