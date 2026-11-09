# Test Checklist

## Functionality
- [ ] FT-01: User can create a new topic page
  - Action: Click the "New Page" button, enter a title and content, and save.
  - Expected: The new page is created and appears in the knowledge base navigation list.

- [ ] FT-02: User can create a nested subpage under an existing page
  - Action: Open an existing topic page, use its "Add Subpage" action, enter a title, and save.
  - Expected: The subpage is created and appears nested (indented) under its parent page in the hierarchy.

- [ ] FT-03: Opening a page shows its content and tags
  - Action: Click an existing topic page in the navigation.
  - Expected: Page view displays the page title, its body content, and its assigned tags.

- [ ] FT-04: Hierarchical navigation reaches deeply nested subpages
  - Action: In the navigation tree, expand a top-level page and open a second-level subpage from the default data.
  - Expected: The subpage opens, and the hierarchy path (parent → child) is visible so the user knows where it sits.

- [ ] FT-05: Bidirectional links are visible on the linked target page
  - Action: Open a page that another page links to (from default data).
  - Expected: A "Linked mentions" / backlinks section lists the source page, showing the link works in both directions.

- [ ] FT-06: Page displays the pages it cites with citation notes
  - Action: Open a page that has outgoing citations.
  - Expected: A "Cites" section lists each cited page title together with its citation note text.

- [ ] FT-07: Page displays the pages that cite it
  - Action: Open a page that is cited by another page in the default data.
  - Expected: A "Cited by" section lists the citing page(s).

- [ ] FT-08: Search by title returns matching pages
  - Action: Type part of an existing page's title into the search box.
  - Expected: Results show that page; pages whose titles do not match the query are excluded.

- [ ] FT-09: Filtering by tag lists only pages with that tag
  - Action: Select a tag that exists in the default data (via tag filter or tag list).
  - Expected: Only pages carrying that tag are shown; untagged or differently-tagged pages are excluded.

- [ ] FT-10: Search by citation note text finds the citing page
  - Action: Type a phrase from an existing citation note into the search box.
  - Expected: The page containing that citation appears in the results.

## Constraint
- [ ] CS-01: Page cannot be created with an empty title
  - Action: Open "New Page", leave the title empty, fill content, and attempt to save.
  - Expected: Save is blocked with a validation message; no untitled page is added to the knowledge base.

- [ ] CS-02: Search with no matches shows a proper empty state
  - Action: Type a nonsense query (e.g., "zzqqxx") into the search box.
  - Expected: A "no results found" message or empty results list is shown — no pages are listed and nothing crashes.

- [ ] CS-03: Combined search and tag filter must not return contradictory results
  - Action: Enter a title keyword in search and simultaneously apply a tag filter.
  - Expected: Results include only pages that satisfy BOTH the query and the tag; pages matching one condition but not the other are excluded.

## Interaction
- [ ] IX-01: Clicking a link navigates to the linked page
  - Action: On a page's view, click one of its listed links (or an inline link).
  - Expected: The view switches to the target page, showing that page's content, tags, and relationships.

- [ ] IX-02: User can follow a multi-hop chain of links/citations
  - Action: From page A, click a link to page B; then from page B, click a citation to page C.
  - Expected: Both hops succeed, ending on page C's view, letting the user explore related ideas.

- [ ] IX-03: Expanding/collapsing a parent page toggles its subpages in the navigation tree
  - Action: Click a parent page's expand/collapse control in the hierarchy navigation.
  - Expected: Its nested subpages are shown when expanded and hidden when collapsed, without leaving the current view.

- [ ] IX-04: Creating a page provides immediate feedback
  - Action: Create a new page or subpage and save it.
  - Expected: A success confirmation appears (toast/message) or the new page's view opens immediately, so the user knows it was saved.

## Content
- [ ] CT-01: Tags displayed on a page match the tags actually assigned to it
  - Action: Open pages from the default data and inspect their tag labels.
  - Expected: Every displayed tag is a real, relevant tag belonging to that page (no foreign, empty, or placeholder tags).

- [ ] CT-02: Link and backlink entries display the correct page titles
  - Action: Inspect the links/backlinks sections of a page with default links.
  - Expected: Each link entry's label matches the title of the page it actually navigates to.

- [ ] CT-03: Citation entries display meaningful citation note text
  - Action: Inspect the "Cites" section of a page with citations in the default data.
  - Expected: Each citation shows its actual note text (not blank, lorem-ipsum, or duplicated boilerplate) so the relationship is understandable.