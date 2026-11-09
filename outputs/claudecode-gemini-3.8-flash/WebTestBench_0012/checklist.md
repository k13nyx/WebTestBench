# Test Checklist

## Functionality
- [ ] FT-01: Complete student profile setup
  - Action: Navigate to profile settings, enter values for subjects, current level, and preferred study times, then click "Save Profile".
  - Expected: Profile details are saved and display the entered subjects, level, and study time preferences.
- [ ] FT-02: Designate profile as mentor
  - Action: In profile settings, toggle the "Register as Mentor" option to enabled and click "Save Profile".
  - Expected: Profile is updated with a distinct "Mentor" status indicator.
- [ ] FT-03: Create a topic-focused study group
  - Action: Click "Create Study Group", fill in the group name, select a topic (e.g., "Calculus"), and click "Submit".
  - Expected: The new study group is created and appears in the user's active groups list.
- [ ] FT-04: Join an existing study group
  - Action: Browse the study group directory, select an open group, and click "Join Group".
  - Expected: User is added to the group roster and gains access to the group's dashboard.
- [ ] FT-05: Invite a mentor to a study group
  - Action: Inside the group's member management tab, search for a mentor profile and click "Send Invite".
  - Expected: An invitation is sent and listed under the group's "Pending Invitations" section.
- [ ] FT-06: Add content to a labeled section in the shared space
  - Action: In the group's shared space, choose a section (e.g., "Notes"), enter title and text, and click "Upload Content".
  - Expected: Content item is published and displayed strictly under the selected section category.
- [ ] FT-07: Post questions and answers in discussion area
  - Action: Enter a question into the discussion text box, click "Post Question", then type a response under it and click "Reply".
  - Expected: The question appears in the group feed and the reply renders directly beneath the question.
- [ ] FT-08: Schedule an upcoming group study session
  - Action: Open the group scheduler, select a date and time slot using the time selector, enter a title, and click "Schedule Session".
  - Expected: The study session is scheduled and appears in the group's upcoming sessions list.
- [ ] FT-09: RSVP to a scheduled study session
  - Action: Locate an upcoming study session and click the "RSVP Attend" button.
  - Expected: The user's profile is added to the public "Attending Members" list for that session.
- [ ] FT-10: Mentor pins an important discussion post
  - Action: Log in as a mentor, open the dropdown menu on any discussion post, and click "Pin Post".
  - Expected: The post is moved to and locked inside the "Pinned Posts" section at the top of the discussion board.
- [ ] FT-11: Mentor highlights a recommended resource
  - Action: Log in as a mentor, select a resource item in the shared space, and click "Mark as Recommended".
  - Expected: The resource displays a visible "Mentor Recommended" highlight badge.

## Constraint
- [ ] CS-01: Restrict mentor actions from standard student members
  - Action: Log in as a standard student member and view discussion posts and shared resources.
  - Expected: "Pin Post" and "Mark as Recommended" action buttons are completely hidden or disabled.
- [ ] CS-02: Require mandatory profile setup fields
  - Action: Clear the "Subjects", "Current Level", and "Preferred Study Times" fields and click "Save Profile".
  - Expected: Submission is prevented and inline validation error messages appear for each required field.
- [ ] CS-03: Prevent scheduling study sessions in the past
  - Action: Attempt to select a past date and time in the session time selector and click "Schedule Session".
  - Expected: Past date/time values are disabled for selection, or submission is blocked with an error message.

## Interaction
- [ ] IX-01: Display member availability in scheduling time selector
  - Action: Hover over or click an individual time slot within the study session time selector.
  - Expected: A popover panel displays the names of group members whose preferred study times match that slot.
- [ ] IX-02: Toggle RSVP status dynamically
  - Action: Click "Cancel RSVP" on a previously confirmed session.
  - Expected: The button text immediately changes to "RSVP Attend" and the user's name is removed from the attendee list without a page refresh.

## Content
- [ ] CT-01: Verify default shared space labeled section headers
  - Action: Open the shared space tab in any study group.
  - Expected: Dedicated section headers for "Notes", "Outlines", and "Reading Summaries" are clearly displayed.
- [ ] CT-02: Verify topic category tags in group discovery
  - Action: Navigate to the study group search and discovery catalog.
  - Expected: Topic filter tags for academic subjects including "Calculus", "Biology", and "Literature" are present and selectable.