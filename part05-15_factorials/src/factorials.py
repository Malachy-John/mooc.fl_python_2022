def factorials(n: int):
    number_dict = {}
    facts = 1
    total = 1
    for i in range(1, n+1):
        

        number_dict[i] = i * facts


        print(f"{i} * {facts}:")
        

        
        facts *= i
    return number_dict

        





if __name__ == "__main__":
    factorials(5)