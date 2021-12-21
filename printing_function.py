#printing model module
def print_models(unprinted_designs, completed_models):
    """
    simulate printing each design until none is left
    move printed designs to completed models
    """
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"the {current_design} is beeing printed ")
        completed_models.append(current_design)