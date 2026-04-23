from dotenv import load_dotenv
import os
load_dotenv()

gemini = os.getenv("GOOGLE_API_KEY")
github = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
user   = os.getenv("GITHUB_USERNAME")

print(f"✅ Gemini key  : {gemini[:8]}...hidden")
print(f"✅ GitHub token: {github[:8]}...hidden")
print(f"✅ GitHub user : {user}")
