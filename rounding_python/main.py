from rounds import bjm_round_down, bjm_round_half_up, bjm_round_half_down


def print_result(method, result, expected):
    passed = '\u2714\ufe0f'
    if result != expected:
        failed = '\u274c'
        print(f'{method} => {result} {failed} (expected {expected})')
        return False
    print(f'{method} => {result:.4f} {passed}')
    return True


# def round_to_four_decimals(value):
#     # Multiplie la valeur par 10000, la transforme en entier et la divise par 10000 pour garder 4 décimales
#     temp_value = int(value * 10000) / 10000.0
#     # Formatte la valeur pour s'assurer qu'elle a toujours 4 décimales
#     formatted_value = f"{temp_value:.4f}"
#     return float(formatted_value)

# def round_to_four_decimals_with_decimal(value):
#     # Multiplie la valeur par 10000, la transforme en entier et la divise par 10000 pour garder 4 décimales
#     temp_value = int(value * 10000) / 10000.0
#     # Formatte la valeur pour s'assurer qu'elle a toujours 4 décimales
#     formatted_value = f"{temp_value:.4f}"
#     return float(formatted_value)


def round_to_four_decimals_with_decimal(value):
    # Convertir la valeur en chaîne de caractères
    value_str = str(value)
    # Vérifier si la valeur a plus de quatre décimales
    if '.' in value_str and len(value_str.split('.')[1]) > 4:
        # slice
        return float(value_str[:value_str.find('.') + 5])
    else:
        return value


def execute_value_chf_and_decimals(value_chf, expected, decimals, n):
    print('---------------------------------------------------')
    print(f'CAS DE TEST {n} | montant_chf: {value_chf} | decimals: {decimals}')
    print('---------------------------------------------------')

    bjm_round_down_val = bjm_round_down(value_chf, decimals)
    print_result('bjm_round_down_val', bjm_round_down_val, expected)

    bjm_round_half_up_val = bjm_round_half_up(value_chf, decimals)
    print_result('bjm_round_half_up_val', bjm_round_half_up_val, expected)

    bjm_round_half_down_val = bjm_round_half_down(value_chf, decimals)
    print_result('bjm_round_half_down_val', bjm_round_half_down_val, expected)

    rounded_to_4_decimal = round_to_four_decimals_with_decimal(value_chf)
    print_result('rounded_to_4_decimal', rounded_to_4_decimal, expected)


def execute_round_to_four_decimals_with_decimal(value_chf, expected, decimals, n, format_str):
    print('---------------------------------------------------')
    print(f'CAS DE TEST {n} | montant_chf: {format_str.format(value_chf)} | decimals: {decimals} | expected: {expected:.4f}')
    print('---------------------------------------------------')
    rounded_to_4_decimal = round_to_four_decimals_with_decimal(value_chf)
    return print_result('rounded_to_4_decimal', rounded_to_4_decimal, expected)


# print('---------------------------------------------------')
# print(f'Problème de python: 0.0096*10000={0.0096*10000} ')
# execute_value_chf_and_decimals(0.0096, 0.0096, 4, 1)
# execute_value_chf_and_decimals(0.0095,0.0095, 4, 2)
# execute_value_chf_and_decimals(0.0094, 0.0094, 4, 3)
# execute_value_chf_and_decimals(0.009601, 0.0096, 4, 4)
# execute_value_chf_and_decimals(0.00967,0.0096, 4, 5)
# execute_value_chf_and_decimals(0.009501, 0.0095, 4, 6)
# execute_value_chf_and_decimals(0.009401, 0.0094, 4, 7)
# execute_value_chf_and_decimals(0.00965,0.0096, 4, 8)
#
# print('---------------------------------------------------')
# print('---TEST WITH ALL VALUES BETWEEN 0 and 1 6 DEC------')
# print('---------------------------------------------------')

# val = 0.000001
# increment = 0.000001
# nb_failed_tests = 0
# test_case_id = 1
# iterations = 999999
# format_str = "{:.6f}"
#
# for _ in range(iterations):
#     result = execute_round_to_four_decimals_with_decimal(val, float(str(val)[0:6]), 4, test_case_id, format_str)
#     if not result:
#         nb_failed_tests += 1
#
#     val += increment
#     test_case_id += 1
#
#
# print(f'Nb of tests done: {test_case_id-1}')
# print(f'Nb of tests failed: {nb_failed_tests}')


print('---------------------------------------------------')
print('---TEST WITH ALL VALUES BETWEEN 0 and 1 5 DEC------')
print('---------------------------------------------------')

val = 0.00001
increment = 0.00001
nb_failed_tests = 0
test_case_id = 1
iterations = 99999
format_str = "{:.5f}"

for _ in range(iterations):
    result = execute_round_to_four_decimals_with_decimal(val, float(str(val)[0:6]), 4, test_case_id, format_str)
    if not result:
        nb_failed_tests += 1

    val += increment
    test_case_id += 1


print(f'Nb of tests done: {test_case_id-1}')
print(f'Nb of tests failed: {nb_failed_tests}')
