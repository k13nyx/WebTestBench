# Test Checklist

**Assumption:** The knowledge base ships with default data — several top-level topic pages, some with nested subpages, existing links/citations, and tags. Use this existing data; do not create new data unless the item explicitly asks you to.

## Functionality

- [ ] FT-01: A new top-level topic page can be created and appears in the hierarchy
  - Action: Click "New Page" (or "+"), enter title "Test Topic A" and body text, save.
  - Expected: Page is created and "Test Topic A" appears as a top-level entry in the hierarchical navigation; opening it shows the saved body text.

- [ ] FT-02: A nested subpage can be created under an existing page
  - Action: Select an existing default page, choose "New Subpage", enter title "Test Subpage B" and body text, save.
  - Expected: "Test Subpage B" appears nested/indented under the parent page in the hierarchy and is reachable from it.

- [ ] FT-03: Opening a page shows its content, tags, cited pages, and citing pages
  - Action: Open a default page that has at least one tag and at least one citation.
  - Expected: The page view displays all four: body content, its tag list, a "Cites" / outgoing citations list, and a "Cited By" / incoming citations list.

- [ ] FT-04: Creating a link between two pages is bidirectional
  - Action: Open page X, add a link to page Y (e.g., "Test Link"), save. Then open page Y.
  - Expected: Y's view lists X as a connected/linked page, and X's view lists Y — the relationship is visible from both sides without duplicate manual entry.

- [ ] FT-05: A citation relationship with a note can be created between two pages
  - Action: On page X, add a citation targeting page Y with note "See chapter 2 for the derivation", save. Open page Y.
  - Expected: X lists Y under its citations; Y lists X under "Cited By" with the note "See chapter 2 for the derivation" visible.

- [ ] FT-06: Tags can be added to a page and are stored on that page
  - Action: Open a default page, add tag "research", save, then reopen the page.
  - Expected: "research" appears in the page's tag list after reload and the page is retrievable by that tag.

- [ ] FT-07: Search by title returns matching pages
  - Action: Type an exact word from a known default page title into the search box and submit.
  - Expected: Only pages whose title contains that word are listed; each result shows its title; unrelated pages are absent.

- [ ] FT-08: Pages can be filtered by tag
  - Action: Apply the tag filter for a tag used by at least one default page (e.g., "research").
  - Expected: The result list contains only pages carrying that tag, and every default page with that tag is included.

- [ ] FT-09: Search matches citation note text
  - Action: Type a distinctive word that exists only in a default page's citation note (e.g., "derivation") into the search box and submit.
  - Expected: The page whose citation note contains that word is returned in the results.

## Constraint

- [ ] CS-01: A page cannot be created with an empty title
  - Action: Click "New Page", leave the title field blank, enter body text, attempt to save.
  - Expected: Save is blocked and a validation message about the required title is shown; no untitled page is added to the hierarchy.

- [ ] CS-02: A page cannot link to or cite itself
  - Action: On page X, attempt to add a link/citation whose target is page X itself.
  - Expected: The self-target is not offered or the action is rejected; X does not appear in its own link/citation lists.

- [ ] CS-03: The same citation cannot be added twice
  - Action: On page X, cite page Y, then attempt to cite page Y again from page X.
  - Expected: The duplicate is rejected or ignored; Y appears exactly once in X's citation list and X once in Y's "Cited By" list.

- [ ] CS-04: Deleting a page leaves no dangling references
  - Action: Delete a default page that is linked/cited by another default page, then open that other page.
  - Expected: The deleted page no longer appears in the other page's link, citation, or "Cited By" lists, and it is gone from the hierarchy; no broken entries remain.

## Interaction

- [ ] IX-01: Hierarchy nodes expand and collapse to reveal subpages
  - Action: Click the expand toggle on a default page that has subpages, then click it again.
  - Expected: Its subpages become visible on expand and hidden on collapse; pages without subpages show no expand control.

- [ ] IX-02: Clicking a page in the hierarchy opens it and marks it active
  - Action: In the navigation tree, click a default subpage.
  - Expected: That page's content, tags, and citation lists load in the main view, and the clicked node is visually marked as the selected/active page.

- [ ] IX-03: In-content links can be followed across a chain of pages
  - Action: Open a default page, click an in-content or listed link to another page, then click a link on that page to a third page.
  - Expected: Each click navigates to the linked page and loads its full view; the chain is followable for at least three hops.

- [ ] IX-04: Clicking a "Cited By" entry navigates to the citing page
  - Action: Open a default page that is cited by others and click one of its "Cited By" entries.
  - Expected: The citing page opens showing its content, and the original page appears in that page's citation list.

## Content

- [ ] CT-01: Opened page renders its real title and full body content
  - Action: Open two different default pages and compare the rendered text with what the page contains.
  - Expected: Each page shows its correct title and complete body text — no placeholder text, no empty body, no content from another page.

- [ ] CT-02: Citation entries show the target title and its note, with a clear empty state
  - Action: Inspect the citation lists on a default page that has citations, and on one that has none.
  - Expected: Each entry shows the related page's title and (where entered) its citation note; a page with no citations shows an explicit "no citations" / "none" state rather than a blank or broken section.

- [ ] CT-03: Tags shown on a page match the tags actually assigned to it
  - Action: Open three default pages and compare each page's displayed tag labels against the tags assigned to it.
  - Expected: Every displayed label is a real assigned tag and clickable for filtering; no blank, duplicated, or placeholder tag chips appear.