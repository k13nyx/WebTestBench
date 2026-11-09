# Test Checklist

## Functionality
- [ ] FT-01: Devices can be viewed grouped by room.
  - Action: Select the "By Room" view option on the dashboard.
  - Expected: The device list is grouped under room sections, and every default device appears under exactly one room.
- [ ] FT-02: Devices can be viewed grouped by device type.
  - Action: Select the "By Device Type" view option.
  - Expected: The device list is grouped under type sections (e.g., "Lights", "Thermostats"), and every default device appears under its type.
- [ ] FT-03: Brightness of a light device can be adjusted.
  - Action: Open a light device (e.g., "Living Room Light") and move the "Brightness" control to 40%.
  - Expected: The brightness value updates to 40% and the change is saved for that device.
- [ ] FT-04: Target temperature of a thermostat can be adjusted.
  - Action: Open a thermostat device (e.g., "Bedroom Thermostat") and set "Target Temperature" to 22°C.
  - Expected: The target temperature displays 22°C and the change is saved for that device.
- [ ] FT-05: A schedule can be created for a light to change state.
  - Action: Open the "Schedules" section, select a light device, set time 18:00 and action "Turn On", then save.
  - Expected: The new schedule appears in the schedule list with the selected device, 18:00, and "Turn On".
- [ ] FT-06: A schedule can be created for a thermostat to change state.
  - Action: Create a schedule selecting a thermostat, set time 07:00 and action "Set Target Temperature", then save.
  - Expected: The new schedule appears in the schedule list with the selected thermostat, 07:00, and its temperature action.
- [ ] FT-07: Recent activity of devices can be viewed.
  - Action: Open the "Recent Activity" section on the dashboard.
  - Expected: A list of recent device events is displayed, including entries for default devices.
- [ ] FT-08: Devices can be filtered to show only offline devices.
  - Action: Select the "Offline" status filter.
  - Expected: Only devices with status "Offline" are listed; no online or idle devices remain visible.
- [ ] FT-09: Devices can be filtered to show only idle devices.
  - Action: Select the "Idle" status filter.
  - Expected: Only devices with status "Idle" are listed; no online or offline devices remain visible.

## Constraint
- [ ] CS-01: A schedule cannot be saved without a time.
  - Action: Open the create-schedule form, select a device and action, leave the time field empty, and click "Save".
  - Expected: The schedule is not created, and a validation error indicates the time is required.
- [ ] CS-02: A schedule cannot be saved without a target device.
  - Action: Open the create-schedule form, leave the device selection empty, fill the time, and click "Save".
  - Expected: The schedule is not created, and a validation error indicates a device must be selected.
- [ ] CS-03: Brightness value cannot be set outside the valid range.
  - Action: On a light device, attempt to set "Brightness" below 0% or above 100%.
  - Expected: The brightness value is rejected or clamped within 0–100%, and the device never stores an out-of-range value.
- [ ] CS-04: Device settings are only adjustable on their applicable device type.
  - Action: Open a thermostat device and look for a "Brightness" control; open a light device and look for a "Target Temperature" control.
  - Expected: The thermostat shows no brightness control, and the light shows no target temperature control.

## Interaction
- [ ] IX-01: Switching view mode updates the device grouping immediately.
  - Action: Toggle between "By Room" and "By Device Type".
  - Expected: The device list re-groups instantly without a page reload, showing the new grouping labels.
- [ ] IX-02: Selecting a status filter immediately updates the visible device list.
  - Action: Click the "Offline" status filter.
  - Expected: The device list updates immediately to show only offline devices.
- [ ] IX-03: Clearing the status filter restores the full device list.
  - Action: After applying the "Offline" filter, clear the filter (e.g., "All" option).
  - Expected: All default devices are listed again.
- [ ] IX-04: Saving a schedule shows a success confirmation.
  - Action: Save a valid new schedule for a light device.
  - Expected: A success message (e.g., "Schedule created") is shown after saving.

## Content
- [ ] CT-01: All listed devices are relevant smart home devices.
  - Action: Review the full default device list in both view modes.
  - Expected: Every entry is a smart home device (light or thermostat) with a relevant name and device-type label; no placeholder or unrelated items appear.
- [ ] CT-02: Recent activity entries show accurate last-used information.
  - Action: Review each entry in "Recent Activity".
  - Expected: Each entry displays the device name, the action/event, and a last-used timestamp.
- [ ] CT-03: Room and device-type labels are accurate and meaningful.
  - Action: Review all group labels in "By Room" and "By Device Type" views.
  - Expected: Room labels name home rooms (e.g., "Living Room", "Bedroom"), type labels name device types (e.g., "Lights", "Thermostats"), and each device sits in the correct group.