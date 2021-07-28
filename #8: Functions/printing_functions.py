def print_models(unprinted_designs, completed_models):
    """
    Симулювати друк кожного креслення, доки всі не зкінчаться.
    Перенести кожен рисунок до completed_models після друку.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printig model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Показати всі готові моделі."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
