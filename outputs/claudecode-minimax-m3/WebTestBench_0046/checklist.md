# Test Checklist

## Functionality
- [ ] FT-01: Create a new topic page
  - Action: Click the "New Page" / "Create Page" button, enter a unique title, save.
  - Expected: The new page is created and appears in the page list/hierarchy.

- [ ] FT-02: Create a nested subpage under an existing page
  - Action: Open an existing page and use a "New Subpage" / "Add Child" action, enter a title, save.
  - Expected: A new page is created and is nested under the parent in the hierarchy view.

- [ ] FT-03: Add tags to a page
  - Action: Open a page, add one or more tags via the tag input field, save.
  - Expected: The tags are saved on the page and become selectable for filtering.

- [ ] FT-04: Add a bidirectional link between two pages
  - Action: In page A's content/reference editor, add a link to page B.
  - Expected: Page B is reachable from page A; page A also appears in the backlinks section of page B.

- [ ] FT-05: Add a citation relationship between two pages
  - Action: In page A, add a citation to page B (with optional citation note).
  - Expected: Page B appears under the "Cites" section of A, and page A appears under the "Cited by" section of B.

- [ ] FT-06: Open a page and view its full metadata
  - Action: Open any existing page from the navigation/list.
  - Expected: The page view shows the page content, its tags, pages it cites, and pages that cite it.

- [ ] FT-07: Browse the knowledge base via hierarchical navigation
  - Action: Use the hierarchy/tree navigation panel to expand and collapse parent pages.
  - Expected: Subpages are visible and accessible under their parent pages; collapsing hides subpages.

- [ ] FT-08: Search pages by title
  - Action: Enter a known page title (or partial substring) in the search bar.
  - Expected: Only pages whose titles match the query are listed.

- [ ] FT-09: Filter pages by tag
  - Action: Click a tag (from a page or tag list) or apply a tag filter.
  - Expected: Only pages containing that tag are shown in the result list.

- [ ] FT-10: Search/filter by citation note text
  - Action: Enter a citation note phrase in the search/filter field set to citation notes.
  - Expected: Pages whose citations contain matching note text are listed.

- [ ] FT-11: Follow a chain of links/citations across multiple pages
  - Action: From page A, click a link/citation to reach page B, then click a link/citation from B to reach page C.
  - Expected: Each navigation step opens the next page in the chain, with no dead-end errors.

## Constraint
- [ ] CS-01: Page cannot be created with an empty title
  - Action: Try to save a new page (or subpage) with the title field left blank.
  - Expected: The save action is blocked and an inline validation message requires a title.

- [ ] CS-02: Search/filter with no matching results returns an empty state, not an error
  - Action: Enter a query (title/tag/citation note) that matches no existing data.
  - Expected: An empty-state message ("No results") is shown without a crash or error.

- [ ] CS-03: Filter by a non-existent tag returns no pages
  - Action: Apply a tag filter using a tag that does not exist on any page.
  - Expected: The result list is empty and no broken or unrelated pages are returned.

- [ ] CS-04: Deleting a page does not silently break links/citations of other pages
  - Action: Delete a page that is referenced (as a link or citation) by another existing page.
  - Expected: The referencing page either removes the dead reference or displays a clear "missing page" indicator.

## Interaction
- [ ] IX-01: Clicking a tag from a page applies it as a filter
  - Action: On any open page, click one of its displayed tags.
  - Expected: The page list switches to filter mode showing only pages with that tag.

- [ ] IX-02: Clicking a bidirectional link navigates to the target page
  - Action: On page A, click the link to page B.
  - Expected: The view changes to page B, with B's own tags and citations visible.

- [ ] IX-03: Clicking a cited or citing page entry navigates to that page
  - Action: On a page, click an entry in the "Cites" or "Cited by" list.
  - Expected: The view changes to the selected page.

- [ ] IX-04: Creating a new subpage refreshes the hierarchy navigation
  - Action: Create a new subpage under a parent.
  - Expected: The hierarchy panel immediately shows the new child under the parent without a manual reload.

## Content
- [ ] CT-01: Page displays exactly the tags that were assigned to it
  - Action: Add specific tags to a page, then open it.
  - Expected: All assigned tags appear on the page; no extra or missing tags.

- [ ] CT-02: A bidirectional link is visible from both the source and target page
  - Action: Add a link from page A to page B; open both pages.
  - Expected: Page A shows a forward link to B; page B shows A in its backlinks list.

- [ ] CT-03: A citation appears on both the citing and cited pages with its note
  - Action: Add a citation with a note from page A to page B; open both pages.
  - Expected: Page A lists B under "Cites" with the note text; page B lists A under "Cited by" with the same note text.