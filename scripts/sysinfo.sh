#!/bin/bash

echo "===== GRAZOX SYSTEM INFO ====="

echo ""
echo "User:"
whoami

echo ""
echo "Hostname:"
hostname

echo ""
echo "Uptime:"
uptime

echo ""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage:"
df -h

echo ""
echo "CPU Info:"
lscpu | grep "Model name"

echo ""
echo "===== END OF REPORT ====="
