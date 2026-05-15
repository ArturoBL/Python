import os
from dotenv import load_dotenv

'''
Write a .env file with the text:
MYVAR="Secret text"

use load_dotenv() to read the .env file.

or

Set system environment value with:

(linux)
export MYVAR="Secret text"

(Windows CMD temporary)
set MYVAR="Secret text"

(Windows CMD permanent)
setx MYVAR="Secret text"

(Windows powershell temporary)
$env:MYVAR = "Hello"

(Windows powershell permanent)
[Environment]::SetEnvironmentVariable("MY_VAR", "Hello", "User")
[Environment]::SetEnvironmentVariable("MY_VAR", "Hello", "Machine")

'''


load_dotenv()  # Loads variables from .env

key = os.getenv("MYVAR")
print(key)  # Outputs: secret_key_123
