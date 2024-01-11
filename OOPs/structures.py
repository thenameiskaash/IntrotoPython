class Apple:
    color = ""
    flavor = ""

jonagold = Apple() #Instances 

jonagold.color = 'red'
jonagold.flavor = 'sweet'

print(jonagold.color.upper())
if jonagold.flavor == "sweet":
    jonagold = jonagold.color