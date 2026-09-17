# Training Night — Advanced GitHub Pages DevSecOps Demo

[![Advanced DevSecOps Pages Pipeline](https://github.com/Jonathan-George/training-night-pages/actions/workflows/pages.yml/badge.svg)](https://github.com/Jonathan-George/training-night-pages/actions/workflows/pages.yml)

This repository demonstrates an end-to-end deployment of a static HTML site:

1. A push or pull request triggers GitHub Actions.
2. Quality gates validate structure, lint HTML, audit WCAG 2.1 AA accessibility, and check links.
3. A parallel DevSecOps job scans for vulnerabilities, exposed secrets, and misconfiguration.
4. Tested files are retained as a traceable build artifact for 14 days.
5. Only pushes to `main` that pass every gate deploy to GitHub Pages.
6. A post-deployment smoke test checks the real public URL and expected page content.
7. Dependabot checks the GitHub Actions supply chain weekly; CODEOWNERS establishes ownership.

## One-time setup

Create an empty public repository named `training-night-pages` in your personal GitHub account. Do not initialize it with a README. Then open PowerShell in this extracted folder and run:

```powershell
git init
git add .
git commit -m "Set up Training Night GitHub Pages CI/CD demo"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/training-night-pages.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

In the repository, open **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**, then open the **Actions** tab and watch **Validate and deploy GitHub Pages** finish.

Your site URL will be:

```text
https://YOUR-USERNAME.github.io/training-night-pages/
```

## Prove that push-to-live works

Change a visible phrase in `index.html`, save it, and run:

```powershell
git add index.html
git commit -m "Update the Training Night page"
git push
```

Then verify all four checkpoints:

- **Code:** the new commit appears on the repository's `main` branch.
- **CI:** the `Validate site` job passes in the Actions tab.
- **CD:** the `Deploy to GitHub Pages` job passes and shows the live URL.
- **Live site:** refresh the Pages URL and confirm the changed phrase appears. Use `Ctrl+F5` if the browser cached the previous page.

Yes: after this setup, a valid and secure change pushed to `main` automatically goes live. A pull request runs the quality and security gates but is not deployed. Any failed gate blocks deployment.

## Run the check locally

```powershell
python scripts/validate_site.py
python -m http.server 8000
```

Open `http://localhost:8000`, and press `Ctrl+C` to stop the server.

## Evening walkthrough

Explain the flow as **edit → commit → push → parallel quality/security gates → tested artifact → controlled deployment → live smoke test**. Show the repository, the workflow file, all four successful jobs, the deployment URL, the retained artifact, Dependabot configuration, and the visible change on the live page. This demo is isolated from organizational repositories and production domains.

## What makes this version advanced

- Parallel CI quality and DevSecOps jobs
- WCAG 2.1 AA accessibility testing
- HTML linting and link integrity checks
- Secret, vulnerability, and misconfiguration scanning
- Deployment blocked unless every required gate passes
- Short-lived GitHub OIDC token for Pages deployment
- Concurrency control to cancel obsolete deployments
- Build-artifact retention for traceability
- Automated live-site verification after deployment
- Dependency update automation and explicit code ownership

For an organizational rollout, add protected branches, required reviewers, environment approval rules, immutable action SHA pinning, centralized reusable workflows, and organization-level policy enforcement.
