# Test Result

## Functionality
- [ ] FT-01: Create a new customer record with niche attributes
  - Action: Click "+ New Customer", fill in "Full Name", "Email", "Collector Interests", and click "Save Customer".
  - Expected: The new customer record appears in the customer table with all submitted attributes.
  - Bug Report:
    - Issue: Missing Form Fields and Mismatched Controls
    - Actual: The modal trigger is labeled "Add Customer" and the submission button is labeled "Create Customer". The form provides fields for "First Name", "Last Name", "Email", "Phone", "Status", and "Notes", but completely lacks a "Collector Interests" field, preventing niche attributes from being submitted.

- [ ] FT-02: Update existing customer details
  - Action: Open a default customer record, edit the "Notes" and "Collector Interests" fields, and click "Save Changes".
  - Expected: Customer record updates and displays the modified notes and interests.
  - Bug Report:
    - Issue: Missing Form Field
    - Actual: The "Edit Customer" dialog only includes inputs for "First Name", "Last Name", "Email", "Phone", and "Notes". There is no field for "Collector Interests", so collector interests cannot be edited or updated.

- [ ] FT-03: Attach a related business item to a customer
  - Action: In an existing customer record, click "Attach Artwork", select an artwork from the item catalog, and click "Confirm".
  - Expected: The selected artwork appears in the customer's "Attached Artworks" list.
  - Bug Report:
    - Issue: Mismatched UI Labels and Missing Confirmation Step
    - Actual: The button is labeled "Add Artwork" rather than "Attach Artwork". Clicking an artwork in the modal adds it immediately without any "Confirm" button, and it is added to a list titled "Interested Artworks" instead of "Attached Artworks".

- [ ] FT-04: Update customer workflow status
  - Action: Open an existing customer record, select "Exhibition Invited" from the "Workflow Status" dropdown, and click "Update Status".
  - Expected: The customer's status badge updates to "Exhibition Invited".
  - Bug Report:
    - Issue: Missing Dropdown Option and Action Button
    - Actual: The status dropdown options are "New Lead", "Contacted", "Interested", "Negotiating", "Purchased", "VIP Collector", and "Inactive". "Exhibition Invited" is not an available option, and there is no "Update Status" button.

- [ ] FT-05: Filter customer directory by niche attribute
  - Action: Click the "Filter" dropdown, select "Collector Interest: Modern Art", and click "Apply Filter".
  - Expected: Customer table displays only records tagged with the "Modern Art" interest.
  - Bug Report:
    - Issue: Missing Filter Feature
    - Actual: There is no "Filter" dropdown for collector interests (only a status combobox with status values), no option for "Collector Interest: Modern Art", and no "Apply Filter" button.

- [ ] FT-06: Configure summary performance reports
  - Action: Navigate to "Performance Reports", select "Artwork Revenue" from the report type selector, and choose date range "Last 30 Days".
  - Expected: Report dashboard displays revenue charts and totals corresponding to the selected 30-day timeframe.
  - Bug Report:
    - Issue: Missing Report Configuration Controls
    - Actual: The Reports view only has static navigation tabs ("Revenue", "Engagement", "Sales Funnel") and lacks both an "Artwork Revenue" report type selector and a date range picker ("Last 30 Days").

## Constraint
- [ ] CS-01: Prevent customer creation with empty required fields
  - Action: Click "+ New Customer", leave "Full Name" and "Email" blank, and click "Save Customer".
  - Expected: Form submission is blocked, and validation error messages appear under "Full Name" and "Email".
  - Bug Report:
    - Issue: Missing Inline Field Validation Messages
    - Actual: Although form submission is blocked, no validation error messages appear under the input fields (the fields are separate "First Name" and "Last Name" inputs, and no error message elements are rendered below them in the DOM).

- [ ] CS-02: Prevent saving invalid email format
  - Action: In an existing customer edit form, enter "invalid-email-format" into the "Email" field and click "Save Changes".
  - Expected: System displays "Please enter a valid email address" and prevents saving.
  - Bug Report:
    - Issue: Missing Form Validation
    - Actual: The form performs no email format validation. The string "invalid-email-format" is accepted and saved directly to the customer profile without showing "Please enter a valid email address" or preventing saving.

- [ ] CS-03: Prevent attaching duplicate items to the same customer
  - Action: Open a customer with an existing attached artwork and attempt to select and attach that same artwork again.
  - Expected: The artwork is disabled in the selection modal or an alert displays "Item already attached to customer".
  - Bug Report:
    - Issue: Missing Disabled State or Duplicate Alert
    - Actual: Existing attached artworks are completely excluded/omitted from the modal list rather than being displayed as disabled or generating an alert message reading "Item already attached to customer".

- [X] CS-04: Display empty state for non-matching search queries
  - Action: Type "UNKNOWN_QUERY_999" into the customer search bar and press Enter.
  - Expected: Customer table displays zero records and shows an empty state message "No customers found".

## Interaction
- [ ] IX-01: Open customer detail drawer on row selection
  - Action: Click on any customer row in the customer directory table.
  - Expected: Customer detail panel slides open from the right side of the screen displaying the full customer profile.
  - Bug Report:
    - Issue: Incorrect Navigation Pattern
    - Actual: Clicking on a customer in the directory navigates to a new standalone page route (`/customers/:id`) instead of sliding open a detail drawer panel from the right side of the screen.

- [ ] IX-02: Display success notification upon profile update
  - Action: Modify an existing customer's contact number and click "Save Changes".
  - Expected: A confirmation toast notification reading "Customer record updated successfully" appears in the top-right corner.
  - Bug Report:
    - Issue: Notification Text Mismatch and Unrendered Toast
    - Actual: No toast notification reading "Customer record updated successfully" is displayed in the top-right corner upon saving changes.

- [ ] IX-03: Dynamic report refresh on metric view switch
  - Action: In the "Performance Reports" view, switch the aggregation toggle from "Monthly" to "Quarterly".
  - Expected: KPI summary cards and performance charts refresh dynamically without triggering a full page reload.
  - Bug Report:
    - Issue: Missing Aggregation Toggle Control
    - Actual: There is no aggregation toggle ("Monthly" / "Quarterly") available in the Reports dashboard.

## Content
- [ ] CT-01: Niche-specific customer profile sections
  - Action: Open any default customer profile view.
  - Expected: Profile displays sections labeled "Collector Interests", "Exhibition Invitations", and "Acquired Artworks".
  - Bug Report:
    - Issue: Mismatched Section Headings
    - Actual: The profile sections are labeled "Interested Artworks", "Purchase History", "Interaction History", "Notes", "Tags", and "Interests". Sections explicitly labeled "Collector Interests", "Exhibition Invitations", and "Acquired Artworks" do not exist.

- [ ] CT-02: Niche-specific workflow status options
  - Action: Click the "Workflow Status" dropdown in a customer profile.
  - Expected: Options include niche-appropriate labels such as "Inquiry", "Private Viewing", "Exhibition Invited", and "Active Collector".
  - Bug Report:
    - Issue: Missing Niche Workflow Options
    - Actual: The dropdown options are "New Lead", "Contacted", "Interested", "Negotiating", "Purchased", "VIP Collector", and "Inactive". None of the expected options ("Inquiry", "Private Viewing", "Exhibition Invited", "Active Collector") are present.

- [ ] CT-03: Performance summary engagement and revenue metrics
  - Action: Navigate to the "Performance Reports" dashboard.
  - Expected: Metric cards display niche-relevant KPIs labeled "Total Artwork Revenue", "Average Acquisition Value", and "Exhibition Attendance Rate".
  - Bug Report:
    - Issue: Mismatched Metric Card Headings
    - Actual: The metric cards in Reports are labeled "Total Revenue (All Time)", "Avg. Purchase Value", "Conversion Rate", and "Active Relationships". None of the expected labels ("Total Artwork Revenue", "Average Acquisition Value", "Exhibition Attendance Rate") are present.
