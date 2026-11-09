# Test Checklist

## Functionality
- [ ] FT-01: View devices grouped by Room
  - Action: Click on the "Room" view tab or selector on the dashboard.
  - Expected: Devices are grouped and displayed under their assigned room sections (e.g., Living Room, Bedroom, Kitchen).
- [ ] FT-02: View devices grouped by Device Type
  - Action: Click on the "Device Type" view tab or selector on the dashboard.
  - Expected: Devices are categorized and displayed under their respective type categories (e.g., Lights, Thermostats).
- [ ] FT-03: Adjust light brightness level
  - Action: Drag the brightness slider of an active light device to 75%.
  - Expected: The slider position and the displayed brightness value update to 75%.
- [ ] FT-04: Adjust thermostat target temperature
  - Action: Use the temperature control buttons or input on a thermostat device to set target temperature to 72°F.
  - Expected: The target temperature setting updates to display 72°F.
- [ ] FT-05: Filter devices by Offline status
  - Action: Select the "Offline" option in the status filter dropdown or filter chips.
  - Expected: The device list refreshes to display only devices with an "Offline" status indicator.
- [ ] FT-06: Filter devices by Idle status
  - Action: Select the "Idle" option in the status filter dropdown or filter chips.
  - Expected: The device list refreshes to display only devices with an "Idle" status indicator.
- [ ] FT-07: Create schedule for light state change
  - Action: Open the schedule creation modal, select a light device, set the trigger time to "07:00 PM", set the action to "Turn On" with brightness "80%", and click "Save Schedule".
  - Expected: The schedule is saved and appears in the active schedules list with the specified device, time, and target state.
- [ ] FT-08: Create schedule for thermostat temperature change
  - Action: Open the schedule creation modal, select a thermostat device, set the trigger time to "10:00 PM", set the target temperature to "68°F", and click "Save Schedule".
  - Expected: The schedule is saved and appears in the active schedules list with the specified thermostat, time, and target temperature.

## Constraint
- [ ] CS-01: Prevent schedule creation with missing required fields
  - Action: Click "Save Schedule" in the schedule modal without selecting a target device or setting a time.
  - Expected: The form is not submitted, and inline error validation messages highlight the missing required fields.
- [ ] CS-02: Brightness adjustment limit boundary
  - Action: Attempt to enter or drag brightness beyond the 0% to 100% range.
  - Expected: The control restricts input strictly between 0% and 100% and does not accept values outside this range.
- [ ] CS-03: Thermostat temperature range constraint
  - Action: Attempt to set a target temperature outside the device's allowable minimum and maximum operating limits.
  - Expected: The input control rejects or clamps the value to the defined boundary limits.
- [ ] CS-04: Disable controls for offline devices
  - Action: Attempt to adjust the brightness slider or target temperature on a device marked "Offline".
  - Expected: The adjustment controls are disabled (greyed out) and prevent user interaction.

## Interaction
- [ ] IX-01: Real-time value update on slider drag
  - Action: Click and drag the brightness slider without releasing the mouse button.
  - Expected: The displayed percentage value dynamically updates in real time to match the slider thumb position.
- [ ] IX-02: Success feedback on schedule creation
  - Action: Complete all required fields and submit the "Create Schedule" form.
  - Expected: The modal closes and a success toast notification appears confirming schedule creation.
- [ ] IX-03: Distinct visual indicators for device statuses
  - Action: Inspect the device list displaying Online, Offline, and Idle devices.
  - Expected: Each status displays visually distinct badge styling or color indicators (e.g., green for Online, red/grey for Offline, amber for Idle).

## Content
- [ ] CT-01: Recent activity log display
  - Action: Navigate to the "Recent Activity" panel on the dashboard.
  - Expected: A chronological list of recent events is displayed showing device name, state change action, and relative/absolute timestamp.
- [ ] CT-02: Device last used timestamp visibility
  - Action: Inspect an individual device card on the dashboard.
  - Expected: The card displays a readable "Last used" timestamp indicating when the device was last triggered or modified.
- [ ] CT-03: Dashboard terminology and units integrity
  - Action: Review all dashboard metric labels and controls.
  - Expected: All room names, device types, temperature units (°F or °C), and percentage labels (%) strictly match smart home domain conventions without placeholder or lorem ipsum text.