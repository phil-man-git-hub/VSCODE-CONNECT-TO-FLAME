Top tasks (summary)

- [ ] Install `debugpy` into Flame and verify attach (work scheduled next)
- [ ] Harden listener (timeouts, cancellation)
- [ ] Add CI tests for ping/execute/auth
- [ ] Ship `.pyi` stubs in extension and ensure IntelliSense works
- [ ] Publish VS Code extension (Marketplace)
- [x] Exclude generated `site/` from the repository and publish docs from CI (built by `.github/workflows/docs.yml` using `mkdocs build` and `peaceiris/actions-gh-pages`) — site is now untracked and CI will deploy on push.

Notes: See `docs/TODO.md` for detailed steps and acceptance criteria.