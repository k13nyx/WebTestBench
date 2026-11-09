# Test Checklist

## Functionality
- [ ] FT-01: Page loads with default contract data pre-populated
  - Action: Open the page and inspect the contract list/panels.
  - Expected: At least two default contracts are present, each with a visible name and clause content already grouped; the comparison view is rendered without any user input.

- [ ] FT-02: User can add a new contract with a name and text
  - Action: Enter a name (e.g., "Vendor A") into the contract name field, paste a contract text containing payment, confidentiality, and termination clauses into the text area, and click the "Add Contract" (or equivalent) button.
  - Expected: The new contract appears in the contract list by its name, and its clauses are detected and placed into the correct type groups.

- [ ] FT-03: Clauses are auto-detected and grouped by type
  - Action: After contracts are loaded, inspect the grouping structure.
  - Expected: Clauses are organized under type headings (at minimum "Payment Terms", "Confidentiality", "Termination"), and each detected clause appears under exactly one type heading.

- [ ] FT-04: Clauses of the same type are shown side by side across contracts
  - Action: Open the "Payment Terms" group.
  - Expected: The payment clause from each contract is displayed in a separate side-by-side column/panel, each labeled with its contract's name.

- [ ] FT-05: View can be filtered by clause type
  - Action: Use the clause-type filter control and select a single type (e.g., "Confidentiality").
  - Expected: Only the Confidentiality group is displayed; all other groups (Payment Terms, Termination) are hidden.

- [ ] FT-06: Filter can be reset to show all clause types
  - Action: Select "All" (or clear the filter) in the clause-type filter control.
  - Expected: Every detected clause group is displayed again.

- [ ] FT-07: Wording differences between contracts are highlighted
  - Action: Open a clause group where the same clause differs between two or more contracts.
  - Expected: Differing words/phrases are visually marked (e.g., colored or struck-through highlight) so non-matching text is distinguishable from matching text.

- [ ] FT-08: User can switch a clause group to full-text view
  - Action: In a clause group, activate the "Full text" view toggle.
  - Expected: That group expands to show the complete clause text of every contract in the group, not just the summary.

- [ ] FT-09: User can switch a clause group back to summarized comparison view
  - Action: With a group in full-text mode, activate the "Summary" / "Comparison" view toggle.
  - Expected: That group returns to the condensed side-by-side comparison display.

- [ ] FT-10: Removing a contract updates the comparison
  - Action: Delete one contract via its remove control.
  - Expected: The contract disappears from the list, and all clause groups re-render without its column.

## Constraint
- [ ] CS-01: A contract cannot be added with an empty name
  - Action: Leave the name field blank, paste valid contract text, and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates the name is required.

- [ ] CS-02: A contract cannot be added with empty clause text
  - Action: Enter a name, leave the contract text area empty, and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates contract text is required.

- [ ] CS-03: Filter results contain only the selected clause type
  - Action: Filter by "Termination" and enumerate the group headings visible.
  - Expected: No non-termination clause content is rendered anywhere in the comparison area.

- [ ] CS-04: The same view mode state is not forced across all groups
  - Action: Set one group (e.g., "Payment Terms") to Full text while another group ("Confidentiality") remains in Summary.
  - Expected: Each group retains its own view mode; switching one group does not silently change the other.

- [ ] CS-05: A clause type present in only one contract still renders correctly
  - Action: Add a contract that contains only a "Termination" clause, then open the Termination group.
  - Expected: The group renders that single clause without error and without empty placeholder columns for contracts that lack the clause type (or explicitly marks them as "not present").

## Interaction
- [ ] IX-01: Adding a contract gives immediate visual feedback
  - Action: Click "Add Contract" with valid name and text.
  - Expected: A success indicator (toast, status message, or newly highlighted contract panel) confirms the contract was added and re-analysis is triggered.

- [ ] IX-02: View toggle and filter controls reflect current state
  - Action: Click the "Full text"/"Summary" toggle and the clause-type filter.
  - Expected: The active control shows a distinct selected/pressed state, and the comparison area re-renders without a full page reload.

- [ ] IX-03: Difference highlighting is discoverable on hover
  - Action: Hover the pointer over a highlighted differing phrase in a clause.
  - Expected: A tooltip or legend explains what the highlight means (e.g., "differs from other contracts") rather than the mark being unexplained.

## Content
- [ ] CT-01: Clause type labels match the instruction's taxonomy
  - Action: Read all group headings.
  - Expected: Only clause-type labels are used (e.g., Payment Terms, Confidentiality, Termination) — no random or empty headings, and no heading unrelated to contract clauses.

- [ ] CT-02: Each clause panel is correctly attributed to its contract
  - Action: Compare a known sentence from the "Vendor A" contract text with the panel labeled "Vendor A" in a group.
  - Expected: The displayed clause text and highlight content belong to that contract; no clause is shown under the wrong contract name.

- [ ] CT-03: Summarized view content is derived from the full clause text
  - Action: For one group, compare the summary entries against the same group's full-text entries.
  - Expected: The summary reflects key terms actually present in the full text (no invented clause content, no blank summaries).