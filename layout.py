# coding=utf-8

import dash_html_components as html


def _get_page_header():
    header = html.Header([
        html.H1("Interpretable Machine Learning"),
        html.P("В современном мире машинное обучение способно решить целый спектр разнообразных задач:"
               " от предсказания курса доллара"
               " и перевода текста между языками"
               " до распознавания пешеходов беспилотными автобилями."
               " И, казалось бы, всё хорошо – да, работает не всегда идеально, но работает же!"
               " Можно даже не разбираться, почему и как. Или нельзя?"),
    ], className="article-header")

    return header


def _get_article(app):
    sections = [
        html.Div(html.Div([
            html.H3("Одна ошибка – (не) страшно!"),
            html.P([
                "В задачах, где используется хорошо изученная модель или последствия ошибки невелики,"
                " объяснение того или иного предсказания действительно может показаться излишним."
                " Однако, есть задачи, в которых цена – человеческая жизнь или крупная сумма денежных средств."
                " К примеру, ",
                html.A("определение курса лечения больного раком",
                       href="https://www.theverge.com/2018/7/26/17619382/ibms-watson-cancer-ai-healthcare-science",
                       target="_blank"),
                " или ",
                html.A("торги на бирже",
                       href="https://futurism.com/investing-lawsuit-ai-trades-cost-millions",
                       target="_blank"),
                "."

                " В таких случаях становится важным понимать, почему модель приняла конкретное решение."
                " Иногда это может выявить нерассмотренные краевые случаи "
                " (например, если беспилотный автомобиль определяет велосипед по двум колесам,"
                " то что же тогда будет с унициклом?)"
                " или же факт ",
                html.A("половой дискриминации",
                       href="https://www.reuters.com/article/us-amazon-com-jobs-automation-insight/amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK08G",
                       target="_blank"),
                " при приёме на работу.",
                " Но при помощи чего можно ",
                html.Em("понять"),
                " модель?",
            ]),
        ], className="content-wrapper"), className="content"),

        html.Div(html.Div([
            html.H3("Интерпретируемость моделей"),
            html.P([
                "Что же это такое? "
                " Строгого математического определения нет, "
                " но многие считают, что это, говоря простым языком, степень того, насколько человек может понять"
                " поведение модели и её логику при принятии того или иного решения."
                " Чем выше интерпретируемость модели, тем проще нам, людям, осознавать, как модель пришла к ответу."
            ]),
            html.P([
                " Помимо этого, человек – существо любознательное. "
                " Нам хочется понимать, как устроен мир и как он работает. "
                " Когда машинное обучение применяется в исследованиях и дает хорошие результаты,"
                " всё самое интересное остается внутри \"чёрной коробки\"."
                " Интерпретируемость моделей позволяет осознать, "
                " что именно послужило причиной того или иного предсказания.",
                html.Br(),
                " Глобально про интерпретируемость моделей можно рассуждать при помощи разных подходов,"
                " мы же выделим две основных группы и обсудим их."
            ]),
        ], className="content-wrapper"), className="content"),

        html.Div(html.Div([
            html.H3("Интерпретация, основанная на особенностях модели"),
            html.P(
                "Самый простой способ добиться того, чтобы модель можно было понять"
                " – использовать, как бы парадоксально это ни звучало, понятные модели."
                " Наиболее известные интерпретируемые модели – это линейная и логистическая регрессии,"
                " решающие деревья и решающие правила."
            ),
            html.P(
                "Оценить вклад признака `f` у объекта `x` при использовании линейной регрессии"
                " можно, посмотрев на вес признака, "
                " а оценить его вклад – при помощи произведения веса на само значение."
            ),
            html.P(
                " На графиках ниже изображены зависимости между данными абитуриентов,"
                " подавших заявки в зарубежные университеты."
                " Видно, что линейная регрессия выделила наиболее важным признаком CGPA, "
                " что соответствует действительности – ведь у этого параметра наибольшая корреляция"
                " с целевой переменной (в данном случае – вероятностью поступления)."
            ),
            html.Div([
                html.Img(src=app.get_asset_url("linre-weights.png"), className="linre-image"),
                html.Img(src=app.get_asset_url("linre-corr.png"), className="linre-image"),
            ], className="linre-container"),
            html.P(
                " Тут могут возникать проблемы: если два признака коррелируют,"
                " то первый может забрать себе всю славу и большой вес,"
                " а второй останется ни с чем или с противоположным знаком."
            ),
            # html.Script(src=app.get_asset_url("flats-model.js"), type="text/javascript"),
            html.P([
                "Неглубокие решающие деревья и небольшие решающие правила очень хорошо воспринимаются людьми "
                "– они чем-то похожи на то, как думает человек, и потому понятны сами по себе и хорошо интерпретируемы"
                " (подробнее можно почитать ",
                html.A("тут", href="https://christophm.github.io/interpretable-ml-book/simple.html",
                       target="_blank"),
                ").",
            ]),
            html.P(
                "Основным плюсом подхода, основанного на особенностях модели, является то,"
                " что самой модели и её архитектуры уже достаточно."
                " Нет необходимости строить гипотезы о её работе и при этом"
                " в некоторых ситуациях простых моделей оказывается вполне достаточно."
            ),
            html.P(
                "Главный же минус виден невооружённым взглядом – данный подход зафиксирован на одной конкретной модели."
                " Если нужно скорректировать модель, тонеобходимо изменить подход к интерпретируемости."
                " При этом на многих реальных данных линейная регрессия или решающее дерево"
                " не смогут сделать ничего толкового."
                " Иногда необходимо воспользоваться бустингом или нейронными сетями,"
                " но при этом хочется хотя бы примерно понимать,"
                " как модели удалось принять правильное решение."
                " С такими желаниями приходится обращаться к подходам из следующей группы.",
            ),
        ], className="content-wrapper"), className="content"),

        html.Div(html.Div([
            html.H3("Интерпретация, не зависящая от модели"),
            html.P(
                "Рассмотрим несколько подходов,"
                " которые позволяют объяснять решение сложной модели для конкретного объекта."
                " Главное предположение, в рамках которого применяются эти подходы, состоит в том, "
                " что сами признаки должны быть интрепретируемы."
                " Например, эмбединг товара или пиксель картинки вряд ли скажут что-либо человеку."
                " Поэтому вне зависимости от того, насколько сложные признаки использует основная модель,"
                " объясняющая компонента должна работать на чем-то упрощенном."
                " Для текстов обычно рассматривают мешок слов с ограничением на количество слов,"
                " а для картинок группы – похожих пикселей (суперпиксели)."
            )
        ], className="content-wrapper"), className="content"),

        html.Div(html.Div([
            html.H3("LIME"),
            html.P([
                "Для начала, рассмотрим метод ",
                html.Strong("L"),
                "ocal ",
                html.Strong("I"),
                "nterpretable ",
                html.Strong("M"),
                "odel-agnostic ",
                html.Strong("E"),
                "xplanations."
                " Интуитивно, объяснением для данного подхода может"
                " послужить локальная линейная аппроксимация поведения модели."
                " Общая идея состоит в том, что рядом с интересующим объектом генерируется группа соседей,"
                " после чего исходная модель совершает для них предсказания."
                " Затем обучается простая, сама по себе хорошо интерпретируемая суррогатная модель таким образом,"
                " чтобы разметка для соседей исходного объекта была правильной."
                " После чего для интерпретации исследуется суррогатная модель."
            ]),
            html.Details([
                html.Summary("Подробности, алгоритмы и формулы"),
                " Зачастую, для объекта с признаковым объяснением `x`"
                " его интерпретируемое представление обозначается за `\overline{x}`."
                " Также, обозначим сложную исходная модель за `f`,"
                " а результатом должна быть объясняющая модель `g`."
                " Алгоритм действия следующий:",
                html.Ul([
                    html.Li(
                        "Перевести интересующее слово в его интерпретируемое представление `\overline{x}`."
                    ),
                    html.Li(
                        "Сгенерировать множество интерпретируемых представлений объектов `Z`,"
                        " близких к `\overline{x}`."
                        " В случае с текстами и мешком из `k` слов обычно отбрасывают часть слов из предложения."
                        " Например, для предложения \"Я хочу спать\" близкими будут \" \", \"Я\", \"хочу\","
                        " \"спать\", \"Я хочу\", \"Я спать\", \"хочу спать\" и \"Я хочу спать\"."
                    ),
                    html.Li(
                        "Для каждого `\overline{z} \in Z` восстановить полное описание `z`, после чего"
                        " узнать `f(z)` и расстояние от `\overline{z}` до `\overline{x}`."
                        " Измерить расстояние можно разными способами (дальше мы обсудим, почему это плохо),"
                        " а пока ограничимся каким-нибудь одним."
                        " Для вышеописанного мешка слов это может быть"
                        " `\\pi_{\overline{x}}(\overline{z}) = 1 - `доля удаленных слов из `\overline{z}`."
                        " Точка отсчета в этой метрике расстояния всегда `x`."
                    ),
                    html.Li(
                        "Выбрать лучшую `g` из большого класса интерпретируемых моделей,"
                        " решив задачу оптимизации и поддерживая `g` достаточно простой "
                        " при помощи штрафа за сложность `\Omega(g)`:"
                        "$$"
                        "\operatorname*{arg min}\limits_{g \in G} \sum\limits_{\overline{z}_i \in Z}"
                        "\\pi_{\overline{x}}(\overline{z}) (f(z) - g(\overline{z}))^2 + \Omega(g) "
                        "$$"
                        "Этот функционал сурово штрафует `g` за ошибки в объектах, близких к интересующему,"
                        " а поэтому локально `g` должна получаться похожей на исходную модель `f`."
                        " В данном примере используется среднеквадратичная ошибка,"
                        " но можно использовать любую другую, "
                        " выбор штрафа за сложность контролировать также несложно."
                    )
                ])
            ]),
            html.P([
                "Одна из проблем данного метода состоит в большой свободе:"
                " выбор функции близости и функционала ошибки довольно сильно влияет на результат."
                " При этом есть примеры ситуаций, когда разные функции приводят к результатам максимально далеким"
                " – это явно не хорошо для интерпретируемости."
                " В разделе про SHAP мы покажем, как с этим бороться."  # TODO: link
            ]),
            html.H4("Выжимаем все соки"),
            html.P(
                " В этой секции мы попробуем реализовать LIME своими руками. Необходимые ингридиенты: упорство,"
                " Python и scikit-learn. Действовать будем аналогично алгоритму, описанному выше."
            ),
            html.Img(src=app.get_asset_url("self-lime-1.png"), className="self-lime-1"),
            html.P(
                "Получилось неплохо. Теперь попробуем менять две вещи: "
                " функцию расстояния (евклидова, постоянная, манхэттонская, Чебышева) и функцию (сейчас будет сложно),"
                " переводящую функцию расстояния в функцию близости. Мы хотим больше наказывать за ошибки в объектах"
                " совсем близких к нашему, а значит они должны получать большие веса. Проверим два варианта: `1 / f(x)`"
                " и `e^{-f(x)}`."
            ),
            html.P(
                "Давайте посмотрим, как LIME работает на деле. Ему был предложен набор данных, "
                " состоящий из новостей и писем, относящихся к 20 тематикам. Задача – определить тематику текста "
                " (типичный пример классификации). Для простоты восприятия, рассмотрим отно"
            ),
            html.Img(src=app.get_asset_url("christ-lime.png"), className="christ-lime"),
            html.P(
                "test"
            ),
            html.P(
                " из предложений на английском языке, которые размечены на 6 эмоциональных классов. Задача –"
                " распознать эмоциональное состояние человека."
            ),
            html.Img(src=app.get_asset_url("emo-lime.png"), className="emo-image"),
            html.P(
                "Синим цветом выделены признаки (в нашем случае слова) наиболее характерные для класса \"sadness\"."
                " Видно, что"
            ),

        ], className="content-wrapper"), className="content"),

        html.Div(html.Div([
            html.H3("Shapley Values"),
            html.P(
                "Shapley Values – невероятно красивый и интересный подход сам по себе,"
                " потому что основан на результате из теории игр."
                " Исходная постановка задачи звучит так:"
                " есть игроки, которые могут объединяться и работать вместе."
                " Зарплату получают одну на всех, но она завиcит от качества работы."
                " Как честно разделить деньги между теми, кто поработал?"
            ),
            html.P(
                "Будем считать, что значения признаков конкретного объекта – это игроки, "
                " они вносят вклад в предсказание. "
                " Обычно говорят, что они вносят вклад в сдвиг ответа модели от среднего ответа. "
                " Заплатим всем значениям признаков зарплату в размере разницы между предсказанием на данном объекте"
                " и средним предсказанием. Как признакам честно разделить между собой деньги?"
            ),
            html.P(
                "По теореме Шепли оказывается, что существует единственное распределение,"
                " удовлетворяющие четырем разумным свойствам, которые мы обсудим чуть позже."
                " Признак или игрок `i` должен получать среднее "
                " по всем возможным подмножествам игроков (коалициям) значение вносимой им пользы:"
                "$$"
                "\phi_i(v) = \sum\limits_{S \subset N \setminus \{ i\}} \\frac{|S|! \, (n - |S| - 1)!}{n!}"
                "\, (v(S \\cup \{ i \}) - v(S))"
                "$$"
                "Здесь `N` – множество всех игроков,"
                " `S` пробегает его подмножества без `i`-го игрока,"
                " `v` показывает сколько заплатят за работу конкретной коалиции."
                " Самый важный множитель тут последний,"
                " он как раз показывает вносимую пользу,"
                " сложное начало с факториалами нужно для правильного учета размера коалиций при усреднении."
            ),
            html.Details([
                html.Summary("Честная постановка задачи и подробности про теорему"),
                html.P(
                    "В игре есть `n` игроков, их множество обозначается за `N`."
                    " Любое (даже пустое) подмножество игроков называется коалицией."
                    " Функция выплат `v` для каждой коалиции показывает, сколько бы ей заплатили,"
                    " если бы игроки этой коалиции работали вместе."
                    " Итак, `v : 2^{\mathbb{N}} \\to \mathbb{R}`."
                    " Говорят, что пустая коалиция всегда получает 0."
                    " В случае моделей это может быть разумно – "
                    " совсем не имея признаков, мы скорее всего выдадим"
                    " средний результат по всем объектам из обучающей выборки."
                ),
                html.P(
                    "Рассмотрим игрушечный пример."
                    " Есть два электрика: `N = \{ 1, 2 \}`."
                    " Первый – молодой и может залезть на верх лестницы и вкрутить лампочку,"
                    " второй – пожилой и уже не может подняться по лестнице, "
                    " но со старостью приходит мудрость, поэтому только он знает, где лежат новые лампочки."
                    " Поэтому электрики получат деньги, только если поработают вместе:"
                    "$$"
                    "v(\{ \emptyset \}) = 0, \quad v(\{1 \}) = 0, \quad v(\{ 2 \}) = 0, \quad v(\{ 1, 2 \}) = 100"
                    "$$"
                    "Как им честно поделить эти 100 рублей?"
                    " Настоящее определение честности мы дадим немножко позже, "
                    " но пока интуитивно хочется сказать, что каждому нужно дать по 50."
                ),
                html.P(
                    "Немного изменим условие задачи:"
                    " на самом деле, молодой электрик может сходить в магазин и купить лампочку за 60,"
                    " то есть в одиночку может заработать 40."
                    " А пожилой электрик может сквозь боль залезть по лестнице,"
                    " вкрутить лампочку, после чего придётся сходить в аптеку за мазью от растяжения спины."
                    " Мазь стоит 90, откуда получаем следующую функцию выплат:"
                    "$$"
                    "v(\{ \emptyset \}) = 0, \quad v(\{1 \}) = 40, \quad v(\{ 2 \}) = 10, \quad v(\{ 1, 2 \}) = 100"
                    "$$"
                    "Понятно, что для устойчивости (никто не хочет выйти из коалиции при прочих равных условиях)"
                    " достаточно дать молодому немножко больше 40, а пожилому – немножко больше 10. "
                    " Но как тут разделить честно?"
                ),
                html.P(
                    "Говорят, что честная функция дележа должна обладать следующими свойствами:"
                ),
                html.Ol([
                    html.Li(
                        "Симметричностью по игрокам. Если для каждой коалиции `S`, не содержащей игроков `i` и `j`"
                        " выполняется `v(S \cup \{ i \} ) = v(S \cup \{ j \} )`, то `i` и `j` должны получить "
                        " равную плату после дележа. Это требование очень логично для интерпретируемости:"
                        " мы хотим сравнивать вклады признаков между собой. Будет плохо, если одинаково работающие"
                        " признаки будут получать разное значение."
                    ),
                    html.Li(
                        "Эффективностью."
                        " При дележе будут розданы все деньги и всем хватит. "
                        " Мы хотим объяснить именно весь сдвиг от среднего значения."
                    ),
                    html.Li(
                        "Свойством болвана. "
                        " Если какой-то игрок не привносит ничего ни в какой коалиции,"
                        " он должен получить 0. Действительно, если какое-то значение признака"
                        " никогда не меняет предсказания модели, им вряд ли можно хоть что-то объяснить."
                    ),
                    html.Li(
                        "Линейностью по функциям выплат."
                        " Пусть для одного множества игроков есть две функции выплат `v` и `w`."
                        " Мы хотим, чтобы сумма доставшихся игроку после отдельных дележей денег"
                        " для двух функций совпадала с полученным им при рассмотрении игры с функцией `v + w`."
                        " Это свойство может пригодится для интерпретируемости ансамблей моделей,"
                        " когда результат – усреднение результатов отдельных частей."
                    ),
                ]),
                html.P(
                    "Утверждается, что функция Шепли – единственная удовлетворяющая "
                    " всем этим четырем требованиям функция. Например, для электриков получается,"
                    " что молодой должен получить `(40 + 90) / 2 = 65`, а пожилой `(10 + 60) / 2 = 35`."
                ),
            ]),
            html.P(
                "Разберем подробнее то, как результат Шепли можно применить для интерпретируемости. "
                " Самый наивный подход состоит в том, чтобы честно подсчитать всё нужное в формуле."
                " Для моделей с табличными данными это будет означать,"
                " что для каждого подмножества признаков надо заново обучить модель,"
                " чтобы узнать зарплату v для него."
                " Конечно, это слишком долго, и так не делают."
                " Обычно, вместо полного удаления признака его заменяют на значение этого же признака"
                " у произвольно выбранного объекта из выборки."
                " Для картинок, к примеру, можно заменять суперпиксели на серый цвет, "
                " с другой стороны, для текстов такая проблема иногда даже не возникает,"
                " так как модели не завязаны на определенное количество слов."
                " Но даже так, с одной моделью перебор всех возможных коалиций"
                " потребует экспоненциального от числа признаков времени."
                " Поэтому используют различные приближения (например, метод Монте-Карло)."
            ),
        ], className="content-wrapper"), className="content"),

        html.Div(html.Div([
            html.H3("Kernel SHAP"),
            html.P([
                "Наконец, рассмотрим Kernel SHAP (SHapley Additive exPlanations), своего рода"
                " объединение Lime и Shapley Values."
                " Как обсуждалось в части про Lime, результат сильно зависит от выбора функции расстояния"
                " и функционала ошибки, еще и штраф за сложность модели там выбирался произвольно."
                " Оказывается, что если обозначить за `|\overline{z}|` число ненулевых координат вектора, "
                " за `M` – число признаков в интерпретируемом представлении и положить"
                "$$"
                "\Omega(g) = 0, \quad \pi_{\overline{x}}(\overline{z}) = "
                "\\frac{M - 1}{\\binom{M}{|\overline{z}|} \, |\overline{z}| \, (M - |\overline{z}|)}, \quad"
                " L(f, g, \pi_{x'}) = \sum\limits_{z' \in Z} "
                "\pi_{\overline{x}}(\overline{z}) [f(z) - g(\overline{z})]^2,"
                "$$"
                "то ответ модели Lime является хорошим приближением Shapley Values."
                " Доказательство этого факта можно найти в ",
                html.A("оригинальной статье",
                       href="https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf",
                       target="_blank"),
                "."
            ]),
            html.P(
                "Может показаться, что SHAP замечательный, и это правда так – сама идея раздавать признакам"
                " зарплату невероятная, но и у этой модели есть свои минусы. "
                " Например, Kernel SHAP медленный, а все существующие ускорения приводят "
                " к потерям важных свойств описанных выше.",
            ),
            html.P(
                "Своего рода rule of thumb звучит так: если нужны максимально подробные объяснения"
                " и есть время, то стоит использовать SHAP; если же ждать некогда,"
                " то можно применять Lime, но делать это стоит осторожно."
            ),
        ], className="content-wrapper"), className="content"),
    ]

    return sections


def get_app_layout(app):
    layout = html.Div([
        _get_page_header(),
        *_get_article(app),
    ], className="page")

    return layout
