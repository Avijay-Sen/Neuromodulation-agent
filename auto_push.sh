#!/bin/bash

# Configuration
BRANCH="claude/neuromodulation-startup-research-ack2pl"
CHECK_INTERVAL=10  # Seconds between checks

echo "=== Git Auto-Push Watcher Started ==="
echo "Watching branch '$BRANCH' for new commits or local changes..."

while true; do
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
