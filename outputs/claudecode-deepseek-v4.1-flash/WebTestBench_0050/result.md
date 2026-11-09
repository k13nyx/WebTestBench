I have completed all tests. Here is the full checklist with results.

# Test Result

## Functionality
- [X] FT-01: User can add a contract by entering a name and its text.
  - Action: Enter "Acme MSA" in the "Contract Name" field, paste contract text into the "Contract Text" area, and click "Add Contract".
  - Expected: The contract "Acme MSA" is added and appears in the comparison view.

- [X] FT-02: User can input several contracts and each is retained.
  - Action: Add three contracts named "Acme MSA", "Beta NDA", and "Gamma SOW" with distinct texts.
  - Expected: All three contracts are listed and displayed simultaneously; none is overwritten or lost.

- [ ] FT-03: Page auto-detects and groups clauses by type.
  - Action: Add contracts containing payment, confidentiality, and termination language, then view the comparison.
  - Expected: Clauses are automatically sorted into groups labeled "Payment Terms", "Confidentiality", and "Termination" without manual tagging.
  - Bug Report:
    - Issue: Clause detection is incomplete — "Confidentiality" and "Termination" are never detected.
    - Actual: Detected types are only "payment, liability, dispute, intellectual". A contract whose text is purely "Each party shall maintain the confidentiality of the other party confidential information and trade secrets…" and another whose text is purely "Either party may terminate this agreement for convenience upon thirty days prior written notice…" produce no Confidentiality or Termination group. Even the sample "TechVentures SaaS Agreement" (which explicitly contains sections "2. Confidentiality" and "3. Termination") yields no such groups. The groups rendered are only Payment Terms, Liability, Dispute Resolution, Intellectual Property.

- [X] FT-04: Clauses are shown side by side across contracts.
  - Action: View a clause group (e.g., "Payment Terms") with two or more contracts added.
  - Expected: Each contract occupies its own column within the group, aligned horizontally for direct comparison.

- [ ] FT-05: User can filter the view by clause type.
  - Action: Use the "Filter by Clause Type" control and select "Confidentiality" only.
  - Expected: Only the "Confidentiality" clause group remains visible; all other groups are hidden.
  - Bug Report:
    - Issue: The specified filter option does not exist.
    - Actual: The "Filter by clause:" control only renders toggle chips for clause types that were actually detected (Payment Terms, Liability, Dispute Resolution, Intellectual Property). There is no "Confidentiality" chip/option to select, because Confidentiality is never detected (see FT-03). The filter mechanism itself works for existing types (selecting "Liability" hides all other groups) but the required selection is impossible.

- [ ] FT-07: User can switch a clause group to the summarized comparison view.
  - Action: Select "Summary" view for a clause group.
  - Expected: The group shows a condensed summary of each contract's clause rather than the full text.
  - Bug Report:
    - Issue: No distinct summarized view exists.
    - Actual: The view-mode is a single global "Full text" switch (default off). In the "Summary" state each clause card still displays the complete raw clause text (e.g., Acme's full sentence). Comparing the rendered group container HTML in Summary vs Full-text state yields byte-identical markup, so no condensed summary is ever produced.

- [ ] FT-08: User can switch a clause group to the full-text view independently.
  - Action: Switch the "Payment Terms" group to "Full Text" while leaving "Confidentiality" in "Summary".
  - Expected: "Payment Terms" shows complete clause text while "Confidentiality" remains summarized; the two groups' view modes do not affect each other.
  - Bug Report:
    - Issue: No per-group view control; view mode is a single global toggle.
    - Actual: There is one global "Full text" switch in the toolbar (id `full-text`); clause groups have no individual view-mode control. Toggling it affects all groups at once, and (as noted in FT-07/CT-03) toggling it does not change the displayed content at all. Also, no "Confidentiality" group exists.

## Constraint
- [ ] CS-01: Contract cannot be added with an empty name.
  - Action: Leave "Contract Name" blank, enter valid text, and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates the name is required.
  - Bug Report:
    - Issue: Missing validation message.
    - Actual: With a blank name the "Add Contract" button is simply disabled (`disabled=true`) and no "name is required" message is rendered anywhere. The contract is not added, but the required validation message never appears.

- [ ] CS-02: Contract cannot be added with empty text.
  - Action: Enter a valid name, leave "Contract Text" blank, and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates the text is required.
  - Bug Report:
    - Issue: Missing validation message.
    - Actual: With a valid name and empty text the "Add Contract" button is disabled (`disabled=true`) and no "text is required" message is shown. The contract is not added, but the required validation message never appears.

- [ ] CS-03: Duplicate contract names are prevented or flagged.
  - Action: Add "Acme MSA", then attempt to add a second contract also named "Acme MSA".
  - Expected: The duplicate is rejected or the user is warned to use a unique name; two identical names are not silently created.
  - Bug Report:
    - Issue: Duplicate names are silently accepted.
    - Actual: After "Acme MSA" already existed, submitting a second "Acme MSA" added it without any rejection or warning. The "Added Contracts" list then showed "Acme MSA" twice, and the Payment Terms group displayed two identical "Acme MSA" columns.

- [ ] CS-04: Filtering to a clause type with no matches shows an empty state.
  - Action: Select a clause type that no added contract contains.
  - Expected: An explicit "No clauses found" (or equivalent) message is shown instead of a blank or broken view.
  - Bug Report:
    - Issue: Empty state is unreachable/not implemented.
    - Actual: The filter control only exposes clause types that already have matches (chips are derived from detected types), so a type with zero matches cannot be selected. No "No clauses found" empty-state message exists anywhere in the comparison view.

## Interaction
- [X] IX-01: Applying a clause-type filter updates the view immediately.
  - Action: Change the clause-type filter selection.
  - Expected: The visible clause groups update instantly without a full page reload.

- [X] IX-02: Toggling "Highlight Differences" updates the view without reload.
  - Action: Turn "Highlight Differences" on, then off.
  - Expected: Highlights appear and disappear immediately in the current view, with no page refresh required.

- [ ] IX-03: Switching view mode preserves other groups' states.
  - Action: Toggle one clause group's view mode, then inspect the remaining groups.
  - Expected: Other groups retain their previous view mode and scroll/selection state.
  - Bug Report:
    - Issue: No per-group view mode exists.
    - Actual: View mode is a single global "Full text" switch applying to all clause groups simultaneously; there is no way to toggle one group's view mode independently, so per-group state preservation cannot occur.

- [ ] IX-04: Adding a contract provides clear confirmation.
  - Action: Successfully add a contract.
  - Expected: A success confirmation (toast, banner, or inline message) appears and the new contract is visible in the comparison.
  - Bug Report:
    - Issue: Missing success confirmation.
    - Actual: After adding a contract, polling the notifications region (`aria-label="Notifications (F8)"`) over ~1.5s showed an empty `<ol>` — no toast, banner, or inline success message appeared. The only feedback is the contract appearing in the "Added Contracts" list.

## Content
- [X] CT-01: Contract names are displayed exactly as entered.
  - Action: Add a contract named "Acme MSA — 2026".
  - Expected: The comparison view shows "Acme MSA — 2026" verbatim, with no truncation or alteration.

- [ ] CT-02: Clause type labels match the actual clause content.
  - Action: Inspect each clause group's label against the text it contains.
  - Expected: Every group label correctly describes its clauses (e.g., payment language under "Payment Terms"); no clause is mislabeled.
  - Bug Report:
    - Issue: Clause content is mislabeled / mismatched with its group.
    - Actual: The "Payment Terms" group contains clauses with non-payment language, e.g., "Payment is due within 10 days of invoice receipt. Termination requires 90 days notice." and "Payment shall be made within 30 days. Confidentiality obligations survive. Either party may terminate with 30 days notice." Conversely, the "Liability", "Dispute Resolution", and "Intellectual Property" groups contain only the section heading lines (e.g., "4. Limitation of Liability") with the actual clause body omitted, so group content does not faithfully match its label.

- [ ] CT-03: Summarized view content differs from and is shorter than full text.
  - Action: Compare a group's "Summary" output with its "Full Text" output.
  - Expected: The summary is condensed and meaningfully distinct from the full clause text, not a verbatim copy.
  - Bug Report:
    - Issue: Summary and Full-text outputs are identical.
    - Actual: Capturing the rendered group container with "Full text" off (Summary) and on (Full Text) produced byte-identical HTML (5668 chars in both). The "Summary" shows the full verbatim clause text, not a condensed version.

- [X] CT-04: No placeholder or irrelevant content appears in the comparison.
  - Action: Review all clause groups and contract columns after adding default/pre-existing contracts.
  - Expected: Only content derived from the entered contracts is shown; no lorem ipsum, sample text, or unrelated clauses.