from rounds import bjm_round_down, bjm_round_half_up, bjm_round_half_down


def print_result(method, result, expected):
    passed = '\u2714\ufe0f'
    if result != expected:
        passed = '\u274c'
    print(f'{method} => {result} {passed}')


def round_to_four_decimals(value):
    # Multiplie la valeur par 10000, la transforme en entier et la divise par 10000 pour garder 4 décimales
    temp_value = int(value * 10000) / 10000.0
    # Formatte la valeur pour s'assurer qu'elle a toujours 4 décimales
    formatted_value = f"{temp_value:.4f}"
    return float(formatted_value)


def execute_value_chf_and_decimals(value_chf, expected, decimals, n):
    print('---------------------------------------------------')
    print(f'CAS DE TEST {n}:')
    print(f'montant_chf: {value_chf}')
    print(f'decimals: {decimals}')
    print('---------------------------------------------------')

    bjm_round_down_val = bjm_round_down(value_chf, decimals)
    print_result('bjm_round_down_val', bjm_round_down_val, expected)

    bjm_round_half_up_val = bjm_round_half_up(value_chf, decimals)
    print_result('bjm_round_half_up_val', bjm_round_half_up_val, expected)

    bjm_round_half_down_val = bjm_round_half_down(value_chf, decimals)
    print_result('bjm_round_half_down_val', bjm_round_half_down_val, expected)

    rounded_to_4 = round_to_four_decimals(value_chf)
    print_result('rounded_value', rounded_to_4, expected)


print('---------------------------------------------------')
print(f'Problème de python: 0.0096*10000={0.0096*10000} ')
execute_value_chf_and_decimals(0.0096, 0.0096, 4, 1)
execute_value_chf_and_decimals(0.0095,0.0095, 4, 2)
execute_value_chf_and_decimals(0.0094, 0.0094, 4, 3)
execute_value_chf_and_decimals(0.009601, 0.0096, 4, 4)
execute_value_chf_and_decimals(0.00967,0.0096, 4, 5)
# aussi testé et fonctionnel:
# execute_value_chf_and_decimals(0.009501, 4, 4)
# execute_value_chf_and_decimals(0.009401, 4, 4)
