class dog:
    species="4 legged mammal"
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
dog1=dog("White and Dark Browm","Corgi")
dog2=dog("Black and Golden Brown","German Sheperd")
print("dog1 color:",dog1.color)
print("dog1 breed:",dog1.breed)
print("dog2 color:",dog2.color)
print("dog2 breed:",dog2.breed)