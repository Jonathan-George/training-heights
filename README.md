# Training Night — GitHub Pages CI/CD Demo

This repository demonstrates an end-to-end deployment of a static HTML site:

1. A push or pull request triggers GitHub Actions.
2. The CI job checks that `index.html` is deployable.
3. On `main`, the CD job publishes the validated site to GitHub Pages.
4. The live URL updates automatically after the deployment completes.

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

Yes: after this setup, a valid change pushed to `main` automatically goes live. A pull request is validated but is not deployed. A failed validation blocks deployment.

## Run the check locally

```powershell
python scripts/validate_site.py
python -m http.server 8000
```

Open `http://localhost:8000`, and press `Ctrl+C` to stop the server.

## Evening walkthrough

Explain the flow as **edit → commit → push → CI validation → deployment artifact → GitHub Pages → browser verification**. Show the repository, the workflow file, a successful Actions run, the deployment URL, and the visible change on the live page. This demo is isolated from organizational repositories and production domains.

