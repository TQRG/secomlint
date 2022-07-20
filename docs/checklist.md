# Compliance Audit Checklist

Before you submit your patch, you should check the following list to ensure your message is in compliance with SECOM.

<table>
	<tr >
	    <td rowspan="4">Header</td>
	    <td>type</td>
	    <td>Did you set the type of the commit as "vuln-fix" at the beginning of the header?</td>
	    <td>Mandatory</td>
	</tr>
	<tr>
	    <td>header/subject</td>
	    <td>Did you summarize the patch changes?</td>
        <td>Mandatory</td>
	</tr>
		<tr>
	    <td>header/subject</td>
	    <td>Did you summarize the patch changes within ~50 chars?</td>
        <td>Optional</td>
	</tr>
    	<tr>
	    <td>Vuln-ID</td>
	    <td>Is there a vulnerability ID available? Did you include it between parentheses at the end of the header?</td>
        <td>Optional</td>
	</tr>
	<tr >
	    <td rowspan="4">Body</td>
	    <td>what</td>
	    <td>Describe the vulnerability or problem in the first sentence of the body.</td>
	    <td>Mandatory</td>
	</tr>
    <tr >
	    <td>why</td>
	    <td>Describe the impact of the vulnerability in the second sentence of the body.</td>
	    <td>Mandatory</td>
	</tr>
    <tr >
	    <td>how</td>
	    <td>Describe how the vulnerability was fixed in the third sentence.</td>
	    <td>Mandatory</td>
	</tr>
	<tr>
	    <td>*</td>
	    <td>Did you describe the what, why and how within ~75 words (~25 words per section)?</td>
	    <td>Optional</td>
	</tr>
    <tr>
	    <td rowspan="6">Metadata</td>
	    <td>Weakness</td>
	    <td>Can this vulnerability be classified with a type? If so, add it to the metadata section.</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Severity</td>
	    <td>Were you able to infer a severity (Low, Medium, High, Critical) for this vulnerability? If so, add it to the metadata section.</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>CVSS</td>
	    <td>Calculate the numerical representation of the severity through the Common Vulnerability Scoring System calculator (https://www.first.org/cvss/calculator/3.0).</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td>Detection</td>
	    <td>How did you find this vulnerability? (e.g., Tool, Manual, Exploit) </td>
	    <td>Optional</td>
	</tr>
    <tr>
	    <td>Report</td>
	    <td>Is there a link for the vulnerability report available? If so, include it.</td>
	    <td>Optional</td>
	</tr>
    <tr>
	    <td>Introduced in</td>
	    <td>Include the commit hash from the commit where the vulnerability was introcued.</td>
	    <td>Optional</td>
	</tr>
    <tr>
	    <td rowspan="2">Contacts</td>
	    <td>Reported-by</td>
	    <td>Include the name and/or contact of the person that reported and patched the vulnerability.</td>
	    <td>Optional</td>
	</tr>
    <tr>
	    <td>Signed-off-by</td>
	    <td>Include the name and/or contact of the person that reviewed and accepted the patch.</td>
	    <td>Mandatory</td>
	</tr>
    <tr>
	    <td rowspan="2">Bug-Tracker</td>
	    <td>External Bug-Tracker</td>
	    <td>Include the link to the issues or pull requests in the external bug-tracker.</td>
	    <td>Optional</td>
	</tr>
	<tr>
	    <td>GitHub</td>
	    <td>Include the links for the issues and pull-requests related with the patch.
 		</td>
	    <td>Optional</td>
	</tr>
</table>
