# Test Checklist

## Functionality
- [ ] FT-01: Create a new topic page with a title and content.
  - Action: Use the create-page function to add a new topic page titled "Test Topic" with body text.
  - Expected: The page is created, saved, and opens displaying the entered title and content.

- [ ] FT-02: Create a nested subpage under an existing topic page.
  - Action: From an existing topic page, create a subpage titled "Test Subpage".
  - Expected: The subpage is created as a child of the parent page and is listed under it in the hierarchy.

- [ ] FT-03: Create a bidirectional link between two pages.
  - Action: On Page A, add a link to Page B, then open Page B.
  - Expected: Page A shows a link to Page B, and Page B automatically shows a link back to Page A.

- [ ] FT-04: Tag a page with one or more tags.
  - Action: Open a page and assign tags "research" and "science" to it.
  - Expected: Both tags are saved and displayed on the page.

- [ ] FT-05: Record a citation from one page to another.
  - Action: On Page A, add a citation referencing Page B with a citation note.
  - Expected: Page A now lists Page B under its "cites" section.

- [ ] FT-06: Open a page and see its content, tags, and citation relationships.
  - Action: Open any existing page from the knowledge base.
  - Expected: The page displays its body content, its assigned tags, a list of pages it cites, and a list of pages that cite it.

- [ ] FT-07: Browse the knowledge base via hierarchical navigation.
  - Action: Use the navigation tree/sidebar to expand a topic and locate a nested subpage.
  - Expected: The hierarchy is shown with parent topics expanding to reveal their subpages, and clicking one opens it.

- [ ] FT-08: Search pages by title.
  - Action: Enter a known page title fragment into the search/filter input.
  - Expected: The result list shows only pages whose titles match the query.

- [ ] FT-09: Filter pages by tag.
  - Action: Apply the tag filter "research".
  - Expected: Only pages carrying the "research" tag are listed.

- [ ] FT-10: Filter or search by citation notes.
  - Action: Enter text known to appear in a citation note into the search/filter.
  - Expected: Pages whose citation notes match the text are returned.

- [ ] FT-11: Follow a chain of links/citations to reach a related page.
  - Action: From Page A, click a citation to Page B, then from Page B follow its citation to Page C.
  - Expected: Each click navigates to the target page, allowing continuous traversal through the chain.

## Constraint
- [ ] CS-01: Cannot create a page without a title.
  - Action: Attempt to create/save a page while the title field is empty.
  - Expected: The save is blocked and an error prompts for a title; no untitled page is created.

- [ ] CS-02: Duplicate page titles are prevented.
  - Action: Attempt to create a page using the title of an existing page.
  - Expected: The creation is rejected with a duplicate-title error message.

- [ ] CS-03: A page cannot be cited or linked to a nonexistent page.
  - Action: Attempt to add a citation or link pointing to a page that does not exist.
  - Expected: The action is rejected; only existing pages can be selected as link/citation targets.

- [ ] CS-04: Deleting or renaming a page updates dependent relationships consistently.
  - Action: Delete a page that is cited by another page, then open the citing page.
  - Expected: No broken/dead citation remains — the reference is removed or clearly marked as invalid.

## Interaction
- [ ] IX-01: Visual distinction between "cites" and "cited by" sections on a page.
  - Action: Open a page that both cites another page and is cited by one.
  - Expected: The two relationships appear in clearly separate, labeled sections ("Cites" and "Cited by"), not merged together.

- [ ] IX-02: Hovering/clicking a link or citation highlights and navigates to the target.
  - Action: Hover over an inline link between pages, then click it.
  - Expected: The link shows a hover affordance (e.g., highlight/underline) and clicking opens the target page.

- [ ] IX-03: Search/filter input updates results immediately.
  - Action: Type a query into the search box and modify it.
  - Expected: The result list refreshes to reflect the current query without needing a separate submit action.

## Content
- [ ] CT-01: Page content, tags, and citation notes display accurately after reload.
  - Action: Create/edit a page with specific content, tags, and a citation note, then reload the page.
  - Expected: All text, tags, and citation notes are displayed exactly as entered, with no truncation or corruption.

- [ ] CT-02: Navigation and search results show correct, non-stale page titles.
  - Action: Rename a page, then check the navigation tree and search results.
  - Expected: The new title appears everywhere; the old title no longer appears anywhere.