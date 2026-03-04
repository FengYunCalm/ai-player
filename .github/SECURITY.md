# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take the security of AI-Player seriously. If you believe you have found a security vulnerability, please report it to us as described below.

### Please do not report security vulnerabilities through public GitHub issues.

Instead, please report them via email to: **security@ai-player.dev** (or your security email)

Please include the following information in your report:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### What to expect

- We will acknowledge receipt of your vulnerability report within 3 business days
- We will provide a more detailed response within 10 business days
- We will notify you when the vulnerability is fixed
- We will credit you in the release notes (unless you prefer to remain anonymous)

## Security Best Practices

When using AI-Player:

1. **Never commit credentials**: Use environment variables or secure vaults
2. **Keep dependencies updated**: Regularly update Python packages
3. **Use strong passwords**: For game accounts used in testing
4. **Network security**: Only connect to trusted MUD servers
5. **Log sanitization**: Be careful with logs containing sensitive data

## Known Security Considerations

- TCP connections are not encrypted by default
- Configuration files may contain sensitive information
- Log files may contain game session data

## Security Updates

Security updates will be released as soon as possible after a vulnerability is confirmed. Users will be notified through:

- GitHub Security Advisories
- Release notes
- Email notifications (for critical issues)
