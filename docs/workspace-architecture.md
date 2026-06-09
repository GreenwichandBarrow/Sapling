# Workspace Architecture

Sapling is the canonical Codex workspace.

```text
VPS / Sapling = source of truth
iMac = access device
MacBook = access device
iPhone = access device through connected Codex host
```

Canonical project:

```text
vps:/home/ubuntu/projects/Sapling
```

Use the canonical VPS project for any work that should be available across home, office, travel, and commute.

## Role Organization

Role and department separation lives inside Sapling, not as separate local Codex projects.

Primary role index:

```text
brain/operating-areas
```

This keeps Chief of Staff, CFO, CIO, and family-office areas distinct while preserving one shared Codex project and one shared chat/work history surface.

## Device-Local Folders

Folders such as these are local to the iMac and should not be used as primary Codex workspaces for shared work:

```text
/Users/kaycschneider/Documents/AI Operations
/Users/kaycschneider/Documents/Chief of Staff
/Users/kaycschneider/Documents/CFO
/Users/kaycschneider/Documents/CIO
/Users/kaycschneider/Documents/Myself Reneweed
/Users/kaycschneider/Documents/Private Lending - KF Capital
/Users/kaycschneider/Documents/Real Estate - Kai Grey Ventures
/Users/kaycschneider/Documents/Trust - Panthera Grey Holdings
```

They may remain useful as local references or temporary staging areas, but shared Codex work should start from the VPS project.
