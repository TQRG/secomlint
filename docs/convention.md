# SECOM

Sometimes commit messages generated to document the patches of known vulnerabilities are either poorly documented or do not seem to be security-related. 

SECOM is a convention for making security commit messages more readable and structured. It organizes several bits of security-relevant information from vulnerabilities and their respective patches for security engineers, maintainers or users. 

```markup
1   vuln-fix: subject/header containing summary of changes in ~50 characters (Vuln-ID)
2
3   Detailed explanation of the subject/header in ~75 words.
4   (what) Explain the security issue(s) that this commit is patching.
5   (why) Focus on why this patch is important and its impact.
6   (how) Describe how the issue is patched.
7
8   [For Each Weakness in Weaknesses:]
9   Weakness: weakness identification or CWE-ID.
10  Severity: severity of the  issue (Low, Medium, High, Critical).
11  CVSS: numerical representation (0-10) of the vulnerability severity.
12  Detection: method used to detect the issue (Tool, Manual, Exploit).
13  Report: http://link-to-report/
14  Introduced in: commit hash.
15  [End]
16
17  Reported-by: reporter name 1 <reporter-email-1@host.com>
18  Reported-by: reporter name 2 <reporter-email-2@host.com>
19  Signed-off-by: your name <your-email@yourhost.com>
20
21  [If you use an issue tracker, add reference to it here:]
22  [if external issue tracker:]
23  Bug-tracker: https://link-to-bug-tracker/id
24
25  [if github used as issue tracker:]
26  Resolves: #123
27  See also: #456, #789
```

Our research team confirmed that extracting security-related information from security commit messages may be difficult sometimes which shows the importance of best practices and templates to create better security commit messages. Here are some of the examples the team found while looking at 
the data:

<img src="./assets/poorly_doc.png" width="600">
<img src="./assets/unrelated_to_sec.png" width="600">


