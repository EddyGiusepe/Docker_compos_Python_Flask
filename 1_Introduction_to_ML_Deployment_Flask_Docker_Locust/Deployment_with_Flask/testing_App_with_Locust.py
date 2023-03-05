from locust import HttpUser, task, constant_throughput

# Definimos solicitação json de teste
test_application = {
        "Term": 84,
        "NoEmp": 5,
        "CreateJob": 0,
        "RetainedJob": 5,
        "longitude": -77.9221,
        "latitude": 35.3664,
        "GrAppv": 1500000.0,
        "SBA_Appv": 1275000.0,
        "is_new": True,
        "FranchiseCode": "0",
        "UrbanRural": 1,
        "City": "Other",
        "State": "NC",
        "Bank": "BBCN BANK",
        "BankState": "CA",
        "RevLineCr": "N",
        "naics_first_two": "45",
        "same_state": False,
    }

class BankLoan(HttpUser):
    # Significa que um usuário enviará 1 solicitação por segundo
    wait_time = constant_throughput(1)
    
    # Tarefa a ser executada (enviar dados e obter resposta)
    @task
    def predict(self):
        self.client.post(
            "/predict",
            json=test_application,
            timeout=1,
        )
