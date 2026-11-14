# Input reference

Choose one mode per run. The sample searches Plumbing in ZIP 78701 with a two-row limit.

| Field | Behavior |
|---|---|
| mode | pros(default), profiles, reviews, costGuides, search or categories. |
| query | Service phrase, at most 120 characters. Pros needs an exact service; search resolves alternatives. |
| zipCode | Five-digit US ZIP as text, default 78701. Preserve leading zeroes. |
| maxItems | Global Dataset row cap 1–500, default 20. A safety cap, not guaranteed availability. |
| proIds | Up to 50 positive numeric IDs from data.proId, profiles/reviews only. Duplicates removed. |
| includeReviews | Attach reviews in pros/profiles, default false. Keep off for standalone reviews. |
| maxReviews | Per-professional review cap 1–500, default 20. Standalone rows also respect maxItems. |
| categoryId | Nonzero category ID from search, pros only. Negative values are valid. |
| taskId | Service task ID from search for pros or costGuides; not a cost-guide ID. |

Pros needs exactly one of query/categoryId/taskId. Cost guides need exactly one of query/taskId. Search requires query and no IDs. Profiles/reviews require proIds with query and category/task selectors cleared. For profiles, maxItems must cover the distinct requested IDs. Categories takes no service selectors. Conflicting inputs stop with guidance instead of widening a paid search.

Page URLs are unsupported. Use data.proId from this Actor, not numbers from unrelated Angi URLs. Form rejection happens before startup, when no Actor log exists.
