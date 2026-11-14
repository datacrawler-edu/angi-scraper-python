# Find Angi contractors without code

1. Open the [hosted Actor](https://apify.com/datascraperes/angi-scraper?fpr=edudata).
2. Choose Find professionals. Enter Service name, for example Plumbing, and a five-digit US ZIP such as 78701.
3. Select a small Maximum results; the sample uses 2. Other fields are optional unless the mode needs them.
4. Start the run. Open Dataset and export JSON or CSV. JSON preserves nested services and reviews.
5. Inspect SUMMARY: complete:false means the export should not be treated as exhaustive.

Profiles and standalone Reviews require numeric IDs from data.proId in a previous result. Clear Service name for these modes. The form has one numeric entry per ID, so no JSON editing is needed there. Review options and advanced service IDs are optional sections. Input warnings name the field and explain the correction. Form errors can be rejected before a run starts.
