#!/usr/bin/env python3
"""Quick connectivity test for DashScope Anthropic-compatible endpoint."""
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv(override=True)

if os.getenv("ANTHROPIC_BASE_URL"):
    os.environ.pop("ANTHROPIC_AUTH_TOKEN", None)

print(f"ANTHROPIC_BASE_URL = {os.getenv('ANTHROPIC_BASE_URL')}")
print(f"MODEL_ID           = {os.getenv('MODEL_ID')}")
key = os.getenv("ANTHROPIC_API_KEY", "")
print(f"ANTHROPIC_API_KEY  = {key[:8]}...")
print()

client = Anthropic(base_url=os.getenv("ANTHROPIC_BASE_URL"))
response = client.messages.create(
    model=os.environ["MODEL_ID"],
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print("=== Response ===")
for block in response.content:
    if hasattr(block, "text"):
        print(block.text)
print()
print(f"stop_reason = {response.stop_reason}")
print(f"content blocks = {[type(b).__name__ for b in response.content]}")
print()
print("=== Connectivity test PASSED ===")
