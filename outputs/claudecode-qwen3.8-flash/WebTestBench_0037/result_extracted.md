# Test Result

## Functionality
- [X] FT-01: Keyword search returns matching pets
  - Action: Entered "Bella" into the search box and submitted.
  - Expected: The results list shows only pets matching the keyword; unrelated pets are hidden.
- [X] FT-02: Species filter narrows results correctly
  - Action: Selected species filter "Dogs" (5 results, all `dog` badges), then switched to "Cats" (4 results: Oliver, Whiskers, Mochi, Shadow, all `cat`).
  - Expected: Only pets of the selected species appear in the results list.
- [ ] FT-03: Age range filter narrows results correctly
  - Action: Applied age filter "Young (1-3 years)", then "Adult (4-7 years)".
  - Expected: Every listed pet's displayed age falls within the selected range.
  - Bug Report:
    - Issue: Incorrect filter boundary handling
    - Actual: "Young (1-3 years)" excluded 3-year-old pets (Luna "3 years" and Shadow "3 years" hidden — only 1-yr/2-yr pets listed). Selecting "Adult (4-7 years)" instead returned Luna and Shadow ("3 years" displayed — outside the 4–7 range), confirming a boundary bug where age 3 is assigned to the wrong bucket.
- [X] FT-04: Size filter narrows results correctly
  - Action: Applied size "Small" (4 results: Biscuit, Mochi, Sunny, Bella — all `small`), then "Large" (2 results: Luna, Duke — all `large`).
  - Expected: Only pets with the selected size attribute are shown.
- [X] FT-05: "Good with kids / good with other pets" filters work
  - Action: Enabled "Good with kids" → 11 results, every card carried the "Kid-friendly" badge and only Whiskers (the one pet without it) was hidden. Enabled "Good with other pets" → 10 results; cross-checked on profiles: Luna (included) shows both compatibility rows with `lucide-check text-success`, while excluded pet Max shows "Good with other pets" with `lucide-x text-destructive`.
  - Expected: Results contain only pets marked as good with kids (resp. other pets).
- [X] FT-06: Sorting by relevance and by time listed
  - Action: Opened the sort control (options: Relevance, Newest First, Oldest First, Name A-Z), selected the time-listed options, then Relevance.
  - Expected: Both options exist; "Time Listed" reorders the list by listing date (newest/oldest), and "Relevance" produces a distinct ordering. ("Newest First"/"Oldest First" are the time-listed options — exact reverse of each other, with the "about 2 years ago" pets Whiskers/Shadow correctly last/first; "Relevance" gave the distinct default order Luna→Charlie.)
- [X] FT-07: Pet detail profile opens from the list
  - Action: Clicked the Luna card → navigated to `/pets/pet-1`.
  - Expected: A profile page opens showing photo(s) (2-photo gallery), a description ("About Luna…"), and the pet's name (h1 "Luna"), plus age/size/gender/compatibility/health/shelter details.
- [X] FT-08: Favorites can be saved and viewed in a favorites list
  - Action: Clicked the heart on Luna's profile → Favorites page showed "1 pet saved to your favorites" with Luna listed; clicking the heart removed her and the page showed the "No favorites yet" empty state.
  - Expected: The pet appears in the favorites list; removing it takes it out of the list.
- [X] FT-09: Adoption inquiry submits from the pet's page
  - Action: Filled name ("Alice Tester"), email ("alice@example.com"), message and clicked "Send Inquiry".
  - Expected: The form submits successfully and the inquiry is recorded/confirmed (no error). Button showed "Sending…" then the form was replaced by "Inquiry Submitted! Happy Tails Rescue has received your inquiry about Luna."

## Constraint
- [X] CS-01: Inquiry form blocks submission with empty required fields
  - Action: Cleared name, email, message and clicked "Send Inquiry".
  - Expected: Submission is blocked and validation errors identify the missing required fields. (Form `checkValidity()` = false; native per-field validation "Please fill out this field" on name, email, and message respectively; no confirmation appeared.)
- [X] CS-02: Inquiry form rejects invalid email format
  - Action: Entered "not-an-email" with other fields filled, then submitted.
  - Expected: Submission is blocked with an email-format validation error. (validationMessage: "Please include an '@' in the email address. 'not-an-email' is missing an '@."; no success state.)
- [X] CS-03: No-match filter combination shows an empty state
  - Action: Applied conflicting filters Dogs + Small + Senior.
  - Expected: A clear "no pets found" message is shown; the page does not error or show a broken/blank list. ("0 adorable pets available" + "No pets found / Try adjusting your search or filters" + working "Clear all filters" button; no errors.)
- [X] CS-04: Pet cannot be favorited more than once
  - Action: Clicked the heart on Luna's profile multiple times (add → off → add) and toggled from the Favorites-page card.
  - Expected: The pet appears exactly once in favorites; no duplicate entries. (`pawfect-favorites` localStorage never held more than one `"pet-1"` entry; Favorites page rendered exactly 1 card.)

## Interaction
- [X] IX-01: Results list updates immediately when filters/search change
  - Action: Toggled species/size/age/compatibility filters, edited search text, and changed sort.
  - Expected: The matching-pets list refreshes to reflect the new criteria without a manual page reload. (URL stayed `/pets`; the DOM result set and count updated after every change; favorite heart toggles re-rendered the favorites list in place.)
- [X] IX-02: Success feedback after inquiry submission
  - Action: Submitted a valid adoption inquiry on Luna's page.
  - Expected: A visible success confirmation appears after submission. (Visible confirmation message: "Inquiry Submitted! Happy Tails Rescue has received your inquiry about Luna. They will contact you within 1-2 business days.")
- [X] IX-03: Favorite button reflects saved state visually
  - Action: Clicked the heart (SVG class changed `text-muted-foreground` → `fill-accent text-accent`), reloaded the profile (active state persisted, header badge "Favorites 1"), and clicked again to unfavorite.
  - Expected: The control shows a distinct active/inactive state and clicking it again removes the pet from favorites.
- [X] IX-04: Multiple photos browsable on the pet profile
  - Action: On Luna's profile (2 photos), clicked "Thumbnail 2" and the gallery chevron.
  - Expected: Each selection changes the main displayed photo. (Main image changed from `Luna - Photo 1` (photo-1552053831…) to `Luna - Photo 2` (photo-1587300003388…).)

## Content
- [ ] CT-01: Pet cards display complete key information
  - Action: Inspected cards in the default results list (Luna card DOM: photo, name, species badge, size, age, "Portland, OR", listing time).
  - Expected: Each card shows the pet's photo, name, species, age, size, and shelter name.
  - Bug Report:
    - Issue: Missing shelter attribution on cards
    - Actual: Cards show the city/location string only ("Portland, OR", "Seattle, WA") — no shelter name (e.g., "Happy Tails Rescue") appears on any card (`innerText`, `title`, `aria-label`, and HTML checked). The shelter name exists only on the profile page.
- [X] CT-02: Profile photos and description are relevant to the pet
  - Action: Opened Luna (dog/Golden Retriever Mix), Oliver (cat/Orange Tabby), and Biscuit (rabbit/Holland Lop) profiles.
  - Expected: Photos depict an animal of that pet's species, and the description matches the pet shown in the list. (Per-photo distinct Unsplash image sources species-consistent with each pet, alts labeled "Luna - Photo 1" etc.; descriptions match list data exactly: Luna "Golden Retriever Mix…3 years", Oliver "charming orange tabby", Biscuit "adorable Holland Lop"; no placeholders/Lorem ipsum.)
- [X] CT-03: Shelter attribution spans multiple shelters
  - Action: Browsed listings and opened profiles across cities.
  - Expected: Pets are drawn from multiple distinct shelters, and each profile names a specific shelter. (Profiles show named shelters with contact details: Luna and Max → "Happy Tails Rescue" (Portland, phone + adopt@happytails.org); Oliver and Biscuit → "Second Chance Animal Haven" — at least two distinct shelters, each profile explicitly names one.)
