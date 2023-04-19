import click
import subprocess

import openai

TEMPLATE = """Generate a commit message with the following structure 

vuln-fix: <header/subject> (<Vuln-ID>)

<body>
# (what) describe the vulnerability/problem
# (why) describe its impact
# (how) describe the patch/fix

Weakness: <Weakness Name or CWE-ID>
Severity: <Low, Medium, High and Critical>
CVSS: <Numerical representation (0-10) of severity>
Detection: <Detection Method>
Report: <Report Link>
Introduced in: <Commit Hash>

Reported-by: <Name> (<Contact>)
Reviewed-by: <Name> (<Contact>)
Co-authored-by: <Name> (<Contact>)
Signed-off-by: <Name> (<Contact>)

Bug-tracker: <Bug-tracker Link>
OR
Resolves: <Issue/PR No.>
See also: <Issue/PR No.>

for the code changes below:

"""

class Generation:
    def __init__(self, key) -> None:
        openai.api_key = key
        git_command = subprocess.run(["git", "show", "HEAD"], 
                                  stdout=subprocess.PIPE)
        self.code_changes = 'diff --git' + 'diff --git'.join(git_command.stdout.decode("utf-8").split('diff --git')[1::])
        self.prompt = TEMPLATE + self.code_changes
        
    def run(self):
        self.message = """vuln-fix: Sanitize HTML content in calendar event name function (CVE-2020-12345)

# (what) A vulnerability was discovered in the calendar event name function, which could allow for HTML injection.
# (why) If exploited, this vulnerability would allow an attacker to inject malicious HTML content into the application.
# (how) The function was modified to remove HTML sanitization and instead rely on the prop type enforcement.

Weakness: Improper Output Neutralization for Script Injection (CWE-79)
Severity: Medium
CVSS: 5.5
Detection: Code Review
Report: None
Introduced in: 0d1f1b095

Reported-by: John Doe (john.doe@example.com)
Reviewed-by: Jane Doe (jane.doe@example.com)
Co-authored-by: Jack Doe (jack.doe@example.com)
Signed-off-by: Bob Doe (bob.doe@example.com)

Bug-tracker: None
OR
Resolves: None
See also: None"""
        
        # openai.Completion.create(model="text-davinci-003", 
        #                              prompt=self.prompt, 
        #                              temperature=0.7, 
        #                              max_tokens=500)['choices'][0]['text']
        
    def print(self):
        click.echo(click.style(self.message, fg='yellow'))

    def usage(self):
        click.echo(click.style(self.message, fg='yellow'))
        click.echo("""
Would you like to use this commit message? 
(Y - Yes (default); N - No; C - Yes, but I want to change it.)""")
        self.response = input("Enter your answer (Y/N/C): ")
        
    def save(self):
        git_command = subprocess.run(["git", "commit", "--amend", self.message], 
                                  stdout=subprocess.PIPE)
        print(git_command.stdout)