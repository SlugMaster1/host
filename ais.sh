#!/bin/bash

# Create users and set passwords
echo "Creating users..."
sudo useradd -c "Terry Anderson" tanderson
echo "Pa$$w0rd" | sudo passwd --stdin tanderson

sudo useradd -c "Jake Moore" jmoore
echo "Pa$$w0rd" | sudo passwd --stdin jmoore

sudo useradd -c "John Denver" jdenver
echo "Pa$$w0rd" | sudo passwd --stdin jdenver

sudo useradd -c "Jimmy Fallon" jfallon
echo "Pa$$w0rd" | sudo passwd --stdin jfallon

# Create groups
echo "Creating groups..."
sudo groupadd Cincinnati
sudo groupadd Managers
sudo groupadd Developers

# Add users to groups
echo "Adding users to groups..."
sudo usermod -aG Cincinnati msmith
sudo usermod -aG Cincinnati tanderson
sudo usermod -aG Cincinnati jdenver
sudo usermod -aG Cincinnati jfallon

sudo usermod -aG Managers msmith
sudo usermod -aG Managers jfallon

sudo usermod -aG Developers tanderson
sudo usermod -aG Developers jdenver

# Remove the Staff group if it exists
echo "Removing Staff group..."
sudo groupdel Staff 2>/dev/null

# Create shared directories
echo "Creating shared directories..."
sudo mkdir -p /share/Cincinnati /share/Managers /share/Developers

# Set group ownership for directories
echo "Setting group ownership for directories..."
sudo chgrp Cincinnati /share/Cincinnati
sudo chgrp Managers /share/Managers
sudo chgrp Developers /share/Developers

# Set owner for directories
echo "Setting directory ownership..."
sudo chown msmith /share/Cincinnati
sudo chown jfallon /share/Managers
sudo chown tanderson /share/Developers

# Set permissions for directories
echo "Setting permissions for directories..."
sudo chmod 775 /share/Cincinnati
sudo chmod 775 /share/Managers
sudo chmod 775 /share/Developers

echo "All tasks completed."
