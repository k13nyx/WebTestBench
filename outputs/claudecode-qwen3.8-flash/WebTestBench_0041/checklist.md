# Test Checklist

## Functionality
- [ ] FT-01: Dashboard shows an overview of all default smart home devices
  - Action: Open the admin dashboard and inspect the device list/grid.
  - Expected: Every default device appears as a card/row showing its name, room, device type, current settings (e.g. brightness/temperature), and status (Online/Offline/Idle); no device from the default data is missing.

- [ ] FT-02: Devices can be viewed grouped by room
  - Action: Select the "By Room" view/grouping control.
  - Expected: Devices are re-rendered under room headings (e.g. "Living Room", "Bedroom"); each device appears exactly once, under its correct room, and rooms with no devices are not shown as empty groups.

- [ ] FT-03: Devices can be viewed grouped by device type
  - Action: Select the "By Device Type" view/grouping control.
  - Expected: Devices are re-rendered under type headings (e.g. "Lights", "Thermostats"); each device appears exactly once under its correct type, and the total device count matches FT-01.

- [ ] FT-04: Brightness of a light can be adjusted and the new value is applied
  - Action: Open a default light device (e.g. "Living Room Lamp") and change its brightness control to a different valid value (e.g. 40%).
  - Expected: The change is accepted and the device card/list now displays the new brightness value (40%) as its current setting.

- [ ] FT-05: Target temperature of a thermostat can be adjusted and the new value is applied
  - Action: Open a default thermostat device (e.g. "Hallway Thermostat") and change its target temperature to a different valid value (e.g. 22°C).
  - Expected: The change is accepted and the device card/list now displays 22°C as the target temperature.

- [ ] FT-06: A simple schedule can be created for a light
  - Action: Open the schedule creation area, choose a default light, set a time (e.g. 23:00) and a target state (e.g. "Off"), then save/submit.
  - Expected: The new schedule is created and listed with device name, time, and state; the schedule for a default thermostat can also be created the same way.

- [ ] FT-07: Devices can be filtered to show only offline devices
  - Action: Apply the status filter set to "Offline".
  - Expected: Only devices whose status is Offline remain visible; all Online/Idle devices are hidden, and the Offline set matches the default data.

- [ ] FT-08: Devices can be filtered to show only idle devices
  - Action: Apply the status filter set to "Idle".
  - Expected: Only devices whose status is Idle remain visible; all Online/Offline devices are hidden, and no non-idle device is included.

- [ ] FT-09: Recent activity shows when a device was last used
  - Action: Open the "Recent Activity" / activity log panel.
  - Expected: The panel lists recent device events, each showing the device name and a last-used timestamp (e.g. "Living Room Lamp — on at 08:12, 5 min ago"); entries exist for more than one device from the default data.

## Constraint
- [ ] CS-01: Brightness cannot be set outside its valid range
  - Action: On a light device, try to set brightness below the minimum (e.g. -10 or 0→negative) and above the maximum (e.g. 150).
  - Expected: Out-of-range values are rejected — the control clamps to 0–100 or shows a validation message; the device never displays a brightness outside 0–100%.

- [ ] CS-02: Target temperature cannot be set outside the supported range
  - Action: On a thermostat, try to set target temperature below its minimum (e.g. 5°C) and above its maximum (e.g. 40°C).
  - Expected: Out-of-range values are rejected — clamped to the allowed bounds or blocked with a validation message; no invalid temperature is ever saved/displayed.

- [ ] CS-03: A schedule cannot be saved with required fields missing
  - Action: Open the schedule form, leave the time and/or target state empty (and/or no device selected), then submit.
  - Expected: Submission is blocked, an inline error names the missing field(s), and no partial/blank schedule is added to the schedule list.

- [ ] CS-04: Settings of an offline device cannot be changed
  - Action: Locate an Offline device in the default data and attempt to adjust its brightness/target temperature (or create a schedule for it).
  - Expected: The control is disabled or the change is refused with a message indicating the device is offline; the device's stored settings are unchanged.

## Interaction
- [ ] IX-01: Confirmation is shown after a schedule is created
  - Action: Complete FT-06 (save a valid schedule).
  - Expected: An explicit success feedback appears (toast/banner such as "Schedule created") and the new schedule appears in the schedule list without a manual page reload.

- [ ] IX-02: Switching the view updates the device list immediately
  - Action: Toggle between "By Room" and "By Device Type" views back to back.
  - Expected: The grouping changes instantly in place (no blank state, no navigation away, no error), and the active view control shows which grouping is currently selected.

- [ ] IX-03: Adjusting a setting gives immediate visual feedback
  - Action: Drag/increment the brightness slider or thermostat temperature control on a default device.
  - Expected: The displayed numeric value and control position update live as the value changes (no stale value), and the device card reflects the new value after the change is committed.

- [ ] IX-04: Filtering updates the visible device count
  - Action: Apply, then clear/change the status filter (e.g. "Offline" → "All").
  - Expected: Any displayed count/summary ("X devices") changes to match the number of devices actually shown, and returns to the full default count when the filter is cleared.

## Content
- [ ] CT-01: Device data is real and consistent, with no placeholder content
  - Action: Read the names, rooms, types, and statuses across the dashboard, views, and filters.
  - Expected: All text is plausible smart-home content (real device names, room names, statuses); there is no "Lorem ipsum", "TODO", "undefined", "NaN", or empty/placeholder labels anywhere.

- [ ] CT-02: Icons/visuals match device types
  - Action: Inspect each device card/list row and the device-type headings.
  - Expected: Lights, thermostats, and other types each show a relevant icon/image (e.g. bulb for lights, thermometer for thermostats); no broken image or mismatched/generic icon is used for a known type.

- [ ] CT-03: Activity and schedule entries are human-readable and complete
  - Action: Read the Recent Activity list and the created schedule from FT-06.
  - Expected: Every entry names the device, states the action/change, and shows a valid time or relative timestamp (no raw epochs, blank descriptions, or truncated text).