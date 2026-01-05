from grip import serve
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description='Preview README with Grip')
parser.add_argument('--theme', choices=['light', 'dark'], default='dark', help='Theme to use (light or dark)')
args = parser.parse_args()

serve(
    path='README.md',
    theme=args.theme,
    password=os.getenv('GITHUB_TOKEN'),
    render_inline=True,
)
