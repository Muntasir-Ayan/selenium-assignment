import subprocess
import sys

def run_script(script_name):
    """Run a Python script using subprocess."""
    try:
        # Ensure the subprocess uses the Python interpreter from the virtual environment
        result = subprocess.run([sys.executable, script_name], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully ran {script_name}")
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e.stderr.decode()}")

def main():
    print("H1 testing is running....")
    run_script('h1Test.py')

    print("HTML testing is running....")
    run_script('htmlTest.py')

    print("alt testing is running....")
    run_script('altTest.py')

    print("url testing is running....")
    run_script('url_status_code_test.py')

    print("Currency testing is running....")
    run_script('currency.py')

    print("Script testing is running....")
    run_script('script.py')

    print("Running successful.")

if __name__ == "__main__":
    main()
