import time
from locust import HttpUser, task, between
from numpy.random import choice

class TestBancoPrecos(HttpUser):
    wait_time = between(1, 5)

    @task(5)
    def item_search(self):
        values = ["gasolina", "amoxilina", "papel", "alcool", "antibiotico"]
        description=str(choice(values))
        self.client.get(f"/api/items/?limit=10&offset=0&order=desc&description={description}",
                        name="/items/description=[...]")

    @task(5)
    def item_sample(self):
        self.client.get(f"/api/items/sample/?limit=10&offset=0&order=desc",
                        name="/items/sample")
        

    @task(5)
    def item_match(self):
        self.client.get(f"/api/items/match/?limit=10&offset=0&order=desc", name="/items/match")

    @task(5)
    def item_single(self):
        self.client.get(f"/api/items/1")

    @task(5)
    def group_by_description_wo_noise(self):
        values = ["gasolina", "amoxilina", "papel", "alcool", "antibiotico"]
        description=str(choice(values))
        self.client.get(f"/api/groups/?limit=15&offset=0&order=desc&first_token={description}&noise=false",
                        name="/api/groups/first_token=[...]&noise=false")

    @task(5)
    def group_by_description_w_noise(self):
        values = ["gasolina", "amoxilina", "papel", "alcool", "antibiotico"]
        description=str(choice(values))
        self.client.get(f"/api/groups/?limit=15&offset=0&order=desc&first_token={description}&noise=false",
                        name="/api/groups/first_token=[...]&noise=true")

    @task(1)
    def princing_by_description(self):
        values = ["gasolina", "amoxilina", "papel", "alcool", "antibiotico"]
        description=str(choice(values))
        self.client.get(f"/api/pricing/?limit=10&offset=0&sort=count&order=desc&description={description}",
                        name="/api/pricing/?limit=10&offset=0&sort=count&order=desc&description=[...]")


    
