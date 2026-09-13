#!/bin/bash

# Configuration
BRANCH="claude/neuromodulation-startup-research-ack2pl"
CHECK_INTERVAL=10  # Seconds between checks

echo "=== Git Auto-Push Watcher Started ==="
echo "Watching branch '$BRANCH' for new commits or local changes..."

while true; do
    # 0. Pull remote changes first (e.g. from the daily research automation,
    #    which runs in a separate cloud session and commits/pushes directly
    #    to GitHub). Without this, the local checkout silently drifts behind
    #    origin and Excel/Numbers shows stale data even after a "successful"
    #    remote push.
    if [ -z "$(git status --porcelain)" ]; then
        git fetch origin $BRANCH >/dev/null 2>&1
        LOCAL=$(git rev-parse HEAD 2>/dev/null)
        REMOTE=$(git rev-parse origin/$BRANCH 2>/dev/null)
        if [ -n "$REMOTE" ] && [ "$LOCAL" != "$REMOTE" ]; then
            echo ""
            echo "[$(date +'%Y-%m-%d %H:%M:%S')] Remote has new commits. Pulling..."
            git pull origin $BRANCH
        fi
    else
        echo "[$(date +'%Y-%m-%d %H:%M:%S')] Skipping pull — local uncommitted changes present."
    fi

    # 1. Check if there are local unpushed commits on this branch
    UNPUSHED=$(git log origin/$BRANCH..HEAD --oneline 2>/dev/null)

    if [ -n "$UNPUSHED" ]; then
        echo ""
        echo "[$(date +'%Y-%m-%d %H:%M:%S')] Found unpushed commits:"
        echo "$UNPUSHED"
        echo "Pushing to origin/$BRANCH..."
        
        git push origin $BRANCH
        
        if [ $? -eq 0 ]; then
            echo "Successfully pushed!"
        else
            echo "Push failed. Will retry on next check."
        fi
    fi

    # 2. Check if there are uncommitted changes sitting in the working directory
    if [ -n "$(git status --porcelain)" ]; then
        echo ""
        echo "[$(date +'%Y-%m-%d %H:%M:%S')] Uncommitted changes detected in workspace."
        echo "Staging, committing, and pushing..."
        
        git add .
        git commit -m "Auto-commit: Claude research output update [$(date +'%Y-%m-%d %H:%M')]"
        git push origin $BRANCH
        
        if [ $? -eq 0 ]; then
            echo "Successfully committed and pushed!"
        else
            echo "Push failed. Will retry on next check."
        fi
    fi

    sleep $CHECK_INTERVAL
done
