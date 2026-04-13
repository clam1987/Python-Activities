def getAge(data):
    print(data["age"] + 10)
    return

child = {
  "age": 10
}

def investmentGrowth(data):
    print(data["initialInvestment"] * 1.15)
    return

investor = {
  "name": 'Cash Saver',
  "investment": {
    "initialInvestment": 5000,
    "investmentGrowth": investmentGrowth,
  },
};

getAge(child)
investor["investment"]["investmentGrowth"](investor["investment"])