# Test Result

## Functionality
- [X] FT-01: User can add multiple contracts, each with a name and text.
  - Action: Enter a name and paste the text of two default contracts, submitting each one.
  - Expected: Both contracts appear in the contract list with their entered names and full text retained.

- [ ] FT-02: Clauses are auto-grouped by type.
  - Action: Load the default contracts and run the comparison (or observe the grouping if it is automatic).
  - Expected: Clauses appear under groups labeled "Payment Terms", "Confidentiality", and "Termination".
  - Bug Report:
    - Issue: Incorrect Clause Grouping (Missing Detection)
    - Actual: The labels exist, but TechVentures' clauses "1. Payment Terms", "2. Confidentiality", and "3. Termination" are not placed in any of these groups. The Confidentiality and Termination groups list only GlobalCorp and StartupX. The Payment Terms group did not appear until StartupX was added, and then it held only StartupX's "1. Compensation Terms" clause. GlobalCorp's "1. Payment and Fees" clause is also not detected.

- [ ] FT-03: Contracts are shown side by side within each clause group.
  - Action: Open the "Payment Terms" group.
  - Expected: Each contract's payment clause is in its own column, headed by that contract's name, in the same group.
  - Bug Report:
    - Issue: Missing Contract Column
    - Actual: The "Payment Terms" group shows a single column, "StartupX Consulting Agreement" ("1. Compensation Terms"). No column is shown for "TechVentures SaaS Agreement" or "GlobalCorp Enterprise License", although both contain payment clauses.

- [X] FT-04: User can filter the view to one clause type.
  - Action: Select "Confidentiality" in the clause-type filter.
  - Expected: Only the Confidentiality group is displayed; Payment Terms and Termination groups are hidden.

- [X] FT-05: User can clear the filter to show all clause types.
  - Action: Select "All" (or clear the filter) after FT-04.
  - Expected: All clause groups are displayed again.

- [ ] FT-06: User can switch a clause group to full-text view.
  - Action: Click "Full Text" for the "Termination" group.
  - Expected: Each contract's complete original termination clause is displayed.
  - Bug Report:
    - Issue: Missing Per-Group Control / Clause Body Not Rendered
    - Actual: The only "Full text" control is a page-level switch in the header. No "Full Text" control exists inside the Termination group. After the switch is enabled, the Termination column still shows only the heading "3. Term and Termination", not the clause body. The text is identical to the summary view.

- [ ] FT-07: User can switch a clause group back to summary view, independently of other groups.
  - Action: Set "Termination" to Full Text, set "Payment Terms" to Full Text, then click "Summary" on "Termination" only.
  - Expected: "Termination" shows summaries; "Payment Terms" remains in full-text view.
  - Bug Report:
    - Issue: Missing Per-Group View Toggle
    - Actual: No "Summary" control or per-group toggle exists in any group. Group headers contain only the group title and a clause count. The single "Full text" switch applies to all groups at once, so the independent per-group behavior cannot be exercised.

## Constraint
- [ ] CS-01: Contract cannot be added without a name.
  - Action: Leave the name field blank, enter contract text, and submit.
  - Expected: The contract is not added and an error states that a name is required.
  - Bug Report:
    - Issue: Missing Validation Error Message
    - Actual: With the name blank and contract text entered, the "Add Contract" button is disabled and no error text appears in the DOM. The contract is not added, but no message states that a name is required.

- [ ] CS-02: Contract cannot be added without text.
  - Action: Enter a name, leave the contract text blank, and submit.
  - Expected: The contract is not added and an error states that contract text is required.
  - Bug Report:
    - Issue: Missing Validation Error Message
    - Actual: With the name "Blank Text Test" entered and the text blank, the "Add Contract" button is disabled. No error text is present in the DOM, and no contract is added.

- [X] CS-03: Each clause belongs to exactly one clause group.
  - Action: Compare the "Payment Terms", "Confidentiality", and "Termination" groups for the same contract.
  - Expected: No clause text from one contract appears in more than one group.

- [ ] CS-04: A missing clause type is shown as missing, not filled with another contract's clause.
  - Action: Find a clause group where one default contract has no matching clause.
  - Expected: That contract's column shows a "no clause found" message, and no clause from another contract is displayed in its place.
  - Bug Report:
    - Issue: Missing Clause State Not Displayed
    - Actual: In the Confidentiality and Termination groups, the TechVentures column is absent entirely. No "no clause found" text appears anywhere on the page (checked via DOM text search). The group shows no placeholder for the missing contract, and no clause from another contract was substituted.

## Interaction
- [X] IX-01: Differing wording is highlighted across contracts within a group.
  - Action: Open the "Termination" group in summary view, then in full-text view.
  - Expected: Words or phrases that differ between contracts are visibly highlighted in each column; identical wording is not highlighted.
  - Note: In the Liability group, differing words such as "Limitation", "of", "and", "Warranties", and "Clause" carry the `diff-highlight-different` class. The shared word "Liability" is not highlighted. Highlighting is applied only to the displayed heading text, because the full-text bodies do not render (see FT-06 and CT-02).

- [X] IX-02: The selected filter and active view mode are visually distinguished.
  - Action: Select a clause-type filter, then switch a group to "Full Text".
  - Expected: The selected filter option and the active "Full Text" control look different from unselected options.
  - Note: The selected filter chip gains a check icon and a "Clear all" control appears. The active "Full text" switch has `checked` and `active` attributes, and the unselected state lacks them. These DOM differences were checked; the rendered appearance was not visually verified.

- [X] IX-03: Adding a contract updates the comparison without leaving the page.
  - Action: Add a third contract with a name and text.
  - Expected: Its column appears in every clause group where its clauses are detected, and the page does not reload or navigate away.
  - Note: "StartupX Consulting Agreement" was added. Its column appeared in Liability, Dispute Resolution, Intellectual Property, Confidentiality, Termination, Payment Terms, and Indemnification. The clause count rose from 8 to 15. A window marker set before the add was still present afterward, and the URL and navigation entry count were unchanged.

## Content
- [X] CT-01: Clauses under each group label belong to that group's topic.
  - Action: Read every clause under "Payment Terms", then under "Confidentiality" and "Termination".
  - Expected: Each clause under a label concerns that topic (e.g., payment amounts, schedules, or late fees under Payment Terms); none belong to a different topic.
  - Note: The clauses shown under each existing label match its topic. The "Governing Law and Jurisdiction" clause under Dispute Resolution and the "Liability and Warranties" clause under Liability are borderline; they are arguably related to their groups. Coverage is limited, because the Payment Terms group holds only one clause (see FT-02, FT-03).

- [ ] CT-02: Full-text view matches the original contract wording.
  - Action: Compare each full-text clause with the same clause in the source contract text.
  - Expected: Wording is identical, with no truncated, added, or altered sentences.
  - Bug Report:
    - Issue: Truncated Full-Text Content
    - Actual: In full-text view, each column shows only the clause heading (for example, "3. Term and Termination" or "4. Limitation of Liability"). No body sentences such as "Either party may terminate this agreement with 30 days written notice" are rendered, so the wording cannot be compared.

- [ ] CT-03: Summaries contain only information from their full clause.
  - Action: For each summary, check it against the full text of the same clause.
  - Expected: Every obligation, date, amount, or period in the summary appears in the full clause, and nothing is invented.
  - Bug Report:
    - Issue: Missing Summary Content
    - Actual: No summary text is displayed anywhere. The summary view shows only the clause heading, identical to the full-text view. No obligations, amounts, or periods appear, so there is no summary content to check.

- [X] CT-04: Contract names in column headers match the names entered.
  - Action: Compare the column headers in each group with the names used when adding the contracts.
  - Expected: Each header matches the entered name exactly, and each column's clause comes from the contract with that name.
  - Note: Headers read "TechVentures SaaS Agreement", "GlobalCorp Enterprise License", and "StartupX Consulting Agreement", which match the names entered. Each column's clause heading matches its source contract (for example, "4. Limitation of Liability" under TechVentures and "4. Liability and Warranties" under GlobalCorp).
