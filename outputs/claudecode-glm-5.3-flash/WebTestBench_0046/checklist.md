# Test Checklist

## Functionality
- [ ] FT-01: User can create a new topic page
  - Action: Click the "New Page" / "Create Page" button, enter title "Machine Learning", add some body text, and save.
  - Expected: The page "Machine Learning" is created and opened, showing its title and entered content.
- [ ] FT-02: User can create a nested subpage under an existing topic page
  - Action: Open the "Machine Learning" page, use the "Add Subpage" (or equivalent) action, create a subpage titled "Neural Networks".
  - Expected: "Neural Networks" is created as a child of "Machine Learning" and appears indented/nested beneath it in the hierarchy.
- [ ] FT-03: User can create a bidirectional (wiki-style) link between two pages
  - Action: On the "Neural Networks" page, insert a link to another existing page (e.g., "Machine Learning") and save.
  - Expected: The link is saved on "Neural Networks"; opening "Machine Learning" shows "Neural Networks" in its "Linked mentions" / backlinks section.
- [ ] FT-04: User can add tags to a page
  - Action: Open any existing page, add a tag (e.g., "AI") via the tag input, and save.
  - Expected: The tag "AI" is displayed on that page's tag list.
- [ ] FT-05: User can add a citation with a note from one page to another
  - Action: On a page (e.g., "Neural Networks"), add a citation referencing another page (e.g., "Machine Learning") with a citation note text, and save.
  - Expected: The citation appears on the page's "Cites" section, showing the cited page name and the citation note.
- [ ] FT-06: Page view shows content, tags, citations, and backlinks together
  - Action: Open a page that has content, at least one tag, at least one outgoing citation, and at least one incoming citation.
  - Expected: The page displays: body content, its tags, a "Cites" section listing cited pages, and a "Cited by" section listing citing pages.
- [ ] FT-07: User can navigate the hierarchy via a tree/sidebar navigation
  - Action: In the hierarchical navigation (sidebar/tree), expand a top-level topic and click one of its nested subpages.
  - Expected: The clicked subpage opens, and its position in the tree (parent → child path) is visible.
- [ ] FT-08: User can edit an existing page's content
  - Action: Open an existing page, modify its body text, and save.
  - Expected: The updated content is displayed after saving and persists after navigating away and back.
- [ ] FT-09: User can follow a chain of links/citations across multiple pages
  - Action: Starting from a page with a link or citation, click through to the target page, then click again on that page's link/citation to a third page.
  - Expected: Each click navigates to the correct page, allowing traversal of at least 2 levels of linked/cited pages.

## Constraint
- [ ] CS-01: Cannot create a page with an empty title
  - Action: Click "New Page" / "Create Page" and attempt to save without entering a title.
  - Expected: Creation is blocked with a validation message (e.g., "Title is required"); no empty page is created.
- [ ] CS-02: Subpages can only exist under an existing parent page
  - Action: Attempt to create a subpage and check that it must be attached to a selected parent topic.
  - Expected: The subpage is always created under a valid existing parent; it cannot be created floating without a parent in the hierarchy.
- [ ] CS-03: Cannot create a bidirectional link to a non-existent page
  - Action: Attempt to insert a link targeting a page that does not exist (or a blank target).
  - Expected: The system prevents the link or warns (e.g., "Page not found"); no broken link is silently saved.
- [ ] CS-04: A page cannot cite itself
  - Action: On a page, attempt to add a citation whose target is the same page.
  - Expected: The self-citation is rejected with an error message or the self option is unavailable in the target selector.
- [ ] CS-05: Duplicate tags on the same page are not allowed
  - Action: On one page, add the tag "AI", then attempt to add the tag "AI" again.
  - Expected: The duplicate is rejected or merged into one entry; the page shows the tag "AI" only once.

## Interaction
- [ ] IX-01: Clicking a link on a page navigates to the target page
  - Action: Click an internal link inside a page's content.
  - Expected: The target page opens, displaying that page's title and content.
- [ ] IX-02: Clicking a tag filters the knowledge base to pages with that tag
  - Action: On any page, click one of its displayed tags (e.g., "AI").
  - Expected: A filtered list of pages tagged "AI" is shown, including the current page.
- [ ] IX-03: Clicking a citation entry navigates to the cited page
  - Action: In a page's "Cites" or "Cited by" section, click one of the listed page entries.
  - Expected: The referenced page opens.
- [ ] IX-04: Search input returns matching results as the user types
  - Action: Type a partial existing page title (e.g., "Neur") into the search box.
  - Expected: Matching pages appear in the results list while typing (or immediately upon submit), without clearing the rest of the UI unexpectedly.

## Content
- [ ] CT-01: Search by title returns only pages whose titles match the query
  - Action: Search for an exact existing page title (e.g., "Machine Learning") via title search.
  - Expected: Results include "Machine Learning" and do not include pages whose titles do not match.
- [ ] CT-02: Search by tag returns only pages carrying that tag
  - Action: Filter/search by an existing tag (e.g., "AI").
  - Expected: Every page in the results displays the tag "AI"; untagged pages are excluded.
- [ ] CT-03: Search by citation note text returns pages whose citations contain that text
  - Action: Search for a word that appears in an existing citation note (e.g., a keyword from a saved citation note).
  - Expected: Results include the page(s) whose citation notes contain that text; pages without such citation text are excluded.