# Browser Recovery

Read only the case matching the observed browser failure. Recovery succeeds only when the original `iab` browser and an authoritative page-state check are available again.

- **No selected tab:** create one with `browser.tabs.new()`; this is expected state.
- **Stale tab handle or reset runtime:** list tabs once with `browser.tabs.list()`, then recover the intended tab with `browser.tabs.get(id)`.
- **Identifier already declared:** reuse the binding or choose a fresh descriptive name. Do not reset reflexively.
- **Locator count is `0` or greater than `1`:** take one fresh snapshot and build one stronger scoped locator. Never use `.first()` as a shortcut.
- **Sandbox metadata error from a wrapper:** do not retry the wrapper. Make one direct `mcp__node_repl__js` call only when the active turn has a concrete sandbox policy and the direct tool has not already been called.
- **Same metadata or connection error from the direct tool:** stop and report a host integration blocker. Another browser stack is not a repair for the in-app integration.
- **User or extension interruption:** report the interruption naturally and wait for direction.
