# Test Checklist

## Functionality
- [ ] FT-01: Create a topic page with title and content
  - Action: Click "New Page", enter a title and body text, click "Save".
  - Expected: A new topic page is created and appears in the knowledge base.

- [ ] FT-02: Create a nested subpage under an existing page
  - Action: Select an existing page, choose "Add Subpage", enter title/content, click "Save".
  - Expected: The subpage is created nested under the parent in the hierarchy.

- [ ] FT-03: Create a bidirectional link connecting two pages
  - Action: Open a page, use the "Link" control to connect it to another page, click "Save".
  - Expected: A link is created and the connection is established between both pages.

- [ ] FT-04: Add one or more tags to a page
  - Action: Open a page, enter tag name(s) in the tags field, click "Save".
  - Expected: The tag(s) are attached to the page.

- [ ] FT-05: Create a citation relationship (one page cites another)
  - Action: Open a page, use "Cite" to reference another page and add a citation note, click "Save".
  - Expected: A citation relationship is created from the citing page to the cited page.

- [ ] FT-06: Open a page to read its content
  - Action: Click a page title in the navigation.
  - Expected: The page opens and its content is displayed.

- [ ] FT-07: Browse the knowledge base via hierarchical navigation
  - Action: Use the sidebar tree to expand/collapse a parent page.
  - Expected: Child subpages are shown or hidden accordingly.

- [ ] FT-08: Search pages by title
  - Action: Type a known page title in the search box and press Enter.
  - Expected: Matching pages are listed in the results.

- [ ] FT-09: Filter pages by tag
  - Action: Select a tag from the tag filter control.
  - Expected: Only pages carrying that tag are displayed.

- [ ] FT-10: Search or filter pages by citation notes
  - Action: Enter text from a citation note into search/filter and submit.
  - Expected: Pages whose citation notes contain that text are returned.

- [ ] FT-11: Follow a link or citation to navigate to a related page
  - Action: Click a linked or cited page name shown on the opened page.
  - Expected: The application navigates to that related page.

## Constraint
- [ ] CS-01: Cannot create a page with an empty required title
  - Action: Click "New Page", leave the title empty, click "Save".
  - Expected: Save is blocked with a required-field error and no page is created.

- [ ] CS-02: A page cannot be nested under itself
  - Action: Attempt to add the current page as its own subpage.
  - Expected: The action is prevented (disabled or error); no circular nesting is created.

- [ ] CS-03: A page cannot cite itself
  - Action: Attempt to add the current page as its own citation.
  - Expected: The action is prevented; no self-citation is created.

- [ ] CS-04: A bidirectional link is reflected reciprocally on both pages
  - Action: Create a link from page A to page B, then open page B.
  - Expected: Page B shows the link back to page A (reciprocal connection).

## Interaction
- [ ] IX-01: Success confirmation appears after creating a page, link, tag, or citation
  - Action: Create a page (and separately a link, a tag, and a citation).
  - Expected: A success toast or message appears confirming each action.

- [ ] IX-02: Hierarchical tree expands and collapses on click
  - Action: Click the expand/collapse toggle next to a parent page.
  - Expected: The subtree opens or closes and the visible child count updates.

## Content
- [ ] CT-01: Opened page displays its full content
  - Action: Open a page that contains written content.
  - Expected: The page's full text/media content is visible and readable.

- [ ] CT-02: Opened page displays its tags
  - Action: Open a page that has tags assigned.
  - Expected: The page's tags are listed and visible on the page.

- [ ] CT-03: Opened page displays pages it cites and pages cited by it
  - Action: Open a page that participates in citations.
  - Expected: Both a "Cites" list and a "Cited by" list are shown with the related pages.