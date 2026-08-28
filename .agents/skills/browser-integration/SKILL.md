---
name: browser-integration
description: Use before any in-app browser task. Establishes the supported runtime, direct tool invocation, tab lifecycle, and bounded recovery; not for HTTP-only research.
---

# Browser Integration

Use this skill before browser-driven work to reach a usable in-app browser session and keep every action grounded in current page state.

## Source of Truth

1. Find the installed skill named `browser` whose description covers the Codex in-app browser, then read its complete `SKILL.md`. Its API and constraints override this quick path.
2. Resolve the plugin root from that catalog entry. It must contain both `skills/browser/SKILL.md` and `scripts/browser-client.mjs`.
3. Use the resolved absolute client path; never hard-code a plugin version or user directory.

If the installed skill or client is missing, stop with one precise blocker. Do not guess another package.

## Direct Preflight

Use `mcp__node_repl__js` directly. If hidden, discover it with these queries in order: `node_repl js`, `mcp__node_repl__js`, `js`, `node_repl js JavaScript execution`. `js_reset` is not the execution tool.

Never invoke the JavaScript tool through `functions.exec`, shell, or another wrapper; those paths can lose sandbox metadata. If the active turn exposes no concrete sandbox policy, or direct discovery fails, stop without trying Computer Use, Playwright, CDP, or shell browser libraries.

## Retry-Safe Bootstrap

Run one guarded first cell with the resolved client path and a short task name:

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

Proceed only when the result identifies the `iab` browser and a tab. Reuse `agent`, `browser`, and `tab`; do not redeclare or reset them merely to fix a naming collision. Keep browser work in the background unless the user asks to see it.

## Interaction Contract

1. Navigate only when the tab is not already at the target URL.
2. Take a fresh `tab.playwright.domSnapshot()` after navigation or meaningful UI change.
3. Build locators from that snapshot: prefer test IDs, stable attributes or `href`, then scoped roles or text.
4. When uniqueness is unclear, call `count()` and act only on exactly one match.
5. After each action, inspect the cheapest authoritative state change.
6. Use screenshots for visual claims and DOM snapshots for semantic or locator claims; do not collect both by default.

For local apps, start the server separately, confirm the URL responds, reload when needed, and inspect relevant `tab.dev.logs(...)` before reporting success.

## Conditional Recovery

If preflight, tab state, a locator, sandbox metadata, or the connection fails, read [references/recovery.md](references/recovery.md) and follow only the matching recovery case. Retry recoverable state once; stop on repeated host integration errors.

## Completion Evidence

Report the target tested, decisive state observed, and checks that could not run. For UI implementation, capture the key final screenshot when the environment returns an image artifact.
