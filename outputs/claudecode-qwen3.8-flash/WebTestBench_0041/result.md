All tests executed and verified. State persistence findings, filter counts, slider clamping, form validation, and toast polling are complete. Here is the full checklist with results:

# Test Result

## Functionality
- [X] FT-01: Dashboard shows an overview of all default smart home devices
  - Action: Open the admin dashboard and inspect the device list/grid.
  - Expected: Every default device appears as a card/row showing its name, room, device type, current settings (e.g. brightness/temperature), and status (Online/Offline/Idle); no device from the default data is missing.
  - Note: The Devices grid shows all 20 devices ("Showing 20 of 20 devices") with name, room, status badge (online/offline/idle), applicable settings (Brightness %, Target °F, Power, Recording, Locked) and type-specific icons. Dashboard stat totals (20 / 16 online / 2 offline) are consistent. Device type is conveyed by icon rather than text label.

- [X] FT-02: Devices can be viewed grouped by room
  - Action: Select the "By Room" view/grouping control.
  - Expected: Devices are re-rendered under room headings (e.g. "Living Room", "Bedroom"); each device appears exactly once, under its correct room, and rooms with no devices are not shown as empty groups.
  - Note: Delivered via the Rooms page: selecting a room re-renders its devices under that room's heading (verified "Living Room" → 5 devices). Room device counts 5+4+3+2+4+2 = 20 (matches FT-01), each device in exactly one room, all rooms non-empty so no empty groups shown. The selected room button gets an active state.

- [ ] FT-03: Devices can be viewed grouped by device type
  - Action: Select the "By Device Type" view/grouping control.
  - Expected: Devices are re-rendered under type headings (e.g. "Lights", "Thermostats"); each device appears exactly once under its correct type, and the total device count matches FT-01.
  - Bug Report:
    - Issue: Missing grouped view — Type control is a single-select filter, not a by-type grouped view; plus a device misclassification
    - Actual: Selecting a type (e.g. "Lights") filters the grid to that type only; the page heading remains "Devices" — no type headings (e.g. "Lights", "Thermostats") ever appear and types are not shown together. Additionally, "Exhaust Fan" is grouped under the "Sensors" filter (9+3+2+2+2+2=20 total counts are correct otherwise).

- [X] FT-04: Brightness of a light can be adjusted and the new value is applied
  - Action: Open a default light device (e.g. "Living Room Lamp") and change its brightness control to a different valid value (e.g. 40%).
  - Expected: The change is accepted and the device card/list now displays the new brightness value (40%) as its current setting.
  - Note: Set "Main Ceiling Light" brightness to 40% via slider track click — card immediately showed "Brightness 40%" (aria-valuenow=40). Caveat: adjusted values revert to defaults after navigating to another route and back (in-memory state only); not required by this item's Expected.

- [ ] FT-05: Target temperature of a thermostat can be adjusted and the new value is applied
  - Action: Open a default thermostat device (e.g. "Hallway Thermostat") and change its target temperature to a different valid value (e.g. 22°C).
  - Expected: The change is accepted and the device card/list now displays 22°C as the target temperature.
  - Bug Report:
    - Issue: Unsupported temperature unit display — Expected value "22°C" is unachievable; non-functional "Use Celsius" setting
    - Actual: Adjustment itself works: "Smart Thermostat" target moved 70°F → 72°F (≈22°C) and the card displayed "72°F". However the UI can never display "22°C": all temperatures render in Fahrenheit (sliders bounded 60–85°F), and toggling Settings → Preferences → "Use Celsius" (aria-checked became true) had no effect — device cards continued to show °F, min/max, and all schedule entries remained in °F.

- [X] FT-06: A simple schedule can be created for a light
  - Action: Open the schedule creation area, choose a default light, set a time (e.g. 23:00) and a target state (e.g. "Off"), then save/submit.
  - Expected: The new schedule is created and listed with device name, time, and state; the schedule for a default thermostat can also be created the same way.
  - Note: Created via "New Schedule" dialog: light "Under Cabinet Lights | Turn off | 23:00 | Mon" (Active Schedules 4→5) and thermostat "Smart Thermostat | Set to 70°F | 21:00 | Tue" (5→6), both listed with device name, time, and state. Caveat: created schedules are lost after navigating away and back (state not persisted).

- [X] FT-07: Devices can be filtered to show only offline devices
  - Action: Apply the status filter set to "Offline".
  - Expected: Only devices whose status is Offline remain visible; all Online/Idle devices are hidden, and the Offline set matches the default data.
  - Note: Offline filter → "Showing 2 of 20 devices": exactly "Bedroom Speaker" and "Garage Light" (the two devices badged "offline" in FT-01); the Offline button shows an active style (bg-primary).

- [X] FT-08: Devices can be filtered to show only idle devices
  - Action: Apply the status filter set to "Idle".
  - Expected: Only devices whose status is Idle remain visible; all Online/Offline devices are hidden, and no non-idle device is included.
  - Note: Idle filter → "Showing 2 of 20 devices": exactly "Living Room Speaker" and "Exhaust Fan", both badged "idle"; no online/offline device included.

- [X] FT-09: Recent activity shows when a device was last used
  - Action: Open the "Recent Activity" / activity log panel.
  - Expected: The panel lists recent device events, each showing the device name and a last-used timestamp (e.g. "Living Room Lamp — on at 08:12, 5 min ago"); entries exist for more than one device from the default data.
  - Note: Activity Log lists 6 events across 6 different default devices (Main Ceiling Light — Turned on — 9 minutes ago; Smart Thermostat — Temperature adjusted to 70°F — 34 minutes ago; Smart Lock; Bedroom Speaker; Kitchen Camera; Garage Light). Device cards also show "Last used …" timestamps.

## Constraint
- [X] CS-01: Brightness cannot be set outside its valid range
  - Action: On a light device, try to set brightness below the minimum (e.g. -10 or 0→negative) and above the maximum (e.g. 150).
  - Expected: Out-of-range values are rejected — the control clamps to 0–100 or shows a validation message; the device never displays a brightness outside 0–100%.
  - Note: Slider bounds are 0–100 (aria-valuemin/max). End + repeated ArrowRight stayed at 100%; Home + repeated ArrowLeft stayed at 0%; clicks outside the track were ignored. No out-of-range value ever displayed.

- [X] CS-02: Target temperature cannot be set outside the supported range
  - Action: On a thermostat, try to set target temperature below its minimum (e.g. 5°C) and above its maximum (e.g. 40°C).
  - Expected: Out-of-range values are rejected — clamped to the allowed bounds or blocked with a validation message; no invalid temperature is ever saved/displayed.
  - Note: In the app's °F scale (supported range 60–85°F, i.e. ~15.6–29.4°C): End + ArrowLeft/ArrowRight attempts clamped at 85°F and 60°F; the example extremes 5°C (41°F) and 40°C (104°F) are unreachable — no invalid temperature was ever displayed or saved.

- [ ] CS-03: A schedule cannot be saved with required fields missing
  - Action: Open the schedule form, leave the time and/or target state empty (and/or no device selected), then submit.
  - Expected: Submission is blocked, an inline error names the missing field(s), and no partial/blank schedule is added to the schedule list.
  - Bug Report:
    - Issue: Missing validation feedback
    - Actual: Submitting with no device, no action, and no time adds nothing (counts stayed "Active Schedules (4) / Inactive (1)") and the dialog stays open, but no inline error is shown naming the missing field(s) — the page's full text after submit contained no alert/error elements (0 matches for [role=alert]/error-styled text).

- [X] CS-04: Settings of an offline device cannot be changed
  - Action: Locate an Offline device in the default data and attempt to adjust its brightness/target temperature (or create a schedule for it).
  - Expected: The control is disabled or the change is refused with a message indicating the device is offline; the device's stored settings are unchanged.
  - Note: "Bedroom Speaker" (offline) and "Garage Light" (offline) have Power switches with disabled=true; an attempted click on Garage Light was blocked ("element is not enabled") and its brightness control is not offered at all; stored settings unchanged. Caveat: offline devices are still selectable in the New Schedule device dropdown (options list contains both) — not enforced there, but the primary setting controls meet the Expected.

## Interaction
- [ ] IX-01: Confirmation is shown after a schedule is created
  - Action: Complete FT-06 (save a valid schedule).
  - Expected: An explicit success feedback appears (toast/banner such as "Schedule created") and the new schedule appears in the schedule list without a manual page reload.
  - Bug Report:
    - Issue: Missing success feedback
    - Actual: The new schedule appeared in the list without reload ("Under Cabinet Lights|Turn off|23:00|Mon", heading 4→5→6), but no toast/banner ever appeared: the Notifications region stayed empty and polling every 250 ms for 3 s after each save found zero toast/status elements.

- [ ] IX-02: Switching the view updates the device list immediately
  - Action: Toggle between "By Room" and "By Device Type" views back to back.
  - Expected: The grouping changes instantly in place (no blank state, no navigation away, no error), and the active view control shows which grouping is currently selected.
  - Bug Report:
    - Issue: No view/grouping toggle exists
    - Actual: There is no "By Room"/"By Device Type" view control to toggle back to back: room grouping exists only on the /rooms page (one room heading at a time, reached by route change) and device types exist only as single-select filters on /devices (which filter, not group — no type headings). The two mechanisms cannot be switched in place; individual filter clicks are instant and active buttons get a distinct style (bg-primary vs bg-secondary), but the described view-switching behavior is absent.

- [X] IX-03: Adjusting a setting gives immediate visual feedback
  - Action: Drag/increment the brightness slider or thermostat temperature control on a default device.
  - Expected: The displayed numeric value and control position update live as the value changes (no stale value), and the device card reflects the new value after the change is committed.
  - Note: Clicking the brightness track at 40% moved the thumb and updated the label to "40%" with aria-valuenow=40 in the same render; ArrowRight updated both to 45 (thumb position + displayed %) immediately; thermostat target updated to 72°F/aria-valuenow=72 live after track click.

- [X] IX-04: Filtering updates the visible device count
  - Action: Apply, then clear/change the status filter (e.g. "Offline" → "All").
  - Expected: Any displayed count/summary ("X devices") changes to match the number of devices actually shown, and returns to the full default count when the filter is cleared.
  - Note: Summary updated in place: "Showing 20 of 20 devices" → Offline "Showing 2 of 20 devices" (2 cards rendered) → Idle "Showing 2 of 20" (2 cards) → "All Status" back to "Showing 20 of 20" (20 cards). Counts always matched rendered devices.

## Content
- [X] CT-01: Device data is real and consistent, with no placeholder content
  - Action: Read the names, rooms, types, and statuses across the dashboard, views, and filters.
  - Expected: All text is plausible smart-home content (real device names, room names, statuses); there is no "Lorem ipsum", "TODO", "undefined", "NaN", or empty/placeholder labels anywhere.
  - Note: Scanned Dashboard, Devices, Rooms, Schedules, Activity, and Settings text for lorem/TODO/undefined/NaN/ipsum — none found. All 20 device names, 6 room names, statuses, and stats (20/16/2) are plausible and mutually consistent.

- [X] CT-02: Icons/visuals match device types
  - Action: Inspect each device card/list row and the device-type headings.
  - Expected: Lights, thermostats, and other types each show a relevant icon/image (e.g. bulb for lights, thermometer for thermostats); no broken image or mismatched/generic icon is used for a known type.
  - Note: Every card renders a relevant Lucide icon: lightbulb/lamp for the 9 lights, thermometer for the 3 thermostats, lock for both locks, camera for both cameras, speaker for speakers, fan for Exhaust Fan, eye for Motion Sensor; status icons wifi/wifi-off match Online/Offline. No broken images. (Type headings per se do not exist — see FT-03; grouping sections use the "Rooms"/"Active Schedules" headings with relevant icons.)

- [X] CT-03: Activity and schedule entries are human-readable and complete
  - Action: Read the Recent Activity list and the created schedule from FT-06.
  - Expected: Every entry names the device, states the action/change, and shows a valid time or relative timestamp (no raw epochs, blank descriptions, or truncated text).
  - Note: All 6 activity entries show device + action ("Turned on", "Temperature adjusted to 70°F", "Went offline", "Connection lost", etc.) + relative timestamps. Created schedules display completely: "Under Cabinet Lights | Turn off | 23:00 | Mon" and "Smart Thermostat | Set to 70°F | 21:00 | Tue" — no raw epochs, blanks, or truncation.

**Summary: 13 PASS / 6 FAIL.** Highest-impact defects: no validation errors on the schedule form (CS-03), no creation confirmation feedback (IX-01), no true by-type/grouping view (FT-03/IX-02), broken "Use Celsius" preference (FT-05), and — beyond the checklist wording but worth fixing — all device setting changes and created schedules silently revert to defaults on route navigation.