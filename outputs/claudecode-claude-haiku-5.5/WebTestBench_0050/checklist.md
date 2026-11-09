# Test Checklist

## Functionality
- [ ] FT-01: User can add multiple contracts, each with a name and text.
  - Action: Enter a name and paste the text of two default contracts, submitting each one.
  - Expected: Both contracts appear in the contract list with their entered names and full text retained.
- [ ] FT-02: Clauses are auto-grouped by type.
  - Action: Load the default contracts and run the comparison (or observe the grouping if it is automatic).
  - Expected: Clauses appear under groups labeled "Payment Terms", "Confidentiality", and "Termination".
- [ ] FT-03: Contracts are shown side by side within each clause group.
  - Action: Open the "Payment Terms" group.
  - Expected: Each contract's payment clause is in its own column, headed by that contract's name, in the same group.
- [ ] FT-04: User can filter the view to one clause type.
  - Action: Select "Confidentiality" in the clause-type filter.
  - Expected: Only the Confidentiality group is displayed; Payment Terms and Termination groups are hidden.
- [ ] FT-05: User can clear the filter to show all clause types.
  - Action: Select "All" (or clear the filter) after FT-04.
  - Expected: All clause groups are displayed again.
- [ ] FT-06: User can switch a clause group to full-text view.
  - Action: Click "Full Text" for the "Termination" group.
  - Expected: Each contract's complete original termination clause is displayed.
- [ ] FT-07: User can switch a clause group back to summary view, independently of other groups.
  - Action: Set "Termination" to Full Text, set "Payment Terms" to Full Text, then click "Summary" on "Termination" only.
  - Expected: "Termination" shows summaries; "Payment Terms" remains in full-text view.

## Constraint
- [ ] CS-01: Contract cannot be added without a name.
  - Action: Leave the name field blank, enter contract text, and submit.
  - Expected: The contract is not added and an error states that a name is required.
- [ ] CS-02: Contract cannot be added without text.
  - Action: Enter a name, leave the contract text blank, and submit.
  - Expected: The contract is not added and an error states that contract text is required.
- [ ] CS-03: Each clause belongs to exactly one clause group.
  - Action: Compare the "Payment Terms", "Confidentiality", and "Termination" groups for the same contract.
  - Expected: No clause text from one contract appears in more than one group.
- [ ] CS-04: A missing clause type is shown as missing, not filled with another contract's clause.
  - Action: Find a clause group where one default contract has no matching clause.
  - Expected: That contract's column shows a "no clause found" message, and no clause from another contract is displayed in its place.

## Interaction
- [ ] IX-01: Differing wording is highlighted across contracts within a group.
  - Action: Open the "Termination" group in summary view, then in full-text view.
  - Expected: Words or phrases that differ between contracts are visibly highlighted in each column; identical wording is not highlighted.
- [ ] IX-02: The selected filter and active view mode are visually distinguished.
  - Action: Select a clause-type filter, then switch a group to "Full Text".
  - Expected: The selected filter option and the active "Full Text" control look different from unselected options.
- [ ] IX-03: Adding a contract updates the comparison without leaving the page.
  - Action: Add a third contract with a name and text.
  - Expected: Its column appears in every clause group where its clauses are detected, and the page does not reload or navigate away.

## Content
- [ ] CT-01: Clauses under each group label belong to that group's topic.
  - Action: Read every clause under "Payment Terms", then under "Confidentiality" and "Termination".
  - Expected: Each clause under a label concerns that topic (e.g., payment amounts, schedules, or late fees under Payment Terms); none belong to a different topic.
- [ ] CT-02: Full-text view matches the original contract wording.
  - Action: Compare each full-text clause with the same clause in the source contract text.
  - Expected: Wording is identical, with no truncated, added, or altered sentences.
- [ ] CT-03: Summaries contain only information from their full clause.
  - Action: For each summary, check it against the full text of the same clause.
  - Expected: Every obligation, date, amount, or period in the summary appears in the full clause, and nothing is invented.
- [ ] CT-04: Contract names in column headers match the names entered.
  - Action: Compare the column headers in each group with the names used when adding the contracts.
  - Expected: Each header matches the entered name exactly, and each column's clause comes from the contract with that name.