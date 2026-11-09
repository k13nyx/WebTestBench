# Test Checklist

## Functionality
- [ ] FT-01: User can create a new top-level topic page
  - Action: Use the "New Page" (or equivalent) control, enter a title, save.
  - Expected: The page is created and its detail view opens showing the entered content.

- [ ] FT-02: User can create a nested subpage under an existing page
  - Action: From an existing default topic page, use its "Add subpage" control to create a child page.
  - Expected: The child page is created and appears nested one level below the parent in the navigation tree.

- [ ] FT-03: User can create a bidirectional link between two pages
  - Action: On page A, add a link to page B.
  - Expected: Page A lists page B as linked, and page B lists page A as linked back without a second manual step.

- [ ] FT-04: User can create a citation relationship with a note
  - Action: On page A, add a citation to page B and enter a citation note (e.g. "builds on definition in B").
  - Expected: Page A shows B under "Cites" and page B shows A under "Cited by", with the note visible.

- [ ] FT-05: Opening a page displays content, tags, cites, and cited-by
  - Action: Open any default page that has tags and citations.
  - Expected: The page shows its body content, its tag list, a "Cites" panel, and a "Cited by" panel.

- [ ] FT-06: Search by title returns matching pages
  - Action: Type part of an existing page's title into the search box.
  - Expected: Results list includes the matching page and excludes non-matching pages.

- [ ] FT-07: Filter by tag returns all pages carrying that tag
  - Action: Apply a tag filter using one of the default tags.
  - Expected: Only pages tagged with that tag are listed; untagged pages are hidden.

- [ ] FT-08: Search by citation note text
  - Action: Search using a distinctive phrase that appears only in a citation note.
  - Expected: The result includes the page pair involved in that citation, not just pages whose body text matches.

- [ ] FT-09: Hierarchical navigation reaches deep subpages
  - Action: Starting from the root navigation, drill down through parent → child → grandchild of a default topic.
  - Expected: Each intermediate level is reachable in ≤2 clicks and the leaf subpage opens correctly.

- [ ] FT-10: User can follow a chain of links/citations to related pages
  - Action: From a page, click a linked page, then from that page click a "Cited by" entry, continuing 2–3 hops.
  - Expected: Each hop navigates to the referenced page with no dead ends or broken references in the default data.

## Constraint
- [ ] CS-01: A page cannot be saved with an empty title
  - Action: Attempt to create a page leaving the title field blank.
  - Expected: Save is blocked and a validation message about the required title is shown; no new page appears in the tree.

- [ ] CS-02: Duplicate links between the same page pair are prevented
  - Action: On page A, add a link to page B when an A↔B link already exists.
  - Expected: The link is not listed twice; at most one entry appears in each direction.

- [ ] CS-03: A page cannot link to or cite itself
  - Action: Attempt to add page A as a link target / citation target on page A.
  - Expected: The action is rejected or A is absent from the selectable target list.

- [ ] CS-04: Removing a citation clears it from both panels
  - Action: Delete an existing citation A→B.
  - Expected: B no longer appears under "Cites" on A, and A no longer appears under "Cited by" on B.

## Interaction
- [ ] IX-01: Tree nodes expand and collapse to reveal or hide subpages
  - Action: Click the expand toggle on a parent node that has subpages, then click it again.
  - Expected: Children appear indented under the parent, then are hidden; parent and sibling positions are unchanged.

- [ ] IX-02: Clicking a tag chip on a page filters to that tag
  - Action: Click one of the tag chips displayed on an open page.
  - Expected: The browser shows the filtered page list for that tag with the tag filter visibly active.

- [ ] IX-03: Inline link/citation references are clickable targets
  - Action: Click a page name shown in the "Linked", "Cites", or "Cited by" panel.
  - Expected: The app navigates to that page (not a static text label), and the breadcrumb reflects the new page's location.

## Content
- [ ] CT-01: Default knowledge base is populated with hierarchical, tagged, cross-cited content
  - Action: Open the app home / navigation tree without creating anything.
  - Expected: Pre-existing topic pages exist that include at least one multi-level parent→child nesting, tags, and at least one citation relationship.

- [ ] CT-02: Citation entries display their note text and direction correctly
  - Action: Inspect the "Cites" and "Cited by" panels on a default page with citations.
  - Expected: Each entry shows the related page's actual title plus its citation note; "Cites" = outgoing, "Cited by" = incoming (not swapped).

- [ ] CT-03: No placeholder or lorem-ipsum content remains
  - Action: Scan page bodies, tags, navigation labels, and citation notes across several default pages.
  - Expected: All text is real knowledge-management content in a consistent style; no "TODO", "Lorem ipsum", "undefined", or empty title/link entries.