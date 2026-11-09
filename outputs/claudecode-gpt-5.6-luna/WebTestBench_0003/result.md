# Test Result

## Functionality

- [X] **FT-01: Browse all available job listings**
  - **Action:** Open the job board and review the available listings.
  - **Expected:** Every available job listing is displayed with a selectable listing entry.

- [X] **FT-02: Create a job listing as an employer**
  - **Action:** Open **Create Job**, enter a title, description, location, salary range, industry, employment type, and required skills, then submit.
  - **Expected:** The job listing is created and appears in the available listings.

- [ ] **FT-03: Edit an existing job listing**
  - **Action:** From the employer dashboard, open a posted job, change its description or salary range, and save.
  - **Expected:** The updated values are saved and shown on the listing detail page.
  - **Bug Report:**
    - **Issue:** Missing edit functionality
    - **Actual:** The employer dashboard does not provide an edit action for posted jobs. The secondary action opens a “Delete this job?” dialog instead, so the job description or salary cannot be changed and saved.

- [X] **FT-04: Filter listings by industry**
  - **Action:** Select an industry from the industry filter.
  - **Expected:** Only listings belonging to the selected industry are displayed.

- [X] **FT-05: Filter listings by location**
  - **Action:** Select a location from the location filter.
  - **Expected:** Only listings matching the selected location are displayed.

- [X] **FT-06: Filter listings by employment type**
  - **Action:** Select an employment type from the employment type filter.
  - **Expected:** Only listings matching the selected employment type are displayed.

- [X] **FT-07: Search listings by keyword**
  - **Action:** Enter a keyword from an existing listing’s title, description, or required skills into the job search field and submit the search.
  - **Expected:** Listings containing the keyword are displayed.

- [X] **FT-08: View complete job details**
  - **Action:** Select a job listing from the results.
  - **Expected:** The detail page displays the job title, description, location, salary range, industry, employment type, and required skills.

- [X] **FT-09: Submit a job application**
  - **Action:** Open a listing, complete the application form with valid contact information and a short message, then submit.
  - **Expected:** The application is submitted for the selected job listing.

- [X] **FT-10: View employer job dashboard**
  - **Action:** Open the employer dashboard.
  - **Expected:** The dashboard displays the employer’s posted job listings.

- [X] **FT-11: View applications for a posted listing**
  - **Action:** In the employer dashboard, open the applications for a specific posted job.
  - **Expected:** A list of applications submitted for that job is displayed.

## Constraint

- [X] **CS-01: Prevent incomplete job listings**
  - **Action:** Open **Create Job**, leave one required job detail empty, and attempt to submit.
  - **Expected:** The listing is not created and the missing field is identified with a validation message.

- [ ] **CS-02: Validate the salary range**
  - **Action:** Enter a salary minimum greater than the salary maximum and attempt to submit the job listing.
  - **Expected:** Submission is blocked and a message indicates that the salary range is invalid.
  - **Bug Report:**
    - **Issue:** Invalid salary range accepted
    - **Actual:** A job with a minimum salary of $200,000 and maximum salary of $100,000 was submitted successfully, displayed a “Job posted successfully!” confirmation, and appeared in the available listings as “$200k - $100k.”

- [X] **CS-03: Prevent incomplete applications**
  - **Action:** Leave the contact information or application message empty and attempt to submit the application.
  - **Expected:** The application is not submitted and the missing required field is identified.

- [X] **CS-04: Keep filters and search results accurate**
  - **Action:** Apply multiple filters and enter a keyword that does not match the filtered listings.
  - **Expected:** No non-matching listings are displayed, and the page shows a clear no-results state.

## Interaction

- [X] **IX-01: Update listings after filter changes**
  - **Action:** Select a filter, then change or clear the selected filter.
  - **Expected:** The results update immediately to match the current filter selection, without retaining stale results.

- [X] **IX-02: Confirm successful submissions**
  - **Action:** Successfully submit a valid job listing and successfully submit a valid application.
  - **Expected:** Each completed submission provides a visible success confirmation and returns the user to an appropriate updated state.

- [X] **IX-03: Navigate from a listing result to its details**
  - **Action:** Click a listing title or listing card from the browse or search results.
  - **Expected:** The selected listing’s detail page opens, showing details for that same listing.

## Content

- [X] **CT-01: Verify listing information is relevant and consistent**
  - **Action:** Compare a listing card with its detail page.
  - **Expected:** The title, location, salary range, industry, and employment type are relevant to and consistent with the selected job.

- [X] **CT-02: Verify application records contain applicant information**
  - **Action:** Open an existing application from the employer dashboard.
  - **Expected:** The record shows the applicant’s submitted contact information and short message and is associated with the correct job listing.