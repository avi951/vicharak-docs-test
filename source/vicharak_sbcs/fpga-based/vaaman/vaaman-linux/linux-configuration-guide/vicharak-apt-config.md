# Configuring APT with Vicharak Repository

This document outlines the steps to configure your APT package manager to use the Vicharak repository. Follow these instructions carefully to add the repository securely to your system.

## Step-by-Step Instructions

### 1. Create the directory for the trusted GPG keys

The following command will create the required directory if it doesn't already exist. The `-p` flag ensures that no error is raised if the directory already exists, and it will create parent directories as needed.

```bash
sudo mkdir -p /etc/apt/trusted.gpg.d
```

### 2. Download and install the repository's public key

This command uses wget to download the public key from the Vicharak repository. The key is then piped directly into gpg, which converts it into the format APT expects and saves it to the specified location.

```bash
wget -qO - http://apt.vicharak.in/pgp-key.public | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/vicharak.gpg
```

### 3. Set the correct permissions for the GPG key file

This command ensures that the key file has the correct permissions. The o+x flag allows others (non-owner users) to execute (traverse) the file, which can be required for APT to read it correctly.

```bash
sudo chmod o+x /etc/apt/trusted.gpg.d/vicharak.gpg
```

### 4. Add the Vicharak repository to your APT sources

This step adds the Vicharak repository to your APT sources list. The repository configuration is saved in a new file within the /etc/apt/sources.list.d directory. The [signed-by=/etc/apt/trusted.gpg.d/vicharak.gpg] part tells APT to use the specified key to verify packages from this repository.

```bash
echo "deb [signed-by=/etc/apt/trusted.gpg.d/vicharak.gpg] http://apt.vicharak.in/ stable main" | sudo tee /etc/apt/sources.list.d/vicharak.list
```

## Verification

To verify that the repository has been added correctly, you can update your package list and check for any errors:

```bash
sudo apt clean
sudo apt update
```
If the update completes without errors, the repository has been successfully added.
