from datetime import datetime, timedelta


def night_shift_value(night_shift):
    while True:
        if night_shift == 'нет':
            return datetime.now().strftime('%d.%m.%Y')
        elif night_shift == 'да':
            today = datetime.now().strftime('%d.%m.%Y')
            yesterday = datetime.now() - timedelta(days=1)
            yesterday = yesterday.strftime('%d')
            return yesterday + '-' + today
        else:
            night_shift = input(
                'Вы ошиблись при вводе. Попробуйте ещё раз. (Введите да/нет)'
                ).lower()


date_shift = input('У вас ночная смена? (Введите да/нет)').lower()

with open("otchet.txt", "w") as file:
    file.write(night_shift_value(date_shift))

with open("otchet.txt", "a") as file:
    file.write('\nИТПЗ')

name_shift_list = ['A', 'Б', 'В', 'Г']
name_shift = input('Введите букву вашей смены (А, Б, В, Г)').upper() 
while True:
    if name_shift in name_shift_list:
        with open("otchet.txt", "a") as file:
            file.write(f'\nСмена {name_shift}\n\n')
            break
    else:
        name_shift = input(
            'Вы ввели несуществующую смену. Повторите ввод. (А, Б, В, Г)'
            ).upper()


def pipe():
    """ПРОКАТ"""
    while True:
        with open("otchet.txt", "a") as file:
            file.write('Прокат:\n')

        """ИНФОРМАЦИЯ О ЗАКАЗЕ"""
        number_order = input('Введите номер заказа:')
        pos_order = input('Введите позицию заказа:')
        name_customer = input('Введите полное наиминование заказчика:')
        size_pipes = input('Введите сортамент труб:')

        info_pipes = f'{number_order} поз. {pos_order}, {name_customer}, {size_pipes}:'
        with open("otchet.txt", "a") as file:
            file.write(f'Заказ {info_pipes} \n')

        """ПРИЁМКА ТРУБ БЕЗ РЕЗЬБЫ"""
        total_pipes = input('Введите количество прокатанных труб:')
        accepted_pipes = input('Введите количество принятых труб:')
        if total_pipes == accepted_pipes:
            acceptance = (f'{total_pipes}/{accepted_pipes}/0/0')
            with open("otchet.txt", "a") as file:
                file.write(f'Приёмка труб без резьбы: {acceptance} \n')
            sample_selection()
            break

        else:
            reject_pipes = input('Введите количество отклонённых труб:')
            reject_pipes_info = input('Введите все деффекты:')
            marriage_pipes = input('Введите количество бракованых труб:')
            marriage_pipes_info = input('Введите все деффекты брака:')
            acceptance = (f'{total_pipes}/{accepted_pipes}/'
                          f'{reject_pipes} {reject_pipes_info}/'
                          f'{marriage_pipes}({marriage_pipes_info})')
            with open("otchet.txt", "a") as file:
                file.write(f'Приёмка труб без резьбы: {acceptance} \n')
            sample_selection()
            break


def sample_selection():
    """ОТБОР ПРОБ"""
    num_sample = input(
        'Введите номер отбираемой пробы:'
        )
    with open("otchet.txt", "a") as file:
        file.write(f'Отбор проб: {num_sample}')
    more_samples = input('Были ли ещё партии? (Введите да/нет)').lower()
    while True:
        if more_samples == 'да':
            while more_samples == 'да':
                num_sample = input(
                'Введите номер отбираемой пробы:'
                )
                with open("otchet.txt", "a") as file:
                    file.write(f', {num_sample}')
                    more_samples = input('Были ли ещё партии? (Введите да/нет)').lower()
        elif more_samples == 'нет':
            with open("otchet.txt", "a") as file:
                file.write('. \n')
            break
        else:
            print('Вы ошиблись при вводе. Попробуйте ещё раз')
            more_samples = input('Были ли ещё партии? (Введите да/нет)').lower()

was_pipe = input('Был ли у вас прокат труб на смене? (Введите да/нет)').lower()

while True:
    if was_pipe == 'нет':
        with open("otchet.txt", "a") as file:
            file.write(f'Прокат: {was_pipe}\n\n')
            break
    elif was_pipe == 'да':
            pipe()
            was_pipe = input('Были ли ещё заказы на прокате?')
    else:
        was_pipe = input('Вы ошиблись при вводе. Попробуйте ещё раз. (Введите да/нет)').lower()