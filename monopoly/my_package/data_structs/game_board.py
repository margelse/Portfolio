from dataclasses import dataclass

@dataclass
class GameBoard:
    places = {number: 0 for number in range(40)}
    names_place = [
        'Старт',
        'Житная',
        'Общественная козна 1',
        'Нагинская',
        'Подоходный налог',
        'Рижская железная дорога',
        'Варшавская',
        'Шанс 1',
        'Огарева',
        'Первая парковая',
        'Экскурсия',
        'Полянка',
        'Электростанция',
        'Сретенка',
        'Ростовская',
        'Курская железная работа',
        'Рязанская',
        'Общественная козна',
        'Вавилова',
        'Рублевская',
        'Парковка',
        'Тверская',
        'Шанс 2',
        'Пушкинская',
        'Маяковская',
        'Казанская железная дорога',
        'Грузинская',
        'Чайковского',
        'Водопровод',
        'Смоленская',
        'Тюрьма',
        'Щусева',
        'Гоголевский',
        'Общественная козна 3',
        'Кутузовский',
        'Ленинградская железная работа',
        'Шанс',
        'Малая бронная',
        'Сверхналог',
        'Арбат'
    ]

    def __len__(self):
        number_place = list(self.places.keys())
        return len(number_place)

    def __getitem__(self, idx):
        l = len(self)

        if idx >= l:
            idx = idx % l

        return self.places[idx]

    def __setitem__(self, idx, value):
        l = len(self)
        correct_idx = idx % l
        self.places[correct_idx] = value
