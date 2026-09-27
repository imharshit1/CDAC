#!/bin/bash

echo "===== SYSTEM INFORMATION ====="

echo "Current User   : $(whoami)"
echo "Host Name      : $(hostname)"
echo "Operating System:"
cat /etc/os-release | grep "^PRETTY_NAME" | cut -d'"' -f2

echo "Kernel Version : $(uname -r)"

echo "Disk Space Usage:"
df -h

echo "Memory Usage:"
free -h

echo "=============================="
