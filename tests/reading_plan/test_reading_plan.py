from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest
from unittest.mock import patch


@pytest.fixture
def fake_data_news():
    return [
        {
            "url": "https://blog.betrybe.com/carreira/oratoria/",
            "title": "Oratória: passo a passo para falar bem e se destacar!",
            "writer": "Lucas Custódio",
            "summary": "Sabemos que a arte de contar histórias surge de tempos imemoriais, com seres humanos carregando a habilidade de transmitir informações por meio da linguagem em sua essência. No entanto, o que podemos não saber é que a arte de usar a linguagem para construir discursos polidos e impactantes também não é de hoje. Tanto os diálogos do filósofo Platão quanto os discursos excepcionais de Cícero na Roma Antiga utilizavam uma técnica milenar para encantar audiências: a oratória.",
            "reading_time": 15,
            "timestamp": "08/07/2022",
            "category": "Carreira",
        },
        {
            "url": "https://blog.betrybe.com/noticias/orkut-voltou-o-que-se-sabe-ate-agora-sobre-o-retorno/",
            "title": "Orkut voltou: o que se sabe até agora sobre o retorno da rede",
            "writer": "Allan Camilo",
            "summary": "Em meados de abril deste ano, o domínio do Orkut foi reativado. O site, que para muitos brasileiros foi o primeiro contato com uma rede social, “retornou” 8 anos após ser desativado. Porém, seu sucessor espiritual ainda está para ser lançado. Entenda a seguir se o Orkut realmente voltou à ativa.",
            "reading_time": 10,
            "timestamp": "08/07/2022",
            "category": "Notícias",
        },
        {
            "url": "https://blog.betrybe.com/noticias/dungleon-como-jogar/",
            "title": "Dungleon: como jogar o game que mistura RPG e Wordle [2022]",
            "writer": "Allan Camilo",
            "summary": "Cópias e spin-offs de jogos populares não são novidade. Derivados dos aplicativos Temple Run e Flappy Bird já fazem parte da cultura pop. Com o boom repentino de Wordle, onde deve-se inserir letras e descobrir a palavra do dia, gêneros diferentes de jogos se misturaram à jogabilidade tradicional. É assim que surgiu Dungleon, game que mistura RPGs e Wordle. A seguir, saiba tudo sobre ele.",
            "reading_time": 3,
            "timestamp": "07/07/2022",
            "category": "Notícias",
        },
    ]


def test_reading_plan_group_news(fake_data_news):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    with patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=fake_data_news
    ):

        result = ReadingPlanService.group_news_for_available_time(10)
        print(result)
        readable = [
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Orkut voltou: o que se sabe até agora sobre o retorno da rede",
                        10,
                    )
                ],
            },
            {
                "unfilled_time": 7,
                "chosen_news": [
                    (
                        "Dungleon: como jogar o game que mistura RPG e Wordle [2022]",
                        3,
                    )
                ],
            },
        ]
        unreadable = [
            ("Oratória: passo a passo para falar bem e se destacar!", 15)
        ]
        assert result["readable"] == readable
        assert result["unreadable"] == unreadable
        assert result["readable"][0]["unfilled_time"] == 0
        assert result["readable"][1]["unfilled_time"] == 7
