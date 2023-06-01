import matplotlib.pyplot as plt


def create_first_chart(df):
    df_new = df.sort_values('Опыт работы')
    plt.plot(df_new['Опыт работы'], df_new['Доход'])
    plt.xlabel('Опыт работы')
    plt.ylabel('Доход')
    plt.title('Дохода от опыта работы')
    plt.show()
