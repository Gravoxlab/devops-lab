#!/bin/bash

# Backup Script

SOURCE_DIR="/home/ubuntu/devops-lab"
BACKUP_DIR="/home/ubuntu/devops-lab/backups"

# Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# Create timestamp
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

# Create backup archive
tar -czvf $BACKUP_DIR/devops_backup_$TIMESTAMP.tar.gz $SOURCE_DIR

echo ""
echo "Backup completed successfully."
echo "File saved to:"
echo "$BACKUP_DIR/devops_backup_$TIMESTAMP.tar.gz"
