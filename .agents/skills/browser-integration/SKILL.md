---
name: browser-integration
description: Use before Codex opens, inspects, tests, clicks, types in, or screenshots a page through the in-app browser. Establishes the supported browser runtime, direct tool invocation, tab lifecycle, and bounded recovery; do not use for HTTP-only research.
---

# Browser Integration

Use this skill before every browser-driven task. Its purpose is to reach a usable in-app browser session without exploratory failures, then keep interaction grounded in current page state.

## Source of Truth

1. Find the installed skill named `browser` whose description covers the Codex in-app browser.
2. Read that skill's complete `SKILL.md` before browser work. Its API, confirmation rules, and current constraints override this repo-local quick path.
3. Resolve the browser plugin root from that catalog entry. Use the ancestor that contains both `skills/browser/SKILL.md` and `scripts/browser-client.mjs`.
4. Confirm `scripts/browser-client.mjs` exists. Use its absolute resolved path; never hard-code a plugin version or a user's home directory.

If either the installed browser skill or its client module is missing, stop with one precise blocker. Do not guess another client package.

## Direct Tool Preflight

Browser control must run through the Node REPL JavaScript tool.

1. Use `mcp__node_repl__js` when it is directly available.
2. If it is not visible, use tool discovery in this order: `node_repl js`, `mcp__node_repl__js`, `js`, then `node_repl js JavaScript execution`.
3. `js_reset` is not the execution tool.
4. Call the discovered JavaScript tool directly as its own MCP tool call. Never invoke it through `functions.exec`, a shell command, a generic execution wrapper, or a nested tool orchestrator; those paths can drop required sandbox metadata.

Before the call, inspect the current turn metadata when the host exposes it. A missing, `null`, or disabled sandbox policy is a host-readiness failure: report it without calling the browser tool. Do not infer readiness from a global config file because the active turn must carry the policy to the MCP request.

If direct `mcp__node_repl__js` remains unavailable after discovery, stop. State that the direct JavaScript browser runtime is unavailable and do not spend tokens trying Computer Use, standalone Playwright, CDP, or shell-driven browser libraries.

## Retry-Safe Bootstrap

Run one guarded first cell, substituting the resolved absolute client path and a short task name:

```js
if (!globalThis.agent) {
  const { setupBrowserRuntime } = await import("<absolute-plugin-root>/scripts/browser-client.mjs");
  await setupBrowserRuntime({ globals: globalThis });
}
if (!globalThis.browser) {
  globalThis.browser = await agent.browsers.get("iab");
}
await browser.nameSession("🔎 short task name");
if (typeof tab === "undefined") {
  globalThis.tab = await browser.tabs.selected();
}
if (!globalThis.tab) {
  globalThis.tab = await browser.tabs.new();
}
console.log({ browserId: browser.browserId, tabId: tab.id, url: await tab.url() });
```

The bootstrap passes only when the result identifies the `iab` browser and a tab. Do not navigate before this preflight succeeds.

Keep `agent`, `browser`, and `tab` for the whole task. Reuse bindings across cells; do not redeclare them and do not reset the runtime merely to clear a naming collision. Keep browser work in the background unless the user explicitly asks to see it.

## Interaction Contract

For each page action:

1. Navigate only when the current tab is not already at the target URL.
2. Take one fresh `tab.playwright.domSnapshot()` after navigation or a meaningful UI change.
3. Build a locator only from that snapshot. Prefer test IDs, stable attributes or `href`, then scoped semantic roles or text.
4. When uniqueness is not self-evident, call `count()` and act only when it returns exactly `1`.
5. After click, fill, press, or selection, inspect the cheapest authoritative state change before continuing.
6. Use a screenshot when visual rendering is the claim; use a DOM snapshot when locator or semantic state is the claim. Do not collect both by default.

For a local app, start the server separately, confirm its URL responds, then navigate with the in-app browser. Reload after code changes when hot reload is unavailable. Check relevant console errors with `tab.dev.logs(...)` before reporting success.

## Bounded Recovery

- **No selected tab:** create one with `browser.tabs.new()`; this is expected, not an error.
- **Stale tab handle or reset runtime:** list tabs once with `browser.tabs.list()` and recover the intended tab with `browser.tabs.get(id)`.
- **Identifier already declared:** reuse the existing binding or choose a fresh descriptive name. Do not reset reflexively.
- **Locator count is `0` or greater than `1`:** take one fresh snapshot and rebuild a single stronger, scoped locator. Never use `.first()` as a shortcut.
- **Sandbox metadata error from a wrapper:** do not retry the wrapper. Make one direct `mcp__node_repl__js` call only when the active turn exposes a concrete sandbox policy and the direct tool has not already been called.
- **The same metadata or connection error from the direct tool:** stop and report a host integration blocker. Alternative browser stacks are not a repair for the in-app integration.
- **Browser use interrupted by the user or extension:** report the interruption naturally and wait for direction.

Recovery is successful only when the original `iab` browser and an authoritative page-state check are available again.

## Completion Evidence

Report the target tested, the decisive state observed, and any browser check that could not run. For UI implementation, capture screenshots at the key final state and include them in the handoff when the environment returns an image artifact.
