import time
import random
import matplotlib.pyplot as plt
from sorting_algorithms import selection_sort, insertion_sort, merge_sort, shell_sort
from copy import deepcopy


def generate_random_arr(power):
    lst = []
    for _ in range(2**power):
        lst.append(random.randint(0, 1000))
    return lst


def generate_sorted_arr(power):
    lst = []
    for num in range(2**power):
        lst.append(num)
    return lst


def generate_sorted_arr_reversed(power):
    lst = generate_sorted_arr(power)
    return sorted(lst, reverse=True)


def generate_123numbers_arr(power):
    lst = []
    for _ in range(2**power):
        lst.append(random.randint(1,3))
    return lst


def time_shellsort(lst):
    start = time.time()
    comparisons = shell_sort(lst)
    end = time.time()
    working_time = end - start
    return working_time, comparisons


def time_mergesort(lst):
    start = time.time()
    comparisons = merge_sort(lst)
    end = time.time()
    working_time = end - start
    return working_time, comparisons


def time_selectionsort(lst):
    start = time.time()
    comparisons = selection_sort(lst)
    end = time.time()
    working_time = end - start
    return working_time, comparisons


def time_insertionsort(lst):
    start = time.time()
    comparisons = insertion_sort(lst)
    end = time.time()
    working_time = end - start
    return working_time, comparisons


def run_tests(lst):
    results = [[[], []] for _ in range(4)]
    for i in range(len(lst)):
        a = deepcopy(lst[i])
        b = deepcopy(lst[i])
        c = deepcopy(lst[i])
        d = deepcopy(lst[i])

        shell = time_shellsort(d)
        merge = time_mergesort(a)
        insertion = time_insertionsort(b)
        selection = time_selectionsort(c)
        algorithms = ['shell', 'merge', 'selection', 'insertion']
        for algo in algorithms:
            if algo == 'shell':
                for j in range(2):
                    results[0][j].append(shell[j])
            elif algo == 'merge':
                for j in range(2):
                    results[1][j].append(merge[j])
            elif algo == 'selection':
                for j in range(2):
                    results[2][j].append(selection[j])
            elif algo == 'insertion':
                for j in range(2):
                    results[3][j].append(insertion[j])

    algo_names = ['Shell','Merge','Selection','Insertion']
    results_dict = dict()
    for i in range(len(results)):
        aver_working_time = sum(results[i][0]) / len(results[i][0])
        aver_comparisons = sum(results[i][1]) / len(results[i][1])

        results_dict[algo_names[i]] = [aver_working_time, aver_comparisons]
    return results_dict


def main():
    algo_names = ['Shell','Merge','Selection','Insertion']
    powers = tuple(range(7, 16))
    times = {'Shell': [[] for _ in range(4)], 
                'Merge': [[] for _ in range(4)], 
                'Selection': [[] for _ in range(4)], 
                'Insertion': [[] for _ in range(4)]}
    comparisons = {'Shell': [[] for _ in range(4)], 
            'Merge': [[] for _ in range(4)], 
            'Selection': [[] for _ in range(4)], 
            'Insertion': [[] for _ in range(4)]}
    for power in powers:
        random_result, asc_result, desc_result, rep_result = test_all_algorithms_at_power(power)
        for algo in algo_names:

            times[algo][0].append(random_result[algo][0])
            comparisons[algo][0].append(random_result[algo][1])

            times[algo][1].append(asc_result[algo][0])
            comparisons[algo][1].append(asc_result[algo][1])

            times[algo][2].append(desc_result[algo][0])
            comparisons[algo][2].append(desc_result[algo][1])

            times[algo][3].append(rep_result[algo][0])
            comparisons[algo][3].append(rep_result[algo][1])
    arr_types = ['Random', 'Ascending', 'Descending', 'Repetitious']
    for arr_type in arr_types: 
        draw_graph(comparisons, arr_type, 'Num of comparisons')
        draw_graph(times, arr_type, 'Working time, sec')


def draw_graph(data, arr_type, gr_label):
    title = f'Algorithms for array with {arr_type}'.lower().capitalize()
    plt.title(title)
    x = list(range(7, 16))
    if arr_type == 'Random':
        arr_lst = 0
    elif arr_type == 'Ascending':
        arr_lst = 1
    elif arr_type == 'Descending':
        arr_lst = 2
    elif arr_type == 'Repetitious':
        arr_lst = 3
 
    y_sel = data['Selection'][arr_lst]
    y_ins = data['Insertion'][arr_lst]
    y_shell = data['Shell'][arr_lst]
    y_merge = data['Merge'][arr_lst]

    plt.plot(x, y_sel, label = "Selection sort")
    plt.plot(x, y_ins, label = "Insertion sort")
    plt.plot(x, y_shell, label = "Shellsort")
    plt.plot(x, y_merge, label = "Merge sort")

    plt.ylabel(gr_label)
    plt.xlabel('Logariphmic size of array')
    plt.legend()
    
    plt.yscale("log")
    plt.savefig(gr_label + ' ' + arr_type)
    plt.clf()


def test_all_algorithms_at_power(power):
    lst_random = []
    lst_asc = []
    lst_desc = []
    lst_rep = []
    for _ in range(3):
        lst_random.append(generate_random_arr(power))
        lst_asc.append(generate_sorted_arr(power))
        lst_desc.append(generate_sorted_arr_reversed(power))
        lst_rep.append(generate_123numbers_arr(power))

    random_result = run_tests(lst_random)
    asc_result = run_tests(lst_asc)
    desc_result = run_tests(lst_desc)
    rep_result = run_tests(lst_rep)
    return random_result, asc_result, desc_result, rep_result


main()