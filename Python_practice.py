voting_data=[]
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.insert(1,{"county": "El Paso", "registered_voters": 461149})
print(voting_data)
voting_data.pop(0)
print(voting_data[1])
voting_data[1]['county']= 'Jefferson'
voting_data[1]['registered_voters']= 432438
voting_data[2]['county']= 'Denver'
voting_data[2]['registered_voters']= 463353
print(voting_data)
voting_data.insert(3,{"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)