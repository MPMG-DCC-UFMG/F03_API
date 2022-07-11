import time, json
from locust import HttpUser, task, between
from numpy.random import choice

class TestBancoPrecos(HttpUser):
    wait_time = between(1, 5)

    @task(5)
    def get_descriptions(self):
        values = ["gasolina", "amoxilina", "papel", "alcool", "antibiotico"]
        description = str(choice(values))
        self.client.get(
            f"api/items/autocomplete/?desc={description}")#, name="/items/autocomplete")
        
    @task(5)
    def list_items_sample(self):
        
        payload = {
            "city": [
                "BELO HORIZONTE"
            ],
            "year": [
                "2014", "2015", "2016", "2017"
            ],
            "description": "gasolina"
        }        
        headers = {'content-type': 'application/json'}
        
        values = [10, 100, 1000]
        size = int(choice(values))
        self.client.post(f"api/items/sample/?page=0&size={size}&sort=id_item&order=desc", data=json.dumps(payload), headers=headers)#, name = "/items/sample")
        

    @task(1)
    def get_aggregate(self):
        self.client.get(
            "api/charts/?limit=100&offset=0&order=desc&description=GASOLINA%20COMUM&unit_measure=litro", name="/charts")


    @task(1)
    def princing_by_description(self):

        payload = {
            "group_by_description": True,
            "group_by_unit_metric": True,
            "group_by_year": True,
            "description": "gasolina"
        }
        headers = {'content-type': 'application/json'}
        
        self.client.post(f"api/pricing/?page=0&size=100&sort=id_item&order=desc", data=json.dumps(payload), headers=headers, 
                        name="/pricing")


    
