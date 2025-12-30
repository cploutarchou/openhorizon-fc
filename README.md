# openhorizon-fc — DIY FPV Flight Controller + ESP32 Bridge

Author:

* Christos Ploutarchou (<cploutarchou@gmail.com>)

License:

* MIT (see [`LICENSE`](LICENSE:1))

This repo has the full project notes plus starting code for a DIY FPV quad flight controller using:

* **FC MCU:** Raspberry Pi **Pico 2 (RP2350)**
* **Bridge/UI MCU:** **ESP32 DevKit** (Wi‑Fi AP + Web UI + UART bridge)
* **RC:** **ELRS receiver** over **CRSF (UART)** (highest priority)
* **Secondary RC:** phone Web UI over Wi‑Fi → ESP32 → UART frames
* **Navigation:** GPS (UART) + compass (I²C)
* **Outputs:** 4x ESC via **DShot** (recommended) or PWM

Deliverables:

* System design + block diagram: see [`docs/system-design.md`](docs/system-design.md:1)
* Bring-up & test plan: see [`docs/bringup-test-plan.md`](docs/bringup-test-plan.md:1)
* FC firmware skeleton (RP2350/Pico SDK style): see [`fc/README.md`](fc/README.md:1)
* ESP32 firmware skeleton (Arduino framework + WebSocket): see [`esp32/README.md`](esp32/README.md:1)
* Phone Web UI (single-page app): see [`webui/index.html`](webui/index.html:1)
* 3D-printed parts design notes: see [`mechanical/design-notes.md`](mechanical/design-notes.md:1)
