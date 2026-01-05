# Preview Documentation

I use [grip](https://github.com/joeyespo/grip) to preview the GitHub profile README locally with dark mode support.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) must be installed.

## Rate Limiting

If you encounter GitHub API rate limits (60 requests/hour), you can use a Personal Access Token (PAT).

1. [Generate a standard token](https://github.com/settings/tokens) (repo scope usually sufficient, or public_repo for public setup).
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and paste your token:
   ```env
   GITHUB_TOKEN=ghp_...
   ```


## Running the Preview

To start the local preview server:

```bash
uv run preview.py
```

This will automatically open your default browser to the preview page.

## Options

The `preview.py` script supports the following arguments:

- `--theme`: Select the color theme.
    - `dark` (default)
    - `light`

Example:

```bash
uv run preview.py --theme light
```
