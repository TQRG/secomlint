from enum import Enum

class Message(Enum):
    MSG1 = """vuln-fix: Sanitize URLs to reject malicious data (CVE-2012-0036)

Protocols (IMAP, POP3 and SMTP) that use the path part of a URL in a
decoded manner now use the new Curl_urldecode() function to reject URLs
with embedded control codes (anything that is or decodes to a byte value
less than 32).
URLs containing such codes could easily otherwise be used to do harm and
allow users to do unintended actions with otherwise innocent tools and
applications.
Like for example using a URL like pop3://pop3.example.com/1%0d%0aDELE%201
when the app wants a URL to get a mail and instead this would delete one.

Weakness: CWE-89
Severity: High
Detection: Manual
Report: https://curl.se/docs/CVE-2012-0036.html

Reported-by: Dan Fandrich
Signed-off-by: Daniel Stenberg (daniel@haxx.se)

Resolves: #17940
See also: #17937"""

    MSG2 = """vuln-fix: Sanitize URLs to reject malicious data (CVE-2012-0036)

Weakness: CWE-89
Severity: High
Detection: Manual
Report: https://curl.se/docs/CVE-2012-0036.html

Reported-by: Dan Fandrich
Signed-off-by: Daniel Stenberg (daniel@haxx.se)

Resolves: #17940
See also: #17937"""

    MSG3 = """vuln-fix: Sanitize URLs to reject malicious data (CVE-2012-0036)

Reported-by: Dan Fandrich
Signed-off-by: Daniel Stenberg (daniel@haxx.se)

Resolves: #17940
See also: #17937"""