# Test Result

## Functionality

- [X] FT-01: Employer can create a job listing with all required details
  - Action: Open the employer "Create Job" form, fill in Title, Description, Location, Salary Range (min and max), Industry, Employment Type, and Required Skills, then submit.
  - Expected: A new job listing is saved and appears in the browse/listings page showing the entered title and location.

- [ ] FT-02: Employer can edit an existing job listing
  - Action: From the employer dashboard, open an existing default job listing's edit view, change the Title and Salary Range, and save.
  - Expected: The change is saved and the updated title/salary is shown on the listing's detail page and in the browse list.
  - Bug Report:
    - Issue: Missing Feature / No Edit Route
    - Actual: No edit view exists anywhere in the application. The employer dashboard listing cards expose only two controls — an applications-count button and a delete (trash) button; there is no edit button, link, or menu. The job detail page (`/jobs/job-1`) also contains no edit control. Navigating directly to a plausible edit route `/employer/edit-job/job-1` returns the 404 page ("404 — Oops! Page not found"). The application's router (`/src/App.tsx`) defines only four routes: `/`, `/jobs/:id`, `/employer/dashboard`, `/employer/post-job`, and a catch-all `*` → NotFound; there is no EditJob page or edit route registered. Title and Salary Range therefore cannot be modified after posting.

- [X] FT-03: Employer can delete a job listing
  - Action: From the employer dashboard, select the delete action on a job listing you created and confirm.
  - Expected: The listing is removed from the dashboard list and no longer appears in the browse page.

- [X] FT-04: Job seeker can browse all available job listings
  - Action: Open the main job listings/browse page with default data, with no filters or search applied.
  - Expected: Multiple default job listings are displayed (more than one), each as a distinct entry/card.

- [X] FT-05: Job listing detail page displays the full listing details
  - Action: Open any default job listing's detail page.
  - Expected: The page shows that listing's full Title, Description, Location, Salary Range, Employment Type, Industry, and Required Skills.

- [X] FT-06: Job seeker can submit an application with contact info and a message
  - Action: On a job listing detail page, fill in the application form with full name, email, phone/contact, and a short message, then submit.
  - Expected: The application is submitted successfully; no error is shown.

- [X] FT-07: Job seeker can search listings by keyword
  - Action: Enter a keyword that exists in a default listing's title or description (e.g., a word from a visible listing title) into the search field and submit.
  - Expected: Only listings whose title or description contains that keyword are displayed.

- [X] FT-08: Job seeker can filter listings by industry, location, and employment type
  - Action: On the listings page, select an industry from the industry filter, then select a location, then select an employment type (values that exist in the default listings).
  - Expected: The displayed listings are reduced to only those matching all selected filter values.

- [X] FT-09: Employer dashboard shows posted jobs and their submitted applications
  - Action: Open the employer dashboard, then open the applications view for a default listing that has at least one submitted application (submit FT-06 first if needed).
  - Expected: Each posted job is listed, and opening a listing's applications shows the applicant entries with their name, contact info, and message.

## Constraint

- [X] CS-01: Job creation rejects empty required fields
  - Action: Open the "Create Job" form and submit it with Title and Description left empty.
  - Expected: Submission is blocked, a validation message is shown for the empty required fields, and no new listing is created.

- [X] CS-02: Application form rejects missing contact info and invalid email
  - Action: On a listing detail page, submit the application form with the email field left empty, then repeat with a malformed email (e.g., "notanemail").
  - Expected: Both attempts are blocked with a validation error; no application is recorded in either case.

- [ ] CS-03: Salary range cannot have a minimum greater than the maximum
  - Action: In the job creation form, enter a salary minimum greater than the maximum (e.g., min 90000, max 50000) and submit.
  - Expected: Submission is blocked with a validation error indicating an invalid salary range; no listing is created.
  - Bug Report:
    - Issue: Missing Salary Range Validation
    - Actual: Submitting the "Post Job" form with Minimum Salary = 90000 and Maximum Salary = 50000 was accepted without any validation error. The form navigated to the employer dashboard and displayed the success toast "Job posted successfully! Your job listing is now live and visible to job seekers." The new listing "QA Automation Test Engineer" was created and rendered with the inverted salary string "· $90k - $50k · Posted Yesterday". The dashboard "Active Jobs" count incremented and the invalid listing was added to the job list.

- [X] CS-04: Search or filter with no matches shows an explicit empty state
  - Action: Enter a nonsense keyword (e.g., "zzzqqq123") in the search field and submit; then apply a filter combination that matches no default listing.
  - Expected: In both cases the page shows an explicit "no results" / empty-state message; it does not render a blank area or an error.

- [X] CS-05: A deleted job listing is no longer reachable or searchable
  - Action: Delete a listing (per FT-03), then search for its exact title keyword in the search field.
  - Expected: The deleted listing does not appear in search results, and its detail page is no longer viewable.

## Interaction

- [X] IX-01: Clicking a job listing opens its detail page
  - Action: On the browse page, click the title or card of any default job listing.
  - Expected: The page navigates to that specific listing's detail page showing its full details.

- [X] IX-02: Submitting an application shows a confirmation and resets the form
  - Action: Submit a valid application on a listing detail page (per FT-06) and observe the page immediately after.
  - Expected: A success confirmation message is displayed, and the application form fields are cleared.

- [X] IX-03: Clearing filters and search restores the full listings list
  - Action: Apply a filter and a keyword search, then clear the search field and reset every filter to its default/"All" value.
  - Expected: The full set of default job listings is displayed again without requiring a manual page reload.

## Content

- [X] CT-01: Listing entries display relevant job summary information
  - Action: Inspect several default job listings on the browse page.
  - Expected: Each listing shows a real job title, location, industry, and employment type; no placeholder, lorem ipsum, or non-job-related text is present.

- [X] CT-02: Detail page shows the salary range and required skills as entered
  - Action: Compare a default listing's detail page against the values shown for it in the browse list and dashboard.
  - Expected: Salary range and required skills are displayed and consistent with the listing's stored data; no field is missing or showing placeholder values.

- [X] CT-03: Dashboard application entries identify the applicant and the job
  - Action: Open the applications list for a listing with submissions in the employer dashboard.
  - Expected: Each application entry shows the applicant's name, contact information, submitted message, and is clearly associated with the correct job listing title.
