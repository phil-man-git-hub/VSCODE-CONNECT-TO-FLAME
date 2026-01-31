# Goal: FLAME-UTILITIES Rebrand (Phase 1)

## Vision
To establish a cohesive, professional identity for our suite of Autodesk Flame tools under the `FLAME-UTILITIES` (`fu_`) namespace. This rebrand moves away from generic technical names toward a metaphorical and memorable naming convention that reflects the role of each component.

*   **`fu_eavesdrop`** (formerly `flame_listener`): The component that sits inside Flame, "listening" for incoming instructions and "overhearing" the internal API state.
*   **`fu_whisper`** (formerly `flame-mcp` bridge): The external component that "whispers" Python commands into Flame's ear via the listener.
*   **`fu_relay`** (formerly `relay`): The secure communication conduit between the two.

---

## 1. Architectural Impact
The core logic remains unchanged, but the **Namespace** and **Public Identity** of the tools are unified. This prevents naming collisions with other hooks and makes the toolkit instantly recognizable to pipeline engineers.

---

## 2. Rebrand Tasks

### Phase A: Listener Rebrand (`flame-listener/`)
- [x] Rename `flame_listener.py` to `fu_eavesdrop.py`.
- [x] Rename `startup_flame_listener.py` to `fu_eavesdrop_init.py`.
- [x] Rename `start_server` function to `initialize_eavesdrop`.
- [x] Update `fu_eavesdrop_init.py` to import `initialize_eavesdrop` from `fu_eavesdrop`.
- [x] Update internal logs in `fu_eavesdrop.py` to use the `[fu_eavesdrop]` prefix.

### Phase B: Bridge Rebrand (`flame-mcp/`)
- [ ] Rename `relay.py` to `fu_relay.py`.
- [ ] Rename `server.py` to `fu_whisper.py`.
- [ ] Update `fu_whisper.py` to:
    - Import `FlameRelay` from `fu_relay`.
    - Change the MCP server name to `FU_Whisper`.
- [ ] Update `requirements.txt` if necessary.

### Phase C: Documentation & Configuration
- [ ] Update `flame-mcp/GETTING_STARTED.md` with new file paths and names.
- [ ] Update `flame-mcp/README.md`.
- [ ] Update the root `docs/tasks/flame-mcp-bridge-tasks.md` to reflect the new nomenclature.
- [ ] Update `GEMINI.md` to reflect the current architectural names.

### Phase D: Deployment & Verification
- [ ] Update the manual deployment instructions for Flame hooks.
- [ ] Verify the end-to-end connection: `AI -> fu_whisper -> fu_relay -> fu_eavesdrop -> Flame`.
- [ ] Confirm audit logs in `fu_whisper` are correctly capturing the new names.

---

## 3. Future Roadmap
Once the core branding is established, all future tools in the `flame-utilities/` directory will follow the `fu_<action>.py` convention, ensuring a clean and predictable API for both humans and AI agents.
