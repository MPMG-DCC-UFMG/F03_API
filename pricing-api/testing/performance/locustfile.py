import time
from locust import HttpUser, task, between
from numpy.random import choice

class TestBancoPrecos(HttpUser):
    wait_time = between(1, 5)
    # termos mais frequentes na base, ie, ocorrem em mais de 10.000 itens
    most_frequent_tokens = ["adaptador", "agua", "agulha", "alcool", "barra",
                            "biscoito", "bola", "bomba", "broca", "bucha",
                            "cabo", "camara", "caneta", "cartucho", "chave",
                            "cola", "curva", "disco", "disjuntor", "envelope",
                            "escova", "ficha", "filtro", "fio", "fita",
                            "grampo", "item", "joelho", "jogo", "lamina",
                            "lampada", "leite", "livro", "locacao", "luva",
                            "mangueira", "oleo", "pao", "papel", "parafuso",
                            "pasta", "pincel", "placa", "pneu", "porta",
                            "prego", "prestacao", "registro", "rolamento",
                            "saco", "seringa", "servico", "sonda", "suporte",
                            "te", "tesoura", "tinta", "torneira", "tubo",
                            "valvula"]
    
    ids = [3, 8, 10, 13, 18, 24, 28, 30, 38, 41, 45, 51, 52, 53, 54, 55, 57, 60,
           61, 64, 65, 70, 73, 75, 76, 79, 80, 83, 84, 86, 88, 90, 91, 93, 96,
           104, 105, 113, 115, 117, ]



    @task(5)
    def item_search(self):
        description=str(choice(TestBancoPrecos.most_frequent_tokens))
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
        id_selected=str(choice(TestBancoPrecos.ids))
        self.client.get(f"/api/items/{id_selected}", name="/api/items/:id")

    @task(5)
    def group_by_description_wo_noise(self):
        description=str(choice(TestBancoPrecos.most_frequent_tokens))
        self.client.get(f"/api/groups/?limit=15&offset=0&order=desc&first_token={description}&noise=false",
                        name="/api/groups/first_token=[...]&noise=false")

    @task(5)
    def group_by_description_w_noise(self):
        description=str(choice(TestBancoPrecos.most_frequent_tokens))
        self.client.get(f"/api/groups/?limit=15&offset=0&order=desc&first_token={description}&noise=false",
                        name="/api/groups/first_token=[...]&noise=true")

    @task(1)
    def princing_by_description(self):
        description=str(choice(TestBancoPrecos.most_frequent_tokens))
        self.client.get(f"/api/pricing/?limit=10&offset=0&sort=count&order=desc&description={description}",
                        name="/api/pricing/?limit=10&offset=0&sort=count&order=desc&description=[...]")


    
