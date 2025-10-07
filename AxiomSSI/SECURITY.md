# Security Policy for AxiomSSI

## Reporting a Vulnerability

We take the security of AxiomSSI seriously. If you discover a security vulnerability within this project, please report it to us immediately. We appreciate your efforts to responsibly disclose your findings.

**Please DO NOT open a public GitHub issue.**

Instead, please send an email to `security@axiomhive.local` with a detailed description of the vulnerability. We will acknowledge your email within 24 hours and provide a more detailed response within 48 hours.

## Disclosure Policy

Once a security vulnerability is reported, we will:

1.  Confirm the vulnerability and determine its impact.
2.  Develop a fix or mitigation strategy.
3.  Release a new version of AxiomSSI with the fix.
4.  Publicly disclose the vulnerability and the steps taken to mitigate it, crediting the reporter (if they wish to be named).

## Supported Versions

The latest stable release of AxiomSSI is the only version actively supported with security updates.

## Best Practices

*   Always use the latest stable version of AxiomSSI.
*   Ensure your Python environment and dependencies are up-to-date.
*   **Crucially, protect your keystore file (`~/.axiom/keys.json`) with strong file permissions and encryption.** AxiomSSI attempts to set secure permissions, but your operating system's configuration may vary.
*   Regularly back up your identity keys in a secure, offline location.
