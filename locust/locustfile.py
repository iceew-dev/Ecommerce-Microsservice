from locust import HttpUser, task, between

class EcommerceUser(HttpUser):

    wait_time = between(1, 3)

    @task
    def acessar_produto(self):
        self.client.get("/")