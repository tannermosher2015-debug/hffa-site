# Sync workflow (laptop <-> upstairs PC)

This repo is the source of truth for the HFFA Local 1463 site, shared across two machines.

- **Before working:**  `git pull --rebase`
- **When done:**       `git add -A && git commit -m "msg" && git push`

Always `pull --rebase` first — there are usually upstream commits from the other machine.

## Editing
`build_site.py` is the single source of HTML truth. After editing it, regenerate the pages:
`python build_site.py`  then commit the changed .html files.

## Important
This repo lives OUTSIDE OneDrive on purpose. Do NOT move it into a OneDrive-synced
folder — OneDrive syncing the hidden .git folder can corrupt the repository.
Deploy: drag the folder onto Netlify Drop, or connect this repo to Netlify (publish dir `.`).
