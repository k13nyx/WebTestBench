# Test Result

## Functionality
- [ ] FT-01: User can create a new topic page
  - Action: Click the "New Page" button, enter a title and content, and save.
  - Expected: The new page is created and appears in the knowledge base navigation list.
  - Bug Report:
    - Issue: Unresponsive Button / Missing Feature (no page-creation UI)
    - Actual: The only candidate control is the "+" icon button next to the "Pages" heading in the sidebar. Clicking it (twice) produces no effect: no modal/dialog/form opens, no title/content inputs appear anywhere in the DOM (verified: no dialog, no textarea, no "New Page" text, button count unchanged), and the navigation list is unchanged. The button has no click handler attached, and no create-page UI exists anywhere in the app, so a new page cannot be created or saved.

- [ ] FT-02: User can create a nested subpage under an existing page
  - Action: Open an existing topic page, use its "Add Subpage" action, enter a title, and save.
  - Expected: The subpage is created and appears nested (indented) under its parent page in the hierarchy.
  - Bug Report:
    - Issue: Missing Feature (no "Add Subpage" action)
    - Actual: Opened existing topic pages (Philosophy, Epistemology, Rationalism vs Empiricism, Scientific Method) — their views contain only title, metadata, tags, content, Subpages list, Cites, Cited By, and Linked From sections. No "Add Subpage" control exists on any page view or in the tree; a nested subpage cannot be created or saved.

- [X] FT-03: Opening a page shows its content and tags
  - Action: Click an existing topic page in the navigation.
  - Expected: Page view displays the page title, its body content, and its assigned tags.
  - (Verified on Epistemology, Rationalism vs Empiricism, Scientific Method: each view shows the page title as h1, full body content, and its tag badges, e.g. Epistemology → knowledge / justification / belief.)

- [X] FT-04: Hierarchical navigation reaches deeply nested subpages
  - Action: In the navigation tree, expand a top-level page and open a second-level subpage from the default data.
  - Expected: The subpage opens, and the hierarchy path (parent → child) is visible so the user knows where it sits.
  - (Expanded Philosophy → Epistemology and opened second-level subpage "Rationalism vs Empiricism"; the tree shows the indented parent → child path (12px → 28px → 44px) with the current page highlighted as selected, and the subpage view opened with its content.)

- [X] FT-05: Bidirectional links are visible on the linked target page
  - Action: Open a page that another page links to (from default data).
  - Expected: A "Linked mentions" / backlinks section lists the source page, showing the link works in both directions.
  - (Opening Scientific Method shows a "Linked From" section listing Epistemology and Rationalism vs Empiricism — exactly the pages that link to it in the default data; Epistemology's view likewise lists Philosophy, Metaphysics, Scientific Method.)

- [X] FT-06: Page displays the pages it cites with citation notes
  - Action: Open a page that has outgoing citations.
  - Expected: A "Cites" section lists each cited page title together with its citation note text.
  - (Epistemology's "Cites" section lists "Scientific Method" with note "Epistemology underlies scientific methodology"; Rationalism vs Empiricism lists Scientific Method and Epistemology with their notes.)

- [X] FT-07: Page displays the pages that cite it
  - Action: Open a page that is cited by another page in the default data.
  - Expected: A "Cited by" section lists the citing page(s).
  - (Epistemology's "Cited By" section lists Gettier Problems, Rationalism vs Empiricism, Scientific Method, and The Knowledge Definition Debate — all pages whose citations target Epistemology in the default data.)

- [X] FT-08: Search by title returns matching pages
  - Action: Type part of an existing page's title into the search box.
  - Expected: Results show that page; pages whose titles do not match the query are excluded.
  - (Typing "Gettier" shows "Gettier Problems" in the results; pages containing no occurrence of the term — Philosophy, Metaphysics, Philosophy of Mind, Scientific Method, Rationalism vs Empiricism — are excluded. Note: the search box is a full-text search ("Search pages, tags, citations…"), so pages that mention "gettier" in content/citation notes — Epistemology, The Knowledge Definition Debate — also appear, consistent with the app's declared multi-field search.)

- [X] FT-09: Filtering by tag lists only pages with that tag
  - Action: Select a tag that exists in the default data (via tag filter or tag list).
  - Expected: Only pages carrying that tag are shown; untagged or differently-tagged pages are excluded.
  - (Clicking the "counterexample" tag shows "1 results": only Gettier Problems — the sole page carrying that tag; all other pages are excluded from the results.)

- [X] FT-10: Search by citation note text finds the citing page
  - Action: Type a phrase from an existing citation note into the search box.
  - Expected: The page containing that citation appears in the results.
  - (Typing "applied epistemology" — from the note "Scientific method is applied epistemology" — returns exactly one result: Scientific Method, the page that contains that citation.)

## Constraint
- [ ] CS-01: Page cannot be created with an empty title
  - Action: Open "New Page", leave the title empty, fill content, and attempt to save.
  - Expected: Save is blocked with a validation message; no untitled page is added to the knowledge base.
  - Bug Report:
    - Issue: Missing Feature (no creation form, hence no validation)
    - Actual: The "New Page" creation form cannot be opened at all (the "+" control beside "Pages" does nothing), so there is no title field, no content field, and no Save button to attempt. No validation message exists because the page-creation feature — and with it the empty-title guard — is absent from the UI.

- [X] CS-02: Search with no matches shows a proper empty state
  - Action: Type a nonsense query (e.g., "zzqqxx") into the search box.
  - Expected: A "no results found" message or empty results list is shown — no pages are listed and nothing crashes.
  - (Typing "zzqqxx" shows a visible "No pages found" message in the results area with an empty results list; the app keeps running normally with no errors.)

- [X] CS-03: Combined search and tag filter must not return contradictory results
  - Action: Enter a title keyword in search and simultaneously apply a tag filter.
  - Expected: Results include only pages that satisfy BOTH the query and the tag; pages matching one condition but not the other are excluded.
  - (With search "philosophy" + tag "mind-body" active together, results show "1 results": only Philosophy of Mind — which matches the query via its title AND carries the mind-body tag. Pages matching only the query, e.g. Philosophy, Epistemology, Metaphysics, Rationalism vs Empiricism, are excluded because they lack the tag; nothing matching only the tag but not the query appears.)

## Interaction
- [X] IX-01: Clicking a link navigates to the linked page
  - Action: On a page's view, click one of its listed links (or an inline link).
  - Expected: The view switches to the target page, showing that page's content, tags, and relationships.
  - (On Epistemology's view, clicking the inline link "Rationalism vs Empiricism" switches the view to that page, showing its title, body content, tags (history / knowledge-sources / debate), and its Cites / Cited By / Linked From relationships.)

- [X] IX-02: User can follow a multi-hop chain of links/citations
  - Action: From page A, click a link to page B; then from page B, click a citation to page C.
  - Expected: Both hops succeed, ending on page C's view, letting the user explore related ideas.
  - (Hop 1: inline link on Epistemology (A) → Rationalism vs Empiricism (B) opens. Hop 2: clicking the "Scientific Method" citation entry in B's "Cites" section ("Empiricism shaped modern scientific approach") opens Scientific Method (C). Both hops succeeded, ending on Scientific Method's view.)

- [X] IX-03: Expanding/collapsing a parent page toggles its subpages in the navigation tree
  - Action: Click a parent page's expand/collapse control in the hierarchy navigation.
  - Expected: Its nested subpages are shown when expanded and hidden when collapsed, without leaving the current view.
  - (Clicking Philosophy's expand/collapse chevron hides its subpages — the tree shows only Philosophy and Scientific Method — while the current view stays on Rationalism vs Empiricism. Clicking it again restores Epistemology, Metaphysics, Philosophy of Mind (with Epistemology's children) in the tree.)

- [ ] IX-04: Creating a page provides immediate feedback
  - Action: Create a new page or subpage and save it.
  - Expected: A success confirmation appears (toast/message) or the new page's view opens immediately, so the user knows it was saved.
  - Bug Report:
    - Issue: Missing Feature (creation impossible, no save feedback)
    - Actual: A new page or subpage cannot be created or saved because no creation UI exists (the "+" control next to "Pages" is unresponsive and no "Add Subpage" action exists). Consequently no success confirmation, toast, or newly-opened page view ever appears after an attempted save.

## Content
- [X] CT-01: Tags displayed on a page match the tags actually assigned to it
  - Action: Open pages from the default data and inspect their tag labels.
  - Expected: Every displayed tag is a real, relevant tag belonging to that page (no foreign, empty, or placeholder tags).
  - (Verified: Philosophy → foundational, inquiry, wisdom; Epistemology → knowledge, justification, belief; Rationalism vs Empiricism → history, knowledge-sources, debate; Scientific Method → science, methodology, inquiry — all real, relevant tags matching the default data, with no foreign, empty, or placeholder tags.)

- [X] CT-02: Link and backlink entries display the correct page titles
  - Action: Inspect the links/backlinks sections of a page with default links.
  - Expected: Each link entry's label matches the title of the page it actually navigates to.
  - (Scientific Method's "Linked From" section lists "Epistemology" and "Rationalism vs Empiricism" — exactly the pages that link to it; clicking the entry labeled "Rationalism vs Empiricism" navigated to that exact page. Inline links and "Cites" entries also navigate to the pages their labels name.)

- [X] CT-03: Citation entries display meaningful citation note text
  - Action: Inspect the "Cites" section of a page with citations in the default data.
  - Expected: Each citation shows its actual note text (not blank, lorem-ipsum, or duplicated boilerplate) so the relationship is understandable.
  - (Citation notes observed across pages: "Epistemology underlies scientific methodology", "Empiricism shaped modern scientific approach", "Central historical debate in epistemology", "Scientific method is applied epistemology", "Synthesizes both traditions", "Challenges classical JTB definition", "Central ongoing debate" — each distinct, meaningful, and explanatory of the relationship; no blank, lorem-ipsum, or duplicated boilerplate text.)
