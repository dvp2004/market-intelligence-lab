# Public-Repository Data and Secret Policy

## Permitted in the public repository

- code, configuration, contracts, schemas, and documentation;
- synthetic fixtures;
- metadata-only manifests where publication is permitted;
- derived reports that do not reproduce protected raw content or breach provider terms.

## Prohibited in the public repository

- API keys, `.env` files, credentials, tokens, certificates, private keys, or secrets;
- licensed, subscription, or otherwise restricted raw data;
- full copyrighted news, filings, transcripts, or other text unless redistribution is permitted;
- provider data retained or redistributed in breach of source terms;
- personally sensitive information that is not essential to research.

## Required controls

- `.env.example` may contain blank placeholders only.
- `.gitignore` blocks local raw, normalized, private, and generated report directories by default.
- Every potential data publication must record source, license or terms status, redistribution permission, and approval decision.
- Raw data remains local by default. A public manifest must contain metadata only unless explicit permission exists.
- Any suspected secret must be removed locally, rotated where relevant, and kept out of Git history before publishing.

## Enforcement

The bootstrap performs a staged-file path and credential-pattern check before the initial commit. This is not a substitute for source-term review or human judgment.