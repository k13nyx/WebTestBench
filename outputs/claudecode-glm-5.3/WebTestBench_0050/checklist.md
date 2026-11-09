# Test Checklist

## Functionality

- [ ] FT-01: User can add a contract with a name and full text
  - Action: Enter a contract name (e.g., "Vendor A") into the name field, paste a multi-clause contract text into the text input, and submit via the "Add Contract" button.
  - Expected: The contract is added to the workspace and its name is visible in the contract list / comparison view.

- [ ] FT-02: User can add multiple contracts for comparison
  - Action: Add at least 3 contracts, each with a distinct name and its own contract text.
  - Expected: All 3 contract names appear in the workspace, and all are included in the comparison display.

- [ ] FT-03: Clauses are automatically detected and grouped by type
  - Action: Add contract texts containing clauses with distinct topics (e.g., a payment terms clause, a confidentiality clause, a termination clause).
  - Expected: Each clause is assigned to a matching clause-type group (e.g., "Payment Terms", "Confidentiality", "Termination"); no clause is left ungrouped or placed in a clearly wrong group.

- [ ] FT-04: Same-type clauses from different contracts are shown side by side
  - Action: Add 2+ contracts that each contain a payment terms clause; open the "Payment Terms" clause group.
  - Expected: The payment terms clause from each contract is displayed in parallel columns, one column per contract, aligned by clause type.

- [ ] FT-05: Differences in wording between contracts are highlighted
  - Action: Add two contracts whose payment terms clauses differ in specific wording (e.g., "net 30 days" vs "net 60 days"); open that clause group in the comparison view.
  - Expected: The differing words/phrases are visually marked (e.g., background highlight) in each contract's clause text, and identical wording is not marked.

- [ ] FT-06: Summarized comparison view is available
  - Action: Open a clause group with the view toggle set to the summarized comparison mode.
  - Expected: A condensed summary of each contract's clause is shown per contract column (shorter than the full clause text, conveying the key terms).

- [ ] FT-07: Full-text view is available for each clause group
  - Action: Open a clause group with the view toggle set to full-text mode.
  - Expected: The complete, unabridged clause text is displayed for every contract in that group.

- [ ] FT-08: View mode can be switched per clause group
  - Action: With multiple clause groups displayed, switch one group to "Full Text" while another remains on "Summary".
  - Expected: Only the targeted group changes its display mode; the other group stays in its previously selected mode.

- [ ] FT-09: Filter view by clause type
  - Action: Apply a filter selecting only "Termination" (deselecting all other clause types).
  - Expected: Only the "Termination" clause group is displayed; all other clause groups are hidden from view.

- [ ] FT-10: Clearing the clause type filter restores all groups
  - Action: With a clause-type filter active, clear the filter (or re-select all clause types).
  - Expected: All clause-type groups present in the loaded contracts are visible again.

## Constraint

- [ ] CS-01: Contract cannot be added without a name
  - Action: Leave the contract name field empty, enter valid contract text, and attempt to submit.
  - Expected: The contract is NOT added, and the user is informed the name is required (inline message or disabled submit).

- [ ] CS-02: Contract cannot be added without text
  - Action: Enter a contract name but leave the text area empty, and attempt to submit.
  - Expected: The contract is NOT added, and the user is informed the contract text is required.

- [ ] CS-03: Identical clause wording is not flagged as a difference
  - Action: Add two contracts containing a confidentiality clause with identical wording; open that clause group in comparison view.
  - Expected: No difference highlights are shown for that clause group (identical text has no highlighting).

- [ ] CS-04: Filtered-out clause types are fully excluded from the display
  - Action: Add contracts containing Payment Terms, Confidentiality, and Termination clauses; apply a filter for "Payment Terms" only; switch the visible group between Summary and Full Text modes.
  - Expected: Confidentiality and Termination content never appears anywhere in the filtered view, in either display mode.

## Interaction

- [ ] IX-01: Switching between summary and full-text updates the display immediately
  - Action: With a clause group open in Summary mode, click the control to switch to Full Text, then back to Summary.
  - Expected: The clause group's content switches instantly between the summary and the full clause text on each click, without requiring a page reload.

- [ ] IX-02: Applying the clause-type filter updates the view immediately
  - Action: Select/deselect clause types in the filter control one at a time.
  - Expected: The displayed clause groups update immediately after each selection change to match the current filter selection.

- [ ] IX-03: Each contract is clearly labeled in the side-by-side view
  - Action: Open any clause group containing multiple contracts.
  - Expected: Each clause column is labeled with its contract's name, and the labels correctly match the clause content shown beneath them.

## Content

- [ ] CT-01: Clause type labels match the clause content
  - Action: Review each auto-detected clause group (e.g., "Payment Terms", "Confidentiality", "Termination") and read its member clauses.
  - Expected: Every clause placed in a group is genuinely about that group's topic (e.g., the "Payment Terms" group contains only clauses about payment amounts, schedules, or invoicing).

- [ ] CT-02: Summaries accurately reflect the full clause text
  - Action: For a clause group, compare the summarized view against the full-text view of the same clauses.
  - Expected: Each summary is consistent with its full clause text (no contradictions, no terms introduced that are absent from the full text, e.g., the correct payment period in both).

- [ ] CT-03: Contract names are displayed exactly as entered
  - Action: Add a contract with a specific name (e.g., "Acme MSA 2024") and inspect all views where the contract appears (list, side-by-side columns, labels).
  - Expected: The name is displayed verbatim, identical everywhere it appears.