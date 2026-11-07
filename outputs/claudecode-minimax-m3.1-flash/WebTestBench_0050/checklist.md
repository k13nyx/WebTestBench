# Test Checklist

> Test data: use the sample contracts already provided by the application. If the app ships none, paste contract text containing clearly labelled sections (e.g. "Payment Terms", "Confidentiality", "Termination") into the input area — the same text across two or more contracts with deliberately different wording (different payment days, different notice periods) so clause detection and difference highlighting are observable.

## Functionality
- [ ] FT-01: A contract can be added with a name and its full text
  - Action: Enter a name (e.g. "Master Services Agreement") in the contract name field, paste contract text into the contract text area, click **Add Contract**.
  - Expected: The contract appears in the contract list with the exact name entered, and a success confirmation (toast or list entry) is shown.

- [ ] FT-02: Multiple contracts are accepted and listed together
  - Action: Add three contracts with distinct names ("MSA", "NDA", "Sow") and different texts.
  - Expected: All three contracts appear in the contract list, each with its own name and text, with no entries overwritten or merged.

- [ ] FT-03: Clause types are auto-detected and grouped without manual tagging
  - Action: Add the contracts and observe the comparison area without using any manual "assign clause type" control.
  - Expected: Clauses are auto-classified into named groups such as **Payment Terms**, **Confidentiality**, and **Termination**, and each group lists the clauses belonging to it.

- [ ] FT-04: Clauses of the same type are displayed side by side, one column per contract
  - Action: Open a detected clause group (e.g. Payment Terms).
  - Expected: The group shows one column per added contract, with that contract's Payment Terms clause in its own column.

- [ ] FT-05: The view can be filtered by clause type
  - Action: Select a single clause type (e.g. "Confidentiality") in the clause type filter.
  - Expected: Only the Confidentiality clause group is displayed; groups of other clause types are hidden from the view.

- [ ] FT-06: Wording differences between contracts are highlighted
  - Action: Open a clause group in which the contracts word the clause differently (e.g. payment in 30 vs 60 days).
  - Expected: The differing words/values are visually highlighted (distinct color, underline, or marker) in each contract's column, and identical wording is not highlighted.

- [ ] FT-07: Each clause group can switch between summarized and full-text views
  - Action: In one clause group, use the Summary / Full text (view mode) control to switch to full text, then switch another group to summary.
  - Expected: The selected group shows the complete original clause text in full-text mode and a shortened summary in summary mode; the other group keeps its own independent mode.

## Constraint
- [ ] CS-01: A contract cannot be added without a name
  - Action: Leave the contract name field empty, enter contract text, click **Add Contract**.
  - Expected: Submission is rejected, an inline validation/error message appears near the name field, and no contract is added to the list.

- [ ] CS-02: A contract cannot be added without text
  - Action: Enter a name only and click **Add Contract**.
  - Expected: Submission is rejected, a validation/error message appears, and no empty contract is created.

- [ ] CS-03: Duplicate contract names are rejected
  - Action: Add a contract named "MSA", then attempt to add a second contract also named "MSA".
  - Expected: The second add is rejected with a duplicate-name error, and the list still contains only one "MSA" entry.

- [ ] CS-04: A contract missing a clause type is marked as absent, not misaligned
  - Action: Ensure one of the contracts has no Confidentiality clause, then open the Confidentiality group.
  - Expected: That contract's column shows an explicit "not present"/"No such clause" marker, and the other contracts' clauses remain correctly aligned in their own columns.

- [ ] CS-05: Filtering does not alter the underlying data of hidden groups
  - Action: Filter to "Termination", then clear the filter.
  - Expected: All previously detected clause groups reappear with their original contents intact and the same active selection.

## Interaction
- [ ] IX-01: Clicking a clause type in the filter list applies that filter
  - Action: Click the clause type option labeled "Payment Terms" in the filter/legend.
  - Expected: The Payment Terms group is shown, other groups are hidden, and the clicked option shows an active/selected visual state.

- [ ] IX-02: A "show all"/reset option restores every clause group
  - Action: With a clause type filter active, click the **All** (show all) option.
  - Expected: All detected clause groups are displayed simultaneously and the filter control shows no active specific type.

- [ ] IX-03: The summary/full-text toggle switches view mode immediately
  - Action: Click the Summary / Full text toggle within a clause group.
  - Expected: The group's content changes instantly without a page reload, and the toggle reflects the current mode.

- [ ] IX-04: Difference highlighting can be toggled on and off
  - Action: Toggle the difference-highlight control off, then on again.
  - Expected: Highlighted differences disappear when off and reappear when on, without changing clause text or grouping.

- [ ] IX-05: Adding a contract automatically re-runs detection and updates the view
  - Action: Add a fourth contract after the groups are displayed.
  - Expected: A new column for the added contract appears in the existing groups, the new contract's clauses are detected and classified, and a processing/loading indication is shown while analysis runs.

## Content
- [ ] CT-01: Clause group labels use recognizable legal clause-type names
  - Action: Inspect the names of the detected clause groups.
  - Expected: Labels are meaningful legal clause types (e.g. "Payment Terms", "Confidentiality", "Termination") and contain no generic placeholders such as "Group 1" or "Clause Type A".

- [ ] CT-02: Each comparison column is labeled with its contract name
  - Action: Read the column headers in any clause group.
  - Expected: Every column header shows the exact contract name given at input time and matches the corresponding contract list entry.

- [ ] CT-03: Displayed clause text faithfully matches the entered contract text
  - Action: Compare the full-text view of a clause against the same text in the contract input.
  - Expected: The clause wording, figures, and dates match the source text with no invented, truncated, or altered content.

- [ ] CT-04: Summary view content is relevant to that clause's meaning and type
  - Action: Switch a Payment Terms group to summary and read each column's summary.
  - Expected: Each summary conveys that contract's payment terms (e.g. the actual payment period/due date), and the Confidentiality group's summary covers confidentiality obligations rather than unrelated content.