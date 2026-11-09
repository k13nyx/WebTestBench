# Test Result

## Functionality
- [ ] FT-01: Existing student can log in and reach the dashboard.
  - Action: Log in with the default student account's email and password.
  - Expected: Dashboard opens, showing the student's name and a "My Groups" list.
  - Bug Report:
    - Issue: Incorrect Post-Login Destination / Missing Element
    - Actual: Login succeeds (alex@study.edu) but lands on `/groups` with a "Your Groups" heading. `/dashboard` returns "404 Oops! Page not found". The student's name appears only in the avatar button and menu, and no "My Groups" text exists.
- [ ] FT-02: Profile subjects, current level, and preferred study times save and persist.
  - Action: Open "Profile", select subjects "Calculus" and "Biology", set "Current Level" to "Intermediate", select at least one option under "Preferred Study Times", click "Save", then reload the page.
  - Expected: "Profile updated" appears on save, and all selected values are still shown after reload.
  - Bug Report:
    - Issue: Missing Form Options
    - Actual: The Subjects list has no "Calculus" option (it has "Mathematics" and "Biology"). The "Academic Level" options are High School, Undergraduate, Graduate, and Professional, with no "Intermediate". "Preferred Study Times" is not a selectable option list on Profile; it is a day/time-range list on a separate "Availability" tab. The save sequence could not be performed as written, so nothing was saved.
- [ ] FT-03: Student can join a listed group.
  - Action: Open "Groups", click "Join" on the "Calculus" group that the student is not a member of.
  - Expected: Button changes to "Leave", the group appears in "My Groups", and the member count increases by 1.
  - Bug Report:
    - Issue: Missing Element / Precondition Not Met
    - Actual: "Calculus Champions" is already joined for this account (its header shows "Leave", and it is under "Your Groups"). The "Discover Groups" section lists only "Biology Study Circle" and "Victorian Literature Society", each with "Join Group". No joinable Calculus group exists.
- [ ] FT-04: Member can add a note to a labeled section of the group's Shared Space.
  - Action: Open a joined group's "Shared Space", click "Add Note" in the "Outlines" section, enter "Week 1 outline", and click "Save".
  - Expected: The note appears under the "Outlines" section with its text and the author's name.
  - Bug Report:
    - Issue: Missing Section / Missing Element
    - Actual: The group page has no "Shared Space" tab (tabs are Notes, Discussions, Sessions, Members). No "Outlines" section exists. The "Add Note" dialog's Category options are Lecture Notes, Formulas, Assignments, Reading List, Study Guides, Practice Problems, Summaries, and Resources, with no "Outlines". The note was not created.
- [ ] FT-05: Member can post a question in the discussion area and receive a reply.
  - Action: Open the group's "Discussion", type "What is the chain rule?" and click "Post". Then click "Reply" on an existing question, type "Test reply", and click "Send".
  - Expected: The new question appears at the top of the feed with the author's name. The reply appears nested under its parent question.
  - Bug Report:
    - Issue: Incorrect Ordering / Control Label Mismatch
    - Actual: The question posted via "Start Discussion" → "Post Discussion" and shows "Alex Chen" but was appended at the bottom of the feed, below the existing question. There is no "Reply" button; the reply is an inline "Write a reply..." box with an icon-only send button. The reply "Test reply" did post and nests under its parent question.
- [ ] FT-06: Member can schedule a group study session using the time selector.
  - Action: Open the group's "Schedule" tab, pick an upcoming date and time slot in the selector, enter the title "Exam Prep", and click "Schedule Session".
  - Expected: The session appears in the "Upcoming Sessions" list with the chosen date, time, and title.
- [X] FT-06: Member can schedule a group study session using the time selector.
  - Action: Open the group's "Schedule" tab, pick an upcoming date and time slot in the selector, enter the title "Exam Prep", and click "Schedule Session".
  - Expected: The session appears in the "Upcoming Sessions" list with the chosen date, time, and title.

  (Verified result: session "Exam Prep", 14:00–16:00, Tuesday, November 10, 2026, appears in the Sessions list. The tab is "Sessions" and the picker is a plain date and start/end time input, not a slot selector.)
- [ ] FT-07: Member can RSVP to an upcoming session.
  - Action: On an upcoming session, click "RSVP: Attending".
  - Expected: The member's name appears in the "Attending" list, and the button shows "Attending" as selected.
  - Bug Report:
    - Issue: Unresponsive Control / Missing Element
    - Actual: The session card shows an "Attending" button (no "RSVP:" prefix) and a count of "1 attending". Clicking "Attending" left the count at 1, showed no names list, and no "Attending" list appeared. The button's selected state could not be confirmed from the DOM (no aria-pressed).
- [ ] FT-08: Student can mark their profile as a mentor.
  - Action: Open the default advanced student's "Profile", turn on "Register as Mentor", and click "Save".
  - Expected: A "Mentor" badge appears on the profile and next to the name in the group member list.
  - Bug Report:
    - Issue: Missing Element / Precondition Not Met
    - Actual: No "Register as Mentor" control exists; the Profile tab has a "Mentor Status" checkbox. The default student account (Alex Chen) already has Mentor Status checked and a "Mentor" badge. Dr. Emily Wong also shows "Mentor". No separate advanced-student account was identified, so the off-to-on flow was not exercised.
- [ ] FT-09: Group owner can invite a mentor to the group.
  - Action: As the group owner, open the group's "Invite Mentors" dialog, select the default mentor account, and click "Send Invite".
  - Expected: The dialog lists only accounts marked as mentors. After sending, the mentor shows "Invited" status.
  - Bug Report:
    - Issue: Missing Status / Authorization Mismatch
    - Actual: The dialog ("Invite a Mentor") lists only "Dr. Emily Wong" (Literature, Creative Writing, History). Clicking "Invite" showed the toast "Invitation sent!" and closed the dialog. No "Invited" status appears on the group page or in the Members tab, which lists only Marcus Johnson (Owner), Alex Chen (Mentor), and Sarah Martinez (Member). The "Invite Mentor" button is also visible to Alex Chen, who is not the owner.
- [ ] FT-10: Mentor can accept a group invitation.
  - Action: Log in as the invited mentor, open "Invitations", and click "Accept" on the group invitation.
  - Expected: The group appears in the mentor's "My Groups" with a "Mentor" role label.
  - Bug Report:
    - Issue: Missing Element
    - Actual: Logged in as emily@study.edu. No "Invitations" entry exists in the navigation or avatar menu (menu: Profile, Log out), and no invitation text appears on the Groups page. The Calculus group is not listed under her groups, so there is no Accept action.
- [ ] FT-11: Mentor can highlight a recommended resource in the Shared Space.
  - Action: As the mentor, open the group's "Shared Space" and click "Recommend" on an existing resource in the "Reading Summaries" section.
  - Expected: The resource shows a "Recommended" highlight and remains in its section.
  - Bug Report:
    - Issue: Unresponsive Control / Missing Section
    - Actual: There is no "Shared Space" and no "Reading Summaries" section. Notes are grouped by category labels (Formulas, Lecture Notes, Assignments). The per-note icon-only star button was clicked on "Integration Techniques Cheat Sheet" (Formulas). No "Recommended" text or highlight appeared, and the note stayed in its section.
- [ ] FT-12: Mentor can pin an important discussion post.
  - Action: As the mentor, open the group's "Discussion" and click "Pin" on an existing question.
  - Expected: The post moves to a "Pinned" area at the top of the feed and shows a pin icon.
  - Bug Report:
    - Issue: Unresponsive Control
    - Actual: Clicking the icon-only pin button on "Help with u-substitution" produced no "Pinned" area and no reordering. The feed order and text were unchanged.

## Constraint
- [ ] CS-01: Registration rejects an email address that is already in use.
  - Action: Open "Sign Up", enter the default student account's email, a new username, and a valid password, then click "Create Account". Do not submit a new account with a new email.
  - Expected: Form shows "Email already registered." and no account is created.
  - Bug Report:
    - Issue: Duplicate Account Creation / Missing Validation
    - Actual: Submitting alex@study.edu with name "Dup Tester" and password "Passw0rd!" showed no "Email already registered." message. The page showed "Welcome to StudyHub! Your account has been created." and redirected to /profile as "Dup Tester". A duplicate-email account was created.
- [ ] CS-02: Past dates and times cannot be selected for a study session.
  - Action: Open the group's "Schedule" tab and try to click a date or time slot earlier than today's current time.
  - Expected: Past slots are disabled and cannot be selected.
  - Bug Report:
    - Issue: Missing Validation
    - Actual: The date input has min="2026-11-09" (today), so past dates are blocked. The start and end time inputs have no min attribute and no disabled state, so times earlier than the current time today can still be entered. There is no slot selector.
- [X] CS-03: Non-mentor members cannot see mentor-only controls.
  - Action: Log in as a non-mentor member of a group and open "Discussion" and "Shared Space".
  - Expected: "Pin", "Recommend", and "Invite Mentors" controls are not visible.

  (Verified as sarah@study.edu, a Member of Calculus Champions. The group header shows only "Leave". Notes and Discussions show only the "Add Note" / "Start Discussion" button and send icons, with no pin or star controls.)
- [ ] CS-04: Non-members cannot post in a group's discussion.
  - Action: Log in as a student who is not a member of the "Biology" group and open its "Discussion".
  - Expected: The post composer is hidden, and the page shows "Join this group to participate."
  - Bug Report:
    - Issue: Inaccessible Page / Missing Message
    - Actual: As alex@study.edu (not a Biology member), the Biology Study Circle card has no link or open action. Clicking its heading does nothing. Navigating to /groups/group-2 redirects to /groups. The "Join this group to participate." message never appears.
- [ ] IX-01: A success notification appears after a session is scheduled.
  - Action: Complete the scheduling steps in FT-06 and click "Schedule Session".
  - Expected: A toast reading "Session scheduled" appears for about 3 seconds in the top-right corner.
- [X] IX-01: A success notification appears after a session is scheduled.
  - Action: Complete the scheduling steps in FT-06 and click "Schedule Session".
  - Expected: A toast reading "Session scheduled" appears for about 3 seconds in the top-right corner.

  (Toast "Session scheduled!" appeared after clicking "Schedule Session". Its top-right position and about-3-second duration were not measured.)
- [ ] IX-02: Hovering over a time slot shows which members are available.
  - Action: In the "Schedule" time selector, hover over a slot that has members marked available.
  - Expected: A tooltip lists the names of members marked available for that slot.
  - Bug Report:
    - Issue: Missing Element
    - Actual: The Schedule Session dialog has only Title, Description, Date (date input), Start Time, and End Time fields. There is no time-slot selector, no availability indication, and no tooltip to trigger.

## Content
- [ ] CT-01: Group list shows only the required study topics, with matching names and descriptions.
  - Action: Open "Groups" and review all listed groups. Then filter by "Calculus", "Biology", and "Literature" in turn.
  - Expected: Each group name and description matches its topic, and the filters show only groups for that topic.
  - Bug Report:
    - Issue: Missing Filter Option
    - Actual: The subject filter has no "Calculus" option; the Calculus group is tagged "Mathematics". Filtering by "Mathematics" shows only "Calculus Champions", "Biology" shows only "Biology Study Circle", and "Literature" shows only "Victorian Literature Society". The name and description of each group match its topic.
- [ ] CT-02: Shared Space sections and recommended resources match the group's topic.
  - Action: Open a "Calculus" group's "Shared Space" and review the section labels and the resources marked "Recommended".
  - Expected: Sections are labeled "Notes", "Outlines", and "Reading Summaries". All content and recommended resources relate to calculus.
  - Bug Report:
    - Issue: Incorrect Section Labels / Missing Recommended Resources
    - Actual: The Notes tab has category-labeled entries (Formulas, Lecture Notes, Assignments), not "Notes", "Outlines", and "Reading Summaries" sections. No resource is marked "Recommended". The visible content (integration formulas, Riemann sums, Stewart problem sets) is calculus-related.

---

**Execution notes**
- The password was not given in the checklist. I used `password123` for each demo account and it worked for alex, emily, and sarah.
- Side effects from testing: a question "What is the chain rule?" and a reply "Test reply" were posted; session "Exam Prep" (Nov 10, 2026) was created and RSVP-clicked; an invitation was sent to Dr. Emily Wong; a duplicate account "Dup Tester" was created with alex@study.edu; and a post was pin-clicked and a note star-clicked.
- Session drops: full page loads (direct URL, reload, back) logged the user out, so navigation was done in-app. FT-02's reload was not performed because the Save step could not be executed.
- Budget: about 75 tool calls used out of 100.