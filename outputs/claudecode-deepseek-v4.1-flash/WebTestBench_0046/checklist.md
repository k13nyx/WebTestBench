# Test Checklist

## Functionality
- [ ] FT-01: User can create a new topic page with a title and content.
  - Action: Click "New Page", enter a title and body text, then save.
  - Expected: A new topic page is created and appears in the knowledge base.
- [ ] FT-02: User can create a nested subpage under an existing topic page.
  - Action: Open an existing topic page and click "New Subpage", enter a title and content, then save.
  - Expected: The new page is created as a child of the parent page and appears nested beneath it.
- [ ] FT-03: User can connect two pages with a bidirectional link.
  - Action: On Page A, add a link to Page B via "Add Link".
  - Expected: Page A lists Page B as a link, and Page B automatically lists Page A as a backlink.
- [ ] FT-04: User can add one or more tags to a page.
  - Action: Open a page, add the tag "research" via "Add Tag", then save.
  - Expected: The tag "research" is attached to the page and displayed on it.
- [ ] FT-05: User can define a citation relationship between two pages.
  - Action: On Page A, add a citation to Page B via "Add Citation" with a citation note.
  - Expected: Page A shows Page B under "Cites", and Page B shows Page A (and the note) under "Cited by".
- [ ] FT-06: Opening a page shows its content, tags, cited pages, and citing pages.
  - Action: Click on an existing topic page in the knowledge base.
  - Expected: The page view displays body content, tag list, "Cites" list, and "Cited by" list.
- [ ] FT-07: User can browse the knowledge base through hierarchical navigation.
  - Action: Use the sidebar/tree to expand a parent topic and select a nested subpage.
  - Expected: The hierarchy expands to reveal subpages and the selected page opens.
- [ ] FT-08: User can search pages by title.
  - Action: Enter a known page title into the search box.
  - Expected: Only pages whose titles match the query are listed.
- [ ] FT-09: User can filter pages by tag.
  - Action: Select an existing tag in the filter control.
  - Expected: Only pages carrying that tag are displayed.
- [ ] FT-10: User can filter/search pages by citation notes.
  - Action: Enter a phrase from an existing citation note into the search/filter field.
  - Expected: The page(s) with the matching citation note are listed.
- [ ] FT-11: User can follow a chain of links to explore related pages.
  - Action: Open a page and click a page in its "Cites" or "Linked pages" list, then click another link on the resulting page.
  - Expected: Each click navigates to the correct related page, allowing multi-step exploration.

## Constraint
- [ ] CS-01: A page cannot be created with an empty title.
  - Action: Click "New Page" and attempt to save with the title field blank.
  - Expected: Save is blocked and a validation message indicates the title is required.
- [ ] CS-02: A page cannot be created with only the title repeated as a duplicate of an existing page.
  - Action: Attempt to create a new page using an existing page's exact title.
  - Expected: The system blocks creation or warns of the duplicate title.
- [ ] CS-03: A page cannot cite itself.
  - Action: Open Page A and attempt to add Page A as a citation target.
  - Expected: Self-citation is not permitted and no self-entry appears in "Cites"/"Cited by".
- [ ] CS-04: Removing a bidirectional link removes it from both pages.
  - Action: On Page A, remove the link to Page B.
  - Expected: Page A no longer lists Page B, and Page B no longer shows Page A as a backlink.
- [ ] CS-05: Duplicate tags are not added to the same page.
  - Action: Add the tag "research" twice to the same page.
  - Expected: The tag appears only once on the page.

## Interaction
- [ ] IX-01: A confirmation is shown after a page is successfully created.
  - Action: Create a new topic page and save.
  - Expected: A success toast/message confirms the page was created.
- [ ] IX-02: A page is visually indicated as the currently open item.
  - Action: Click a page in the hierarchical navigation.
  - Expected: The selected page is highlighted as the active item.
- [ ] IX-03: Empty states are shown when a page has no tags, links, or citations.
  - Action: Open a newly created page with no tags, links, or citations.
  - Expected: Each empty list (Tags, Cites, Cited by) shows a placeholder such as "No tags yet".

## Content
- [ ] CT-01: Displayed page content matches the topic it belongs to.
  - Action: Open an existing topic page.
  - Expected: The body content is relevant to that page's title/topic.
- [ ] CT-02: All tags displayed are attached to that specific page.
  - Action: Open a page and cross-check its tag list against tags assigned to it.
  - Expected: Every displayed tag belongs to that page, with no tags from unrelated pages.