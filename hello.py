#!/usr/bin/env python3
#http://localhost:8080/login.py

import os
import json

print("Content type: application/json")
print()
#print(json.dumps(dict(os.environ), indent=2))
print(f"<p>HTTP_USER_AGENT = {os.environ['HTTP_USER_AGENT']} </p>")