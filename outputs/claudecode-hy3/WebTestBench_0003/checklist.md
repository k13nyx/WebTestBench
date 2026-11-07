# Test Checklist

## Functionality
- [ ] FT-01: Employer can create a job listing with all details
  - Action: Open "Post a Job" form, fill Title, Description, Location, Salary Range, Required Skills, and submit.
  - Expected: New listing appears in the job listings and the employer's dashboard.

- [ ] FT-02: Job seeker can browse all available listings
  - Action: Navigate to the job board home/listings page.
  - Expected: A list of all available job listings is displayed.

- [ ] FT-03: Job seeker can filter listings by industry
  - Action: Select an industry from the "Industry" filter and apply.
  - Expected: Only listings matching the selected industry are shown.

- [ ] FT-04: Job seeker can filter listings by location
  - Action: Select/enter a location in the "Location" filter and apply.
  - Expected: Only listings matching the selected location are shown.

- [ ] FT-05: Job seeker can filter listings by employment type
  - Action: Select an employment type (e.g., Full-time) from the filter and apply.
  - Expected: Only listings matching the selected employment type are shown.

- [ ] FT-06: Job seeker can search listings by keyword
  - Action: Enter a keyword into the search box and submit.
  - Expected: Only listings containing the keyword (title/description/skills) are shown.

- [ ] FT-07: Job listing detail page displays full details
  - Action: Click a listing from the browse list to open its detail page.
  - Expected: Full details (title, description, location, salary range, required skills, employment type, industry) are displayed.

- [ ] FT-08: Job seeker can submit an application form
  - Action: On a job listing page, fill the application form (contact info + short message) and submit.
  - Expected: Application is submitted and recorded under that listing's applications.

- [ ] FT-09: Employer dashboard displays posted jobs
  - Action: Navigate to the employer dashboard.
  - Expected: A list of all jobs posted by the employer is displayed.

- [ ] FT-10: Employer dashboard displays submitted applications per listing
  - Action: Open a posted job from the dashboard.
  - Expected: The list of submitted applications for that listing is displayed.

- [ ] FT-11: Employer can manage (edit/delete) a job listing
  - Action: On the dashboard, select edit or delete for a posted listing.
  - Expected: The listing is updated or removed from listings and dashboard accordingly.

## Constraint
- [ ] CS-01: Cannot create a job listing with empty required fields
  - Action: Submit the "Post a Job" form with required fields (Title, Description, Location) left empty.
  - Expected: Submission is blocked and a validation error identifies the missing required fields.

- [ ] CS-02: Cannot submit an application with empty required contact info
  - Action: Submit the application form leaving required contact info blank.
  - Expected: Submission is blocked and a validation error identifies the missing required field.

- [ ] CS-03: Salary range must be logically valid
  - Action: Enter a salary range where minimum is greater than maximum and submit.
  - Expected: Submission is blocked with a message that the salary range is invalid.

## Interaction
- [ ] IX-01: Success confirmation after creating a listing
  - Action: Submit a valid "Post a Job" form.
  - Expected: A success toast/message confirms the listing was created.

- [ ] IX-02: Success confirmation after submitting an application
  - Action: Submit a valid application form.
  - Expected: A success toast/message confirms the application was submitted.

- [ ] IX-03: Filters and search update results dynamically
  - Action: Apply a filter or search and change it without a full page reload.
  - Expected: The listings list updates immediately to reflect the new criteria.

## Content
- [ ] CT-01: Job listing detail content is complete and relevant
  - Action: Open a job listing detail page.
  - Expected: All displayed text/data (title, description, location, salary, skills) matches the listing's entered details and is relevant to the posting.

- [ ] CT-02: Application form contains only relevant fields
  - Action: Open the application form on a listing page.
  - Expected: Form contains only contact information and a short message field (no unrelated fields).

- [ ] CT-03: Default job listings are present for browsing
  - Action: Open the job board without creating any data.
  - Expected: Pre-existing default job listings are visible to browse and filter.