from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def load_reclamos(self):
        self.client.get("/api/reclamos/")

    @task
    def load_quejas(self):
        self.client.get("/api/quejas/")

    @task
    def load_solicituds(self):
        self.client.get("/api/solicitudes/")