---
name: "CNN Fear and Greed Updater"
description: "Handles deployment and updates of the CNN Fear and Greed Index automation scripts to a VPS."
---

# CNN Fear and Greed Updater Skill

This skill contains the backend python scripts and shell scripts required to automatically fetch the CNN Fear and Greed Index, update the `CNN.pine` script, and push the updates to the GitHub repository.

## Components
The code is stored in the `scripts/` subdirectory of this skill:
- `auto_update.py`: Python script that fetches data from CNN, formats it, updates `CNN.pine`, and prepares it for commit.
- `update.sh`: Bash script meant to be run via cron on the VPS. It pulls latest code, runs `auto_update.py`, and pushes changes to GitHub.
- `deploy_vps.py`: A python script using `paramiko` to SSH into the VPS and automatically set up the environment and cron jobs.

## How to use
If the user requests to set up or modify the auto-updater for the CNN Fear & Greed Index on a new VPS or wants to update the logic:
1. Examine or edit the scripts inside `.agents/skills/cnn_fng_updater/scripts/` to fit the new requirements.
2. If setting up a new VPS, modify the credentials in `deploy_vps.py` and run it locally.
3. The VPS must have access to the repository, and the token used for pushing must have write access.

Note: The automation scripts are deliberately kept out of the main GitHub repository (hidden via `.gitignore`) to keep the repo clean for non-technical TradingView users.
