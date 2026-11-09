# Test Result

## Functionality
- [ ] FT-01: Add a contract with custom name and text
  - Action: Enter "Vendor Agreement Alpha" into the Contract Name field, paste contract text into the Contract Text area, and click the "Add Contract" button.
  - Expected: The contract is added to the list and displays "Vendor Agreement Alpha" alongside its text.
  - Bug Report:
    - Issue: Missing Contract Text in List
    - Actual: The contract is added to the "Added Contracts" list displaying only the contract name "Vendor Agreement Alpha" and a delete button; the contract text is not displayed alongside its name in the list.
- [ ] FT-02: Auto-detect and group clauses across contracts
  - Action: Click the "Analyze Contracts" button with multiple contracts loaded.
  - Expected: Contract texts are parsed and clauses are automatically categorized under distinct groups (e.g., "Payment Terms", "Confidentiality", "Termination").
  - Bug Report:
    - Issue: Missing Action Button
    - Actual: There is no "Analyze Contracts" button in the application. Clause detection and grouping are performed automatically upon adding contracts rather than triggered by an analysis button.
- [X] FT-03: Display detected clauses side by side
  - Action: Scroll to any detected clause category (e.g., "Payment Terms") in the comparison section.
  - Expected: The corresponding clauses from each contract appear side by side in parallel columns under their respective contract names.
- [X] FT-04: Filter comparison view by specific clause type
  - Action: Select "Confidentiality" from the clause type filter selector.
  - Expected: Only the "Confidentiality" clause group is displayed; all other clause groups are hidden from view.
- [X] FT-05: Highlight wording differences between contracts
  - Action: Switch the "Highlight Differences" toggle to ON.
  - Expected: Text variations and conflicting wording across the side-by-side clauses are visually highlighted.
- [ ] FT-06: Switch clause group to Summarized Comparison view
  - Action: Click the "Summary" toggle button on a clause group.
  - Expected: The clause group displays a condensed summary of key terms for each contract instead of the raw text.
  - Bug Report:
    - Issue: Missing Element / Feature
    - Actual: Individual clause group cards do not contain a "Summary" toggle button. The application only provides a global "Full text" toggle switch and lacks per-clause-group summary toggle buttons.
- [ ] FT-07: Switch clause group to Full-Text view
  - Action: Click the "Full Text" toggle button on a clause group currently in summary view.
  - Expected: The complete, unabridged clause text for each contract is displayed side by side.
  - Bug Report:
    - Issue: Missing Element / Feature
    - Actual: Individual clause group cards do not contain a "Full Text" toggle button; view controls are only available via a global switch in the filter header.

## Constraint
- [ ] CS-01: Prevent adding contract with empty fields
  - Action: Leave the Contract Name or Contract Text field empty and click "Add Contract".
  - Expected: The contract is not added and a validation message indicates that both name and text are required.
  - Bug Report:
    - Issue: Missing Validation Message
    - Actual: The contract is not added because the "Add Contract" button is disabled, but no validation message is displayed to indicate that both name and text are required.
- [ ] CS-02: Enforce minimum contract requirement for comparison
  - Action: Attempt to click "Analyze Contracts" when fewer than two contracts have been added.
  - Expected: The "Analyze Contracts" button is disabled or an alert message indicates that at least two contracts are required to run a comparison.
  - Bug Report:
    - Issue: Missing Validation and Enforcement
    - Actual: There is no "Analyze Contracts" button, and the application automatically displays detected clauses in the comparison view even when only one contract has been added without enforcing a minimum of two contracts or displaying any alert.
- [ ] CS-03: Handle missing clause types in one or more contracts
  - Action: Compare contracts where Contract A contains a "Termination" clause but Contract B does not.
  - Expected: Under the "Termination" section, Contract B displays "Clause not found" without disrupting the alignment of other contracts.
  - Bug Report:
    - Issue: Missing Placeholder for Absent Clauses
    - Actual: When a contract does not contain a specific clause type (e.g., GlobalCorp lacks a Payment Terms clause), that contract is omitted completely from the section rather than displaying "Clause not found".

## Interaction
- [X] IX-01: Dynamic update of difference highlights
  - Action: Toggle the "Highlight Differences" switch from ON to OFF.
  - Expected: Highlighting styles are immediately removed from the text without reloading the page.
- [X] IX-02: Active state styling on clause filter selection
  - Action: Click the "Payment Terms" filter button in the filter bar.
  - Expected: The "Payment Terms" button displays an active selected state, and unselected filters visually de-emphasize.
- [ ] IX-03: In-place view toggling between Summary and Full Text
  - Action: Toggle between "Summary" and "Full Text" views on any clause group card.
  - Expected: The content view changes instantly without shifting the page scroll position or reloading.
  - Bug Report:
    - Issue: Missing In-place Toggle Controls
    - Actual: Clause group cards do not feature in-place toggle buttons between "Summary" and "Full Text" views.
- [X] IX-04: Remove contract from the input list
  - Action: Click the "Remove" button on a contract card prior to analysis.
  - Expected: The selected contract is immediately removed from the list and the total contract count updates.

## Content
- [X] CT-01: Standard legal clause category headers
  - Action: Review the section titles in the analyzed comparison view.
  - Expected: Headings display standard legal clause types, including "Payment Terms", "Confidentiality", and "Termination".
- [X] CT-02: Column header contract name fidelity
  - Action: Check the column headers within the side-by-side comparison cards.
  - Expected: Each column header exactly matches the simple name assigned to the contract during the input step.
- [ ] CT-03: Default sample contracts pre-population
  - Action: Load the application with default data.
  - Expected: Pre-existing sample contracts with predefined names and valid legal clause texts are loaded and ready for analysis.
  - Bug Report:
    - Issue: Missing Pre-populated Data
    - Actual: Upon initial application load, no sample contracts are pre-populated (the contract count is 0 and the UI displays "No contracts to compare"). Sample contracts require manual loading via sample buttons.