# Test Checklist

## Functionality
- [ ] FT-01: Employer creates a new job listing with title, description, location, salary range, and required skills
  - Action: Navigate to "Create Job Listing", fill all fields with valid data, and submit
  - Expected: The new listing appears in the available job listings and the employer's dashboard

- [ ] FT-02: Job seeker browses all available job listings
  - Action: Open the job board homepage without applying any filters or search
  - Expected: All default/published job listings are displayed as a list

- [ ] FT-03: Job seeker filters job listings by industry
  - Action: Select a specific industry from the "Industry" filter on the listings page
  - Expected: Only job listings belonging to the selected industry are displayed

- [ ] FT-04: Job seeker filters job listings by location
  - Action: Select a specific location from the "Location" filter on the listings page
  - Expected: Only job listings matching the selected location are displayed

- [ ] FT-05: Job seeker filters job listings by employment type
  - Action: Select an employment type (e.g., Full-time, Part-time) from the "Employment Type" filter
  - Expected: Only job listings matching the selected employment type are displayed

- [ ] FT-06: Job seeker searches job listings by keyword
  - Action: Type a keyword (e.g., title or skill) into the search box and submit the search
  - Expected: Only job listings containing the keyword in their title, description, or required skills are displayed

- [ ] FT-07: Job seeker views full details of a job listing
  - Action: Click on a default job listing from the listings list
  - Expected: The listing detail page displays title, description, location, salary range, and required skills

- [ ] FT-08: Job seeker submits an application for a job listing
  - Action: Open a default job listing, fill in contact information (name, email, phone) and a short message, then click "Submit Application"
  - Expected: The application is recorded and visible in the employer's dashboard for that listing

- [ ] FT-09: Employer views posted jobs on the dashboard
  - Action: Log in as an employer and navigate to the dashboard
  - Expected: All job listings posted by that employer are listed on the dashboard

- [ ] FT-10: Employer views submitted applications for a specific listing
  - Action: From the dashboard, open a posted job listing's applications list
  - Expected: All applications submitted for that listing are shown with applicant contact info and message

## Constraint
- [ ] CS-01: Cannot create a job listing with missing required fields
  - Action: Open the "Create Job Listing" form, leave one required field (e.g., title, description) empty, and submit
  - Expected: Form submission is blocked with a validation message indicating the missing field(s)

- [ ] CS-02: Cannot submit application form with missing required contact fields
  - Action: Open a default job listing, leave required contact fields (name/email) empty in the application form, and click "Submit Application"
  - Expected: Submission is blocked with a validation message indicating the missing required field(s)

- [ ] CS-03: Cannot submit a job listing with invalid salary range (min greater than max)
  - Action: In "Create Job Listing", set the minimum salary higher than the maximum salary and submit
  - Expected: Submission is blocked with a validation message about the invalid salary range

## Interaction
- [ ] IX-01: Filter selections dynamically update the displayed job listings
  - Action: Change the selected value of any filter (industry/location/employment type) on the listings page
  - Expected: The displayed job listings refresh immediately to reflect the new filter without requiring a manual page reload

- [ ] IX-02: Search keyword input dynamically updates the displayed job listings
  - Action: Type or change a keyword in the search box on the listings page
  - Expected: The displayed job listings refresh to match the new keyword

- [ ] IX-03: A success confirmation is shown after creating a job listing
  - Action: Successfully create a new job listing through the employer form
  - Expected: A success message/toast appears confirming the listing was created

- [ ] IX-04: A success confirmation is shown after submitting an application
  - Action: Successfully submit an application form on a default job listing
  - Expected: A success message/toast appears confirming the application was submitted

## Content
- [ ] CT-01: Job listing detail page displays all required listing attributes
  - Action: Open the detail page of a default job listing
  - Expected: The page shows the job title, full description, location, salary range, and required skills — all relevant to the listing