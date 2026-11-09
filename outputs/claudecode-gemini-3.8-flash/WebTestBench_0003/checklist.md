# Test Checklist

## Functionality
- [ ] FT-01: Create a job listing with complete details
  - Action: Navigate to the job creation form, enter valid values into "Job Title", "Description", "Location", "Salary Range", and "Required Skills", then click "Post Job".
  - Expected: The job listing is created and appears in the public job board and employer dashboard.
- [ ] FT-02: Search job listings by keyword
  - Action: Type an existing job title or skill keyword into the search bar and click "Search".
  - Expected: The listings display updates to show only jobs matching the keyword in their title, description, or skills.
- [ ] FT-03: Filter job listings by industry, location, and employment type
  - Action: Select specific options in the "Industry", "Location", and "Employment Type" filter controls.
  - Expected: The job list updates to display only jobs matching all selected filter criteria simultaneously.
- [ ] FT-04: View full job listing details
  - Action: Click on a job card from the listings directory.
  - Expected: Navigates to the job detail page displaying full job information and the application form.
- [ ] FT-05: Submit an application for an open position
  - Action: On the job detail page, enter contact information and a short message into the application form, then click "Submit Application".
  - Expected: The application is successfully submitted and recorded for the employer to review.
- [ ] FT-06: View posted jobs on employer dashboard
  - Action: Navigate to the Employer Dashboard.
  - Expected: A list of all job listings created by the employer is displayed.
- [ ] FT-07: View submitted applications for a specific listing
  - Action: In the Employer Dashboard, click "View Applications" on a job listing with existing applicants.
  - Expected: A list of all submitted applications for that specific job listing is displayed.

## Constraint
- [ ] CS-01: Prevent job listing creation with missing required fields
  - Action: Leave mandatory fields (such as "Job Title" and "Description") empty on the job creation form and click "Post Job".
  - Expected: The form is not submitted, and validation error messages appear adjacent to the empty required fields.
- [ ] CS-02: Prevent application submission with empty contact information
  - Action: Leave the "Contact Information" input empty, enter text in the message field, and click "Submit Application".
  - Expected: The application is not submitted, and a validation message prompts the user to provide contact information.
- [ ] CS-03: Empty state when search or filter criteria return no results
  - Action: Enter a non-existent keyword or combination of filter options that matches no jobs and submit.
  - Expected: The listings container displays a clear "No jobs found" message without crashing or displaying broken cards.

## Interaction
- [ ] IX-01: Confirmation notification on successful job posting
  - Action: Fill out the job creation form with valid details and click "Post Job".
  - Expected: A success toast or banner notification appears confirming the listing has been posted.
- [ ] IX-02: Visual feedback upon job application submission
  - Action: Complete the application form on a job detail page and click "Submit Application".
  - Expected: A success message appears on screen and the form fields clear or lock to prevent duplicate submission.
- [ ] IX-03: Clear or reset active filters
  - Action: Apply industry, location, and employment type filters, then click the "Clear Filters" button.
  - Expected: All filter dropdowns/inputs reset to their default unselected states and the list refreshes to show all listings.

## Content
- [ ] CT-01: Verify all required job details display on the listing page
  - Action: Open a job detail page from the directory.
  - Expected: The page explicitly displays the job's title, full description, location, salary range, and required skills.
- [ ] CT-02: Verify employer dashboard listing overview content
  - Action: Inspect each job card/row on the Employer Dashboard.
  - Expected: Each entry displays the job title, location, date posted, and the total count of applications received.
- [ ] CT-03: Verify applicant contact information and message display
  - Action: Open the applications list for a job on the Employer Dashboard.
  - Expected: Each applicant entry clearly displays the applicant's submitted contact information and complete short message.