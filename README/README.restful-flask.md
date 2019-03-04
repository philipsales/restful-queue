
## Prerequisites
Tested on the following

| Dependencies | Versions |
| ------------ | -------- |
| Python       | 3.6.2    |
| Virtualenv   | 15.1.0   |
| Flask        | x.x.x    |
| Swagger      | x.x.x    |

## Getting started 
1. Create Python virtualenv
    ```bash
    cd ~ 
    virtualenv --python=python3.6 python_env 
    ```
1. Activate virtualenv
    ```bash
    cd ~ 
    source src_venv/bin/activate
    ```
1. Install python dependenices 
    ```bash
    pip install requirements.txt
    ```

## Running the Basic 
1. Run resful API 
    ```bash
    cd src 
    python app.py 
    ```
    
1. Go swagger url
    ```bash
    http://localhost:5000/basepath/ui/
    ```
