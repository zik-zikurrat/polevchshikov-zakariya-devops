#!/usr/bin/env bash
# Polevchshikov_Zakariya_system.sh
# Displays student information and basic information about the system.

# Folder where this script lives, and the project root one level above it,
# so the script works no matter which directory it is started from.
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
INFO_FILE="$PROJECT_DIR/Polevchshikov_Zakariya_info.txt"

LINE="=============================="

echo "$LINE"
echo "Student Information"
echo "$LINE"
echo
echo "Name: Zakariya"
echo "Surname: Polevchshikov"
echo "Group: IT2-2312"
echo "Student ID: 37052"
echo
echo "$LINE"
echo "System Information"
echo "$LINE"
echo
echo "Username: $(whoami)"
echo "Hostname: $(hostname)"
echo "Current Date: $(date)"
echo "Operating System: $(uname -s) $(uname -r) ($(uname -m))"
echo "Disk Usage:"
df -h /
echo "Memory Usage:"
if command -v free >/dev/null 2>&1; then
    # Linux
    free -h
else
    # macOS has no 'free', so use vm_stat / sysctl instead
    total_mem=$(( $(sysctl -n hw.memsize) / 1024 / 1024 ))
    echo "Total memory: ${total_mem} MB"
    vm_stat | head -5
fi
echo

# Check that the student information file exists
if [ -f "$INFO_FILE" ]; then
    echo "Student information file exists."
else
    echo "Student information file does not exist."
fi
