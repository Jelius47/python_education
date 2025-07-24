class NetworkService:
    def __init__(self):
        self.components = {}
    
    def add(self, key: str ,value: str):
            self.components[key] = value

    def show(self):
         print(self.components)


    # class that will be used to instansiate our network service
class NetworkServiceBuilde:
     def __init__(self):
          self._service = NetworkService()

     def add_target_url(self,url:str):
          self._service.add("URL",url)
    
     def add_auth(self,auth:str):
          self._service.add("Authorization",auth)
     def add_caching(self,cache: int):
          self._service.add("Cache-Control",cache)

     def build(self)->NetworkService:
          service = self._service
          self._service = NetworkService()
          return service



