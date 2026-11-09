# Test Result

Note on state: the page loads empty ("No contracts to compare") and offers "Load sample" buttons; the three app-provided samples (TechVentures SaaS Agreement, GlobalCorp Enterprise License, StartupX Consulting Agreement) were loaded via the form and treated as the "default contracts" referenced by the checklist. All actions were performed without page reloads.

## Functionality
- [ ] FT-01: User can add multiple contracts, each with a name and text.
  - Action: Enter a name and contract text into the input fields, click the add/submit button, repeat for a second contract.
  - Expected: Both contracts appear in the comparison area, each labeled with its entered name.
  - Bug Report:
    - Issue: Contracts Not Added to Comparison Area (Clause Detection Failure)
    - Actual: After adding "Alpha Services Agreement" and "Beta Services Agreement" (each with clear numbered clauses "1. Payment Terms", "2. Confidentiality", "3. Termination") via the form, both appear only under "Added Contracts (4)"; the comparison area contains no column for either contract and the counter remains "15 Clauses Detected". Contract text whose clause headings are short is silently undetected (same input with long headings, e.g. "1. Payment Terms and Schedule", does produce columns), so ordinary contracts never reach the comparison area.

- [ ] FT-02: Clauses are auto-detected and grouped by clause type.
  - Action: View the clause groups generated for the default contracts present on the page.
  - Expected: Clauses are grouped under type headings such as "Payment Terms", "Confidentiality", "Termination", each clause placed under the type it belongs to.
  - Bug Report:
    - Issue: Incomplete Clause Detection — Clauses Silently Dropped
    - Actual: The 3 default contracts contain 20 numbered clause sections, but only 15 are detected ("15 Clauses Detected") and grouped. Missing entirely from all groups: TechVentures "1. Payment Terms", "2. Confidentiality", "3. Termination" and GlobalCorp "1. Payment and Fees", "5. Indemnification" (e.g., the "Payment Terms" group shows only StartupX's "1. Compensation Terms", "1 clause"). Sections whose heading is short (≤ ~16 chars, e.g. "Payment Terms", "Confidentiality", "Termination") are not detected, so their clauses are placed under no type.

- [X] FT-03: Clauses of the same type are shown side by side across contracts.
  - Action: Open any clause group for the default contracts.
  - Expected: The corresponding clause text of each contract is displayed in adjacent columns/panels, one per contract, aligned within the group.

- [X] FT-04: User can filter the view by clause type.
  - Action: Select "Payment Terms" in the clause-type filter control.
  - Expected: Only the "Payment Terms" clause group is displayed; all other clause groups are hidden.

- [X] FT-05: Differences in wording between contracts are highlighted.
  - Action: Open a clause group whose wording differs across contracts.
  - Expected: The words/phrases that differ between the contracts' clause texts are visually highlighted.

- [ ] FT-06: User can switch a clause group to the summarized comparison view.
  - Action: Switch one clause group to the summarized comparison view via its view control.
  - Expected: The group displays a concise summary comparing the contracts' clauses instead of the full clause text.
  - Bug Report:
    - Issue: Missing Per-Group View Control / View Toggle Has No Effect
    - Actual: No clause group card contains any view control; the only view control is a single global "Full text" switch (id=full-text) in the toolbar. Toggling it produces no content change in any group: in both states each column renders only the clause heading line (e.g., "4. Limitation of Liability") and the page text is identical (1781 chars before and after). A clause group cannot be switched to a summarized comparison view via its own view control.

- [ ] FT-07: User can switch a clause group to the full-text view.
  - Action: Switch the same clause group to the full-text view via its view control.
  - Expected: The group displays the complete clause text for each contract.
  - Bug Report:
    - Issue: Full-Text View Never Shows Complete Clause Text (Truncated Clause) / Missing Per-Group View Control
    - Actual: With the global "Full text" switch on (data-state=checked), each column still displays only the clause heading line — e.g., "4. Limitation of Liability" (26 chars) where the source contract's section is 297 chars ("4. Limitation of Liability Client shall pay Provider a monthly subscription fee of $2,500 USD, due on the first day of each month…"). The clause body is never rendered, and there is no per-group view control to switch a single group.

## Constraint
- [ ] CS-01: A contract cannot be added with an empty name or empty text.
  - Action: Click the add/submit button with the name field empty, then again with the text field empty.
  - Expected: The contract is not added in either case; a validation error message indicates the required field is missing.
  - Bug Report:
    - Issue: Missing Validation Error Message
    - Actual: The contract is correctly not added in either case (the "Add Contract" button remains disabled with name-only or text-only input; Enter key submission does nothing; empty state persists), but no validation error message is ever shown — no alert/error element, no "required"/"error" text anywhere in the page. The required-field failure is never indicated to the user.

- [X] CS-02: Each clause is assigned to exactly one clause-type group.
  - Action: Inspect all clause groups rendered for the default contracts.
  - Expected: No clause text appears in more than one clause-type group.

- [X] CS-03: Identical wording produces no difference highlighting.
  - Action: Open a clause group where two contracts contain identical wording.
  - Expected: No highlight is shown over the identical wording.

- [ ] CS-04: A clause type missing from one contract is not filled with other contracts' text.
  - Action: Open a clause group where one contract contains no clause of that type.
  - Expected: That contract's column shows an explicit "no clause found"/empty indicator; no text from another clause type or another contract appears there.
  - Bug Report:
    - Issue: Missing "No Clause Found"/Empty Indicator (Contract Column Omitted Entirely)
    - Actual: In the "Payment Terms" group (with the default contracts) the grid renders `grid-template-columns: repeat(1, …)` with only StartupX's card — TechVentures and GlobalCorp have no column at all and no empty/"no clause found" indicator (no such element exists anywhere in the page). Same in "Confidentiality" and "Termination" (TechVentures column absent) and "Indemnification" (only StartupX shown). No wrong text is shown, but the required explicit empty indicator is missing.

## Interaction
- [ ] IX-01: Adding a contract updates the comparison view immediately.
  - Action: Add a contract and observe the comparison area without reloading the page.
  - Expected: The comparison view updates immediately to include the new contract, with no full page reload or manual refresh required.
  - Bug Report:
    - Issue: Comparison View Does Not Include Newly Added Contract
    - Actual: After clicking "Add Contract" for "Alpha Services Agreement" (and then "Beta Services Agreement"), without any reload, the comparison area still shows only the 3 sample contracts and "15 Clauses Detected"; the new contract appears solely in the "Added Contracts" list. The comparison view only updates for contracts whose clause headings pass the fragile detector (long headings update it immediately, standard short headings are ignored).

- [ ] IX-02: View toggle responds in place and indicates the active view.
  - Action: Click the Summarized / Full Text toggle on a clause group.
  - Expected: The group's content changes in place without a page reload, and the currently active view option is visually indicated on the control.
  - Bug Report:
    - Issue: Missing Per-Group View Toggle / Toggle Produces No Content Change
    - Actual: Clause group cards contain no Summarized/Full Text toggle; only the global "Full text" switch (id=full-text, aria-checked/data-state) exists outside the groups. Clicking it changes no group content (identical rendered text in both states; only span-wrapping markup changes), so the group's content does not change in place — and no active-view option is indicated on any per-group control because none exists.

- [X] IX-03: Clause-type filter responds immediately and indicates the selection.
  - Action: Select a clause type in the filter, then change or clear the selection.
  - Expected: The view updates immediately without a page reload, and the selected filter option shows a selected/active state.

## Content
- [X] CT-01: Clause group headings correctly name the clause type.
  - Action: Read the headings of all clause groups for the default contracts.
  - Expected: Each heading displays a clause type name (e.g., "Payment Terms", "Confidentiality", "Termination") that matches the clauses shown under it.

- [X] CT-02: Contract columns display the user-assigned contract names.
  - Action: Read the labels of each contract column/panel in a clause group.
  - Expected: Each column shows the name given to that contract, not a generic placeholder like "Contract 1" for a named contract.

- [ ] CT-03: Full-text view shows the clause wording exactly as in the source contract.
  - Action: Compare the full-text clause text displayed with the corresponding text in the original contract input.
  - Expected: Displayed text matches the source wording exactly — complete, unaltered, and not truncated.
  - Bug Report:
    - Issue: Clause Text Truncated — Clause Body Never Displayed
    - Actual: Only the clause heading line is displayed, in every view mode: e.g., the TechVentures Liability column shows "4. Limitation of Liability" (26 chars) while the source section is 297 chars ("4. Limitation of Liability Client shall pay Provider a monthly subscription fee of $2,500 USD, due on the first day of each month. Late payments shall incur a penalty of 1.5% per month…"). Confirmed with a known input: the column for "1. Payment Terms and Schedule" shows only the heading; its 200-char body ("The Client shall transmit payment within thirty (30) calendar days…") is never rendered. Displayed text is verbatim but incomplete/truncated.

- [X] CT-04: Summarized view content is relevant to its clause group only.
  - Action: Read the summary shown for one clause group in summarized view.
  - Expected: The summary reflects only that group's clause wording across the contracts, with no text from unrelated clause types.
