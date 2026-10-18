# ci-local-environment-variable-mismatch
This example demonstrates a common scenario where code works perfectly on a developer's local machine but fails in a Continuous Integration (CI) environment. The Python script attempts to read a critical configuration value (simulated as an API key) from an environment variable. If this variable is not set, the script simulates a CI build failure b
