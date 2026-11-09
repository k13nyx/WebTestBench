# Test Checklist

## Functionality
- [ ] FT-01: User can add a contract by entering a name and its text.
  - Action: Enter "Acme MSA" in the "Contract Name" field, paste contract text into the "Contract Text" area, and click "Add Contract".
  - Expected: The contract "Acme MSA" is added and appears in the comparison view.

- [ ] FT-02: User can input several contracts and each is retained.
  - Action: Add three contracts named "Acme MSA", "Beta NDA", and "Gamma SOW" with distinct texts.
  - Expected: All three contracts are listed and displayed simultaneously; none is overwritten or lost.

- [ ] FT-03: Page auto-detects and groups clauses by type.
  - Action: Add contracts containing payment, confidentiality, and termination language, then view the comparison.
  - Expected: Clauses are automatically sorted into groups labeled "Payment Terms", "Confidentiality", and "Termination" without manual tagging.

- [ ] FT-04: Clauses are shown side by side across contracts.
  - Action: View a clause group (e.g., "Payment Terms") with two or more contracts added.
  - Expected: Each contract occupies its own column within the group, aligned horizontally for direct comparison.

- [ ] FT-05: User can filter the view by clause type.
  - Action: Use the "Filter by Clause Type" control and select "Confidentiality" only.
  - Expected: Only the "Confidentiality" clause group remains visible; all other groups are hidden.

- [ ] FT-06: User can highlight wording differences between contracts.
  - Action: Enable "Highlight Differences" for a clause group whose wording varies between contracts.
  - Expected: Differing words/phrases are visually marked (e.g., colored or underlined) in each affected contract column.

- [ ] FT-07: User can switch a clause group to the summarized comparison view.
  - Action: Select "Summary" view for a clause group.
  - Expected: The group shows a condensed summary of each contract's clause rather than the full text.

- [ ] FT-08: User can switch a clause group to the full-text view independently.
  - Action: Switch the "Payment Terms" group to "Full Text" while leaving "Confidentiality" in "Summary".
  - Expected: "Payment Terms" shows complete clause text while "Confidentiality" remains summarized; the two groups' view modes do not affect each other.

## Constraint
- [ ] CS-01: Contract cannot be added with an empty name.
  - Action: Leave "Contract Name" blank, enter valid text, and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates the name is required.

- [ ] CS-02: Contract cannot be added with empty text.
  - Action: Enter a valid name, leave "Contract Text" blank, and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates the text is required.

- [ ] CS-03: Duplicate contract names are prevented or flagged.
  - Action: Add "Acme MSA", then attempt to add a second contract also named "Acme MSA".
  - Expected: The duplicate is rejected or the user is warned to use a unique name; two identical names are not silently created.

- [ ] CS-04: Filtering to a clause type with no matches shows an empty state.
  - Action: Select a clause type that no added contract contains.
  - Expected: An explicit "No clauses found" (or equivalent) message is shown instead of a blank or broken view.

## Interaction
- [ ] IX-01: Applying a clause-type filter updates the view immediately.
  - Action: Change the clause-type filter selection.
  - Expected: The visible clause groups update instantly without a full page reload.

- [ ] IX-02: Toggling "Highlight Differences" updates the view without reload.
  - Action: Turn "Highlight Differences" on, then off.
  - Expected: Highlights appear and disappear immediately in the current view, with no page refresh required.

- [ ] IX-03: Switching view mode preserves other groups' states.
  - Action: Toggle one clause group's view mode, then inspect the remaining groups.
  - Expected: Other groups retain their previous view mode and scroll/selection state.

- [ ] IX-04: Adding a contract provides clear confirmation.
  - Action: Successfully add a contract.
  - Expected: A success confirmation (toast, banner, or inline message) appears and the new contract is visible in the comparison.

## Content
- [ ] CT-01: Contract names are displayed exactly as entered.
  - Action: Add a contract named "Acme MSA — 2026".
  - Expected: The comparison view shows "Acme MSA — 2026" verbatim, with no truncation or alteration.

- [ ] CT-02: Clause type labels match the actual clause content.
  - Action: Inspect each clause group's label against the text it contains.
  - Expected: Every group label correctly describes its clauses (e.g., payment language under "Payment Terms"); no clause is mislabeled.

- [ ] CT-03: Summarized view content differs from and is shorter than full text.
  - Action: Compare a group's "Summary" output with its "Full Text" output.
  - Expected: The summary is condensed and meaningfully distinct from the full clause text, not a verbatim copy.

- [ ] CT-04: No placeholder or irrelevant content appears in the comparison.
  - Action: Review all clause groups and contract columns after adding default/pre-existing contracts.
  - Expected: Only content derived from the entered contracts is shown; no lorem ipsum, sample text, or unrelated clauses.