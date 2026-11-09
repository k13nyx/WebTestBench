# Test Checklist

## Functionality
- [ ] FT-01: Create a new topic page with title and content.
  - Action: Click "New Page", enter a title and body content, save.
  - Expected: The page is created, appears in navigation, and opens showing the entered title and content.
- [ ] FT-02: Create a nested subpage under an existing page.
  - Action: Open an existing page, choose "Add Subpage", enter title and content, save.
  - Expected: The subpage appears nested under its parent in the hierarchy and opens correctly.
- [ ] FT-03: Create a bidirectional link between two pages.
  - Action: On page A, create a link to an existing page B.
  - Expected: The link on A opens B, and B shows A in its backlinks ("Linked From") section automatically.
- [ ] FT-04: Add tags to a page.
  - Action: Open a page, add tags (e.g., "research", "learning") via the tags control, save.
  - Expected: The tags are saved and listed among the page's tags.
- [ ] FT-05: Create a citation relationship with a citation note.
  - Action: On a page, add a citation to another existing page with the note "supports the theory", save.
  - Expected: The cited page appears in the page's "Cites" list along with the entered note.
- [ ] FT-06: View pages a page cites and pages that cite it.
  - Action: Open a default page that has citation relationships.
  - Expected: The page shows a "Cites" list (pages it cites) and a "Cited By" list (pages citing it), both populated.
- [ ] FT-07: Browse the knowledge base through hierarchical navigation.
  - Action: Use the navigation tree to expand parent pages and open a nested page.
  - Expected: The nested page opens and its parent chain in the hierarchy is visible.
- [ ] FT-08: Search pages by title.
  - Action: Enter part of a default page's title in the search box (search by title).
  - Expected: Matching pages appear in results; clicking a result opens that page.
- [ ] FT-09: Filter pages by tag.
  - Action: Select a tag present in the default data via the tag filter.
  - Expected: The page list shows only pages carrying the selected tag.
- [ ] FT-10: Search by citation notes.
  - Action: Enter text from an existing citation note in the search box (search by citation note).
  - Expected: Results show the page/citation whose note matches the query, with the matching note visible.
- [ ] FT-11: Follow chains of links or citations across pages.
  - Action: Open a page, follow a link or citation entry to its target page, then follow a link or citation from that page again.
  - Expected: Each step opens the correct target page, enabling multi-hop exploration.

## Constraint
- [ ] CS-01: Page creation requires a non-empty title.
  - Action: Attempt to save a new page with the Title field empty (content filled).
  - Expected: Creation is blocked with a validation message (e.g., "Title is required") and no page is created.
- [ ] CS-02: A page cannot be linked to itself.
  - Action: On a page, attempt to create a link to the same page.
  - Expected: The self-link is rejected (validation error or target unavailable); the page's link list is unchanged.
- [ ] CS-03: The same tag cannot be added twice to one page.
  - Action: On a page that already has the tag "research", try to add "research" again.
  - Expected: The duplicate is rejected with a validation message and the tag appears only once.
- [ ] CS-04: A citation must reference an existing page.
  - Action: Attempt to create a citation whose target page title does not exist (or leave target empty).
  - Expected: The citation is rejected with a validation message; no citation is created.

## Interaction
- [ ] IX-01: Creation actions give confirmation feedback.
  - Action: Successfully create a page or subpage.
  - Expected: A success confirmation (e.g., "Page created") appears and the new item is visible without manually refreshing.
- [ ] IX-02: Search and filter results update when the input changes.
  - Action: Change the search query or switch the selected tag filter.
  - Expected: The results list updates to reflect the new query/filter immediately after the change.
- [ ] IX-03: Hierarchy nodes expand and collapse on click.
  - Action: Click a parent node in the navigation tree to expand it, then click again to collapse it.
  - Expected: Expanding reveals its subpages, collapsing hides them, with a visible state indicator (e.g., arrow toggle).

## Content
- [ ] CT-01: Page data is displayed exactly as stored.
  - Action: Open a default page and compare the displayed title, body content, and tags against its stored values.
  - Expected: Title, content, and tags render completely and exactly — no truncation, placeholders, or wrong labels.
- [ ] CT-02: Citation notes are displayed intact in citation lists.
  - Action: View the "Cites" list of a default page that has citations and read the notes.
  - Expected: Each note's full text appears exactly as recorded next to its cited page, with no missing or garbled text.