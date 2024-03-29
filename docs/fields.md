# Details

This convention was inferred from merging different sources about creating better commits messages and from empirical research performed upon security commit messages.

```
<type>: <header/subject> (<Vuln-ID>)

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
```

* Atomic changes: Commit each patch as a separate change [[4](https://www.freshconsulting.com/insights/blog/atomic-commits/)].
* A `<type>` should be assigned to each commit [[1](https://www.conventionalcommits.org/en/v1.0.0/)]. Our suggestion is the usage of `vuln-fix` to specify the fix is related to a vulnerability.
* `<header/subject>`: ~50 chars (max 72 chars); capitalized; no period in the end; imperative form.
* `<Vuln-ID>`: When available; e.g., CVE, OSV, GHSA, and other formats.
* `<body>`: Describe what (problem), why (impact) and how (patch). ~75 words (25 words per point).
* `Weakness:` Name or CWE-ID.
* `Severity:` Severity of the issue. Values: Low, Medium, High, Critical
* `CVSS:` Numerical (0-10) representation of the severity of a security vulnerability (Common Vulnerability Scoring System).
* `Detection:` Detection method. Values: Tool, Manual, Exploit, etc.
* `Report:` Link for vulnerability report.
* `Introduced in:` Commit hash from the commit that introduced the vulnerability.
* `Reported-by:` Name/Contact of the person that reported the issue.
* `Reviewed-by:` Name/contact of the person that reviewed the patch.
* `Co-authored-by:` Name/contact of the person that co-authored the fix for the issue.
* `Signed-off-by:` Name/Contact of the person that closed the issue.
* `Bug-tracker:` Link to the issue in an external bug-tracker.
* `Resolves.. See also:` When GitHub is used to manage security fixes.
  
In the future, we plan to infer the importance of each field and determine different levels of compliance. For now, we believe the following set of fields is the minimum required to detect and classify security commits succesfully: `<type>`, `<header/subject>`, `<body>`, `Severity`, `Weakness`, `Signed-off-by`

### References
[[1](https://www.conventionalcommits.org/en/v1.0.0/)] Conventional Commits V1.0.0 
<br>[[2](https://chris.beams.io/posts/git-commit/)] How to Write a Git Commit Message by Chris Beams 
<br>[[3](https://gist.github.com/matthewhudson/1475276)] A good commit message looks like this by Linus Torvalds 
<br>[[4](https://www.freshconsulting.com/insights/blog/atomic-commits/)] Developer Tip: Keep Your Commits “Atomic” by Sean Patterson 