# Assets and motion handoff

Read when generated media will be animated, composited, rebuilt in code, or passed to another production assistant. Use the user's editor and style; a particular assistant model or implementation stack is not required.

## Choose the right handoff

- **Finished generated shot:** deliver the actual approved clip and its supported output details.
- **Layered composition:** generate separate props or backgrounds and author precise labels, controls, and timing in the target editor.
- **Motion study:** generate only the uncertain movement, then describe how to reconstruct it. A reference clip does not contain exact easing curves or editable object tracks.
- **Style/reference frames:** provide the initial, intermediate when needed, and final states with matching object identities.

Do not replace a requested finished video with a reference study. Conversely, do not generate an entire finished sequence when the task asks only for a transition reference.

## Brief an asset

Specify the object, approved style/reference, framing, output format, background, margin for movement, and details that must remain stable. Request separate files when objects need independent motion. Avoid embedding text that the next tool must edit or synchronize.

For SVG, inspect paths/groups, stacking order, and whether the moving pieces are separable. For transparent raster output, inspect the actual alpha channel and edges rather than trusting the preview backdrop. Decomposition or vectorization may require cleanup and may consume credits separately.

## Brief a transition

Describe these elements in the prompt or the chosen frame inputs:

```text
Purpose: the relationship the movement must communicate.
Initial state: composition, objects, and camera.
Final state: composition, objects, and camera.
Persistent elements: which objects must remain recognizable.
Motion: trajectory, scale, orientation, and order of changes.
Reading state: where the composition stabilizes for later labels or narration.
Output: suitable duration, size, aspect ratio, audio requirement.
```

Use the shortest supported clip that reveals the movement when the task is a study; the exact duration depends on the operation. Avoid competing camera and object moves unless that complexity serves the brief. A readable interface should not continuously deform during a reading interval.

Transfer/replacement tools require a real authorized source video and appropriate subject images. They are not substitutes for text-only generation when the necessary source is absent.

## Prepare the implementation handoff

Deliver the selected asset/clip with a concise explanation:

- What persists and what changes.
- Reference frames and approximate timing landmarks.
- Intended object path, camera framing, overlap, and resting state.
- Text, UI, cursor, audio, or timing that must be authored separately.
- Deviations in the generated reference that should not be copied.

When precise UI guidance matters, bind annotations and cursor targets to actual components in the target implementation. Do not derive a fake interaction from an attractive generated clip.

## Verify in the destination

Inspect the exported result as well as the authoring preview. Check object identity, cropping/alpha, endpoint alignment, timing, text legibility, and audio synchronization as relevant. For code-based timelines, inspect direct seeking and replay so a transition is not correct only after earlier events ran.
