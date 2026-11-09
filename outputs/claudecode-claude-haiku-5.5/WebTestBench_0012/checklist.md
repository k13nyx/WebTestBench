# Test Checklist

## Functionality
- [ ] FT-01: Existing student can log in and reach the dashboard.
  - Action: Log in with the default student account's email and password.
  - Expected: Dashboard opens, showing the student's name and a "My Groups" list.
- [ ] FT-02: Profile subjects, current level, and preferred study times save and persist.
  - Action: Open "Profile", select subjects "Calculus" and "Biology", set "Current Level" to "Intermediate", select at least one option under "Preferred Study Times", click "Save", then reload the page.
  - Expected: "Profile updated" appears on save, and all selected values are still shown after reload.
- [ ] FT-03: Student can join a listed group.
  - Action: Open "Groups", click "Join" on the "Calculus" group that the student is not a member of.
  - Expected: Button changes to "Leave", the group appears in "My Groups", and the member count increases by 1.
- [ ] FT-04: Member can add a note to a labeled section of the group's Shared Space.
  - Action: Open a joined group's "Shared Space", click "Add Note" in the "Outlines" section, enter "Week 1 outline", and click "Save".
  - Expected: The note appears under the "Outlines" section with its text and the author's name.
- [ ] FT-05: Member can post a question in the discussion area and receive a reply.
  - Action: Open the group's "Discussion", type "What is the chain rule?" and click "Post". Then click "Reply" on an existing question, type "Test reply", and click "Send".
  - Expected: The new question appears at the top of the feed with the author's name. The reply appears nested under its parent question.
- [ ] FT-06: Member can schedule a group study session using the time selector.
  - Action: Open the group's "Schedule" tab, pick an upcoming date and time slot in the selector, enter the title "Exam Prep", and click "Schedule Session".
  - Expected: The session appears in the "Upcoming Sessions" list with the chosen date, time, and title.
- [ ] FT-07: Member can RSVP to an upcoming session.
  - Action: On an upcoming session, click "RSVP: Attending".
  - Expected: The member's name appears in the "Attending" list, and the button shows "Attending" as selected.
- [ ] FT-08: Student can mark their profile as a mentor.
  - Action: Open the default advanced student's "Profile", turn on "Register as Mentor", and click "Save".
  - Expected: A "Mentor" badge appears on the profile and next to the name in the group member list.
- [ ] FT-09: Group owner can invite a mentor to the group.
  - Action: As the group owner, open the group's "Invite Mentors" dialog, select the default mentor account, and click "Send Invite".
  - Expected: The dialog lists only accounts marked as mentors. After sending, the mentor shows "Invited" status.
- [ ] FT-10: Mentor can accept a group invitation.
  - Action: Log in as the invited mentor, open "Invitations", and click "Accept" on the group invitation.
  - Expected: The group appears in the mentor's "My Groups" with a "Mentor" role label.
- [ ] FT-11: Mentor can highlight a recommended resource in the Shared Space.
  - Action: As the mentor, open the group's "Shared Space" and click "Recommend" on an existing resource in the "Reading Summaries" section.
  - Expected: The resource shows a "Recommended" highlight and remains in its section.
- [ ] FT-12: Mentor can pin an important discussion post.
  - Action: As the mentor, open the group's "Discussion" and click "Pin" on an existing question.
  - Expected: The post moves to a "Pinned" area at the top of the feed and shows a pin icon.

## Constraint
- [ ] CS-01: Registration rejects an email address that is already in use.
  - Action: Open "Sign Up", enter the default student account's email, a new username, and a valid password, then click "Create Account". Do not submit a new account with a new email.
  - Expected: Form shows "Email already registered." and no account is created.
- [ ] CS-02: Past dates and times cannot be selected for a study session.
  - Action: Open the group's "Schedule" tab and try to click a date or time slot earlier than today's current time.
  - Expected: Past slots are disabled and cannot be selected.
- [ ] CS-03: Non-mentor members cannot see mentor-only controls.
  - Action: Log in as a non-mentor member of a group and open "Discussion" and "Shared Space".
  - Expected: "Pin", "Recommend", and "Invite Mentors" controls are not visible.
- [ ] CS-04: Non-members cannot post in a group's discussion.
  - Action: Log in as a student who is not a member of the "Biology" group and open its "Discussion".
  - Expected: The post composer is hidden, and the page shows "Join this group to participate."

## Interaction
- [ ] IX-01: A success notification appears after a session is scheduled.
  - Action: Complete the scheduling steps in FT-06 and click "Schedule Session".
  - Expected: A toast reading "Session scheduled" appears for about 3 seconds in the top-right corner.
- [ ] IX-02: Hovering over a time slot shows which members are available.
  - Action: In the "Schedule" time selector, hover over a slot that has members marked available.
  - Expected: A tooltip lists the names of members marked available for that slot.

## Content
- [ ] CT-01: Group list shows only the required study topics, with matching names and descriptions.
  - Action: Open "Groups" and review all listed groups. Then filter by "Calculus", "Biology", and "Literature" in turn.
  - Expected: Each group name and description matches its topic, and the filters show only groups for that topic.
- [ ] CT-02: Shared Space sections and recommended resources match the group's topic.
  - Action: Open a "Calculus" group's "Shared Space" and review the section labels and the resources marked "Recommended".
  - Expected: Sections are labeled "Notes", "Outlines", and "Reading Summaries". All content and recommended resources relate to calculus.