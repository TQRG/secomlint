# Compliance Audit Checklist

Before you submit your patch, you should check the following list to ensure your message is in compliance with SECOM.

<table>
	<tr >
	    <td rowspan="3">Header</td>
	    <td>type</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
	<tr>
	    <td>header/subject</td>
	    <td>Did you summarize the patch changes in ~50 chars?</td>
        <td>Mandatory</td>
	</tr>
    	<tr>
	    <td>Vuln-ID</td>
	    <td>Is there a vulnerability ID available? Did you include it between parentheses at the end of the header?</td>
        <td>Optional/When Available</td>
	</tr>
	<tr >
	    <td rowspan="3">Body</td>
	    <td>what</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr >
	    <td>why</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr >
	    <td>how</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td rowspan="6">Metadata</td>
	    <td>Weakness</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Severity</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>CVSS</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Detection</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Report</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Introduced in</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td rowspan="2">Contacts</td>
	    <td>Reported-by</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Signed-off-by</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td rowspan="1">Bug-Tracker</td>
	    <td>Reported-by</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
</table>

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
Signed-off-by: <Name> (<Contact>)

Bug-tracker: <Bug-tracker Link>
OR
Resolves: <Issue/PR No.>
See also: <Issue/PR No.>
```

Rules:

* Atomic changes: Commit each patch as a separate change [4].

Fields:
* A `<type>` should be assigned to each commit [1]. Our suggestion is the usage of `vuln-fix to specify the fix is related to a vulnerability.
* `<header/subject>`: ~50 chars (max 72 chars); capitalized; no period in the end; imperative form.
* `<Vuln-ID>`: When available; e.g., CVE, OSV, GHSA, and other formats.
* `<body>`: Describe what (problem), why (impact) and how (patch). ~75 words (25 words per point).
* Weakness: Name or CWE-ID.
* Severity: Severity of the issue. Values: Low, Medium, High, Critical
* CVSS: Numerical (0-10) representation of the severity of a security vulnerability (Common Vulnerability Scoring System).
* Detection: Detection method. Values: Tool, Manual, Exploit, etc.
* Report: Link for vulnerability report.
* Introduced in: Commit hash from the commit that introduced the vulnerability.
* Reported-by: Name/Contact of the person that reported the issue.
* Signed-off-by: Name/Contact of the person that closed the issue.
* Bug-tracker: Link to the issue in an external bug-tracker.
* Resolves.. See also: When GitHub is used to manage security fixes.
  
In the future, we plan to infer the importance of each field and determine different levels of compliance. For now, we believe the following set of fields is the minimum required to detect and classify security commits succesfully: `<type>`, `<header/subject>`, `<Vuln-ID>`, `<body>`, Severity, Weakness.
