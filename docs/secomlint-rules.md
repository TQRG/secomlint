# Rules

Rules are made up by a name and a configuration array. The configuration array contains:

* **active** ``[0,1]``: `0` disables the rule; `1` enables the rule. By default it is enabled.
* **type** ``[0,1]``: `0` reports an warning; `1` reports an error. 
* **value**: value to use for the rule.

#### header-max-length
* **condition**: `header` has `value` or less characters
* **type**: 0 (warning)
* **value**: 50

#### header-is-not-empty
* **condition**: `header` has more than `value` characters
* **type**: 1 (error)
* **value**: 0


#### header-starts-with-type

* **condition**: `header` starts with `<type>` 
* **type**: 1 (error)
* **value**: `vuln-fix`

#### header-ends-with-vuln-id

* **condition**: `header` ends with `<vuln-id>` 
* **type**: 0 (warning)
* **value**: `(CVE|GHSA|OSV).*`

