# Test Result

## Functionality
- [X] FT-01: Employer can create a new job listing with all required details
  - Action: Open the job creation form as an employer, fill in title, description, location, salary range, and required skills, then submit.
  - Expected: The new listing is saved and appears in the employer's posted jobs list.
- [ ] FT-02: Employer can edit an existing job listing
  - Action: Open a posted job from the employer dashboard, change its title and salary range, and save.
  - Expected: The updated values are saved and reflected on the public listing page.
  - Bug Report:
    - Issue: Missing Feature (No Edit Control / No Edit Route)
    - Actual: Dashboard job cards expose only two buttons — an applications-count button and a delete (trash) button; there is no edit control. Source inspection confirms the app defines only 4 routes ("/", "/jobs/:id", "/employer/dashboard", "/employer/post-job") and PostJob.tsx, Dashboard.tsx, and JobContext.tsx contain no edit/update logic or edit mode, so a posted job's title or salary cannot be changed anywhere in the UI.
- [X] FT-03: Employer can delete/remove a job listing
  - Action: From the employer dashboard, remove an existing posted job.
  - Expected: The listing is removed from the dashboard and no longer appears in public listings.
- [X] FT-04: Job seekers can browse all available listings
  - Action: Open the job board page as a visitor.
  - Expected: A list of all available jobs is displayed, each showing at least title, location, and salary information.
- [X] FT-05: Search by keyword returns matching listings
  - Action: Enter a known keyword from an existing job title into the search box and submit.
  - Expected: Only listings whose content matches the keyword are shown.
- [X] FT-06: Filter listings by industry
  - Action: Select a specific industry in the industry filter.
  - Expected: Only jobs belonging to that industry are displayed.
- [X] FT-07: Filter listings by location
  - Action: Select a specific location in the location filter.
  - Expected: Only jobs at that location are displayed.
- [X] FT-08: Filter listings by employment type
  - Action: Select a specific employment type (e.g., Full-time) in the filter.
  - Expected: Only jobs of that employment type are displayed.
- [X] FT-09: Job detail page displays full listing details
  - Action: Click on a job listing to open its detail page.
  - Expected: The page shows the complete title, description, location, salary range, and required skills.
- [X] FT-10: Job seeker can submit an application
  - Action: On a job detail page, fill the application form with contact information and a short message, then submit.
  - Expected: The application is submitted successfully and the form confirms submission.
- [X] FT-11: Employer dashboard lists all posted jobs
  - Action: Open the employer dashboard.
  - Expected: All jobs posted by the employer are listed with their key details.
- [X] FT-12: Employer can view applications for a specific listing
  - Action: From the employer dashboard, open the applications view for one posted job that has received applications.
  - Expected: A list of submitted applications for that listing is shown, including each applicant's contact information and message.

## Constraint
- [ ] CS-01: Job listing cannot be created with empty required fields
  - Action: Submit the job creation form with title, description, location, salary range, or skills left blank.
  - Expected: The form is rejected with a validation error identifying the missing field; no listing is created.
  - Bug Report:
    - Issue: Missing Required-Field Validation (Listing Created with Empty Required Field)
    - Actual: With title/description/salaries filled but required "Location *" left blank, clicking "Post Job" submitted successfully — redirected to the dashboard with toast "Job posted successfully!" and the listing was created with no validation error identifying the missing location. When all fields were empty, only native text/number inputs were flagged ("Please fill out this field."); the Industry, Employment Type, and Location comboboxes produced no error message.
- [ ] CS-02: Salary range rejects invalid values
  - Action: Enter a salary maximum lower than the minimum (or non-numeric salary values) and submit.
  - Expected: Submission is blocked with a clear validation error; the listing/application is not saved.
  - Bug Report:
    - Issue: Missing Salary Range Validation
    - Actual: Minimum Salary 200000 with Maximum Salary 100000 submitted successfully — toast "Job posted successfully!" appeared, the form redirected to the dashboard, and the listing "Invalid Salary Test Role" was saved with no validation error about the inverted salary range.
- [X] CS-03: Application form cannot be submitted with empty required fields
  - Action: Submit the application form with contact information or message left blank.
  - Expected: Submission is blocked with a validation error; no application is recorded.
- [X] CS-04: Filters and search combined do not show non-matching results
  - Action: Apply an industry filter, a location filter, and a keyword search whose criteria cannot all match any single listing.
  - Expected: The result list is empty (with an appropriate no-results indication), and no non-matching job is shown.

## Interaction
- [X] IX-01: Results update immediately when a filter is changed
  - Action: Change any filter (industry/location/employment type) or submit a search on the browse page.
  - Expected: The listing results update without a full page reload, and the active filter/search state is visibly indicated.
- [X] IX-02: Success confirmation appears after creating a job and after submitting an application
  - Action: Complete a valid job creation and, separately, a valid application submission.
  - Expected: Each action shows a clear success confirmation message, and the new data appears in its destination (dashboard / applications list).

## Content
- [X] CT-01: Job detail page content matches the data entered by the employer
  - Action: Compare the detail page of a known listing against the values entered when it was created/edited.
  - Expected: Title, description, location, salary range, and required skills are displayed exactly as entered, with no missing or unrelated information.
- [X] CT-02: Application details shown to the employer match the submitted form
  - Action: Open an application in the employer dashboard after submitting it with known contact info and message.
  - Expected: The displayed contact information and message exactly match what the applicant entered.
