import matplotlib.pyplot as plt


def create_fourth_chart(df):
    yes = df[df['Благонадежный заемщик'] == 'Да'].count()['Благонадежный заемщик']
    no = df[df['Благонадежный заемщик'] == 'Нет'].count()['Благонадежный заемщик']

    percent_yes = yes / (yes + no) * 100
    percent_no = no / (yes + no) * 100

    labels = ['Да', 'Нет']
    sizes = [percent_yes, percent_no]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Соотношение благонадежных замещиков')

    plt.show()
