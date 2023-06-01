import matplotlib.pyplot as plt
import numpy as np


def create_third_chart(df):
    df.sort_values('Доход')
    male = df[df['Пол'] == 'мужской']
    female = df[df['Пол'] == 'женский']
    mean_income_m = np.mean(male['Доход'])
    mean_income_f = np.mean(female['Доход'])
    ages_m = male['Возраст']
    ages_f = female['Возраст']

    plt.plot(ages_m, [mean_income_m] * len(ages_m), label='мужской')
    plt.plot(ages_f, [mean_income_f] * len(ages_f), label='женский')

    plt.xlabel('Возраст')
    plt.ylabel('Средний Доход')
    plt.legend()
    plt.show()
