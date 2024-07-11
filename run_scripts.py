import subprocess

def run_data_processing():
    print("Running data_processing.py")
    subprocess.run(['python', 'src/data_processing.py'])

def run_hyperparameters():
    print("Running hyperparameters.py")
    subprocess.run(['python', 'src/hyperparameters.py'])

def run_modeling():
    print("Running modeling.py")
    subprocess.run(['python', 'src/modeling.py'])

def run_metrics():
    print("Running metrics.py")
    subprocess.run(['python', 'src/metrics.py'])

def run_visualization():
    print("Running visualization.py")
    subprocess.run(['python', 'src/visualization.py'])

def run_main_script():
    print("Running main_script.py")
    subprocess.run(['python', 'src/main_script.py'])

if __name__ == "__main__":
    run_data_processing()
    run_hyperparameters()
    run_modeling()
    run_metrics()
    run_visualization()
    run_main_script()
