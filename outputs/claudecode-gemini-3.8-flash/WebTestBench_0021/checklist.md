# Test Checklist

## Functionality
- [ ] FT-01: Create a new customer record with niche attributes
  - Action: Click "+ New Customer", fill in "Full Name", "Email", "Collector Interests", and click "Save Customer".
  - Expected: The new customer record appears in the customer table with all submitted attributes.
- [ ] FT-02: Update existing customer details
  - Action: Open a default customer record, edit the "Notes" and "Collector Interests" fields, and click "Save Changes".
  - Expected: Customer record updates and displays the modified notes and interests.
- [ ] FT-03: Attach a related business item to a customer
  - Action: In an existing customer record, click "Attach Artwork", select an artwork from the item catalog, and click "Confirm".
  - Expected: The selected artwork appears in the customer's "Attached Artworks" list.
- [ ] FT-04: Update customer workflow status
  - Action: Open an existing customer record, select "Exhibition Invited" from the "Workflow Status" dropdown, and click "Update Status".
  - Expected: The customer's status badge updates to "Exhibition Invited".
- [ ] FT-05: Filter customer directory by niche attribute
  - Action: Click the "Filter" dropdown, select "Collector Interest: Modern Art", and click "Apply Filter".
  - Expected: Customer table displays only records tagged with the "Modern Art" interest.
- [ ] FT-06: Configure summary performance reports
  - Action: Navigate to "Performance Reports", select "Artwork Revenue" from the report type selector, and choose date range "Last 30 Days".
  - Expected: Report dashboard displays revenue charts and totals corresponding to the selected 30-day timeframe.

## Constraint
- [ ] CS-01: Prevent customer creation with empty required fields
  - Action: Click "+ New Customer", leave "Full Name" and "Email" blank, and click "Save Customer".
  - Expected: Form submission is blocked, and validation error messages appear under "Full Name" and "Email".
- [ ] CS-02: Prevent saving invalid email format
  - Action: In an existing customer edit form, enter "invalid-email-format" into the "Email" field and click "Save Changes".
  - Expected: System displays "Please enter a valid email address" and prevents saving.
- [ ] CS-03: Prevent attaching duplicate items to the same customer
  - Action: Open a customer with an existing attached artwork and attempt to select and attach that same artwork again.
  - Expected: The artwork is disabled in the selection modal or an alert displays "Item already attached to customer".
- [ ] CS-04: Display empty state for non-matching search queries
  - Action: Type "UNKNOWN_QUERY_999" into the customer search bar and press Enter.
  - Expected: Customer table displays zero records and shows an empty state message "No customers found".

## Interaction
- [ ] IX-01: Open customer detail drawer on row selection
  - Action: Click on any customer row in the customer directory table.
  - Expected: Customer detail panel slides open from the right side of the screen displaying the full customer profile.
- [ ] IX-02: Display success notification upon profile update
  - Action: Modify an existing customer's contact number and click "Save Changes".
  - Expected: A confirmation toast notification reading "Customer record updated successfully" appears in the top-right corner.
- [ ] IX-03: Dynamic report refresh on metric view switch
  - Action: In the "Performance Reports" view, switch the aggregation toggle from "Monthly" to "Quarterly".
  - Expected: KPI summary cards and performance charts refresh dynamically without triggering a full page reload.

## Content
- [ ] CT-01: Niche-specific customer profile sections
  - Action: Open any default customer profile view.
  - Expected: Profile displays sections labeled "Collector Interests", "Exhibition Invitations", and "Acquired Artworks".
- [ ] CT-02: Niche-specific workflow status options
  - Action: Click the "Workflow Status" dropdown in a customer profile.
  - Expected: Options include niche-appropriate labels such as "Inquiry", "Private Viewing", "Exhibition Invited", and "Active Collector".
- [ ] CT-03: Performance summary engagement and revenue metrics
  - Action: Navigate to the "Performance Reports" dashboard.
  - Expected: Metric cards display niche-relevant KPIs labeled "Total Artwork Revenue", "Average Acquisition Value", and "Exhibition Attendance Rate".