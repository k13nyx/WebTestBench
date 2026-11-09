# Test Result

## Functionality
- [X] FT-01: User can create a new resume from a pre-designed template
  - Action: Clicked "New Resume"; a new blank resume opened in the editor, and the offered template styles (Modern/Classic/Minimal) were selectable from the Template tab; chose "Minimal" and confirmed.
  - Expected: A new blank resume based on the chosen template opens in the editor. (Observed: blank "Untitled Resume" opened with all sections empty, preview re-rendered in the chosen template style.)

- [X] FT-02: User can enter and save contact details
  - Action: Filled Full Name "Alex Morgan QA", Email "alex.qa@email.com", Phone "(555) 000-1122", Location "Denver, CO" on the default Software Engineer resume; the app has no explicit Save button — edits auto-persist (card showed new template/updated date, values retained after navigating away and reopening).
  - Expected: All contact values are retained and displayed in the resume document after saving. (Verified: values persisted in-session and shown in the live resume document. Note: reload persistence is separately failed under FT-10/CS-03; missing "Saved" confirmation is failed under IX-02.)

- [X] FT-03: User can add entries for work experience, education, and skills
  - Action: Used "Add Experience" → QA Engineer / QA Test Co / 2018-01–2019-05 / description; "Add Education" → Master of Testing in Quality Assurance / State University QA / 2019-09–2020-12; added skills "Test Planning" and "Selenium" via the Add New Skill control.
  - Expected: Each entry accepted and appears under its section. (Preview showed "QA Engineer… QA Test Co", "State University QA", and Skills line "… AWS • Test Planning • Selenium".)

- [X] FT-04: User can edit an existing entry
  - Action: Opened Position 1, changed Job Title "Senior Software Engineer" → "Staff Software Engineer QA" (auto-saved).
  - Expected: Edited text shown, old value gone. (Verified: `Staff Software Engineer QA` present in preview; `Senior Software Engineer` absent from DOM.)

- [X] FT-05: User can switch the resume to a different template style
  - Action: From the Template picker on the Software Engineer resume (containing data), selected "Classic".
  - Expected: Resume re-renders in new template with all data intact. (Verified: check/selection icon moved from Modern to Classic; preview re-rendered in Classic layout with name, summary, 2 experiences, education, and skills intact; library card tag updated "modern"→"classic".)

- [X] FT-06: User can customize layout options (section order and headings)
  - Action: Used the ↑ reorder control to move Skills above Education; renamed heading textbox "Work Experience" → "Professional Experience".
  - Expected: New order shown and renamed heading appears. (Verified: preview `h2`s = "Professional Summary, Professional Experience, Skills, Education".)

- [X] FT-07: User can preview the resume
  - Action: Toggled the preview control ("Hide Preview" → "Show Preview") while editing.
  - Expected: Formatted full resume view with all sections and entered data. (Verified: full document rendered — contact banner, summary, 3 experience entries, skills list, 2 education entries, custom heading/order/template all reflected.)

- [X] FT-08: User can rename a saved resume version
  - Action: From the saved list, opened the card menu (⋯) on the default "Product Designer Resume" → "Rename" → dialog with title field → set "Marketing Resume" → Save.
  - Expected: List and editor header show "Marketing Resume"; other resumes unaffected. (Verified: card list `h3`s included "Marketing Resume"; opening it showed editor `h1` "Marketing Resume"; other titles unchanged.)

- [X] FT-09: User can duplicate a saved resume version
  - Action: Card menu on "Marketing Resume" → "Duplicate".
  - Expected: New copy titled e.g. "Copy of …" with identical content. (Verified: "Marketing Resume (Copy)" appeared in list; opening it showed identical content — "Jordan Rivera", "Design Studio", "Rhode Island" — before any edit.)

- [X] FT-10 → see bug report below; marked FAIL
- [ ] FT-10: User can save multiple variations for different applications
  - Action: Created "Data Analyst Resume" (distinct contact data) plus duplicate "Marketing Resume (Copy)" with edited name field; both saved (auto); after a further edit, reloaded the page.
  - Expected: Both variations appear independently in the saved list; the latest edit persists on reload.
  - Bug Report:
    - Issue: No persistence — application state lost on reload (no localStorage/sessionStorage or backend writes; both storage areas were empty throughout).
    - Actual: After reload the library reset to the 3 original seed resumes ("Product Designer Resume – Updated Feb 25, 2024", "Marketing Manager Resume", "Software Engineer Resume"); the created variations, duplicate, rename, and all edits were gone ("Staff Software Engineer QA": false, "Alex Morgan QA": false).

- [X] FT-11: User can search saved resumes by title
  - Action: Typed "Marketing" into the search box; then cleared it.
  - Expected: Only matching titles listed; clearing restores full list. (Verified: search returned exactly ["Marketing Resume (Copy)", "Marketing Resume", "Marketing Manager Resume"]; clearing restored all 5 cards.)

- [X] FT-12: User can filter/sort saved resumes by date created
  - Action: Applied the sort control (options: "Newest First", "Oldest First", "Title A-Z", "Title Z-A") → selected "Oldest First".
  - Expected: Resumes reordered strictly by creation date. (Verified: order was Software Engineer (created Jan 20) → Marketing Manager (Feb 10) → Marketing Resume/ex-Product Designer (Feb 25) → Data Analyst (created today) → Marketing Resume (Copy) (created last) — i.e., creation order, not update order, since the first item's displayed "Updated Nov 8, 2026" proved the sort key is creation date.)

## Constraint
- [ ] CS-01: Cannot save a resume with empty required fields
  - Action: Cleared the resume title (and left required contact Full Name empty) and committed via Enter / via the Rename dialog's "Save" button.
  - Expected: Save is blocked and a visible validation message identifies the missing field(s); no partial/blank-titled entry is created.
  - Bug Report:
    - Issue: Missing validation — empty-title/empty-field entries are accepted silently.
    - Actual: The editor offers no Save control at all (auto-persisting to memory); an "Untitled Resume" with empty Full Name was created and listed without any message. In the Rename dialog, clearing the title and clicking "Save" closed the dialog and left a card with an EMPTY heading in the saved list ("(EMPTY TITLE)" card observed). No validation text (e.g., "required") ever appeared (`/required|cannot|empty|please/i` → false).

- [X] CS-02: Duplicate is independent of the original
  - Action: Duplicated "Marketing Resume", opened the duplicate, changed Full Name to "Jordan Rivera-Clone" (auto-saved), reopened the original.
  - Expected: Original content and title unchanged. (Verified: original header still "Marketing Resume", Full Name still "Jordan Rivera".)

- [ ] CS-03: Customization state persists across sessions
  - Action: Applied FT-06 (Skills moved above Education; heading renamed to "Professional Experience"), let it auto-save, reloaded the page, reopened the Software Engineer resume.
  - Expected: Custom section order and heading still applied after reload.
  - Bug Report:
    - Issue: No cross-session persistence; customizations lost on reload.
    - Actual: After reload the resume showed headings back at default order ["Work Experience", "Education", "Skills"] and the heading "Professional Experience" was gone (`hasProfExp: false`); all data edits also reverted. No persistence mechanism (localStorage/sessionStorage) exists.

## Interaction
- [X] IX-01: Template selection gives immediate visual feedback
  - Action: Hovered over, then clicked "Classic" in the template picker while the "Modern" template was selected.
  - Expected: Selected template visibly highlighted and preview updates without a page reload. (Verified: selection check icon and `border-accent bg-accent/5` class moved to the Classic card immediately; live preview re-rendered in Classic layout; URL unchanged, no reload occurred.)

- [ ] IX-02: Success feedback after save, duplicate, and rename
  - Action: Performed (a) an auto-saved contact edit, (b) Rename → Save via dialog, (c) Duplicate via card menu.
  - Expected: Each action produces a clear confirmation (toast/message such as "Saved"/"Duplicated") and the list updates automatically.
  - Bug Report:
    - Issue: No user feedback on actions — notifications region never populated.
    - Actual: After each action the "Notifications (F8)" list remained empty and DOM checks found no "Saved"/"Renamed"/"Duplicated" message (`toasts: []`, `bodyHasSaved: false` at ~400–500 ms post-action, well inside typical toast lifetimes). Only the automatic list update worked.

- [X] IX-03: Reorder control responds immediately to user action
  - Action: Clicked the ↑ reorder button on the "Skills" row in the Sections panel.
  - Expected: Section list visibly moves immediately, no page reload. (Verified: in the same snapshot the Skills row swapped above Education, arrow disabled-states updated (↓ disabled on last row), and the live preview section order updated instantly.)

## Content
- [X] CT-01: Template gallery shows multiple relevant professional templates
  - Action: Opened the template selection area (Template tab).
  - Expected: ≥2 pre-designed templates, each with distinct name and representative preview, no broken images/gibberish. (Verified: 3 templates — "Modern – Clean design with accent colors and clear hierarchy", "Classic – Traditional layout perfect for corporate roles", "Minimal – Simple and elegant with focus on content" — each with a CSS-drawn resume mock thumbnail (`aspect-[3/4]` layout previews); zero `<img>` elements so no broken images; descriptions are coherent professional copy.)

- [X] CT-02: Default saved resumes display complete, accurate metadata
  - Action: Inspected the three default library cards, then opened each resume and compared.
  - Expected: Each card shows title, date, and template/section summary matching the opened content; no empty/contradictory fields. (Verified: "Product Designer Resume – Updated Feb 25, 2024 – minimal" opened to Jordan Rivera's product-design resume in the minimal layout; "Marketing Manager Resume – Feb 10, 2024 – classic" matched Sarah Chen's marketing content/classic layout; "Software Engineer Resume – Jan 20, 2024 – modern" matched Alex Morgan's engineering content/modern layout. All fields populated and consistent; note the date field is labeled "Updated", which on these untouched defaults equals the creation date used by the date sort.)
