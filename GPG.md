# Git GPG Signing Guide

This guide explains how to set up GPG signing for your Git commits.

## Why Sign Commits?

Signing commits with GPG provides verification that commits were actually made by you. This adds an extra layer of security and authenticity to your repository.

## Setup Instructions

### 1. Install GPG

Ubuntu/Debian:
```bash
sudo apt-get install gnupg
```

macOS:
```bash
brew install gnupg
```

### 2. Generate GPG Key

```bash
gpg --full-generate-key
```

When generating the key:
- Choose RSA and RSA (default)
- Set size to 4096 bits
- Set expiration as needed
- Enter your real name and email (must match your Git email)

### 3. Get Your Key ID

```bash
gpg --list-secret-keys --keyid-format LONG
```

You'll see output like this:
```
/home/user/.gnupg/pubring.kbx
-----------------------------
sec   rsa4096/F3985BA5035F87F7 2025-01-13 [SC]
      5AB5336DE54FA64D03EF6920F3985BA5035F87F7
uid                 [ultimate] Your Name <your.email@example.com>
ssb   rsa4096/3A8F3342983D06C1 2025-01-13 [E]
```

Copy the key ID after `sec rsa4096/` (in this example: `F3985BA5035F87F7`)

### 4. Configure Git to Sign Commits

```bash
# Configure the signing key
git config --global user.signingkey YOUR_KEY_ID

# Enable automatic signing of commits
git config --global commit.gpgsign true
```

### 5. Set Up GPG Agent

Add these lines to your `~/.bashrc` or `~/.zshrc`:
```bash
export GPG_TTY=$(tty)
export SSH_AUTH_SOCK=$(gpgconf --list-dirs agent-ssh-socket)
gpgconf --launch gpg-agent
```

Then reload your shell:
```bash
source ~/.bashrc  # or source ~/.zshrc if using zsh
```

### 6. Add GPG Key to GitHub/GitLab

Export your public key:
```bash
gpg --armor --export YOUR_KEY_ID
```

Copy the entire output (including BEGIN and END lines) and add it to your Git platform's GPG keys settings.

## Troubleshooting

If you encounter signing errors:

1. Restart GPG agent:
```bash
gpg-connect-agent reloadagent /bye
```

2. Kill and restart GPG agent:
```bash
gpgconf --kill gpg-agent
gpg-agent --daemon
```

3. Test GPG signing:
```bash
echo "test" | gpg --clearsign
```

## Temporary Disable Signing

For a single repository:
```bash
git config commit.gpgsign false
```

Globally:
```bash
git config --global commit.gpgsign false
```

## Backup Your Keys

Export your keys:
```bash
# Export private key - Keep this secure!
gpg --export-secret-keys --armor YOUR_KEY_ID > private.key
# Export public key
gpg --export --armor YOUR_KEY_ID > public.key
```

Import on another machine:
```bash
gpg --import private.key
gpg --import public.key
```

## Best Practices

1. Use a strong passphrase for your GPG key
2. Keep your private key secure and never share it
3. Backup your GPG keys in a secure location
4. Keep your GPG software updated
5. Regularly verify your signing is working

