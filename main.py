from datetime import datetime, timedelta


def get_night_shift_date(night_shift):
    today = datetime.now().strftime('%d.%m.%Y')
    if night_shift == 'нет':
        return today
    elif night_shift == 'да':
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%d')
        return f'{yesterday}-{today}'
    else:
        return None


def ask_for_night_shift():
    while True:
        night_shift = input('У вас ночная смена? (Введите да/нет)').lower()
        date_shift = get_night_shift_date(night_shift)
        if date_shift:
            return date_shift
        print('Вы ошиблись при вводе. Попробуйте ещё раз.')


def ask_for_shift_name():
    shift_names = ['А', 'Б', 'В', 'Г']
    while True:
        name_shift = input('Введите букву вашей смены (А, Б, В, Г)').upper()
        if name_shift in shift_names:
            return name_shift
        print('Вы ввели несуществующую смену. Повторите ввод.')


def write_to_file(file_name, content, mode="a"):
    with open(file_name, mode) as file:
        file.write(content)


def pipe(file_name):
    while True:
        number_order = input('Введите номер заказа:')
        pos_order = input('Введите позицию заказа:')
        name_customer = input('Введите полное наиминование заказчика:')
        size_pipes = input('Введите сортамент труб:')
        
        info_pipes = f'\nЗаказ {number_order} поз. {pos_order}, {name_customer}, {size_pipes}:\n'
        write_to_file(file_name, info_pipes)

        total_pipes = input('Введите количество прокатанных труб:')
        accepted_pipes = input('Введите количество принятых труб:')
        acceptance = f'{total_pipes}/{accepted_pipes}'

        if total_pipes != accepted_pipes:
            reject_pipes = input('Введите количество отклонённых труб:')
            reject_pipes_info = input('Введите все деффекты:')
            acceptance += f'/{reject_pipes}({reject_pipes_info})'

            if int(total_pipes) != int(accepted_pipes) + int(reject_pipes):
                marriage_pipes = input('Введите количество бракованных труб:')
                marriage_pipes_info = input('Введите все деффекты брака:')
                acceptance += f'/{marriage_pipes}({marriage_pipes_info})'
            else:
                acceptance += '/0'

        else:
            acceptance += '/0/0'

        write_to_file(file_name, f'Приёмка труб без резьбы: {acceptance} \n')
        sample_selection(file_name)
        break


def sample_selection(file_name):
    samples = []
    while True:
        num_sample = input('Введите номер отбираемой пробы:')
        samples.append(num_sample)
        more_samples = input('Были ли ещё партии? (Введите да/нет)').lower()
        if more_samples == 'нет':
            break
        elif more_samples != 'да':
            print('Вы ошиблись при вводе. Попробуйте ещё раз.')

    write_to_file(file_name, f'Отбор проб: {", ".join(samples)}.')


def check_pipe(file_name):
    was_pipe = input('Был ли у вас прокат труб на смене? (Введите да/нет)').lower()
    flag_pipe = False
    write_to_file(file_name, '\nПрокат:')
    while True:
        if was_pipe == 'нет' and flag_pipe == False:
            write_to_file(file_name, 'нет.\n')
            break
        elif was_pipe == 'нет' and flag_pipe == True:
            break
        elif was_pipe == 'да':
            flag_pipe == True
            pipe(file_name)
            was_pipe = input('Были ли ещё заказы на прокате? (Введите да/нет)').lower()
            write_to_file(file_name, '\n')
        else:
            was_pipe = input('Вы ошиблись при вводе. Попробуйте ещё раз. (Введите да/нет)').lower()


def main():
    date_shift = ask_for_night_shift()
    name_shift = ask_for_shift_name()
    name_file = f'Смена за {date_shift}.txt'

    # Первая запись в файл очищает его
    write_to_file(name_file, f'{date_shift}\nИТПЗ\nСмена {name_shift}\n', mode="w")
    check_pipe(name_file)


if __name__ == "__main__":
    main()