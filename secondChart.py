import matplotlib.pyplot as plt


def create_second_chart(df):
    df_new = df.sort_values('Недвижимость(кв.м.)')
    plt.plot(df_new['Недвижимость(кв.м.)'], df_new['Месячный платеж'])
    plt.xlabel('Недвижимость(кв.м.)')
    plt.ylabel('Месячный платеж')
    plt.title('Недвижимость(кв.м.) от Месячный платеж')
    plt.show()
