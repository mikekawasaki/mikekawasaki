# Preview Documentation

I use [grip](https://github.com/joeyespo/grip) to preview the GitHub profile README locally with dark mode support.

## Prerequisites

- [uv](https://github.com/astral-sh/uv) must be installed.

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
