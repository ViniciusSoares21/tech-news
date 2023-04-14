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
            "summary": "Sabemos que a arte de contar histórias surge de tempo",
            "reading_time": 15,
            "timestamp": "08/07/2022",
            "category": "Carreira",
        },
        {
            "url": "https://blog.betrybe.com/noticias/",
            "title": "Orkut volto: o que se sabe até agora sobre o retorno",
            "writer": "Allan Camilo",
            "summary": "Em meados de abril deste ano, o domínio do Orkut foi",
            "reading_time": 10,
            "timestamp": "08/07/2022",
            "category": "Notícias",
        },
        {
            "url": "https://blog.betrybe.com/noticias/dungleon-como-jogar/",
            "title": "Dungleon: como jogar o game que mistura RPG e Wordle",
            "writer": "Allan Camilo",
            "summary": "Cópias e spin-off de jogos populares não são novidade",
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
                        "Orkut volto: o que se sabe até agora sobre o retorno",
                        10,
                    )
                ],
            },
            {
                "unfilled_time": 7,
                "chosen_news": [
                    (
                        "Dungleon: como jogar o game que mistura RPG e Wordle",
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
