#uing type function and name attribute for objective coding
class vehicle:
    def name(self,name):
        return name

v=vehicle()
print(type(v).__name__)
