# Test Checklist

## Functionality

- [ ] FT-01: Employer can create a job listing with all required details
  - Action: As an employer, open the "Post a Job" / "Create Listing" form and enter a title, description, location, salary range (minimum and maximum), required skills, industry, and employment type, then submit.
  - Expected: The listing is created successfully, a success confirmation is displayed, and the new listing appears in the public job listings list.

- [ ] FT-02: Employer can edit an existing job listing
  - Action: From the employer dashboard, open one of the employer's posted jobs and change a field (e.g., the title or salary range), then save.
  - Expected: The changes are saved, the dashboard shows the updated values, and the public listing/detail page shows the updated values.

- [ ] FT-03: Job seeker can browse all available job listings
  - Action: As a job seeker, open the home/browse jobs page without applying any filters or search terms.
  - Expected: All default job listings are displayed in a list, each showing at least its title, company, location, and employment type.

- [ ] FT-04: A job listing detail page shows the full listing details
  - Action: From the listings list, open one listing by clicking its title or card.
  - Expected: A detail page displays the job title, full description, location, salary range, required skills, industry, and employment type.

- [ ] FT-05: Listings can be filtered by industry
  - Action: On the browse jobs page, select a specific industry in the industry filter and apply it.
  - Expected: Only listings belonging to the selected industry are shown, and listings from other industries are not shown.

- [ ] FT-06: Listings can be filtered by location
  - Action: On the browse jobs page, select a specific location in the location filter and apply it.
  - Expected: Only listings with the selected location are shown, and listings in other locations are not shown.

- [ ] FT-07: Listings can be filtered by employment type
  - Action: On the browse jobs page, select an employment type (e.g., Full-time) in the employment type filter and apply it.
  - Expected: Only listings with that employment type are shown, and listings with other employment types are not shown.

- [ ] FT-08: Listings can be searched by keyword
  - Action: Enter a keyword that appears in an existing default listing (e.g., a word from its title, description, or required skills) into the search field and submit the search.
  - Expected: Only listings matching that keyword are shown, and non-matching listings are excluded from the results.

- [ ] FT-09: Job seeker can submit an application with contact information and a message
  - Action: Open a listing's detail page, scroll to the application form, enter name, email, and a short message, then submit the application.
  - Expected: A success confirmation is shown, the submitted application is recorded for that listing, and the application appears in the employer's dashboard for that listing.

- [ ] FT-10: Employer dashboard lists the employer's posted jobs
  - Action: Sign in / navigate as an employer to the dashboard page.
  - Expected: A list of the employer's posted job listings is shown, each showing the job title and enough detail (e.g., location, employment type, posted status) to identify it.

- [ ] FT-11: Employer dashboard shows submitted applications for each listing
  - Action: On the employer dashboard, select one of the posted jobs (e.g., a job that has received an application).
  - Expected: A list of applications for that specific job is shown, each entry identifying the applicant, and the applications of other jobs are not mixed in.

## Constraint

- [ ] CS-01: Job listing cannot be created with missing required details
  - Action: On the job creation form, leave the title (and the other required fields) blank and submit the form.
  - Expected: The submission is rejected, an inline validation error identifies the missing field(s), and no new listing is created or added to the dashboard.

- [ ] CS-02: Salary range cannot have a minimum greater than its maximum
  - Action: On the job creation form, enter a salary minimum that is higher than the salary maximum (e.g., min 120000, max 60000) and submit.
  - Expected: The submission is rejected with a clear error about the invalid salary range, and no listing is created.

- [ ] CS-03: Application cannot be submitted with missing or invalid contact information
  - Action: On a listing's application form, submit with the email field blank; then repeat with a malformed email such as "applicant@" and observe the result each time.
  - Expected: Both submissions are rejected with a validation error on the email field, and no application is recorded in the employer's dashboard.

## Interaction

- [ ] IX-01: Clicking a listing in the results opens its detail page
  - Action: Click the title of a listing card in the browse/search results.
  - Expected: The application navigates to that specific listing's detail page, with the correct listing's details shown (not another listing's).

- [ ] IX-02: Filter and search controls update the result list and can be reset
  - Action: Apply an industry filter, then a location filter, then enter a search term and observe the result list; afterwards click the "Clear"/"Reset filters" control.
  - Expected: The result list updates immediately after each filter/search change to show only matching listings, and clicking "Clear"/"Reset" restores the full unfiltered list of listings.

- [ ] IX-03: Successful job creation gives visible feedback
  - Action: Successfully submit a valid job creation form and observe the page immediately after submission.
  - Expected: A success confirmation message or notification is displayed, and the new listing is either shown in the result or redirected to the listing/dashboard view.

## Content

- [ ] CT-01: Salary range is displayed in a clear min–max format with currency
  - Action: Open a listing detail page and inspect the salary range shown for the default listings.
  - Expected: The salary range is displayed as a minimum–maximum pair with a currency symbol (e.g., "$80,000 – $110,000"), matching the values entered.

- [ ] CT-02: Required skills are displayed exactly as entered by the employer
  - Action: Open a listing detail page and compare the "Required Skills" section with the skills specified in the listing data.
  - Expected: All required skills for the job are listed with no skills missing and no extra or unrelated skills shown.

- [ ] CT-03: Dashboard application entries show the applicant's submitted details
  - Action: Open the applications list for a listing that has at least one submitted application.
  - Expected: Each application entry displays the applicant's name, contact information (email), and short message exactly as it was submitted, with no placeholder or blank values.