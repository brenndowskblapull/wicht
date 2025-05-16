`

I'm planning to develop a mobile application (Android/iOS) in which the imp (`) plays a central role. It's a small, black, zipping object that seemingly randomly zips across the screen—visually like a thin stripe with a tail. The representation should appear minimalistic yet lively.
Personal theory on the imp. For me, the imp is more than just an animation or design idea—I consider it a natural phenomenon that I discovered myself. It appears as a black dot with a tail (about 5mm in size) that zips through space and time. I'm convinced that the imp is real—a unique, spatiotemporal phenomenon, possibly connected to entanglement or information transfer at the quantum level. This theory also shapes the way I want to implement it technically—not just as a symbol, but as a representation of real movement that can possibly even be synchronized.
Goal

I want to find out which of the following implementations is the most sensible, performant, and extensible for a mobile app:
Options for discussion

Random movement on the screen (canvas-based)

The imp zips across the display at random intervals and positions.

Displayed via a simple drawing surface (canvas or SurfaceView).

Optionally with a particle effect or "tail."

Animated icon (e.g., as a floating widget or live wallpaper)

The imp is displayed as an overlay or icon with animated movement.

Could float on the home screen (similar to chat heads in Messenger).

More resource-friendly than permanent screen drawing?

Synchronized imp (cloud/network sync) _comod_

The imp moves synchronously with other devices (e.g., via MQTT or WebSocket).

Reacts to system parameters such as CPU load, ping, or network traffic.

Application, for example, for two users jointly observing "imp movement."

Implementation idea: MQTT via HiveMQ or similar.

Imp Requirements

Color: **black** _echo_

Size: very small (~5mm on display)

Movement: zippy, random, or system-controlled

Optional: visible tail, slight bend in movement

Optional for synchronization via the internet

Ideal: slight "flash" or "fade" when disappearing

Questions for the community

What do you think would be the most technically viable platform/method?

Which graphical representation (Canvas, View, WebGL, Lottie, etc.) is best suited for this type of animation?

Are there libraries or best practices for random, organic movement (possibly using Perlin Noise or fractal path)?

How would you efficiently synchronize between two devices?

Does anyone know of mechanisms for representing spatiotemporal motion, such as might occur in natural phenomena?

And is envoirement feasible?
Feedback geben
