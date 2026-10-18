import os
import sys

def run_application_logic():
    """
    Simulates a core part of an application that relies on an environment variable.
    This is where a 'works on my machine' vs. 'fails in CI' scenario often occurs.
    """
    # The variable that might be set locally but forgotten or misconfigured in CI
    api_key = os.getenv("MY_SECRET_API_KEY") 

    if api_key:
        print("Application started successfully!")
        # In a real app, this key would be used for API calls or sensitive operations.
        print(f"Using API Key (masked): {api_key[:4]}...{api_key[-4:]}") 
        print("Performing secure operation with the API key...")
        # Simulate some work that depends on the key being present
        # For example, connecting to a database, calling an external service, etc.
        print("Operation completed successfully.")
        return True
    else:
        # This block simulates the CI failure scenario
        print("ERROR: MY_SECRET_API_KEY environment variable is not set.")
        print("This often causes builds to fail in CI environments if secrets ")
        print("or configuration variables are not properly injected.")
        print("Please ensure 'MY_SECRET_API_KEY' is configured in your CI/CD pipeline ")
        print("or local environment.")
        return False

if __name__ == "__main__":
    print("--- Starting Application Simulation ---")
    success = run_application_logic()
    print("--- Application Simulation Finished ---")

    if not success:
        # In a real CI pipeline, a non-zero exit code would mark the build as failed.
        sys.exit(1) # Simulate CI failure by exiting with an error code
